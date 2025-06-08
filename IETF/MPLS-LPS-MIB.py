# SNMP MIB module (MPLS-LPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/MPLS-LPS-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 20:19:28 2025
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

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexIntegerNextFree")

(mplsOamIdMeIndex,
 mplsOamIdMeMpIndex,
 mplsOamIdMegIndex) = mibBuilder.importSymbols(
    "MPLS-OAM-ID-STD-MIB",
    "mplsOamIdMeIndex",
    "mplsOamIdMeMpIndex",
    "mplsOamIdMegIndex")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22)
)
if mibBuilder.loadTexts:
    mplsLpsMIB.setRevisions(
        ("2017-04-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLpsReq(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("doNotRevert", 1),
          ("reverseRequest", 2),
          ("exercise", 3),
          ("waitToRestore", 4),
          ("manualSwitch", 5),
          ("signalDegrade", 7),
          ("signalFail", 10),
          ("forcedSwitch", 12),
          ("lockoutOfProtection", 14))
    )



class MplsLpsFpathPath(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2



class MplsLpsCommand(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitch", 4),
          ("manualSwitchToWork", 5),
          ("manualSwitchToProtect", 6),
          ("exercise", 7),
          ("freeze", 8),
          ("clearfreeze", 9))
    )



class MplsLpsState(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("unavLOlocal", 2),
          ("unavSFPlocal", 3),
          ("unavSDPlocal", 4),
          ("unavLOremote", 5),
          ("unavSFPremote", 6),
          ("unavSDPremote", 7),
          ("protfailSFWlocal", 8),
          ("protfailSDWlocal", 9),
          ("protfailSFWremote", 10),
          ("protfailSDWremote", 11),
          ("switadmFSlocal", 12),
          ("switadmMSWlocal", 13),
          ("switadmMSPlocal", 14),
          ("switadmFSremote", 15),
          ("switadmMSWremote", 16),
          ("switadmMSPremote", 17),
          ("wtr", 18),
          ("dnr", 19),
          ("exerLocal", 20),
          ("exerRemote", 21))
    )



# MIB Managed Objects in the order of their OIDs

_MplsLpsNotifications_ObjectIdentity = ObjectIdentity
mplsLpsNotifications = _MplsLpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0)
)
_MplsLpsObjects_ObjectIdentity = ObjectIdentity
mplsLpsObjects = _MplsLpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1)
)


class _MplsLpsConfigDomainIndexNext_Type(IndexIntegerNextFree):
    """Custom type mplsLpsConfigDomainIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLpsConfigDomainIndexNext_Type.__name__ = "IndexIntegerNextFree"
_MplsLpsConfigDomainIndexNext_Object = MibScalar
mplsLpsConfigDomainIndexNext = _MplsLpsConfigDomainIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 1),
    _MplsLpsConfigDomainIndexNext_Type()
)
mplsLpsConfigDomainIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsConfigDomainIndexNext.setStatus("current")
_MplsLpsConfigTable_Object = MibTable
mplsLpsConfigTable = _MplsLpsConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLpsConfigTable.setStatus("current")
_MplsLpsConfigEntry_Object = MibTableRow
mplsLpsConfigEntry = _MplsLpsConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1)
)
mplsLpsConfigEntry.setIndexNames(
    (0, "MPLS-LPS-MIB", "mplsLpsConfigDomainIndex"),
)
if mibBuilder.loadTexts:
    mplsLpsConfigEntry.setStatus("current")


class _MplsLpsConfigDomainIndex_Type(Unsigned32):
    """Custom type mplsLpsConfigDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLpsConfigDomainIndex_Type.__name__ = "Unsigned32"
_MplsLpsConfigDomainIndex_Object = MibTableColumn
mplsLpsConfigDomainIndex = _MplsLpsConfigDomainIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 1),
    _MplsLpsConfigDomainIndex_Type()
)
mplsLpsConfigDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLpsConfigDomainIndex.setStatus("current")


class _MplsLpsConfigDomainName_Type(SnmpAdminString):
    """Custom type mplsLpsConfigDomainName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MplsLpsConfigDomainName_Type.__name__ = "SnmpAdminString"
_MplsLpsConfigDomainName_Object = MibTableColumn
mplsLpsConfigDomainName = _MplsLpsConfigDomainName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 2),
    _MplsLpsConfigDomainName_Type()
)
mplsLpsConfigDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigDomainName.setStatus("current")


class _MplsLpsConfigMode_Type(Integer32):
    """Custom type mplsLpsConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psc", 1),
          ("aps", 2))
    )


