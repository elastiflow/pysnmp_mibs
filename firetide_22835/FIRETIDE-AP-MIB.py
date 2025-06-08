# SNMP MIB module (FIRETIDE-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/firetide_22835/FIRETIDE-AP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:02:57 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(CountryCode,
 VerifyOperation,
 firetide) = mibBuilder.importSymbols(
    "FIRETIDE-MESH-MIB",
    "CountryCode",
    "VerifyOperation",
    "firetide")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

firetideAp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApRadioMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("radio108gStaticTurbo", 1),
          ("radio80211a", 2),
          ("radio80211aStaticTurbo", 3),
          ("radio80211b", 4),
          ("radio80211bg", 5),
          ("radio80211g", 6))
    )



class ApRadioDataRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              11,
              12,
              18,
              24,
              36,
              48,
              54,
              72,
              96,
              108)
        )
    )
    namedValues = NamedValues(
        *(("radioDataRateAuto", 0),
          ("radioDataRate1M", 1),
          ("radioDataRate2M", 2),
          ("radioDataRate5dot5M", 5),
          ("radioDataRate6M", 6),
          ("radioDataRate11M", 11),
          ("radioDataRate12M", 12),
          ("radioDataRate18M", 18),
          ("radioDataRate24M", 24),
          ("radioDataRate36M", 36),
          ("radioDataRate48M", 48),
          ("radioDataRate54M", 54),
          ("radioDataRate72M", 72),
          ("radioDataRate96M", 96),
          ("radioDataRate108M", 108))
    )



class ApAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("authOpen", 1),
          ("authShared", 2),
          ("auth801x", 3),
          ("authAuto", 4),
          ("authWpa", 5),
          ("authWpaPsk", 6),
          ("authWpa2", 7),
          ("authWpa2Psk", 8),
          ("authWpaAuto", 9),
          ("authWpaAutoPsk", 10))
    )



class ApCipherType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cipherWep", 1),
          ("cipherTkip", 2),
          ("cipherAesOcb", 3),
          ("cipherAesCcm", 4),
          ("cipherCkip", 5),
          ("cipherNone", 6))
    )



# MIB Managed Objects in the order of their OIDs

_FiretideApNode_ObjectIdentity = ObjectIdentity
firetideApNode = _FiretideApNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1)
)
_ApTable_Object = MibTable
apTable = _ApTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1)
)
if mibBuilder.loadTexts:
    apTable.setStatus("current")
_ApEntry_Object = MibTableRow
apEntry = _ApEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1)
)
apEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
)
if mibBuilder.loadTexts:
    apEntry.setStatus("current")
_ApNodeIndex_Type = Integer32
_ApNodeIndex_Object = MibTableColumn
apNodeIndex = _ApNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 1),
    _ApNodeIndex_Type()
)
apNodeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNodeIndex.setStatus("current")


class _ApDhcpState_Type(TruthValue):
    """Custom type apDhcpState based on TruthValue"""
    defaultValue = 1


_ApDhcpState_Type.__name__ = "TruthValue"
_ApDhcpState_Object = MibTableColumn
apDhcpState = _ApDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 2),
    _ApDhcpState_Type()
)
apDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDhcpState.setStatus("current")
_ApIpAddress_Type = IpAddress
_ApIpAddress_Object = MibTableColumn
apIpAddress = _ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 3),
    _ApIpAddress_Type()
)
apIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAddress.setStatus("current")
_ApIpMask_Type = IpAddress
_ApIpMask_Object = MibTableColumn
apIpMask = _ApIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 4),
    _ApIpMask_Type()
)
apIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpMask.setStatus("current")
_ApDefaultGateway_Type = IpAddress
_ApDefaultGateway_Object = MibTableColumn
apDefaultGateway = _ApDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 5),
    _ApDefaultGateway_Type()
)
apDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDefaultGateway.setStatus("current")
_ApName_Type = DisplayString
_ApName_Object = MibTableColumn
apName = _ApName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 6),
    _ApName_Type()
)
apName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apName.setStatus("current")
_ApGroupName_Type = DisplayString
_ApGroupName_Object = MibTableColumn
apGroupName = _ApGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 7),
    _ApGroupName_Type()
)
apGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGroupName.setStatus("current")


class _ApMgmtVlanEnable_Type(TruthValue):
    """Custom type apMgmtVlanEnable based on TruthValue"""
    defaultValue = 2


_ApMgmtVlanEnable_Type.__name__ = "TruthValue"
_ApMgmtVlanEnable_Object = MibTableColumn
apMgmtVlanEnable = _ApMgmtVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 8),
    _ApMgmtVlanEnable_Type()
)
apMgmtVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMgmtVlanEnable.setStatus("current")


class _ApMgmtVlanId_Type(Integer32):
    """Custom type apMgmtVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ApMgmtVlanId_Type.__name__ = "Integer32"
_ApMgmtVlanId_Object = MibTableColumn
apMgmtVlanId = _ApMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 9),
    _ApMgmtVlanId_Type()
)
apMgmtVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMgmtVlanId.setStatus("current")
_ApSoftwareVer_Type = DisplayString
_ApSoftwareVer_Object = MibTableColumn
apSoftwareVer = _ApSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 10),
    _ApSoftwareVer_Type()
)
apSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVer.setStatus("current")


class _ApSerialNo_Type(DisplayString):
    """Custom type apSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_ApSerialNo_Type.__name__ = "DisplayString"
_ApSerialNo_Object = MibTableColumn
apSerialNo = _ApSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 11),
    _ApSerialNo_Type()
)
apSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialNo.setStatus("current")
_ApMacAddr_Type = MacAddress
_ApMacAddr_Object = MibTableColumn
apMacAddr = _ApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 12),
    _ApMacAddr_Type()
)
apMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacAddr.setStatus("current")
_ApRadioMacAddr_Type = MacAddress
_ApRadioMacAddr_Object = MibTableColumn
apRadioMacAddr = _ApRadioMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 13),
    _ApRadioMacAddr_Type()
)
apRadioMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioMacAddr.setStatus("current")


class _ApNodeOperations_Type(Integer32):
    """Custom type apNodeOperations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("operationCompleted", 1),
          ("operationErrorTryAgain", 2),
          ("applyPending", 3),
          ("applyApInProgress", 4),
          ("rollbackApConfig", 5),
          ("applyApConfig", 6),
          ("rebootAp", 7),
          ("factoryResetAp", 8),
          ("loginToAp", 9),
          ("apDownOrDisconnected", 10),
          ("apConnectionFailed", 11),
          ("apLoginFailed", 12))
    )


_ApNodeOperations_Type.__name__ = "Integer32"
_ApNodeOperations_Object = MibTableColumn
apNodeOperations = _ApNodeOperations_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 14),
    _ApNodeOperations_Type()
)
apNodeOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNodeOperations.setStatus("current")


class _ApNodeErrorString_Type(DisplayString):
    """Custom type apNodeErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApNodeErrorString_Type.__name__ = "DisplayString"
_ApNodeErrorString_Object = MibTableColumn
apNodeErrorString = _ApNodeErrorString_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 15),
    _ApNodeErrorString_Type()
)
apNodeErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNodeErrorString.setStatus("current")


class _ApSelectForUpgrade_Type(Integer32):
    """Custom type apSelectForUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("includeInUpgrade", 1),
          ("excludeFromUpgrade", 2))
    )


_ApSelectForUpgrade_Type.__name__ = "Integer32"
_ApSelectForUpgrade_Object = MibTableColumn
apSelectForUpgrade = _ApSelectForUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 16),
    _ApSelectForUpgrade_Type()
)
apSelectForUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSelectForUpgrade.setStatus("current")


class _ApSoftwareUpgradeCompletion_Type(Integer32):
    """Custom type apSoftwareUpgradeCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSoftwareUpgradeCompletion_Type.__name__ = "Integer32"
_ApSoftwareUpgradeCompletion_Object = MibTableColumn
apSoftwareUpgradeCompletion = _ApSoftwareUpgradeCompletion_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 17),
    _ApSoftwareUpgradeCompletion_Type()
)
apSoftwareUpgradeCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareUpgradeCompletion.setStatus("current")
_ApNodeStatus_Type = RowStatus
_ApNodeStatus_Object = MibTableColumn
apNodeStatus = _ApNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 1, 1, 30),
    _ApNodeStatus_Type()
)
apNodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNodeStatus.setStatus("current")
_StandaloneApTable_Object = MibTable
standaloneApTable = _StandaloneApTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 2)
)
if mibBuilder.loadTexts:
    standaloneApTable.setStatus("current")
_StandaloneApEntry_Object = MibTableRow
standaloneApEntry = _StandaloneApEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 2, 1)
)
standaloneApEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "standaloneApIpAddress"),
)
if mibBuilder.loadTexts:
    standaloneApEntry.setStatus("current")
_StandaloneApIpAddress_Type = IpAddress
_StandaloneApIpAddress_Object = MibTableColumn
standaloneApIpAddress = _StandaloneApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 2, 1, 1),
    _StandaloneApIpAddress_Type()
)
standaloneApIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    standaloneApIpAddress.setStatus("current")
_StandaloneApNodeStatus_Type = RowStatus
_StandaloneApNodeStatus_Object = MibTableColumn
standaloneApNodeStatus = _StandaloneApNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 2, 1, 10),
    _StandaloneApNodeStatus_Type()
)
standaloneApNodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standaloneApNodeStatus.setStatus("current")
_ApSoftwareUpgradePath_Type = DisplayString
_ApSoftwareUpgradePath_Object = MibScalar
apSoftwareUpgradePath = _ApSoftwareUpgradePath_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 3),
    _ApSoftwareUpgradePath_Type()
)
apSoftwareUpgradePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSoftwareUpgradePath.setStatus("current")


