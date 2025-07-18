"""Test the types in the `ethereum_test_rpc` package."""

import pytest

from ethereum_test_rpc import EthConfigResponse

eth_config_json_data = """
{
    "current": {
      "activationTime": 0,
      "blobSchedule": {
        "baseFeeUpdateFraction": 3338477,
        "max": 6,
        "target": 3
      },
      "chainId": "0x88bb0",
      "precompiles": {
        "0x0000000000000000000000000000000000000001": "ECREC",
        "0x0000000000000000000000000000000000000002": "SHA256",
        "0x0000000000000000000000000000000000000003": "RIPEMD160",
        "0x0000000000000000000000000000000000000004": "ID",
        "0x0000000000000000000000000000000000000005": "MODEXP",
        "0x0000000000000000000000000000000000000006": "BN256_ADD",
        "0x0000000000000000000000000000000000000007": "BN256_MUL",
        "0x0000000000000000000000000000000000000008": "BN256_PAIRING",
        "0x0000000000000000000000000000000000000009": "BLAKE2F",
        "0x000000000000000000000000000000000000000a": "KZG_POINT_EVALUATION"
      },
      "systemContracts": {
        "BEACON_ROOTS_ADDRESS": "0x000f3df6d732807ef1319fb7b8bb8522d0beac02"
      }
    },
    "currentHash": "243c27d1",
    "currentForkId": "bef71d30",
    "next": {
      "activationTime": 1742999832,
      "blobSchedule": {
        "baseFeeUpdateFraction": 5007716,
        "max": 9,
        "target": 6
      },
      "chainId": "0x88bb0",
      "precompiles": {
        "0x0000000000000000000000000000000000000001": "ECREC",
        "0x0000000000000000000000000000000000000002": "SHA256",
        "0x0000000000000000000000000000000000000003": "RIPEMD160",
        "0x0000000000000000000000000000000000000004": "ID",
        "0x0000000000000000000000000000000000000005": "MODEXP",
        "0x0000000000000000000000000000000000000006": "BN256_ADD",
        "0x0000000000000000000000000000000000000007": "BN256_MUL",
        "0x0000000000000000000000000000000000000008": "BN256_PAIRING",
        "0x0000000000000000000000000000000000000009": "BLAKE2F",
        "0x000000000000000000000000000000000000000a": "KZG_POINT_EVALUATION",
        "0x000000000000000000000000000000000000000b": "BLS12_G1ADD",
        "0x000000000000000000000000000000000000000c": "BLS12_G1MSM",
        "0x000000000000000000000000000000000000000d": "BLS12_G2ADD",
        "0x000000000000000000000000000000000000000e": "BLS12_G2MSM",
        "0x000000000000000000000000000000000000000f": "BLS12_PAIRING_CHECK",
        "0x0000000000000000000000000000000000000010": "BLS12_MAP_FP_TO_G1",
        "0x0000000000000000000000000000000000000011": "BLS12_MAP_FP2_TO_G2"
      },
      "systemContracts": {
        "BEACON_ROOTS_ADDRESS": "0x000f3df6d732807ef1319fb7b8bb8522d0beac02",
        "CONSOLIDATION_REQUEST_PREDEPLOY_ADDRESS": "0x0000bbddc7ce488642fb579f8b00f3a590007251",
        "DEPOSIT_CONTRACT_ADDRESS": "0x00000000219ab540356cbb839cbe05303d7705fa",
        "HISTORY_STORAGE_ADDRESS": "0x0000f90827f1c53a10cb7a02335b175320002935",
        "WITHDRAWAL_REQUEST_PREDEPLOY_ADDRESS": "0x00000961ef480eb55e80d19ad83579a64c007002"
      }
    },
    "nextHash": "10368496",
    "nextForkId": "0929e24e"
}
"""


@pytest.fixture
def eth_config_response() -> EthConfigResponse:
    """Get the `eth_config` response from the client to be verified by all tests."""
    return EthConfigResponse.model_validate_json(eth_config_json_data)


def test_fork_config_get_hash(eth_config_response: EthConfigResponse) -> None:
    """Test the `get_hash` method of the `ForkConfig` class."""
    assert eth_config_response.current is not None
    assert eth_config_response.current_hash is not None
    assert eth_config_response.current.get_hash() == eth_config_response.current_hash, (
        "Current fork config hash does not match expected value: "
        f"{eth_config_response.current.get_hash()} != {eth_config_response.current_hash}"
    )
    assert eth_config_response.next is not None
    assert eth_config_response.next_hash is not None
    assert eth_config_response.next.get_hash() == eth_config_response.next_hash, (
        "Next fork config hash does not match expected value: "
        f"{eth_config_response.next.get_hash()} != {eth_config_response.next_hash}"
    )