_MplsLpsConfigMode_Type.__name__ = "Integer32"
_MplsLpsConfigMode_Object = MibTableColumn
mplsLpsConfigMode = _MplsLpsConfigMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 3),
    _MplsLpsConfigMode_Type()
)
mplsLpsConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigMode.setStatus("current")


class _MplsLpsConfigProtectionType_Type(Integer32):
    """Custom type mplsLpsConfigProtectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOneUnidirectional", 1),
          ("oneColonOneBidirectional", 2),
          ("onePlusOneBidirectional", 3))
    )


_MplsLpsConfigProtectionType_Type.__name__ = "Integer32"
_MplsLpsConfigProtectionType_Object = MibTableColumn
mplsLpsConfigProtectionType = _MplsLpsConfigProtectionType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 4),
    _MplsLpsConfigProtectionType_Type()
)
mplsLpsConfigProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigProtectionType.setStatus("current")


class _MplsLpsConfigRevertive_Type(Integer32):
    """Custom type mplsLpsConfigRevertive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_MplsLpsConfigRevertive_Type.__name__ = "Integer32"
_MplsLpsConfigRevertive_Object = MibTableColumn
mplsLpsConfigRevertive = _MplsLpsConfigRevertive_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 5),
    _MplsLpsConfigRevertive_Type()
)
mplsLpsConfigRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigRevertive.setStatus("current")


class _MplsLpsConfigSdThreshold_Type(Unsigned32):
    """Custom type mplsLpsConfigSdThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MplsLpsConfigSdThreshold_Type.__name__ = "Unsigned32"
_MplsLpsConfigSdThreshold_Object = MibTableColumn
mplsLpsConfigSdThreshold = _MplsLpsConfigSdThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 6),
    _MplsLpsConfigSdThreshold_Type()
)
mplsLpsConfigSdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigSdThreshold.setStatus("current")


class _MplsLpsConfigSdBadSeconds_Type(Unsigned32):
    """Custom type mplsLpsConfigSdBadSeconds based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_MplsLpsConfigSdBadSeconds_Type.__name__ = "Unsigned32"
_MplsLpsConfigSdBadSeconds_Object = MibTableColumn
mplsLpsConfigSdBadSeconds = _MplsLpsConfigSdBadSeconds_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 7),
    _MplsLpsConfigSdBadSeconds_Type()
)
mplsLpsConfigSdBadSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigSdBadSeconds.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigSdBadSeconds.setUnits("seconds")


class _MplsLpsConfigSdGoodSeconds_Type(Unsigned32):
    """Custom type mplsLpsConfigSdGoodSeconds based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_MplsLpsConfigSdGoodSeconds_Type.__name__ = "Unsigned32"
_MplsLpsConfigSdGoodSeconds_Object = MibTableColumn
mplsLpsConfigSdGoodSeconds = _MplsLpsConfigSdGoodSeconds_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 8),
    _MplsLpsConfigSdGoodSeconds_Type()
)
mplsLpsConfigSdGoodSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigSdGoodSeconds.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigSdGoodSeconds.setUnits("seconds")


class _MplsLpsConfigWaitToRestore_Type(Unsigned32):
    """Custom type mplsLpsConfigWaitToRestore based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_MplsLpsConfigWaitToRestore_Type.__name__ = "Unsigned32"
_MplsLpsConfigWaitToRestore_Object = MibTableColumn
mplsLpsConfigWaitToRestore = _MplsLpsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 9),
    _MplsLpsConfigWaitToRestore_Type()
)
mplsLpsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigWaitToRestore.setUnits("minutes")


class _MplsLpsConfigHoldOff_Type(Unsigned32):
    """Custom type mplsLpsConfigHoldOff based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MplsLpsConfigHoldOff_Type.__name__ = "Unsigned32"
_MplsLpsConfigHoldOff_Object = MibTableColumn
mplsLpsConfigHoldOff = _MplsLpsConfigHoldOff_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 10),
    _MplsLpsConfigHoldOff_Type()
)
mplsLpsConfigHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigHoldOff.setUnits("deciseconds")


class _MplsLpsConfigContinualTxInterval_Type(Unsigned32):
    """Custom type mplsLpsConfigContinualTxInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MplsLpsConfigContinualTxInterval_Type.__name__ = "Unsigned32"