class _ApSoftwareUpgrade_Type(Integer32):
    """Custom type apSoftwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("upgradeAll", 1),
          ("upgradeForce", 2),
          ("upgradeFailed", 3),
          ("upgradeInProgress", 4),
          ("upgradeCompleted", 5),
          ("upgradeSelective", 6),
          ("upgradeCancel", 7))
    )


_ApSoftwareUpgrade_Type.__name__ = "Integer32"
_ApSoftwareUpgrade_Object = MibScalar
apSoftwareUpgrade = _ApSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 4),
    _ApSoftwareUpgrade_Type()
)
apSoftwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSoftwareUpgrade.setStatus("current")
_ApLoginUserName_Type = DisplayString
_ApLoginUserName_Object = MibScalar
apLoginUserName = _ApLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 5),
    _ApLoginUserName_Type()
)
apLoginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoginUserName.setStatus("current")
_ApLoginPasswd_Type = DisplayString
_ApLoginPasswd_Object = MibScalar
apLoginPasswd = _ApLoginPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 6),
    _ApLoginPasswd_Type()
)
apLoginPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLoginPasswd.setStatus("current")
_ApLoginErrorMessage_Type = DisplayString
_ApLoginErrorMessage_Object = MibScalar
apLoginErrorMessage = _ApLoginErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 1, 7),
    _ApLoginErrorMessage_Type()
)
apLoginErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLoginErrorMessage.setStatus("current")
_FiretideApVap_ObjectIdentity = ObjectIdentity
firetideApVap = _FiretideApVap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2)
)
_VapGroupConfigTable_Object = MibTable
vapGroupConfigTable = _VapGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vapGroupConfigTable.setStatus("current")
_VapGroupConfigEntry_Object = MibTableRow
vapGroupConfigEntry = _VapGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1)
)
vapGroupConfigEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
)
if mibBuilder.loadTexts:
    vapGroupConfigEntry.setStatus("current")
_VapGroupName_Type = DisplayString
_VapGroupName_Object = MibTableColumn
vapGroupName = _VapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 1),
    _VapGroupName_Type()
)
vapGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vapGroupName.setStatus("current")


class _VapEnable_Type(TruthValue):
    """Custom type vapEnable based on TruthValue"""
    defaultValue = 2


_VapEnable_Type.__name__ = "TruthValue"
_VapEnable_Object = MibTableColumn
vapEnable = _VapEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 2),
    _VapEnable_Type()
)
vapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEnable.setStatus("current")


class _VapGroupSsid_Type(OctetString):
    """Custom type vapGroupSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VapGroupSsid_Type.__name__ = "OctetString"
_VapGroupSsid_Object = MibTableColumn
vapGroupSsid = _VapGroupSsid_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 3),
    _VapGroupSsid_Type()
)
vapGroupSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapGroupSsid.setStatus("current")


class _VapSsidSuppress_Type(TruthValue):
    """Custom type vapSsidSuppress based on TruthValue"""
    defaultValue = 2


_VapSsidSuppress_Type.__name__ = "TruthValue"
_VapSsidSuppress_Object = MibTableColumn
vapSsidSuppress = _VapSsidSuppress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 4),
    _VapSsidSuppress_Type()
)
vapSsidSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapSsidSuppress.setStatus("current")


class _VapDtimPeriod_Type(Integer32):
    """Custom type vapDtimPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VapDtimPeriod_Type.__name__ = "Integer32"
_VapDtimPeriod_Object = MibTableColumn
vapDtimPeriod = _VapDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 5),
    _VapDtimPeriod_Type()
)
vapDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDtimPeriod.setStatus("current")


class _VapFragmentationThreshold_Type(Integer32):
    """Custom type vapFragmentationThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_VapFragmentationThreshold_Type.__name__ = "Integer32"
_VapFragmentationThreshold_Object = MibTableColumn
vapFragmentationThreshold = _VapFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 6),
    _VapFragmentationThreshold_Type()
)
vapFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapFragmentationThreshold.setStatus("current")


class _VapRtsThreshold_Type(Integer32):
    """Custom type vapRtsThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2346),
    )


_VapRtsThreshold_Type.__name__ = "Integer32"
_VapRtsThreshold_Object = MibTableColumn
vapRtsThreshold = _VapRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 7),
    _VapRtsThreshold_Type()
)
vapRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRtsThreshold.setStatus("current")


class _VapVlanEnable_Type(TruthValue):
    """Custom type vapVlanEnable based on TruthValue"""
    defaultValue = 2


_VapVlanEnable_Type.__name__ = "TruthValue"
_VapVlanEnable_Object = MibTableColumn
vapVlanEnable = _VapVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 8),
    _VapVlanEnable_Type()
)
vapVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapVlanEnable.setStatus("current")


class _VapVlanId_Type(Integer32):
    """Custom type vapVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VapVlanId_Type.__name__ = "Integer32"
_VapVlanId_Object = MibTableColumn
vapVlanId = _VapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 9),
    _VapVlanId_Type()
)
vapVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapVlanId.setStatus("current")


class _VapWdsEnable_Type(TruthValue):
    """Custom type vapWdsEnable based on TruthValue"""
    defaultValue = 2


_VapWdsEnable_Type.__name__ = "TruthValue"
_VapWdsEnable_Object = MibTableColumn
vapWdsEnable = _VapWdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 10),
    _VapWdsEnable_Type()
)
vapWdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWdsEnable.setStatus("current")


class _VapRateLimitEnable_Type(TruthValue):
    """Custom type vapRateLimitEnable based on TruthValue"""
    defaultValue = 2


_VapRateLimitEnable_Type.__name__ = "TruthValue"
_VapRateLimitEnable_Object = MibTableColumn
vapRateLimitEnable = _VapRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 11),
    _VapRateLimitEnable_Type()
)
vapRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRateLimitEnable.setStatus("current")


class _VapRateLimit_Type(Integer32):
    """Custom type vapRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 5120),
    )


_VapRateLimit_Type.__name__ = "Integer32"
_VapRateLimit_Object = MibTableColumn
vapRateLimit = _VapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 12),
    _VapRateLimit_Type()
)
vapRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRateLimit.setStatus("current")


class _VapUserRateLimitEnable_Type(TruthValue):
    """Custom type vapUserRateLimitEnable based on TruthValue"""
    defaultValue = 2


_VapUserRateLimitEnable_Type.__name__ = "TruthValue"
_VapUserRateLimitEnable_Object = MibTableColumn
vapUserRateLimitEnable = _VapUserRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 13),
    _VapUserRateLimitEnable_Type()
)
vapUserRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapUserRateLimitEnable.setStatus("current")


class _VapUserRateLimit_Type(Integer32):
    """Custom type vapUserRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 5120),
    )


_VapUserRateLimit_Type.__name__ = "Integer32"
_VapUserRateLimit_Object = MibTableColumn
vapUserRateLimit = _VapUserRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 14),
    _VapUserRateLimit_Type()
)
vapUserRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapUserRateLimit.setStatus("current")


class _VapIcbEnable_Type(TruthValue):
    """Custom type vapIcbEnable based on TruthValue"""
    defaultValue = 2


_VapIcbEnable_Type.__name__ = "TruthValue"
_VapIcbEnable_Object = MibTableColumn
vapIcbEnable = _VapIcbEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 15),
    _VapIcbEnable_Type()
)
vapIcbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapIcbEnable.setStatus("current")


class _VapIappEnable_Type(TruthValue):
    """Custom type vapIappEnable based on TruthValue"""
    defaultValue = 2


_VapIappEnable_Type.__name__ = "TruthValue"
_VapIappEnable_Object = MibTableColumn
vapIappEnable = _VapIappEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 16),
    _VapIappEnable_Type()
)
vapIappEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapIappEnable.setStatus("current")


class _VapIappPort_Type(Integer32):
    """Custom type vapIappPort based on Integer32"""
    defaultValue = 4001

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_VapIappPort_Type.__name__ = "Integer32"
_VapIappPort_Object = MibTableColumn
vapIappPort = _VapIappPort_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 17),
    _VapIappPort_Type()
)
vapIappPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapIappPort.setStatus("current")


class _VapWmmEnable_Type(TruthValue):
    """Custom type vapWmmEnable based on TruthValue"""
    defaultValue = 2


_VapWmmEnable_Type.__name__ = "TruthValue"
_VapWmmEnable_Object = MibTableColumn
vapWmmEnable = _VapWmmEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 18),
    _VapWmmEnable_Type()
)
vapWmmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWmmEnable.setStatus("current")


class _VapConfigApply_Type(Integer32):
    """Custom type vapConfigApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configChangeApplied", 1),
          ("applyErrorTryAgain", 2),
          ("applyPending", 3),
          ("applyInProgress", 4),
          ("rollbackConfig", 5),
          ("applyToVap", 6),
          ("reconcileConfig", 7))
    )


_VapConfigApply_Type.__name__ = "Integer32"
_VapConfigApply_Object = MibTableColumn
vapConfigApply = _VapConfigApply_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 19),
    _VapConfigApply_Type()
)
vapConfigApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapConfigApply.setStatus("current")


class _VapConfigErrorString_Type(DisplayString):
    """Custom type vapConfigErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VapConfigErrorString_Type.__name__ = "DisplayString"