_MplsLpsConfigContinualTxInterval_Object = MibTableColumn
mplsLpsConfigContinualTxInterval = _MplsLpsConfigContinualTxInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 11),
    _MplsLpsConfigContinualTxInterval_Type()
)
mplsLpsConfigContinualTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigContinualTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigContinualTxInterval.setUnits("seconds")


class _MplsLpsConfigRapidTxInterval_Type(Unsigned32):
    """Custom type mplsLpsConfigRapidTxInterval based on Unsigned32"""
    defaultValue = 3300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_MplsLpsConfigRapidTxInterval_Type.__name__ = "Unsigned32"
_MplsLpsConfigRapidTxInterval_Object = MibTableColumn
mplsLpsConfigRapidTxInterval = _MplsLpsConfigRapidTxInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 12),
    _MplsLpsConfigRapidTxInterval_Type()
)
mplsLpsConfigRapidTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigRapidTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsConfigRapidTxInterval.setUnits("microseconds")


class _MplsLpsConfigCommand_Type(MplsLpsCommand):
    """Custom type mplsLpsConfigCommand based on MplsLpsCommand"""
    defaultValue = 1


_MplsLpsConfigCommand_Type.__name__ = "MplsLpsCommand"
_MplsLpsConfigCommand_Object = MibTableColumn
mplsLpsConfigCommand = _MplsLpsConfigCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 13),
    _MplsLpsConfigCommand_Type()
)
mplsLpsConfigCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigCommand.setStatus("current")
_MplsLpsConfigCreationTime_Type = TimeStamp
_MplsLpsConfigCreationTime_Object = MibTableColumn
mplsLpsConfigCreationTime = _MplsLpsConfigCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 14),
    _MplsLpsConfigCreationTime_Type()
)
mplsLpsConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsConfigCreationTime.setStatus("current")
_MplsLpsConfigRowStatus_Type = RowStatus
_MplsLpsConfigRowStatus_Object = MibTableColumn
mplsLpsConfigRowStatus = _MplsLpsConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 15),
    _MplsLpsConfigRowStatus_Type()
)
mplsLpsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigRowStatus.setStatus("current")


class _MplsLpsConfigStorageType_Type(StorageType):
    """Custom type mplsLpsConfigStorageType based on StorageType"""
    defaultValue = 3


_MplsLpsConfigStorageType_Type.__name__ = "StorageType"
_MplsLpsConfigStorageType_Object = MibTableColumn
mplsLpsConfigStorageType = _MplsLpsConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 2, 1, 16),
    _MplsLpsConfigStorageType_Type()
)
mplsLpsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsConfigStorageType.setStatus("current")
_MplsLpsStatusTable_Object = MibTable
mplsLpsStatusTable = _MplsLpsStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3)
)
if mibBuilder.loadTexts:
    mplsLpsStatusTable.setStatus("current")
_MplsLpsStatusEntry_Object = MibTableRow
mplsLpsStatusEntry = _MplsLpsStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLpsStatusEntry.setStatus("current")
_MplsLpsStatusState_Type = MplsLpsState
_MplsLpsStatusState_Object = MibTableColumn
mplsLpsStatusState = _MplsLpsStatusState_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 1),
    _MplsLpsStatusState_Type()
)
mplsLpsStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusState.setStatus("current")
_MplsLpsStatusReqRcv_Type = MplsLpsReq
_MplsLpsStatusReqRcv_Object = MibTableColumn
mplsLpsStatusReqRcv = _MplsLpsStatusReqRcv_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 2),
    _MplsLpsStatusReqRcv_Type()
)
mplsLpsStatusReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusReqRcv.setStatus("current")
_MplsLpsStatusReqSent_Type = MplsLpsReq
_MplsLpsStatusReqSent_Object = MibTableColumn
mplsLpsStatusReqSent = _MplsLpsStatusReqSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 3),
    _MplsLpsStatusReqSent_Type()
)
mplsLpsStatusReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusReqSent.setStatus("current")
_MplsLpsStatusFpathPathRcv_Type = MplsLpsFpathPath
_MplsLpsStatusFpathPathRcv_Object = MibTableColumn
mplsLpsStatusFpathPathRcv = _MplsLpsStatusFpathPathRcv_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 4),
    _MplsLpsStatusFpathPathRcv_Type()
)
mplsLpsStatusFpathPathRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusFpathPathRcv.setStatus("current")
_MplsLpsStatusFpathPathSent_Type = MplsLpsFpathPath
_MplsLpsStatusFpathPathSent_Object = MibTableColumn
mplsLpsStatusFpathPathSent = _MplsLpsStatusFpathPathSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 5),
    _MplsLpsStatusFpathPathSent_Type()
)
mplsLpsStatusFpathPathSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusFpathPathSent.setStatus("current")
_MplsLpsStatusRevertiveMismatch_Type = TruthValue
_MplsLpsStatusRevertiveMismatch_Object = MibTableColumn
mplsLpsStatusRevertiveMismatch = _MplsLpsStatusRevertiveMismatch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 6),
    _MplsLpsStatusRevertiveMismatch_Type()
)
mplsLpsStatusRevertiveMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusRevertiveMismatch.setStatus("current")
_MplsLpsStatusProtecTypeMismatch_Type = TruthValue
_MplsLpsStatusProtecTypeMismatch_Object = MibTableColumn
mplsLpsStatusProtecTypeMismatch = _MplsLpsStatusProtecTypeMismatch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 7),
    _MplsLpsStatusProtecTypeMismatch_Type()
)
mplsLpsStatusProtecTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusProtecTypeMismatch.setStatus("current")
_MplsLpsStatusCapabilitiesMismatch_Type = TruthValue
_MplsLpsStatusCapabilitiesMismatch_Object = MibTableColumn
mplsLpsStatusCapabilitiesMismatch = _MplsLpsStatusCapabilitiesMismatch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 8),
    _MplsLpsStatusCapabilitiesMismatch_Type()
)
mplsLpsStatusCapabilitiesMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusCapabilitiesMismatch.setStatus("current")
_MplsLpsStatusPathConfigMismatch_Type = TruthValue
_MplsLpsStatusPathConfigMismatch_Object = MibTableColumn
mplsLpsStatusPathConfigMismatch = _MplsLpsStatusPathConfigMismatch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 9),
    _MplsLpsStatusPathConfigMismatch_Type()
)
mplsLpsStatusPathConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusPathConfigMismatch.setStatus("current")
_MplsLpsStatusFopNoResponses_Type = Counter32
_MplsLpsStatusFopNoResponses_Object = MibTableColumn
mplsLpsStatusFopNoResponses = _MplsLpsStatusFopNoResponses_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 10),
    _MplsLpsStatusFopNoResponses_Type()
)
mplsLpsStatusFopNoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusFopNoResponses.setStatus("current")
_MplsLpsStatusFopTimeouts_Type = Counter32
_MplsLpsStatusFopTimeouts_Object = MibTableColumn
mplsLpsStatusFopTimeouts = _MplsLpsStatusFopTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 3, 1, 11),
    _MplsLpsStatusFopTimeouts_Type()
)
mplsLpsStatusFopTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsStatusFopTimeouts.setStatus("current")
_MplsLpsMeConfigTable_Object = MibTable
mplsLpsMeConfigTable = _MplsLpsMeConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 4)
)
if mibBuilder.loadTexts:
    mplsLpsMeConfigTable.setStatus("current")
_MplsLpsMeConfigEntry_Object = MibTableRow
mplsLpsMeConfigEntry = _MplsLpsMeConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 4, 1)
)
mplsLpsMeConfigEntry.setIndexNames(
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIndex"),
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMeIndex"),
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMpIndex"),
)
if mibBuilder.loadTexts:
    mplsLpsMeConfigEntry.setStatus("current")


class _MplsLpsMeConfigDomain_Type(Unsigned32):
    """Custom type mplsLpsMeConfigDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLpsMeConfigDomain_Type.__name__ = "Unsigned32"
_MplsLpsMeConfigDomain_Object = MibTableColumn
mplsLpsMeConfigDomain = _MplsLpsMeConfigDomain_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 4, 1, 1),
    _MplsLpsMeConfigDomain_Type()
)
mplsLpsMeConfigDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsMeConfigDomain.setStatus("current")


class _MplsLpsMeConfigPath_Type(Integer32):
    """Custom type mplsLpsMeConfigPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2))
    )