_VapConfigErrorString_Object = MibTableColumn
vapConfigErrorString = _VapConfigErrorString_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 20),
    _VapConfigErrorString_Type()
)
vapConfigErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapConfigErrorString.setStatus("current")
_VapConfigVerify_Type = VerifyOperation
_VapConfigVerify_Object = MibTableColumn
vapConfigVerify = _VapConfigVerify_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 21),
    _VapConfigVerify_Type()
)
vapConfigVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapConfigVerify.setStatus("current")
_VapConfigComparison_Type = DisplayString
_VapConfigComparison_Object = MibTableColumn
vapConfigComparison = _VapConfigComparison_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 22),
    _VapConfigComparison_Type()
)
vapConfigComparison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapConfigComparison.setStatus("current")
_VapGroupStatus_Type = RowStatus
_VapGroupStatus_Object = MibTableColumn
vapGroupStatus = _VapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 1, 1, 30),
    _VapGroupStatus_Type()
)
vapGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vapGroupStatus.setStatus("current")
_VapSpecificConfigTable_Object = MibTable
vapSpecificConfigTable = _VapSpecificConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2)
)
if mibBuilder.loadTexts:
    vapSpecificConfigTable.setStatus("current")
_VapSpecificConfigEntry_Object = MibTableRow
vapSpecificConfigEntry = _VapSpecificConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1)
)
vapSpecificConfigEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
)
if mibBuilder.loadTexts:
    vapSpecificConfigEntry.setStatus("current")
_VapIpAddress_Type = IpAddress
_VapIpAddress_Object = MibTableColumn
vapIpAddress = _VapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 1),
    _VapIpAddress_Type()
)
vapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapIpAddress.setStatus("current")
_VapIpMask_Type = IpAddress
_VapIpMask_Object = MibTableColumn
vapIpMask = _VapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 2),
    _VapIpMask_Type()
)
vapIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapIpMask.setStatus("current")


class _VapDhcpServerEnable_Type(TruthValue):
    """Custom type vapDhcpServerEnable based on TruthValue"""
    defaultValue = 2


_VapDhcpServerEnable_Type.__name__ = "TruthValue"
_VapDhcpServerEnable_Object = MibTableColumn
vapDhcpServerEnable = _VapDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 3),
    _VapDhcpServerEnable_Type()
)
vapDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpServerEnable.setStatus("current")


class _VapDhcpRenewalTime_Type(Integer32):
    """Custom type vapDhcpRenewalTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 864000),
    )


_VapDhcpRenewalTime_Type.__name__ = "Integer32"
_VapDhcpRenewalTime_Object = MibTableColumn
vapDhcpRenewalTime = _VapDhcpRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 4),
    _VapDhcpRenewalTime_Type()
)
vapDhcpRenewalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpRenewalTime.setStatus("current")
_VapDhcpStartIp_Type = IpAddress
_VapDhcpStartIp_Object = MibTableColumn
vapDhcpStartIp = _VapDhcpStartIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 5),
    _VapDhcpStartIp_Type()
)
vapDhcpStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpStartIp.setStatus("current")
_VapDhcpEndIp_Type = IpAddress
_VapDhcpEndIp_Object = MibTableColumn
vapDhcpEndIp = _VapDhcpEndIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 6),
    _VapDhcpEndIp_Type()
)
vapDhcpEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpEndIp.setStatus("current")
_VapDhcpRouter_Type = IpAddress
_VapDhcpRouter_Object = MibTableColumn
vapDhcpRouter = _VapDhcpRouter_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 7),
    _VapDhcpRouter_Type()
)
vapDhcpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpRouter.setStatus("current")


class _VapDhcpDnsEnable_Type(TruthValue):
    """Custom type vapDhcpDnsEnable based on TruthValue"""
    defaultValue = 2


_VapDhcpDnsEnable_Type.__name__ = "TruthValue"
_VapDhcpDnsEnable_Object = MibTableColumn
vapDhcpDnsEnable = _VapDhcpDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 8),
    _VapDhcpDnsEnable_Type()
)
vapDhcpDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpDnsEnable.setStatus("current")
_VapDhcpPrimaryDns_Type = IpAddress
_VapDhcpPrimaryDns_Object = MibTableColumn
vapDhcpPrimaryDns = _VapDhcpPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 9),
    _VapDhcpPrimaryDns_Type()
)
vapDhcpPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpPrimaryDns.setStatus("current")
_VapDhcpSecondaryDns_Type = IpAddress
_VapDhcpSecondaryDns_Object = MibTableColumn
vapDhcpSecondaryDns = _VapDhcpSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 10),
    _VapDhcpSecondaryDns_Type()
)
vapDhcpSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapDhcpSecondaryDns.setStatus("current")


class _VapGatewayEnable_Type(TruthValue):
    """Custom type vapGatewayEnable based on TruthValue"""
    defaultValue = 2


_VapGatewayEnable_Type.__name__ = "TruthValue"
_VapGatewayEnable_Object = MibTableColumn
vapGatewayEnable = _VapGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 11),
    _VapGatewayEnable_Type()
)
vapGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapGatewayEnable.setStatus("current")
_VapNatEnable_Type = TruthValue
_VapNatEnable_Object = MibTableColumn
vapNatEnable = _VapNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 12),
    _VapNatEnable_Type()
)
vapNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapNatEnable.setStatus("current")
_VapNatPublicIp_Type = IpAddress
_VapNatPublicIp_Object = MibTableColumn
vapNatPublicIp = _VapNatPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 13),
    _VapNatPublicIp_Type()
)
vapNatPublicIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapNatPublicIp.setStatus("current")


class _VapWdsOpMode_Type(Integer32):
    """Custom type vapWdsOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("station", 2))
    )


_VapWdsOpMode_Type.__name__ = "Integer32"
_VapWdsOpMode_Object = MibTableColumn
vapWdsOpMode = _VapWdsOpMode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 14),
    _VapWdsOpMode_Type()
)
vapWdsOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWdsOpMode.setStatus("current")
_VapSpecificConfigStatus_Type = RowStatus
_VapSpecificConfigStatus_Object = MibTableColumn
vapSpecificConfigStatus = _VapSpecificConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 2, 2, 1, 30),
    _VapSpecificConfigStatus_Type()
)
vapSpecificConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vapSpecificConfigStatus.setStatus("current")
_FiretideApRadio_ObjectIdentity = ObjectIdentity
firetideApRadio = _FiretideApRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3)
)
_ApRadioTable_Object = MibTable
apRadioTable = _ApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1)
)
if mibBuilder.loadTexts:
    apRadioTable.setStatus("current")
_ApRadioEntry_Object = MibTableRow
apRadioEntry = _ApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1)
)
apRadioEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
)
if mibBuilder.loadTexts:
    apRadioEntry.setStatus("current")
_ApRadioCountryCode_Type = CountryCode
_ApRadioCountryCode_Object = MibTableColumn
apRadioCountryCode = _ApRadioCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 1),
    _ApRadioCountryCode_Type()
)
apRadioCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioCountryCode.setStatus("current")
_ApRadioMode_Type = ApRadioMode
_ApRadioMode_Object = MibTableColumn
apRadioMode = _ApRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 2),
    _ApRadioMode_Type()
)
apRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioMode.setStatus("current")
_ApChannelAutoSelectEnable_Type = TruthValue
_ApChannelAutoSelectEnable_Object = MibTableColumn
apChannelAutoSelectEnable = _ApChannelAutoSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 3),
    _ApChannelAutoSelectEnable_Type()
)
apChannelAutoSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apChannelAutoSelectEnable.setStatus("current")
_ApRadioChannel_Type = Integer32
_ApRadioChannel_Object = MibTableColumn
apRadioChannel = _ApRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 4),
    _ApRadioChannel_Type()
)
apRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioChannel.setStatus("current")


class _ApRadioDataRate_Type(ApRadioDataRate):
    """Custom type apRadioDataRate based on ApRadioDataRate"""
    defaultValue = 0


_ApRadioDataRate_Type.__name__ = "ApRadioDataRate"
_ApRadioDataRate_Object = MibTableColumn
apRadioDataRate = _ApRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 5),
    _ApRadioDataRate_Type()
)
apRadioDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioDataRate.setStatus("current")


class _ApRadioTransmitPower_Type(Integer32):
    """Custom type apRadioTransmitPower based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 27),
    )


_ApRadioTransmitPower_Type.__name__ = "Integer32"
_ApRadioTransmitPower_Object = MibTableColumn
apRadioTransmitPower = _ApRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 6),
    _ApRadioTransmitPower_Type()
)
apRadioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioTransmitPower.setStatus("current")


class _ApRadioBeaconInterval_Type(Integer32):
    """Custom type apRadioBeaconInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
    )


_ApRadioBeaconInterval_Type.__name__ = "Integer32"
_ApRadioBeaconInterval_Object = MibTableColumn
apRadioBeaconInterval = _ApRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 7),
    _ApRadioBeaconInterval_Type()
)
apRadioBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioBeaconInterval.setStatus("current")