_MplsLpsMeConfigPath_Type.__name__ = "Integer32"
_MplsLpsMeConfigPath_Object = MibTableColumn
mplsLpsMeConfigPath = _MplsLpsMeConfigPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 4, 1, 2),
    _MplsLpsMeConfigPath_Type()
)
mplsLpsMeConfigPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLpsMeConfigPath.setStatus("current")
_MplsLpsMeStatusTable_Object = MibTable
mplsLpsMeStatusTable = _MplsLpsMeStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5)
)
if mibBuilder.loadTexts:
    mplsLpsMeStatusTable.setStatus("current")
_MplsLpsMeStatusEntry_Object = MibTableRow
mplsLpsMeStatusEntry = _MplsLpsMeStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLpsMeStatusEntry.setStatus("current")


class _MplsLpsMeStatusCurrent_Type(Bits):
    """Custom type mplsLpsMeStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("localSelectTraffic", 0),
          ("localSD", 1),
          ("localSF", 2))
    )

_MplsLpsMeStatusCurrent_Type.__name__ = "Bits"
_MplsLpsMeStatusCurrent_Object = MibTableColumn
mplsLpsMeStatusCurrent = _MplsLpsMeStatusCurrent_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 1),
    _MplsLpsMeStatusCurrent_Type()
)
mplsLpsMeStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusCurrent.setStatus("current")
_MplsLpsMeStatusSignalDegrades_Type = Counter32
_MplsLpsMeStatusSignalDegrades_Object = MibTableColumn
mplsLpsMeStatusSignalDegrades = _MplsLpsMeStatusSignalDegrades_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 2),
    _MplsLpsMeStatusSignalDegrades_Type()
)
mplsLpsMeStatusSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusSignalDegrades.setStatus("current")
_MplsLpsMeStatusSignalFailures_Type = Counter32
_MplsLpsMeStatusSignalFailures_Object = MibTableColumn
mplsLpsMeStatusSignalFailures = _MplsLpsMeStatusSignalFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 3),
    _MplsLpsMeStatusSignalFailures_Type()
)
mplsLpsMeStatusSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusSignalFailures.setStatus("current")
_MplsLpsMeStatusSwitchovers_Type = Counter32
_MplsLpsMeStatusSwitchovers_Object = MibTableColumn
mplsLpsMeStatusSwitchovers = _MplsLpsMeStatusSwitchovers_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 4),
    _MplsLpsMeStatusSwitchovers_Type()
)
mplsLpsMeStatusSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusSwitchovers.setStatus("current")
_MplsLpsMeStatusLastSwitchover_Type = TimeStamp
_MplsLpsMeStatusLastSwitchover_Object = MibTableColumn
mplsLpsMeStatusLastSwitchover = _MplsLpsMeStatusLastSwitchover_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 5),
    _MplsLpsMeStatusLastSwitchover_Type()
)
mplsLpsMeStatusLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusLastSwitchover.setStatus("current")
_MplsLpsMeStatusSwitchoverSeconds_Type = Counter32
_MplsLpsMeStatusSwitchoverSeconds_Object = MibTableColumn
mplsLpsMeStatusSwitchoverSeconds = _MplsLpsMeStatusSwitchoverSeconds_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 5, 1, 6),
    _MplsLpsMeStatusSwitchoverSeconds_Type()
)
mplsLpsMeStatusSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLpsMeStatusSwitchoverSeconds.setStatus("current")
if mibBuilder.loadTexts:
    mplsLpsMeStatusSwitchoverSeconds.setUnits("seconds")


class _MplsLpsNotificationEnable_Type(Bits):
    """Custom type mplsLpsNotificationEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("switchover", 0),
          ("revertiveMismatch", 1),
          ("protecTypeMismatch", 2),
          ("capabilitiesMismatch", 3),
          ("pathConfigMismatch", 4),
          ("fopNoResponse", 5),
          ("fopTimeout", 6))
    )

_MplsLpsNotificationEnable_Type.__name__ = "Bits"
_MplsLpsNotificationEnable_Object = MibScalar
mplsLpsNotificationEnable = _MplsLpsNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 1, 6),
    _MplsLpsNotificationEnable_Type()
)
mplsLpsNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLpsNotificationEnable.setStatus("current")
_MplsLpsConformance_ObjectIdentity = ObjectIdentity
mplsLpsConformance = _MplsLpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2)
)
_MplsLpsCompliances_ObjectIdentity = ObjectIdentity
mplsLpsCompliances = _MplsLpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 1)
)
_MplsLpsGroups_ObjectIdentity = ObjectIdentity
mplsLpsGroups = _MplsLpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 2)
)
mplsLpsConfigEntry.registerAugmentions(
    ("MPLS-LPS-MIB",
     "mplsLpsStatusEntry")
)
mplsLpsStatusEntry.setIndexNames(*mplsLpsConfigEntry.getIndexNames())
mplsLpsMeConfigEntry.registerAugmentions(
    ("MPLS-LPS-MIB",
     "mplsLpsMeStatusEntry")
)
mplsLpsMeStatusEntry.setIndexNames(*mplsLpsMeConfigEntry.getIndexNames())

# Managed Objects groups

mplsLpsScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 2, 1)
)
mplsLpsScalarGroup.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsConfigDomainIndexNext"),
        ("MPLS-LPS-MIB", "mplsLpsNotificationEnable"))
)
if mibBuilder.loadTexts:
    mplsLpsScalarGroup.setStatus("current")

mplsLpsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 2, 2)
)
mplsLpsTableGroup.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsConfigDomainName"),
        ("MPLS-LPS-MIB", "mplsLpsConfigRowStatus"),
        ("MPLS-LPS-MIB", "mplsLpsConfigMode"),
        ("MPLS-LPS-MIB", "mplsLpsConfigProtectionType"),
        ("MPLS-LPS-MIB", "mplsLpsConfigRevertive"),
        ("MPLS-LPS-MIB", "mplsLpsConfigSdThreshold"),
        ("MPLS-LPS-MIB", "mplsLpsConfigSdBadSeconds"),
        ("MPLS-LPS-MIB", "mplsLpsConfigSdGoodSeconds"),
        ("MPLS-LPS-MIB", "mplsLpsConfigWaitToRestore"),
        ("MPLS-LPS-MIB", "mplsLpsConfigHoldOff"),
        ("MPLS-LPS-MIB", "mplsLpsConfigContinualTxInterval"),
        ("MPLS-LPS-MIB", "mplsLpsConfigRapidTxInterval"),
        ("MPLS-LPS-MIB", "mplsLpsConfigCommand"),
        ("MPLS-LPS-MIB", "mplsLpsConfigCreationTime"),
        ("MPLS-LPS-MIB", "mplsLpsConfigStorageType"),
        ("MPLS-LPS-MIB", "mplsLpsStatusState"),
        ("MPLS-LPS-MIB", "mplsLpsStatusReqRcv"),
        ("MPLS-LPS-MIB", "mplsLpsStatusReqSent"),
        ("MPLS-LPS-MIB", "mplsLpsStatusFpathPathRcv"),
        ("MPLS-LPS-MIB", "mplsLpsStatusFpathPathSent"),
        ("MPLS-LPS-MIB", "mplsLpsStatusRevertiveMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsStatusProtecTypeMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsStatusCapabilitiesMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsStatusPathConfigMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsStatusFopNoResponses"),
        ("MPLS-LPS-MIB", "mplsLpsStatusFopTimeouts"))
)
if mibBuilder.loadTexts:
    mplsLpsTableGroup.setStatus("current")

mplsLpsMeTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 2, 3)
)
mplsLpsMeTableGroup.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsMeConfigDomain"),
        ("MPLS-LPS-MIB", "mplsLpsMeConfigPath"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusCurrent"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusSignalDegrades"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusSignalFailures"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusSwitchovers"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusLastSwitchover"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusSwitchoverSeconds"))
)
if mibBuilder.loadTexts:
    mplsLpsMeTableGroup.setStatus("current")


# Notification objects

mplsLpsEventSwitchover = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 1)
)
mplsLpsEventSwitchover.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsMeStatusSwitchovers"),
        ("MPLS-LPS-MIB", "mplsLpsMeStatusCurrent"))
)
if mibBuilder.loadTexts:
    mplsLpsEventSwitchover.setStatus(
        "current"
    )

mplsLpsEventRevertiveMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 2)
)
mplsLpsEventRevertiveMismatch.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusRevertiveMismatch")
)
if mibBuilder.loadTexts:
    mplsLpsEventRevertiveMismatch.setStatus(
        "current"
    )

mplsLpsEventProtecTypeMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 3)
)
mplsLpsEventProtecTypeMismatch.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusProtecTypeMismatch")
)
if mibBuilder.loadTexts:
    mplsLpsEventProtecTypeMismatch.setStatus(
        "current"
    )

mplsLpsEventCapabilitiesMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 4)
)
mplsLpsEventCapabilitiesMismatch.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusCapabilitiesMismatch")
)
if mibBuilder.loadTexts:
    mplsLpsEventCapabilitiesMismatch.setStatus(
        "current"
    )

mplsLpsEventPathConfigMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 5)
)
mplsLpsEventPathConfigMismatch.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusPathConfigMismatch")
)
if mibBuilder.loadTexts:
    mplsLpsEventPathConfigMismatch.setStatus(
        "current"
    )

mplsLpsEventFopNoResponse = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 6)
)
mplsLpsEventFopNoResponse.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusFopNoResponses")
)
if mibBuilder.loadTexts:
    mplsLpsEventFopNoResponse.setStatus(
        "current"
    )

mplsLpsEventFopTimeout = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 0, 7)
)
mplsLpsEventFopTimeout.setObjects(
    ("MPLS-LPS-MIB", "mplsLpsStatusFopTimeouts")
)
if mibBuilder.loadTexts:
    mplsLpsEventFopTimeout.setStatus(
        "current"
    )


# Notifications groups

mplsLpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 2, 4)
)
mplsLpsNotificationGroup.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsEventSwitchover"),
        ("MPLS-LPS-MIB", "mplsLpsEventRevertiveMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsEventProtecTypeMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsEventCapabilitiesMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsEventPathConfigMismatch"),
        ("MPLS-LPS-MIB", "mplsLpsEventFopNoResponse"),
        ("MPLS-LPS-MIB", "mplsLpsEventFopTimeout"))
)
if mibBuilder.loadTexts:
    mplsLpsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLpsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 1, 1)
)
mplsLpsModuleFullCompliance.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsScalarGroup"),
        ("MPLS-LPS-MIB", "mplsLpsTableGroup"),
        ("MPLS-LPS-MIB", "mplsLpsMeTableGroup"),
        ("MPLS-LPS-MIB", "mplsLpsNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsLpsModuleFullCompliance.setStatus(
        "current"
    )

mplsLpsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 22, 2, 1, 2)
)
mplsLpsModuleReadOnlyCompliance.setObjects(
      *(("MPLS-LPS-MIB", "mplsLpsScalarGroup"),
        ("MPLS-LPS-MIB", "mplsLpsTableGroup"),
        ("MPLS-LPS-MIB", "mplsLpsMeTableGroup"),
        ("MPLS-LPS-MIB", "mplsLpsNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsLpsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LPS-MIB",
    **{"MplsLpsReq": MplsLpsReq,
       "MplsLpsFpathPath": MplsLpsFpathPath,
       "MplsLpsCommand": MplsLpsCommand,
       "MplsLpsState": MplsLpsState,
       "mplsLpsMIB": mplsLpsMIB,
       "mplsLpsNotifications": mplsLpsNotifications,
       "mplsLpsEventSwitchover": mplsLpsEventSwitchover,
       "mplsLpsEventRevertiveMismatch": mplsLpsEventRevertiveMismatch,
       "mplsLpsEventProtecTypeMismatch": mplsLpsEventProtecTypeMismatch,
       "mplsLpsEventCapabilitiesMismatch": mplsLpsEventCapabilitiesMismatch,
       "mplsLpsEventPathConfigMismatch": mplsLpsEventPathConfigMismatch,
       "mplsLpsEventFopNoResponse": mplsLpsEventFopNoResponse,
       "mplsLpsEventFopTimeout": mplsLpsEventFopTimeout,
       "mplsLpsObjects": mplsLpsObjects,
       "mplsLpsConfigDomainIndexNext": mplsLpsConfigDomainIndexNext,
       "mplsLpsConfigTable": mplsLpsConfigTable,
       "mplsLpsConfigEntry": mplsLpsConfigEntry,
       "mplsLpsConfigDomainIndex": mplsLpsConfigDomainIndex,
       "mplsLpsConfigDomainName": mplsLpsConfigDomainName,
       "mplsLpsConfigMode": mplsLpsConfigMode,
       "mplsLpsConfigProtectionType": mplsLpsConfigProtectionType,
       "mplsLpsConfigRevertive": mplsLpsConfigRevertive,
       "mplsLpsConfigSdThreshold": mplsLpsConfigSdThreshold,
       "mplsLpsConfigSdBadSeconds": mplsLpsConfigSdBadSeconds,
       "mplsLpsConfigSdGoodSeconds": mplsLpsConfigSdGoodSeconds,
       "mplsLpsConfigWaitToRestore": mplsLpsConfigWaitToRestore,
       "mplsLpsConfigHoldOff": mplsLpsConfigHoldOff,
       "mplsLpsConfigContinualTxInterval": mplsLpsConfigContinualTxInterval,
       "mplsLpsConfigRapidTxInterval": mplsLpsConfigRapidTxInterval,
       "mplsLpsConfigCommand": mplsLpsConfigCommand,
       "mplsLpsConfigCreationTime": mplsLpsConfigCreationTime,
       "mplsLpsConfigRowStatus": mplsLpsConfigRowStatus,
       "mplsLpsConfigStorageType": mplsLpsConfigStorageType,
       "mplsLpsStatusTable": mplsLpsStatusTable,
       "mplsLpsStatusEntry": mplsLpsStatusEntry,
       "mplsLpsStatusState": mplsLpsStatusState,
       "mplsLpsStatusReqRcv": mplsLpsStatusReqRcv,
       "mplsLpsStatusReqSent": mplsLpsStatusReqSent,
       "mplsLpsStatusFpathPathRcv": mplsLpsStatusFpathPathRcv,
       "mplsLpsStatusFpathPathSent": mplsLpsStatusFpathPathSent,
       "mplsLpsStatusRevertiveMismatch": mplsLpsStatusRevertiveMismatch,
       "mplsLpsStatusProtecTypeMismatch": mplsLpsStatusProtecTypeMismatch,
       "mplsLpsStatusCapabilitiesMismatch": mplsLpsStatusCapabilitiesMismatch,
       "mplsLpsStatusPathConfigMismatch": mplsLpsStatusPathConfigMismatch,
       "mplsLpsStatusFopNoResponses": mplsLpsStatusFopNoResponses,
       "mplsLpsStatusFopTimeouts": mplsLpsStatusFopTimeouts,
       "mplsLpsMeConfigTable": mplsLpsMeConfigTable,
       "mplsLpsMeConfigEntry": mplsLpsMeConfigEntry,
       "mplsLpsMeConfigDomain": mplsLpsMeConfigDomain,
       "mplsLpsMeConfigPath": mplsLpsMeConfigPath,
       "mplsLpsMeStatusTable": mplsLpsMeStatusTable,
       "mplsLpsMeStatusEntry": mplsLpsMeStatusEntry,
       "mplsLpsMeStatusCurrent": mplsLpsMeStatusCurrent,
       "mplsLpsMeStatusSignalDegrades": mplsLpsMeStatusSignalDegrades,
       "mplsLpsMeStatusSignalFailures": mplsLpsMeStatusSignalFailures,
       "mplsLpsMeStatusSwitchovers": mplsLpsMeStatusSwitchovers,
       "mplsLpsMeStatusLastSwitchover": mplsLpsMeStatusLastSwitchover,
       "mplsLpsMeStatusSwitchoverSeconds": mplsLpsMeStatusSwitchoverSeconds,
       "mplsLpsNotificationEnable": mplsLpsNotificationEnable,
       "mplsLpsConformance": mplsLpsConformance,
       "mplsLpsCompliances": mplsLpsCompliances,
       "mplsLpsModuleFullCompliance": mplsLpsModuleFullCompliance,
       "mplsLpsModuleReadOnlyCompliance": mplsLpsModuleReadOnlyCompliance,
       "mplsLpsGroups": mplsLpsGroups,
       "mplsLpsScalarGroup": mplsLpsScalarGroup,
       "mplsLpsTableGroup": mplsLpsTableGroup,
       "mplsLpsMeTableGroup": mplsLpsMeTableGroup,
       "mplsLpsNotificationGroup": mplsLpsNotificationGroup}
)