class _ApRadioAntennaType_Type(Integer32):
    """Custom type apRadioAntennaType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("antenna1", 1),
          ("antenna2", 2),
          ("diversity", 3))
    )


_ApRadioAntennaType_Type.__name__ = "Integer32"
_ApRadioAntennaType_Object = MibTableColumn
apRadioAntennaType = _ApRadioAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 8),
    _ApRadioAntennaType_Type()
)
apRadioAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioAntennaType.setStatus("current")
_ApRogueApDetection_Type = TruthValue
_ApRogueApDetection_Object = MibTableColumn
apRogueApDetection = _ApRogueApDetection_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 9),
    _ApRogueApDetection_Type()
)
apRogueApDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRogueApDetection.setStatus("current")


class _ApRogueApDetectionPeriodicty_Type(Integer32):
    """Custom type apRogueApDetectionPeriodicty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ApRogueApDetectionPeriodicty_Type.__name__ = "Integer32"
_ApRogueApDetectionPeriodicty_Object = MibTableColumn
apRogueApDetectionPeriodicty = _ApRogueApDetectionPeriodicty_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 10),
    _ApRogueApDetectionPeriodicty_Type()
)
apRogueApDetectionPeriodicty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRogueApDetectionPeriodicty.setStatus("current")


class _ApRogueApDetectionLevel_Type(Integer32):
    """Custom type apRogueApDetectionLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_ApRogueApDetectionLevel_Type.__name__ = "Integer32"
_ApRogueApDetectionLevel_Object = MibTableColumn
apRogueApDetectionLevel = _ApRogueApDetectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 11),
    _ApRogueApDetectionLevel_Type()
)
apRogueApDetectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRogueApDetectionLevel.setStatus("current")
_ApRadioStatus_Type = RowStatus
_ApRadioStatus_Object = MibTableColumn
apRadioStatus = _ApRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 3, 1, 1, 20),
    _ApRadioStatus_Type()
)
apRadioStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadioStatus.setStatus("current")
_FiretideApSecurity_ObjectIdentity = ObjectIdentity
firetideApSecurity = _FiretideApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4)
)
_VapSecurityTable_Object = MibTable
vapSecurityTable = _VapSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vapSecurityTable.setStatus("current")
_VapSecurityEntry_Object = MibTableRow
vapSecurityEntry = _VapSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1)
)
vapSecurityEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
)
if mibBuilder.loadTexts:
    vapSecurityEntry.setStatus("current")


class _VapSecurityEnable_Type(TruthValue):
    """Custom type vapSecurityEnable based on TruthValue"""
    defaultValue = 2


_VapSecurityEnable_Type.__name__ = "TruthValue"
_VapSecurityEnable_Object = MibTableColumn
vapSecurityEnable = _VapSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 1),
    _VapSecurityEnable_Type()
)
vapSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapSecurityEnable.setStatus("current")
_VapAuthType_Type = ApAuthType
_VapAuthType_Object = MibTableColumn
vapAuthType = _VapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 2),
    _VapAuthType_Type()
)
vapAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAuthType.setStatus("current")
_VapCipherType_Type = ApCipherType
_VapCipherType_Object = MibTableColumn
vapCipherType = _VapCipherType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 3),
    _VapCipherType_Type()
)
vapCipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapCipherType.setStatus("current")


class _VapKey1_Type(OctetString):
    """Custom type vapKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(26, 26),
    )


_VapKey1_Type.__name__ = "OctetString"
_VapKey1_Object = MibTableColumn
vapKey1 = _VapKey1_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 4),
    _VapKey1_Type()
)
vapKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKey1.setStatus("current")


class _VapKey2_Type(OctetString):
    """Custom type vapKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(26, 26),
    )


_VapKey2_Type.__name__ = "OctetString"
_VapKey2_Object = MibTableColumn
vapKey2 = _VapKey2_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 5),
    _VapKey2_Type()
)
vapKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKey2.setStatus("current")


class _VapKey3_Type(OctetString):
    """Custom type vapKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(26, 26),
    )


_VapKey3_Type.__name__ = "OctetString"
_VapKey3_Object = MibTableColumn
vapKey3 = _VapKey3_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 6),
    _VapKey3_Type()
)
vapKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKey3.setStatus("current")


class _VapKey4_Type(OctetString):
    """Custom type vapKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(26, 26),
    )


_VapKey4_Type.__name__ = "OctetString"
_VapKey4_Object = MibTableColumn
vapKey4 = _VapKey4_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 7),
    _VapKey4_Type()
)
vapKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKey4.setStatus("current")


class _VapKeyIndex_Type(Integer32):
    """Custom type vapKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_VapKeyIndex_Type.__name__ = "Integer32"
_VapKeyIndex_Object = MibTableColumn
vapKeyIndex = _VapKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 8),
    _VapKeyIndex_Type()
)
vapKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKeyIndex.setStatus("current")


class _VapPassPhrase_Type(OctetString):
    """Custom type vapPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_VapPassPhrase_Type.__name__ = "OctetString"
_VapPassPhrase_Object = MibTableColumn
vapPassPhrase = _VapPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 9),
    _VapPassPhrase_Type()
)
vapPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapPassPhrase.setStatus("current")


class _VapKeyInputType_Type(Integer32):
    """Custom type vapKeyInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_VapKeyInputType_Type.__name__ = "Integer32"
_VapKeyInputType_Object = MibTableColumn
vapKeyInputType = _VapKeyInputType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 10),
    _VapKeyInputType_Type()
)
vapKeyInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapKeyInputType.setStatus("current")


class _VapGroupKeyUpdate_Type(Integer32):
    """Custom type vapGroupKeyUpdate based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VapGroupKeyUpdate_Type.__name__ = "Integer32"
_VapGroupKeyUpdate_Object = MibTableColumn
vapGroupKeyUpdate = _VapGroupKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 11),
    _VapGroupKeyUpdate_Type()
)
vapGroupKeyUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapGroupKeyUpdate.setStatus("current")
_VapRadiusIp_Type = IpAddress
_VapRadiusIp_Object = MibTableColumn
vapRadiusIp = _VapRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 12),
    _VapRadiusIp_Type()
)
vapRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRadiusIp.setStatus("current")


class _VapRadiusPort_Type(Integer32):
    """Custom type vapRadiusPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_VapRadiusPort_Type.__name__ = "Integer32"
_VapRadiusPort_Object = MibTableColumn
vapRadiusPort = _VapRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 13),
    _VapRadiusPort_Type()
)
vapRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRadiusPort.setStatus("current")


class _VapRadiusSecretKey_Type(OctetString):
    """Custom type vapRadiusSecretKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_VapRadiusSecretKey_Type.__name__ = "OctetString"
_VapRadiusSecretKey_Object = MibTableColumn
vapRadiusSecretKey = _VapRadiusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 14),
    _VapRadiusSecretKey_Type()
)
vapRadiusSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRadiusSecretKey.setStatus("current")


class _VapAclPolicy_Type(Integer32):
    """Custom type vapAclPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_VapAclPolicy_Type.__name__ = "Integer32"
_VapAclPolicy_Object = MibTableColumn
vapAclPolicy = _VapAclPolicy_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 15),
    _VapAclPolicy_Type()
)
vapAclPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAclPolicy.setStatus("current")
_VapSecurityStatus_Type = RowStatus
_VapSecurityStatus_Object = MibTableColumn
vapSecurityStatus = _VapSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 1, 1, 20),
    _VapSecurityStatus_Type()
)
vapSecurityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vapSecurityStatus.setStatus("current")
_ApSecurityTable_Object = MibTable
apSecurityTable = _ApSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2)
)
if mibBuilder.loadTexts:
    apSecurityTable.setStatus("current")
_ApSecurityEntry_Object = MibTableRow
apSecurityEntry = _ApSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1)
)
apSecurityEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
)
if mibBuilder.loadTexts:
    apSecurityEntry.setStatus("current")


class _ApSecurityFirewallEnable_Type(TruthValue):
    """Custom type apSecurityFirewallEnable based on TruthValue"""
    defaultValue = 2


_ApSecurityFirewallEnable_Type.__name__ = "TruthValue"
_ApSecurityFirewallEnable_Object = MibTableColumn
apSecurityFirewallEnable = _ApSecurityFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1, 1),
    _ApSecurityFirewallEnable_Type()
)
apSecurityFirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityFirewallEnable.setStatus("current")


class _ApSecurityVpnEnable_Type(TruthValue):
    """Custom type apSecurityVpnEnable based on TruthValue"""
    defaultValue = 2


_ApSecurityVpnEnable_Type.__name__ = "TruthValue"
_ApSecurityVpnEnable_Object = MibTableColumn
apSecurityVpnEnable = _ApSecurityVpnEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1, 2),
    _ApSecurityVpnEnable_Type()
)
apSecurityVpnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityVpnEnable.setStatus("current")
_ApSecurityVpnRemoteIp_Type = IpAddress
_ApSecurityVpnRemoteIp_Object = MibTableColumn
apSecurityVpnRemoteIp = _ApSecurityVpnRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1, 3),
    _ApSecurityVpnRemoteIp_Type()
)
apSecurityVpnRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityVpnRemoteIp.setStatus("current")


class _ApSecurityVpnPassphrase_Type(OctetString):
    """Custom type apSecurityVpnPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_ApSecurityVpnPassphrase_Type.__name__ = "OctetString"
_ApSecurityVpnPassphrase_Object = MibTableColumn
apSecurityVpnPassphrase = _ApSecurityVpnPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1, 4),
    _ApSecurityVpnPassphrase_Type()
)
apSecurityVpnPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecurityVpnPassphrase.setStatus("current")
_ApSecurityStatus_Type = RowStatus
_ApSecurityStatus_Object = MibTableColumn
apSecurityStatus = _ApSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 2, 1, 10),
    _ApSecurityStatus_Type()
)
apSecurityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSecurityStatus.setStatus("current")
_VapAclTable_Object = MibTable
vapAclTable = _VapAclTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 3)
)
if mibBuilder.loadTexts:
    vapAclTable.setStatus("current")
_VapAclEntry_Object = MibTableRow
vapAclEntry = _VapAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 3, 1)
)
vapAclEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
    (0, "FIRETIDE-AP-MIB", "vapAclMac"),
)
if mibBuilder.loadTexts:
    vapAclEntry.setStatus("current")
_VapAclMac_Type = MacAddress
_VapAclMac_Object = MibTableColumn
vapAclMac = _VapAclMac_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 3, 1, 1),
    _VapAclMac_Type()
)
vapAclMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vapAclMac.setStatus("current")
_VapAclStatus_Type = RowStatus
_VapAclStatus_Object = MibTableColumn
vapAclStatus = _VapAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 3, 1, 10),
    _VapAclStatus_Type()
)
vapAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vapAclStatus.setStatus("current")
_ApFirewallTable_Object = MibTable
apFirewallTable = _ApFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 4)
)
if mibBuilder.loadTexts:
    apFirewallTable.setStatus("current")
_ApFirewallEntry_Object = MibTableRow
apFirewallEntry = _ApFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 4, 1)
)
apFirewallEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
    (0, "FIRETIDE-AP-MIB", "apFirewallProtocol"),
    (0, "FIRETIDE-AP-MIB", "apFirewallPort"),
)
if mibBuilder.loadTexts:
    apFirewallEntry.setStatus("current")


class _ApFirewallProtocol_Type(Integer32):
    """Custom type apFirewallProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_ApFirewallProtocol_Type.__name__ = "Integer32"
_ApFirewallProtocol_Object = MibTableColumn
apFirewallProtocol = _ApFirewallProtocol_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 4, 1, 1),
    _ApFirewallProtocol_Type()
)
apFirewallProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apFirewallProtocol.setStatus("current")


class _ApFirewallPort_Type(Integer32):
    """Custom type apFirewallPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApFirewallPort_Type.__name__ = "Integer32"
_ApFirewallPort_Object = MibTableColumn
apFirewallPort = _ApFirewallPort_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 4, 1, 2),
    _ApFirewallPort_Type()
)
apFirewallPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apFirewallPort.setStatus("current")
_ApFirewallEntryStatus_Type = RowStatus
_ApFirewallEntryStatus_Object = MibTableColumn
apFirewallEntryStatus = _ApFirewallEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 4, 4, 1, 10),
    _ApFirewallEntryStatus_Type()
)
apFirewallEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apFirewallEntryStatus.setStatus("current")
_FiretideApStatistics_ObjectIdentity = ObjectIdentity
firetideApStatistics = _FiretideApStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5)
)
_ApStatisticsTable_Object = MibTable
apStatisticsTable = _ApStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1)
)
if mibBuilder.loadTexts:
    apStatisticsTable.setStatus("current")
_ApStatisticsEntry_Object = MibTableRow
apStatisticsEntry = _ApStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1)
)
apStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
)
if mibBuilder.loadTexts:
    apStatisticsEntry.setStatus("current")
_ApWiredInBytes_Type = Counter64
_ApWiredInBytes_Object = MibTableColumn
apWiredInBytes = _ApWiredInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 1),
    _ApWiredInBytes_Type()
)
apWiredInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredInBytes.setStatus("current")
_ApWiredInPackets_Type = Counter64
_ApWiredInPackets_Object = MibTableColumn
apWiredInPackets = _ApWiredInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 2),
    _ApWiredInPackets_Type()
)
apWiredInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredInPackets.setStatus("current")
_ApWiredReceiveErrors_Type = Counter64
_ApWiredReceiveErrors_Object = MibTableColumn
apWiredReceiveErrors = _ApWiredReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 3),
    _ApWiredReceiveErrors_Type()
)
apWiredReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredReceiveErrors.setStatus("current")
_ApWiredOpBytes_Type = Counter64
_ApWiredOpBytes_Object = MibTableColumn
apWiredOpBytes = _ApWiredOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 4),
    _ApWiredOpBytes_Type()
)
apWiredOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredOpBytes.setStatus("current")
_ApWiredOpPackets_Type = Counter64
_ApWiredOpPackets_Object = MibTableColumn
apWiredOpPackets = _ApWiredOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 5),
    _ApWiredOpPackets_Type()
)
apWiredOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredOpPackets.setStatus("current")
_ApWiredTransmitErrors_Type = Counter64
_ApWiredTransmitErrors_Object = MibTableColumn
apWiredTransmitErrors = _ApWiredTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 6),
    _ApWiredTransmitErrors_Type()
)
apWiredTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWiredTransmitErrors.setStatus("current")
_ApWirelessInBytes_Type = Counter64
_ApWirelessInBytes_Object = MibTableColumn
apWirelessInBytes = _ApWirelessInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 7),
    _ApWirelessInBytes_Type()
)
apWirelessInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessInBytes.setStatus("current")
_ApWirelessInPackets_Type = Counter64
_ApWirelessInPackets_Object = MibTableColumn
apWirelessInPackets = _ApWirelessInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 8),
    _ApWirelessInPackets_Type()
)
apWirelessInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessInPackets.setStatus("current")
_ApWirelessReceiveErrors_Type = Counter64
_ApWirelessReceiveErrors_Object = MibTableColumn
apWirelessReceiveErrors = _ApWirelessReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 9),
    _ApWirelessReceiveErrors_Type()
)
apWirelessReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessReceiveErrors.setStatus("current")
_ApWirelessOpBytes_Type = Counter64
_ApWirelessOpBytes_Object = MibTableColumn
apWirelessOpBytes = _ApWirelessOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 10),
    _ApWirelessOpBytes_Type()
)
apWirelessOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessOpBytes.setStatus("current")
_ApWirelessOpPackets_Type = Counter64
_ApWirelessOpPackets_Object = MibTableColumn
apWirelessOpPackets = _ApWirelessOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 11),
    _ApWirelessOpPackets_Type()
)
apWirelessOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessOpPackets.setStatus("current")
_ApWirelessTransmitErrors_Type = Counter64
_ApWirelessTransmitErrors_Object = MibTableColumn
apWirelessTransmitErrors = _ApWirelessTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 12),
    _ApWirelessTransmitErrors_Type()
)
apWirelessTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWirelessTransmitErrors.setStatus("current")
_ApStatisticsStatus_Type = RowStatus
_ApStatisticsStatus_Object = MibTableColumn
apStatisticsStatus = _ApStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 1, 1, 20),
    _ApStatisticsStatus_Type()
)
apStatisticsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStatisticsStatus.setStatus("current")
_ApVapStatisticsTable_Object = MibTable
apVapStatisticsTable = _ApVapStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2)
)
if mibBuilder.loadTexts:
    apVapStatisticsTable.setStatus("current")
_ApVapStatisticsEntry_Object = MibTableRow
apVapStatisticsEntry = _ApVapStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1)
)
apVapStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
)
if mibBuilder.loadTexts:
    apVapStatisticsEntry.setStatus("current")
_ApVapInBytes_Type = Counter64
_ApVapInBytes_Object = MibTableColumn
apVapInBytes = _ApVapInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 1),
    _ApVapInBytes_Type()
)
apVapInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapInBytes.setStatus("current")
_ApVapInPackets_Type = Counter64
_ApVapInPackets_Object = MibTableColumn
apVapInPackets = _ApVapInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 2),
    _ApVapInPackets_Type()
)
apVapInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapInPackets.setStatus("current")
_ApVapReceiveErrors_Type = Counter64
_ApVapReceiveErrors_Object = MibTableColumn
apVapReceiveErrors = _ApVapReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 3),
    _ApVapReceiveErrors_Type()
)
apVapReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapReceiveErrors.setStatus("current")
_ApVapOpBytes_Type = Counter64
_ApVapOpBytes_Object = MibTableColumn
apVapOpBytes = _ApVapOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 4),
    _ApVapOpBytes_Type()
)
apVapOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapOpBytes.setStatus("current")
_ApVapOpPackets_Type = Counter64
_ApVapOpPackets_Object = MibTableColumn
apVapOpPackets = _ApVapOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 5),
    _ApVapOpPackets_Type()
)
apVapOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapOpPackets.setStatus("current")
_ApVapTransmitErrors_Type = Counter64
_ApVapTransmitErrors_Object = MibTableColumn
apVapTransmitErrors = _ApVapTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 6),
    _ApVapTransmitErrors_Type()
)
apVapTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVapTransmitErrors.setStatus("current")
_ApVapStatisticsStatus_Type = RowStatus
_ApVapStatisticsStatus_Object = MibTableColumn
apVapStatisticsStatus = _ApVapStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 2, 1, 10),
    _ApVapStatisticsStatus_Type()
)
apVapStatisticsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apVapStatisticsStatus.setStatus("current")
_ApStationStatisticsTable_Object = MibTable
apStationStatisticsTable = _ApStationStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3)
)
if mibBuilder.loadTexts:
    apStationStatisticsTable.setStatus("current")
_ApStationStatisticsEntry_Object = MibTableRow
apStationStatisticsEntry = _ApStationStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1)
)
apStationStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-AP-MIB", "apNodeIndex"),
    (0, "FIRETIDE-AP-MIB", "vapGroupName"),
    (0, "FIRETIDE-AP-MIB", "apStationMacAddress"),
)
if mibBuilder.loadTexts:
    apStationStatisticsEntry.setStatus("current")
_ApStationMacAddress_Type = MacAddress
_ApStationMacAddress_Object = MibTableColumn
apStationMacAddress = _ApStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 1),
    _ApStationMacAddress_Type()
)
apStationMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apStationMacAddress.setStatus("current")
_ApStationRssi_Type = Counter32
_ApStationRssi_Object = MibTableColumn
apStationRssi = _ApStationRssi_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 2),
    _ApStationRssi_Type()
)
apStationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationRssi.setStatus("current")
_ApStationPower_Type = Integer32
_ApStationPower_Object = MibTableColumn
apStationPower = _ApStationPower_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 3),
    _ApStationPower_Type()
)
apStationPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationPower.setStatus("current")
_ApStationFrequency_Type = DisplayString
_ApStationFrequency_Object = MibTableColumn
apStationFrequency = _ApStationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 4),
    _ApStationFrequency_Type()
)
apStationFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationFrequency.setStatus("current")
_ApStationAuthMode_Type = ApAuthType
_ApStationAuthMode_Object = MibTableColumn
apStationAuthMode = _ApStationAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 5),
    _ApStationAuthMode_Type()
)
apStationAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationAuthMode.setStatus("current")
_ApStationCipherMode_Type = ApCipherType
_ApStationCipherMode_Object = MibTableColumn
apStationCipherMode = _ApStationCipherMode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 6),
    _ApStationCipherMode_Type()
)
apStationCipherMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationCipherMode.setStatus("current")
_ApStationInData_Type = Counter32
_ApStationInData_Object = MibTableColumn
apStationInData = _ApStationInData_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 7),
    _ApStationInData_Type()
)
apStationInData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInData.setStatus("current")
_ApStationInMgmt_Type = Counter32
_ApStationInMgmt_Object = MibTableColumn
apStationInMgmt = _ApStationInMgmt_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 8),
    _ApStationInMgmt_Type()
)
apStationInMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInMgmt.setStatus("current")
_ApStationInCtrl_Type = Counter32
_ApStationInCtrl_Object = MibTableColumn
apStationInCtrl = _ApStationInCtrl_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 9),
    _ApStationInCtrl_Type()
)
apStationInCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInCtrl.setStatus("current")
_ApStationInBytes_Type = Counter32
_ApStationInBytes_Object = MibTableColumn
apStationInBytes = _ApStationInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 10),
    _ApStationInBytes_Type()
)
apStationInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInBytes.setStatus("current")
_ApStationInBeacons_Type = Counter32
_ApStationInBeacons_Object = MibTableColumn
apStationInBeacons = _ApStationInBeacons_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 11),
    _ApStationInBeacons_Type()
)
apStationInBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInBeacons.setStatus("current")
_ApStationInWdsData_Type = Counter32
_ApStationInWdsData_Object = MibTableColumn
apStationInWdsData = _ApStationInWdsData_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 12),
    _ApStationInWdsData_Type()
)
apStationInWdsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInWdsData.setStatus("current")
_ApStationInWdsBytes_Type = Counter32
_ApStationInWdsBytes_Object = MibTableColumn
apStationInWdsBytes = _ApStationInWdsBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 13),
    _ApStationInWdsBytes_Type()
)
apStationInWdsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationInWdsBytes.setStatus("current")
_ApStationOpData_Type = Counter32
_ApStationOpData_Object = MibTableColumn
apStationOpData = _ApStationOpData_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 14),
    _ApStationOpData_Type()
)
apStationOpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationOpData.setStatus("current")
_ApStationOpMgmt_Type = Counter32
_ApStationOpMgmt_Object = MibTableColumn
apStationOpMgmt = _ApStationOpMgmt_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 15),
    _ApStationOpMgmt_Type()
)
apStationOpMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationOpMgmt.setStatus("current")
_ApStationOpBytes_Type = Counter32
_ApStationOpBytes_Object = MibTableColumn
apStationOpBytes = _ApStationOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 16),
    _ApStationOpBytes_Type()
)
apStationOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationOpBytes.setStatus("current")
_ApStationOpWdsData_Type = Counter32
_ApStationOpWdsData_Object = MibTableColumn
apStationOpWdsData = _ApStationOpWdsData_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 17),
    _ApStationOpWdsData_Type()
)
apStationOpWdsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationOpWdsData.setStatus("current")
_ApStationOpWdsBytes_Type = Counter32
_ApStationOpWdsBytes_Object = MibTableColumn
apStationOpWdsBytes = _ApStationOpWdsBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 18),
    _ApStationOpWdsBytes_Type()
)
apStationOpWdsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStationOpWdsBytes.setStatus("current")
_ApStationStatisticsStatus_Type = RowStatus
_ApStationStatisticsStatus_Object = MibTableColumn
apStationStatisticsStatus = _ApStationStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 2, 5, 3, 1, 30),
    _ApStationStatisticsStatus_Type()
)
apStationStatisticsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apStationStatisticsStatus.setStatus("current")
_FiretideApTrap_ObjectIdentity = ObjectIdentity
firetideApTrap = _FiretideApTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16)
)
_FiretideApMibConformance_ObjectIdentity = ObjectIdentity
firetideApMibConformance = _FiretideApMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20)
)
_FiretideApMibGroups_ObjectIdentity = ObjectIdentity
firetideApMibGroups = _FiretideApMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2)
)

# Managed Objects groups

firetideApNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2, 1)
)
firetideApNodeGroup.setObjects(
      *(("FIRETIDE-AP-MIB", "apNodeIndex"),
        ("FIRETIDE-AP-MIB", "apDhcpState"),
        ("FIRETIDE-AP-MIB", "apIpAddress"),
        ("FIRETIDE-AP-MIB", "apIpMask"),
        ("FIRETIDE-AP-MIB", "apDefaultGateway"),
        ("FIRETIDE-AP-MIB", "apName"),
        ("FIRETIDE-AP-MIB", "apGroupName"),
        ("FIRETIDE-AP-MIB", "apMgmtVlanEnable"),
        ("FIRETIDE-AP-MIB", "apMgmtVlanId"),
        ("FIRETIDE-AP-MIB", "apSoftwareVer"),
        ("FIRETIDE-AP-MIB", "apSerialNo"),
        ("FIRETIDE-AP-MIB", "apMacAddr"),
        ("FIRETIDE-AP-MIB", "apRadioMacAddr"),
        ("FIRETIDE-AP-MIB", "apNodeOperations"),
        ("FIRETIDE-AP-MIB", "apNodeErrorString"),
        ("FIRETIDE-AP-MIB", "apLoginUserName"),
        ("FIRETIDE-AP-MIB", "apLoginPasswd"))
)
if mibBuilder.loadTexts:
    firetideApNodeGroup.setStatus("current")

firetideApVapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2, 2)
)
firetideApVapGroup.setObjects(
      *(("FIRETIDE-AP-MIB", "vapGroupName"),
        ("FIRETIDE-AP-MIB", "vapEnable"),
        ("FIRETIDE-AP-MIB", "vapGroupSsid"),
        ("FIRETIDE-AP-MIB", "vapSsidSuppress"),
        ("FIRETIDE-AP-MIB", "vapDtimPeriod"),
        ("FIRETIDE-AP-MIB", "vapFragmentationThreshold"),
        ("FIRETIDE-AP-MIB", "vapRtsThreshold"),
        ("FIRETIDE-AP-MIB", "vapVlanEnable"),
        ("FIRETIDE-AP-MIB", "vapVlanId"),
        ("FIRETIDE-AP-MIB", "vapWdsEnable"),
        ("FIRETIDE-AP-MIB", "vapRateLimitEnable"),
        ("FIRETIDE-AP-MIB", "vapRateLimit"),
        ("FIRETIDE-AP-MIB", "vapUserRateLimitEnable"),
        ("FIRETIDE-AP-MIB", "vapUserRateLimit"),
        ("FIRETIDE-AP-MIB", "vapIcbEnable"),
        ("FIRETIDE-AP-MIB", "vapIappEnable"),
        ("FIRETIDE-AP-MIB", "vapIappPort"),
        ("FIRETIDE-AP-MIB", "vapWmmEnable"),
        ("FIRETIDE-AP-MIB", "vapConfigApply"),
        ("FIRETIDE-AP-MIB", "vapConfigComparison"),
        ("FIRETIDE-AP-MIB", "vapIpAddress"),
        ("FIRETIDE-AP-MIB", "vapIpMask"),
        ("FIRETIDE-AP-MIB", "vapDhcpServerEnable"),
        ("FIRETIDE-AP-MIB", "vapDhcpRenewalTime"),
        ("FIRETIDE-AP-MIB", "vapDhcpStartIp"),
        ("FIRETIDE-AP-MIB", "vapDhcpEndIp"),
        ("FIRETIDE-AP-MIB", "vapDhcpRouter"),
        ("FIRETIDE-AP-MIB", "vapDhcpDnsEnable"),
        ("FIRETIDE-AP-MIB", "vapDhcpPrimaryDns"),
        ("FIRETIDE-AP-MIB", "vapDhcpSecondaryDns"),
        ("FIRETIDE-AP-MIB", "vapGatewayEnable"),
        ("FIRETIDE-AP-MIB", "vapNatEnable"),
        ("FIRETIDE-AP-MIB", "vapNatPublicIp"),
        ("FIRETIDE-AP-MIB", "vapWdsOpMode"))
)
if mibBuilder.loadTexts:
    firetideApVapGroup.setStatus("current")

firetideApRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2, 3)
)
firetideApRadioGroup.setObjects(
      *(("FIRETIDE-AP-MIB", "apRadioCountryCode"),
        ("FIRETIDE-AP-MIB", "apRadioMode"),
        ("FIRETIDE-AP-MIB", "apChannelAutoSelectEnable"),
        ("FIRETIDE-AP-MIB", "apRadioChannel"),
        ("FIRETIDE-AP-MIB", "apRadioDataRate"),
        ("FIRETIDE-AP-MIB", "apRadioTransmitPower"),
        ("FIRETIDE-AP-MIB", "apRadioBeaconInterval"),
        ("FIRETIDE-AP-MIB", "apRadioAntennaType"),
        ("FIRETIDE-AP-MIB", "apRogueApDetection"),
        ("FIRETIDE-AP-MIB", "apRogueApDetectionPeriodicty"),
        ("FIRETIDE-AP-MIB", "apRogueApDetectionLevel"))
)
if mibBuilder.loadTexts:
    firetideApRadioGroup.setStatus("current")

firetideApSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2, 4)
)
firetideApSecurityGroup.setObjects(
      *(("FIRETIDE-AP-MIB", "vapSecurityEnable"),
        ("FIRETIDE-AP-MIB", "vapAuthType"),
        ("FIRETIDE-AP-MIB", "vapCipherType"),
        ("FIRETIDE-AP-MIB", "vapKey1"),
        ("FIRETIDE-AP-MIB", "vapKey2"),
        ("FIRETIDE-AP-MIB", "vapKey3"),
        ("FIRETIDE-AP-MIB", "vapKey4"),
        ("FIRETIDE-AP-MIB", "vapKeyIndex"),
        ("FIRETIDE-AP-MIB", "vapPassPhrase"),
        ("FIRETIDE-AP-MIB", "vapKeyInputType"),
        ("FIRETIDE-AP-MIB", "vapGroupKeyUpdate"),
        ("FIRETIDE-AP-MIB", "vapRadiusIp"),
        ("FIRETIDE-AP-MIB", "vapRadiusPort"),
        ("FIRETIDE-AP-MIB", "vapRadiusSecretKey"),
        ("FIRETIDE-AP-MIB", "vapAclPolicy"),
        ("FIRETIDE-AP-MIB", "apSecurityFirewallEnable"),
        ("FIRETIDE-AP-MIB", "apSecurityVpnEnable"),
        ("FIRETIDE-AP-MIB", "apSecurityVpnRemoteIp"),
        ("FIRETIDE-AP-MIB", "apSecurityVpnPassphrase"),
        ("FIRETIDE-AP-MIB", "vapAclMac"),
        ("FIRETIDE-AP-MIB", "apFirewallProtocol"),
        ("FIRETIDE-AP-MIB", "apFirewallPort"))
)
if mibBuilder.loadTexts:
    firetideApSecurityGroup.setStatus("current")

firetideApStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 2, 5)
)
firetideApStatisticsGroup.setObjects(
      *(("FIRETIDE-AP-MIB", "apWiredInBytes"),
        ("FIRETIDE-AP-MIB", "apWiredInPackets"),
        ("FIRETIDE-AP-MIB", "apWiredReceiveErrors"),
        ("FIRETIDE-AP-MIB", "apWiredOpBytes"),
        ("FIRETIDE-AP-MIB", "apWiredOpPackets"),
        ("FIRETIDE-AP-MIB", "apWiredTransmitErrors"),
        ("FIRETIDE-AP-MIB", "apWirelessInBytes"),
        ("FIRETIDE-AP-MIB", "apWirelessInPackets"),
        ("FIRETIDE-AP-MIB", "apWirelessReceiveErrors"),
        ("FIRETIDE-AP-MIB", "apWirelessOpBytes"),
        ("FIRETIDE-AP-MIB", "apWirelessOpPackets"),
        ("FIRETIDE-AP-MIB", "apWirelessTransmitErrors"),
        ("FIRETIDE-AP-MIB", "apVapInBytes"),
        ("FIRETIDE-AP-MIB", "apVapInPackets"),
        ("FIRETIDE-AP-MIB", "apVapReceiveErrors"),
        ("FIRETIDE-AP-MIB", "apVapOpBytes"),
        ("FIRETIDE-AP-MIB", "apVapOpPackets"),
        ("FIRETIDE-AP-MIB", "apVapTransmitErrors"),
        ("FIRETIDE-AP-MIB", "apStationMacAddress"),
        ("FIRETIDE-AP-MIB", "apStationRssi"),
        ("FIRETIDE-AP-MIB", "apStationPower"),
        ("FIRETIDE-AP-MIB", "apStationFrequency"),
        ("FIRETIDE-AP-MIB", "apStationAuthMode"),
        ("FIRETIDE-AP-MIB", "apStationCipherMode"),
        ("FIRETIDE-AP-MIB", "apStationInData"),
        ("FIRETIDE-AP-MIB", "apStationInMgmt"),
        ("FIRETIDE-AP-MIB", "apStationInCtrl"),
        ("FIRETIDE-AP-MIB", "apStationInBytes"),
        ("FIRETIDE-AP-MIB", "apStationInBeacons"),
        ("FIRETIDE-AP-MIB", "apStationInWdsData"),
        ("FIRETIDE-AP-MIB", "apStationInWdsBytes"),
        ("FIRETIDE-AP-MIB", "apStationOpData"),
        ("FIRETIDE-AP-MIB", "apStationOpMgmt"),
        ("FIRETIDE-AP-MIB", "apStationOpBytes"),
        ("FIRETIDE-AP-MIB", "apStationOpWdsData"),
        ("FIRETIDE-AP-MIB", "apStationOpWdsBytes"))
)
if mibBuilder.loadTexts:
    firetideApStatisticsGroup.setStatus("current")


# Notification objects

apDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 1)
)
apDown.setObjects(
      *(("FIRETIDE-AP-MIB", "apNodeIndex"),
        ("FIRETIDE-AP-MIB", "apIpAddress"))
)
if mibBuilder.loadTexts:
    apDown.setStatus(
        "current"
    )

apUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 2)
)
apUp.setObjects(
      *(("FIRETIDE-AP-MIB", "apNodeIndex"),
        ("FIRETIDE-AP-MIB", "apIpAddress"))
)
if mibBuilder.loadTexts:
    apUp.setStatus(
        "current"
    )

vapConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 3)
)
vapConfigInconsistent.setObjects(
      *(("FIRETIDE-AP-MIB", "vapGroupName"),
        ("FIRETIDE-AP-MIB", "vapConfigComparison"))
)
if mibBuilder.loadTexts:
    vapConfigInconsistent.setStatus(
        "current"
    )

vapConfigConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 4)
)
vapConfigConsistent.setObjects(
      *(("FIRETIDE-AP-MIB", "vapGroupName"),
        ("FIRETIDE-AP-MIB", "vapConfigComparison"))
)
if mibBuilder.loadTexts:
    vapConfigConsistent.setStatus(
        "current"
    )

apLoginError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 5)
)
apLoginError.setObjects(
      *(("FIRETIDE-AP-MIB", "apNodeIndex"),
        ("FIRETIDE-AP-MIB", "apLoginErrorMessage"))
)
if mibBuilder.loadTexts:
    apLoginError.setStatus(
        "current"
    )

concurrentApModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 6)
)
concurrentApModification.setObjects(
    ("FIRETIDE-AP-MIB", "apNodeIndex")
)
if mibBuilder.loadTexts:
    concurrentApModification.setStatus(
        "current"
    )

concurrentVapModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 2, 16, 7)
)
concurrentVapModification.setObjects(
    ("FIRETIDE-AP-MIB", "vapGroupName")
)
if mibBuilder.loadTexts:
    concurrentVapModification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

firetideApMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22835, 2, 20, 1)
)
firetideApMibCompliance.setObjects(
      *(("FIRETIDE-AP-MIB", "firetideApNodeGroup"),
        ("FIRETIDE-AP-MIB", "firetideApVapGroup"),
        ("FIRETIDE-AP-MIB", "firetideApRadioGroup"),
        ("FIRETIDE-AP-MIB", "firetideApSecurityGroup"),
        ("FIRETIDE-AP-MIB", "firetideApStatisticsGroup"))
)
if mibBuilder.loadTexts:
    firetideApMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIRETIDE-AP-MIB",
    **{"ApRadioMode": ApRadioMode,
       "ApRadioDataRate": ApRadioDataRate,
       "ApAuthType": ApAuthType,
       "ApCipherType": ApCipherType,
       "firetideAp": firetideAp,
       "firetideApNode": firetideApNode,
       "apTable": apTable,
       "apEntry": apEntry,
       "apNodeIndex": apNodeIndex,
       "apDhcpState": apDhcpState,
       "apIpAddress": apIpAddress,
       "apIpMask": apIpMask,
       "apDefaultGateway": apDefaultGateway,
       "apName": apName,
       "apGroupName": apGroupName,
       "apMgmtVlanEnable": apMgmtVlanEnable,
       "apMgmtVlanId": apMgmtVlanId,
       "apSoftwareVer": apSoftwareVer,
       "apSerialNo": apSerialNo,
       "apMacAddr": apMacAddr,
       "apRadioMacAddr": apRadioMacAddr,
       "apNodeOperations": apNodeOperations,
       "apNodeErrorString": apNodeErrorString,
       "apSelectForUpgrade": apSelectForUpgrade,
       "apSoftwareUpgradeCompletion": apSoftwareUpgradeCompletion,
       "apNodeStatus": apNodeStatus,
       "standaloneApTable": standaloneApTable,
       "standaloneApEntry": standaloneApEntry,
       "standaloneApIpAddress": standaloneApIpAddress,
       "standaloneApNodeStatus": standaloneApNodeStatus,
       "apSoftwareUpgradePath": apSoftwareUpgradePath,
       "apSoftwareUpgrade": apSoftwareUpgrade,
       "apLoginUserName": apLoginUserName,
       "apLoginPasswd": apLoginPasswd,
       "apLoginErrorMessage": apLoginErrorMessage,
       "firetideApVap": firetideApVap,
       "vapGroupConfigTable": vapGroupConfigTable,
       "vapGroupConfigEntry": vapGroupConfigEntry,
       "vapGroupName": vapGroupName,
       "vapEnable": vapEnable,
       "vapGroupSsid": vapGroupSsid,
       "vapSsidSuppress": vapSsidSuppress,
       "vapDtimPeriod": vapDtimPeriod,
       "vapFragmentationThreshold": vapFragmentationThreshold,
       "vapRtsThreshold": vapRtsThreshold,
       "vapVlanEnable": vapVlanEnable,
       "vapVlanId": vapVlanId,
       "vapWdsEnable": vapWdsEnable,
       "vapRateLimitEnable": vapRateLimitEnable,
       "vapRateLimit": vapRateLimit,
       "vapUserRateLimitEnable": vapUserRateLimitEnable,
       "vapUserRateLimit": vapUserRateLimit,
       "vapIcbEnable": vapIcbEnable,
       "vapIappEnable": vapIappEnable,
       "vapIappPort": vapIappPort,
       "vapWmmEnable": vapWmmEnable,
       "vapConfigApply": vapConfigApply,
       "vapConfigErrorString": vapConfigErrorString,
       "vapConfigVerify": vapConfigVerify,
       "vapConfigComparison": vapConfigComparison,
       "vapGroupStatus": vapGroupStatus,
       "vapSpecificConfigTable": vapSpecificConfigTable,
       "vapSpecificConfigEntry": vapSpecificConfigEntry,
       "vapIpAddress": vapIpAddress,
       "vapIpMask": vapIpMask,
       "vapDhcpServerEnable": vapDhcpServerEnable,
       "vapDhcpRenewalTime": vapDhcpRenewalTime,
       "vapDhcpStartIp": vapDhcpStartIp,
       "vapDhcpEndIp": vapDhcpEndIp,
       "vapDhcpRouter": vapDhcpRouter,
       "vapDhcpDnsEnable": vapDhcpDnsEnable,
       "vapDhcpPrimaryDns": vapDhcpPrimaryDns,
       "vapDhcpSecondaryDns": vapDhcpSecondaryDns,
       "vapGatewayEnable": vapGatewayEnable,
       "vapNatEnable": vapNatEnable,
       "vapNatPublicIp": vapNatPublicIp,
       "vapWdsOpMode": vapWdsOpMode,
       "vapSpecificConfigStatus": vapSpecificConfigStatus,
       "firetideApRadio": firetideApRadio,
       "apRadioTable": apRadioTable,
       "apRadioEntry": apRadioEntry,
       "apRadioCountryCode": apRadioCountryCode,
       "apRadioMode": apRadioMode,
       "apChannelAutoSelectEnable": apChannelAutoSelectEnable,
       "apRadioChannel": apRadioChannel,
       "apRadioDataRate": apRadioDataRate,
       "apRadioTransmitPower": apRadioTransmitPower,
       "apRadioBeaconInterval": apRadioBeaconInterval,
       "apRadioAntennaType": apRadioAntennaType,
       "apRogueApDetection": apRogueApDetection,
       "apRogueApDetectionPeriodicty": apRogueApDetectionPeriodicty,
       "apRogueApDetectionLevel": apRogueApDetectionLevel,
       "apRadioStatus": apRadioStatus,
       "firetideApSecurity": firetideApSecurity,
       "vapSecurityTable": vapSecurityTable,
       "vapSecurityEntry": vapSecurityEntry,
       "vapSecurityEnable": vapSecurityEnable,
       "vapAuthType": vapAuthType,
       "vapCipherType": vapCipherType,
       "vapKey1": vapKey1,
       "vapKey2": vapKey2,
       "vapKey3": vapKey3,
       "vapKey4": vapKey4,
       "vapKeyIndex": vapKeyIndex,
       "vapPassPhrase": vapPassPhrase,
       "vapKeyInputType": vapKeyInputType,
       "vapGroupKeyUpdate": vapGroupKeyUpdate,
       "vapRadiusIp": vapRadiusIp,
       "vapRadiusPort": vapRadiusPort,
       "vapRadiusSecretKey": vapRadiusSecretKey,
       "vapAclPolicy": vapAclPolicy,
       "vapSecurityStatus": vapSecurityStatus,
       "apSecurityTable": apSecurityTable,
       "apSecurityEntry": apSecurityEntry,
       "apSecurityFirewallEnable": apSecurityFirewallEnable,
       "apSecurityVpnEnable": apSecurityVpnEnable,
       "apSecurityVpnRemoteIp": apSecurityVpnRemoteIp,
       "apSecurityVpnPassphrase": apSecurityVpnPassphrase,
       "apSecurityStatus": apSecurityStatus,
       "vapAclTable": vapAclTable,
       "vapAclEntry": vapAclEntry,
       "vapAclMac": vapAclMac,
       "vapAclStatus": vapAclStatus,
       "apFirewallTable": apFirewallTable,
       "apFirewallEntry": apFirewallEntry,
       "apFirewallProtocol": apFirewallProtocol,
       "apFirewallPort": apFirewallPort,
       "apFirewallEntryStatus": apFirewallEntryStatus,
       "firetideApStatistics": firetideApStatistics,
       "apStatisticsTable": apStatisticsTable,
       "apStatisticsEntry": apStatisticsEntry,
       "apWiredInBytes": apWiredInBytes,
       "apWiredInPackets": apWiredInPackets,
       "apWiredReceiveErrors": apWiredReceiveErrors,
       "apWiredOpBytes": apWiredOpBytes,
       "apWiredOpPackets": apWiredOpPackets,
       "apWiredTransmitErrors": apWiredTransmitErrors,
       "apWirelessInBytes": apWirelessInBytes,
       "apWirelessInPackets": apWirelessInPackets,
       "apWirelessReceiveErrors": apWirelessReceiveErrors,
       "apWirelessOpBytes": apWirelessOpBytes,
       "apWirelessOpPackets": apWirelessOpPackets,
       "apWirelessTransmitErrors": apWirelessTransmitErrors,
       "apStatisticsStatus": apStatisticsStatus,
       "apVapStatisticsTable": apVapStatisticsTable,
       "apVapStatisticsEntry": apVapStatisticsEntry,
       "apVapInBytes": apVapInBytes,
       "apVapInPackets": apVapInPackets,
       "apVapReceiveErrors": apVapReceiveErrors,
       "apVapOpBytes": apVapOpBytes,
       "apVapOpPackets": apVapOpPackets,
       "apVapTransmitErrors": apVapTransmitErrors,
       "apVapStatisticsStatus": apVapStatisticsStatus,
       "apStationStatisticsTable": apStationStatisticsTable,
       "apStationStatisticsEntry": apStationStatisticsEntry,
       "apStationMacAddress": apStationMacAddress,
       "apStationRssi": apStationRssi,
       "apStationPower": apStationPower,
       "apStationFrequency": apStationFrequency,
       "apStationAuthMode": apStationAuthMode,
       "apStationCipherMode": apStationCipherMode,
       "apStationInData": apStationInData,
       "apStationInMgmt": apStationInMgmt,
       "apStationInCtrl": apStationInCtrl,
       "apStationInBytes": apStationInBytes,
       "apStationInBeacons": apStationInBeacons,
       "apStationInWdsData": apStationInWdsData,
       "apStationInWdsBytes": apStationInWdsBytes,
       "apStationOpData": apStationOpData,
       "apStationOpMgmt": apStationOpMgmt,
       "apStationOpBytes": apStationOpBytes,
       "apStationOpWdsData": apStationOpWdsData,
       "apStationOpWdsBytes": apStationOpWdsBytes,
       "apStationStatisticsStatus": apStationStatisticsStatus,
       "firetideApTrap": firetideApTrap,
       "apDown": apDown,
       "apUp": apUp,
       "vapConfigInconsistent": vapConfigInconsistent,
       "vapConfigConsistent": vapConfigConsistent,
       "apLoginError": apLoginError,
       "concurrentApModification": concurrentApModification,
       "concurrentVapModification": concurrentVapModification,
       "firetideApMibConformance": firetideApMibConformance,
       "firetideApMibCompliance": firetideApMibCompliance,
       "firetideApMibGroups": firetideApMibGroups,
       "firetideApNodeGroup": firetideApNodeGroup,
       "firetideApVapGroup": firetideApVapGroup,
       "firetideApRadioGroup": firetideApRadioGroup,
       "firetideApSecurityGroup": firetideApSecurityGroup,
       "firetideApStatisticsGroup": firetideApStatisticsGroup}
)
