# SNMP MIB module (CIENA-CES-TIME-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-TIME-SYNC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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

(cienaCesModuleSlotName,) = mibBuilder.importSymbols(
    "CIENA-CES-MODULE-MIB",
    "cienaCesModuleSlotName")

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesTimeSyncMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28)
)
if mibBuilder.loadTexts:
    cienaCesTimeSyncMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-01-21 00:00",
         "2015-09-28 00:00",
         "2015-04-20 00:00",
         "2015-04-10 00:00",
         "2015-03-19 00:00",
         "2015-03-11 00:00",
         "2015-02-04 00:00",
         "2015-01-23 00:00",
         "2015-01-07 00:00",
         "2014-04-25 00:00",
         "2014-03-25 00:00",
         "2013-12-03 00:00",
         "2013-05-17 00:00",
         "2013-05-07 00:00",
         "2013-04-20 00:00",
         "2013-04-16 00:00",
         "2013-04-08 00:00",
         "2013-03-08 00:00",
         "2012-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SsmStratumLevel(TextualConvention, Integer32):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("prc", 2),
          ("ssua", 3),
          ("ssub", 4),
          ("sec", 5),
          ("dnu", 6),
          ("prs", 7),
          ("stu", 8),
          ("st2", 9),
          ("tnc", 10),
          ("st3e", 11),
          ("st3", 12),
          ("smc", 13),
          ("st4", 14),
          ("dus", 15),
          ("prov", 16))
    )



class SyncInterfaceProtocol(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("bits", 2),
          ("synce", 3),
          ("ptp", 4),
          ("gps", 5),
          ("tdm", 6))
    )



class SyncBITSSignalMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("modeunknown", 1),
          ("modet1", 2),
          ("modee1", 3),
          ("modej1", 4),
          ("mode2048khz", 5),
          ("mode64kcc", 6),
          ("mode6312khz", 7))
    )



class SyncBITSSignalFormat(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("cas", 2),
          ("cascrc", 3),
          ("esf", 4),
          ("fas", 5),
          ("fascrc", 6),
          ("sf", 7),
          ("e1crc", 8),
          ("e1nocrc", 9))
    )



class SyncBITSSignalEncoding(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("b8zs", 2),
          ("ami", 3),
          ("hdb3", 4))
    )



class SyncRefOperationalStatus(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("active", 2),
          ("selected", 3),
          ("lossofsignal", 4),
          ("lossofframe", 5),
          ("alarmindicationsignal", 6),
          ("hardwarefault", 7),
          ("hardwarenotconfigured", 8),
          ("qlbelowthreshold", 9),
          ("rxtimeout", 10),
          ("notauthenticated", 11),
          ("loopbacktx", 12),
          ("loopbackrx", 13),
          ("linkflap", 14),
          ("notready", 15),
          ("signalfailure", 16),
          ("warmup", 17),
          ("qlnotconfigured", 18),
          ("noconnectivity", 19),
          ("unsupportedhardware", 20),
          ("unusable", 21))
    )



class SyncTimingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("frequency", 2),
          ("phase", 3),
          ("tod", 4),
          ("phaseandtod", 5))
    )



class SyncPTPRatePps(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("rate1over16pps", 2),
          ("rate1over8pps", 3),
          ("rate1over4pps", 4),
          ("rate1over2pps", 5),
          ("rate1pps", 6),
          ("rate2pps", 7),
          ("rate4pps", 8),
          ("rate8pps", 9),
          ("rate16pps", 10),
          ("rate32pps", 11),
          ("rate64pps", 12),
          ("rate128pps", 13))
    )



class SyncGPSFreqClock(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("clock10mhz", 2),
          ("clock2048khz", 3),
          ("clock1544khz", 4))
    )



class SyncPTPEncapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("udpoveripv4", 2),
          ("udpoveripv6", 3),
          ("ieee802dot3", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesTimeSyncMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBObjects = _CienaCesTimeSyncMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1)
)
_CienaCesTimeSyncObjects_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncObjects = _CienaCesTimeSyncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1)
)
_CienaCesSyncAdminState_Type = CienaGlobalState
_CienaCesSyncAdminState_Object = MibScalar
cienaCesSyncAdminState = _CienaCesSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 1),
    _CienaCesSyncAdminState_Type()
)
cienaCesSyncAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncAdminState.setStatus("current")


class _CienaCesSyncOptionType_Type(Integer32):
    """Custom type cienaCesSyncOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("option1", 2),
          ("option2", 3))
    )


_CienaCesSyncOptionType_Type.__name__ = "Integer32"
_CienaCesSyncOptionType_Object = MibScalar
cienaCesSyncOptionType = _CienaCesSyncOptionType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 2),
    _CienaCesSyncOptionType_Type()
)
cienaCesSyncOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncOptionType.setStatus("current")


class _CienaCesSyncRevertiveMode_Type(Integer32):
    """Custom type cienaCesSyncRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("revertive", 2),
          ("nonrevertive", 3))
    )


_CienaCesSyncRevertiveMode_Type.__name__ = "Integer32"
_CienaCesSyncRevertiveMode_Object = MibScalar
cienaCesSyncRevertiveMode = _CienaCesSyncRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 3),
    _CienaCesSyncRevertiveMode_Type()
)
cienaCesSyncRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncRevertiveMode.setStatus("current")
_CienaCesSyncWaitToRestoreTimer_Type = Unsigned32
_CienaCesSyncWaitToRestoreTimer_Object = MibScalar
cienaCesSyncWaitToRestoreTimer = _CienaCesSyncWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 4),
    _CienaCesSyncWaitToRestoreTimer_Type()
)
cienaCesSyncWaitToRestoreTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncWaitToRestoreTimer.setStatus("current")
_CienaCesSyncInputProtectionGroupTable_Object = MibTable
cienaCesSyncInputProtectionGroupTable = _CienaCesSyncInputProtectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupTable.setStatus("current")
_CienaCesSyncInputProtectionGroupEntry_Object = MibTableRow
cienaCesSyncInputProtectionGroupEntry = _CienaCesSyncInputProtectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1)
)
cienaCesSyncInputProtectionGroupEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupEntry.setStatus("current")


class _CienaCesInputPGEntityId_Type(Integer32):
    """Custom type cienaCesInputPGEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesInputPGEntityId_Type.__name__ = "Integer32"
_CienaCesInputPGEntityId_Object = MibTableColumn
cienaCesInputPGEntityId = _CienaCesInputPGEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 1),
    _CienaCesInputPGEntityId_Type()
)
cienaCesInputPGEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInputPGEntityId.setStatus("current")


class _CienaCesInputPGEntityName_Type(DisplayString):
    """Custom type cienaCesInputPGEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGEntityName_Type.__name__ = "DisplayString"
_CienaCesInputPGEntityName_Object = MibTableColumn
cienaCesInputPGEntityName = _CienaCesInputPGEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 2),
    _CienaCesInputPGEntityName_Type()
)
cienaCesInputPGEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGEntityName.setStatus("current")


class _CienaCesInputPGPreferredReference_Type(DisplayString):
    """Custom type cienaCesInputPGPreferredReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGPreferredReference_Type.__name__ = "DisplayString"
_CienaCesInputPGPreferredReference_Object = MibTableColumn
cienaCesInputPGPreferredReference = _CienaCesInputPGPreferredReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 3),
    _CienaCesInputPGPreferredReference_Type()
)
cienaCesInputPGPreferredReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGPreferredReference.setStatus("deprecated")


class _CienaCesInputPGSelectedReference_Type(DisplayString):
    """Custom type cienaCesInputPGSelectedReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGSelectedReference_Type.__name__ = "DisplayString"
_CienaCesInputPGSelectedReference_Object = MibTableColumn
cienaCesInputPGSelectedReference = _CienaCesInputPGSelectedReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 4),
    _CienaCesInputPGSelectedReference_Type()
)
cienaCesInputPGSelectedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGSelectedReference.setStatus("current")


class _CienaCesInputPGForcedReference_Type(DisplayString):
    """Custom type cienaCesInputPGForcedReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGForcedReference_Type.__name__ = "DisplayString"
_CienaCesInputPGForcedReference_Object = MibTableColumn
cienaCesInputPGForcedReference = _CienaCesInputPGForcedReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 5),
    _CienaCesInputPGForcedReference_Type()
)
cienaCesInputPGForcedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGForcedReference.setStatus("current")
_CienaCesInputPGThresholdQualityLevel_Type = SsmStratumLevel
_CienaCesInputPGThresholdQualityLevel_Object = MibTableColumn
cienaCesInputPGThresholdQualityLevel = _CienaCesInputPGThresholdQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 6),
    _CienaCesInputPGThresholdQualityLevel_Type()
)
cienaCesInputPGThresholdQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGThresholdQualityLevel.setStatus("current")
_CienaCesInputPGState_Type = CienaGlobalState
_CienaCesInputPGState_Object = MibTableColumn
cienaCesInputPGState = _CienaCesInputPGState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 7),
    _CienaCesInputPGState_Type()
)
cienaCesInputPGState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGState.setStatus("deprecated")


class _CienaCesInputPGStateDuration_Type(DisplayString):
    """Custom type cienaCesInputPGStateDuration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPGStateDuration_Type.__name__ = "DisplayString"
_CienaCesInputPGStateDuration_Object = MibTableColumn
cienaCesInputPGStateDuration = _CienaCesInputPGStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 8),
    _CienaCesInputPGStateDuration_Type()
)
cienaCesInputPGStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGStateDuration.setStatus("current")
_CienaCesInputPGReferenceSwitchCount_Type = Unsigned32
_CienaCesInputPGReferenceSwitchCount_Object = MibTableColumn
cienaCesInputPGReferenceSwitchCount = _CienaCesInputPGReferenceSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 9),
    _CienaCesInputPGReferenceSwitchCount_Type()
)
cienaCesInputPGReferenceSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGReferenceSwitchCount.setStatus("current")


class _CienaCesInputPGOperationalStatus_Type(Integer32):
    """Custom type cienaCesInputPGOperationalStatus based on Integer32"""
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
        *(("unknown", 1),
          ("freerun", 2),
          ("holdover", 3),
          ("locked", 4),
          ("acquiringlock", 5),
          ("holdoverexpired", 6))
    )


_CienaCesInputPGOperationalStatus_Type.__name__ = "Integer32"
_CienaCesInputPGOperationalStatus_Object = MibTableColumn
cienaCesInputPGOperationalStatus = _CienaCesInputPGOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 10),
    _CienaCesInputPGOperationalStatus_Type()
)
cienaCesInputPGOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGOperationalStatus.setStatus("current")
_CienaCesInputPGTimingType_Type = SyncTimingType
_CienaCesInputPGTimingType_Object = MibTableColumn
cienaCesInputPGTimingType = _CienaCesInputPGTimingType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 11),
    _CienaCesInputPGTimingType_Type()
)
cienaCesInputPGTimingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGTimingType.setStatus("current")
_CienaCesInputPGOperationalQualityLevel_Type = SsmStratumLevel
_CienaCesInputPGOperationalQualityLevel_Object = MibTableColumn
cienaCesInputPGOperationalQualityLevel = _CienaCesInputPGOperationalQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 12),
    _CienaCesInputPGOperationalQualityLevel_Type()
)
cienaCesInputPGOperationalQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPGOperationalQualityLevel.setStatus("current")
_CienaCesSyncInputProtectionUnitTable_Object = MibTable
cienaCesSyncInputProtectionUnitTable = _CienaCesSyncInputProtectionUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionUnitTable.setStatus("current")
_CienaCesSyncInputProtectionUnitEntry_Object = MibTableRow
cienaCesSyncInputProtectionUnitEntry = _CienaCesSyncInputProtectionUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1)
)
cienaCesSyncInputProtectionUnitEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionUnitEntry.setStatus("current")


class _CienaCesInputPUEntityId_Type(Integer32):
    """Custom type cienaCesInputPUEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CienaCesInputPUEntityId_Type.__name__ = "Integer32"
_CienaCesInputPUEntityId_Object = MibTableColumn
cienaCesInputPUEntityId = _CienaCesInputPUEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 1),
    _CienaCesInputPUEntityId_Type()
)
cienaCesInputPUEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInputPUEntityId.setStatus("current")


class _CienaCesInputPUEntityName_Type(DisplayString):
    """Custom type cienaCesInputPUEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPUEntityName_Type.__name__ = "DisplayString"
_CienaCesInputPUEntityName_Object = MibTableColumn
cienaCesInputPUEntityName = _CienaCesInputPUEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 2),
    _CienaCesInputPUEntityName_Type()
)
cienaCesInputPUEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUEntityName.setStatus("current")
_CienaCesInputPUPGEntityName_Type = DisplayString
_CienaCesInputPUPGEntityName_Object = MibTableColumn
cienaCesInputPUPGEntityName = _CienaCesInputPUPGEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 3),
    _CienaCesInputPUPGEntityName_Type()
)
cienaCesInputPUPGEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUPGEntityName.setStatus("current")


class _CienaCesInputPUTimingInterfaceName_Type(DisplayString):
    """Custom type cienaCesInputPUTimingInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInputPUTimingInterfaceName_Type.__name__ = "DisplayString"
_CienaCesInputPUTimingInterfaceName_Object = MibTableColumn
cienaCesInputPUTimingInterfaceName = _CienaCesInputPUTimingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 4),
    _CienaCesInputPUTimingInterfaceName_Type()
)
cienaCesInputPUTimingInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUTimingInterfaceName.setStatus("current")
_CienaCesInputPUTimingInterfaceProtocol_Type = SyncInterfaceProtocol
_CienaCesInputPUTimingInterfaceProtocol_Object = MibTableColumn
cienaCesInputPUTimingInterfaceProtocol = _CienaCesInputPUTimingInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 5),
    _CienaCesInputPUTimingInterfaceProtocol_Type()
)
cienaCesInputPUTimingInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUTimingInterfaceProtocol.setStatus("current")
_CienaCesInputPUUserPriority_Type = Unsigned32
_CienaCesInputPUUserPriority_Object = MibTableColumn
cienaCesInputPUUserPriority = _CienaCesInputPUUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 6),
    _CienaCesInputPUUserPriority_Type()
)
cienaCesInputPUUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUUserPriority.setStatus("current")
_CienaCesInputPUOperationalQL_Type = SsmStratumLevel
_CienaCesInputPUOperationalQL_Object = MibTableColumn
cienaCesInputPUOperationalQL = _CienaCesInputPUOperationalQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 7),
    _CienaCesInputPUOperationalQL_Type()
)
cienaCesInputPUOperationalQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUOperationalQL.setStatus("current")
_CienaCesInputPUForcedQL_Type = SsmStratumLevel
_CienaCesInputPUForcedQL_Object = MibTableColumn
cienaCesInputPUForcedQL = _CienaCesInputPUForcedQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 8),
    _CienaCesInputPUForcedQL_Type()
)
cienaCesInputPUForcedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUForcedQL.setStatus("current")
_CienaCesInputPUReceivedQL_Type = SsmStratumLevel
_CienaCesInputPUReceivedQL_Object = MibTableColumn
cienaCesInputPUReceivedQL = _CienaCesInputPUReceivedQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 9),
    _CienaCesInputPUReceivedQL_Type()
)
cienaCesInputPUReceivedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUReceivedQL.setStatus("current")


class _CienaCesInputPUSsmEnabled_Type(Integer32):
    """Custom type cienaCesInputPUSsmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_CienaCesInputPUSsmEnabled_Type.__name__ = "Integer32"
_CienaCesInputPUSsmEnabled_Object = MibTableColumn
cienaCesInputPUSsmEnabled = _CienaCesInputPUSsmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 10),
    _CienaCesInputPUSsmEnabled_Type()
)
cienaCesInputPUSsmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUSsmEnabled.setStatus("current")
_CienaCesInputPUOperationalStatus_Type = SyncRefOperationalStatus
_CienaCesInputPUOperationalStatus_Object = MibTableColumn
cienaCesInputPUOperationalStatus = _CienaCesInputPUOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 11),
    _CienaCesInputPUOperationalStatus_Type()
)
cienaCesInputPUOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUOperationalStatus.setStatus("current")
_CienaCesInputPUBITSSignalMode_Type = SyncBITSSignalMode
_CienaCesInputPUBITSSignalMode_Object = MibTableColumn
cienaCesInputPUBITSSignalMode = _CienaCesInputPUBITSSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 12),
    _CienaCesInputPUBITSSignalMode_Type()
)
cienaCesInputPUBITSSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalMode.setStatus("current")
_CienaCesInputPUBITSSignalFormat_Type = SyncBITSSignalFormat
_CienaCesInputPUBITSSignalFormat_Object = MibTableColumn
cienaCesInputPUBITSSignalFormat = _CienaCesInputPUBITSSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 13),
    _CienaCesInputPUBITSSignalFormat_Type()
)
cienaCesInputPUBITSSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalFormat.setStatus("current")
_CienaCesInputPUBITSSignalEncoding_Type = SyncBITSSignalEncoding
_CienaCesInputPUBITSSignalEncoding_Object = MibTableColumn
cienaCesInputPUBITSSignalEncoding = _CienaCesInputPUBITSSignalEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 14),
    _CienaCesInputPUBITSSignalEncoding_Type()
)
cienaCesInputPUBITSSignalEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalEncoding.setStatus("current")
_CienaCesInputPUUserOverridePriority_Type = Unsigned32
_CienaCesInputPUUserOverridePriority_Object = MibTableColumn
cienaCesInputPUUserOverridePriority = _CienaCesInputPUUserOverridePriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 15),
    _CienaCesInputPUUserOverridePriority_Type()
)
cienaCesInputPUUserOverridePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUUserOverridePriority.setStatus("current")
_CienaCesInputPUPTPEncapType_Type = SyncPTPEncapType
_CienaCesInputPUPTPEncapType_Object = MibTableColumn
cienaCesInputPUPTPEncapType = _CienaCesInputPUPTPEncapType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 16),
    _CienaCesInputPUPTPEncapType_Type()
)
cienaCesInputPUPTPEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUPTPEncapType.setStatus("current")
_CienaCesInputPUGPSClockMode_Type = SyncTimingType
_CienaCesInputPUGPSClockMode_Object = MibTableColumn
cienaCesInputPUGPSClockMode = _CienaCesInputPUGPSClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 17),
    _CienaCesInputPUGPSClockMode_Type()
)
cienaCesInputPUGPSClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUGPSClockMode.setStatus("current")
_CienaCesInputPUGPSFreqClock_Type = SyncGPSFreqClock
_CienaCesInputPUGPSFreqClock_Object = MibTableColumn
cienaCesInputPUGPSFreqClock = _CienaCesInputPUGPSFreqClock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 18),
    _CienaCesInputPUGPSFreqClock_Type()
)
cienaCesInputPUGPSFreqClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUGPSFreqClock.setStatus("current")


class _CienaCesInputPUBITSSignalSsmLocation_Type(Integer32):
    """Custom type cienaCesInputPUBITSSignalSsmLocation based on Integer32"""
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
        *(("unknown", 1),
          ("sa4", 2),
          ("sa5", 3),
          ("sa6", 4),
          ("sa7", 5),
          ("sa8", 6))
    )


_CienaCesInputPUBITSSignalSsmLocation_Type.__name__ = "Integer32"
_CienaCesInputPUBITSSignalSsmLocation_Object = MibTableColumn
cienaCesInputPUBITSSignalSsmLocation = _CienaCesInputPUBITSSignalSsmLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 19),
    _CienaCesInputPUBITSSignalSsmLocation_Type()
)
cienaCesInputPUBITSSignalSsmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInputPUBITSSignalSsmLocation.setStatus("current")
_CienaCesSyncOutputTable_Object = MibTable
cienaCesSyncOutputTable = _CienaCesSyncOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesSyncOutputTable.setStatus("current")
_CienaCesSyncOutputEntry_Object = MibTableRow
cienaCesSyncOutputEntry = _CienaCesSyncOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1)
)
cienaCesSyncOutputEntry.setIndexNames(
    (0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesOutputEntityId"),
)
if mibBuilder.loadTexts:
    cienaCesSyncOutputEntry.setStatus("current")


class _CienaCesOutputEntityId_Type(Integer32):
    """Custom type cienaCesOutputEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CienaCesOutputEntityId_Type.__name__ = "Integer32"
_CienaCesOutputEntityId_Object = MibTableColumn
cienaCesOutputEntityId = _CienaCesOutputEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 1),
    _CienaCesOutputEntityId_Type()
)
cienaCesOutputEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOutputEntityId.setStatus("current")


class _CienaCesOutputEntityName_Type(DisplayString):
    """Custom type cienaCesOutputEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesOutputEntityName_Type.__name__ = "DisplayString"
_CienaCesOutputEntityName_Object = MibTableColumn
cienaCesOutputEntityName = _CienaCesOutputEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 2),
    _CienaCesOutputEntityName_Type()
)
cienaCesOutputEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputEntityName.setStatus("current")


class _CienaCesOutputTimingInterfaceName_Type(DisplayString):
    """Custom type cienaCesOutputTimingInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesOutputTimingInterfaceName_Type.__name__ = "DisplayString"
_CienaCesOutputTimingInterfaceName_Object = MibTableColumn
cienaCesOutputTimingInterfaceName = _CienaCesOutputTimingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 3),
    _CienaCesOutputTimingInterfaceName_Type()
)
cienaCesOutputTimingInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputTimingInterfaceName.setStatus("current")
_CienaCesOutputTimingInterfaceProtocol_Type = SyncInterfaceProtocol
_CienaCesOutputTimingInterfaceProtocol_Object = MibTableColumn
cienaCesOutputTimingInterfaceProtocol = _CienaCesOutputTimingInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 4),
    _CienaCesOutputTimingInterfaceProtocol_Type()
)
cienaCesOutputTimingInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputTimingInterfaceProtocol.setStatus("current")
_CienaCesOutputOperationalQL_Type = SsmStratumLevel
_CienaCesOutputOperationalQL_Object = MibTableColumn
cienaCesOutputOperationalQL = _CienaCesOutputOperationalQL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 5),
    _CienaCesOutputOperationalQL_Type()
)
cienaCesOutputOperationalQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputOperationalQL.setStatus("current")
_CienaCesOutputOperationalStatus_Type = SyncRefOperationalStatus
_CienaCesOutputOperationalStatus_Object = MibTableColumn
cienaCesOutputOperationalStatus = _CienaCesOutputOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 6),
    _CienaCesOutputOperationalStatus_Type()
)
cienaCesOutputOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputOperationalStatus.setStatus("current")
_CienaCesOutputBITSSignalMode_Type = SyncBITSSignalMode
_CienaCesOutputBITSSignalMode_Object = MibTableColumn
cienaCesOutputBITSSignalMode = _CienaCesOutputBITSSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 7),
    _CienaCesOutputBITSSignalMode_Type()
)
cienaCesOutputBITSSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalMode.setStatus("current")
_CienaCesOutputBITSSignalFormat_Type = SyncBITSSignalFormat
_CienaCesOutputBITSSignalFormat_Object = MibTableColumn
cienaCesOutputBITSSignalFormat = _CienaCesOutputBITSSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 8),
    _CienaCesOutputBITSSignalFormat_Type()
)
cienaCesOutputBITSSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalFormat.setStatus("current")
_CienaCesOutputBITSSignalEncoding_Type = SyncBITSSignalEncoding
_CienaCesOutputBITSSignalEncoding_Object = MibTableColumn
cienaCesOutputBITSSignalEncoding = _CienaCesOutputBITSSignalEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 9),
    _CienaCesOutputBITSSignalEncoding_Type()
)
cienaCesOutputBITSSignalEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalEncoding.setStatus("current")


class _CienaCesOutputBITSSignalLineBuildout_Type(Integer32):
    """Custom type cienaCesOutputBITSSignalLineBuildout based on Integer32"""
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
        *(("unknown", 1),
          ("lbo133", 2),
          ("lbo266", 3),
          ("lbo399", 4),
          ("lbo533", 5),
          ("lbo655", 6))
    )


_CienaCesOutputBITSSignalLineBuildout_Type.__name__ = "Integer32"
_CienaCesOutputBITSSignalLineBuildout_Object = MibTableColumn
cienaCesOutputBITSSignalLineBuildout = _CienaCesOutputBITSSignalLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 10),
    _CienaCesOutputBITSSignalLineBuildout_Type()
)
cienaCesOutputBITSSignalLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalLineBuildout.setStatus("current")


class _CienaCesOutputBITSSignalSsmLocation_Type(Integer32):
    """Custom type cienaCesOutputBITSSignalSsmLocation based on Integer32"""
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
        *(("unknown", 1),
          ("sa4", 2),
          ("sa5", 3),
          ("sa6", 4),
          ("sa7", 5),
          ("sa8", 6))
    )


_CienaCesOutputBITSSignalSsmLocation_Type.__name__ = "Integer32"
_CienaCesOutputBITSSignalSsmLocation_Object = MibTableColumn
cienaCesOutputBITSSignalSsmLocation = _CienaCesOutputBITSSignalSsmLocation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 11),
    _CienaCesOutputBITSSignalSsmLocation_Type()
)
cienaCesOutputBITSSignalSsmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputBITSSignalSsmLocation.setStatus("current")
_CienaCesOutputGPSClockMode_Type = SyncTimingType
_CienaCesOutputGPSClockMode_Object = MibTableColumn
cienaCesOutputGPSClockMode = _CienaCesOutputGPSClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 12),
    _CienaCesOutputGPSClockMode_Type()
)
cienaCesOutputGPSClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputGPSClockMode.setStatus("current")
_CienaCesOutputGPSFreqClock_Type = SyncGPSFreqClock
_CienaCesOutputGPSFreqClock_Object = MibTableColumn
cienaCesOutputGPSFreqClock = _CienaCesOutputGPSFreqClock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 13),
    _CienaCesOutputGPSFreqClock_Type()
)
cienaCesOutputGPSFreqClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputGPSFreqClock.setStatus("current")
_CienaCesOutputPTPEncapType_Type = SyncPTPEncapType
_CienaCesOutputPTPEncapType_Object = MibTableColumn
cienaCesOutputPTPEncapType = _CienaCesOutputPTPEncapType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 14),
    _CienaCesOutputPTPEncapType_Type()
)
cienaCesOutputPTPEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOutputPTPEncapType.setStatus("current")
_CienaCesSyncPTPConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncPTPConfig = _CienaCesSyncPTPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8)
)
_CienaCesSyncPTPGlobalConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncPTPGlobalConfig = _CienaCesSyncPTPGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1)
)


class _CienaCesSyncPTPAddrMode_Type(Integer32):
    """Custom type cienaCesSyncPTPAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("unicast", 2),
          ("multicast", 3))
    )


_CienaCesSyncPTPAddrMode_Type.__name__ = "Integer32"
_CienaCesSyncPTPAddrMode_Object = MibScalar
cienaCesSyncPTPAddrMode = _CienaCesSyncPTPAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 1),
    _CienaCesSyncPTPAddrMode_Type()
)
cienaCesSyncPTPAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPAddrMode.setStatus("current")
_CienaCesSyncPTPTagPriority_Type = Unsigned32
_CienaCesSyncPTPTagPriority_Object = MibScalar
cienaCesSyncPTPTagPriority = _CienaCesSyncPTPTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 2),
    _CienaCesSyncPTPTagPriority_Type()
)
cienaCesSyncPTPTagPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPTagPriority.setStatus("current")


class _CienaCesSyncPTPProtocolVersion_Type(Integer32):
    """Custom type cienaCesSyncPTPProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("v2", 2))
    )


_CienaCesSyncPTPProtocolVersion_Type.__name__ = "Integer32"
_CienaCesSyncPTPProtocolVersion_Object = MibScalar
cienaCesSyncPTPProtocolVersion = _CienaCesSyncPTPProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 3),
    _CienaCesSyncPTPProtocolVersion_Type()
)
cienaCesSyncPTPProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPProtocolVersion.setStatus("current")


class _CienaCesSyncPTPProfileVersion_Type(Integer32):
    """Custom type cienaCesSyncPTPProfileVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("version1dot0", 2))
    )


_CienaCesSyncPTPProfileVersion_Type.__name__ = "Integer32"
_CienaCesSyncPTPProfileVersion_Object = MibScalar
cienaCesSyncPTPProfileVersion = _CienaCesSyncPTPProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 4),
    _CienaCesSyncPTPProfileVersion_Type()
)
cienaCesSyncPTPProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPProfileVersion.setStatus("current")
_CienaCesSyncPTPProfileIdentifier_Type = MacAddress
_CienaCesSyncPTPProfileIdentifier_Object = MibScalar
cienaCesSyncPTPProfileIdentifier = _CienaCesSyncPTPProfileIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 5),
    _CienaCesSyncPTPProfileIdentifier_Type()
)
cienaCesSyncPTPProfileIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPProfileIdentifier.setStatus("current")
_CienaCesSyncPTPDomainNumber_Type = Unsigned32
_CienaCesSyncPTPDomainNumber_Object = MibScalar
cienaCesSyncPTPDomainNumber = _CienaCesSyncPTPDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 6),
    _CienaCesSyncPTPDomainNumber_Type()
)
cienaCesSyncPTPDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPDomainNumber.setStatus("current")


class _CienaCesSyncPTPClockType_Type(Integer32):
    """Custom type cienaCesSyncPTPClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ocslave", 2),
          ("bc", 3))
    )


_CienaCesSyncPTPClockType_Type.__name__ = "Integer32"
_CienaCesSyncPTPClockType_Object = MibScalar
cienaCesSyncPTPClockType = _CienaCesSyncPTPClockType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 7),
    _CienaCesSyncPTPClockType_Type()
)
cienaCesSyncPTPClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPClockType.setStatus("current")


class _CienaCesSyncPTPClockID_Type(DisplayString):
    """Custom type cienaCesSyncPTPClockID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesSyncPTPClockID_Type.__name__ = "DisplayString"
_CienaCesSyncPTPClockID_Object = MibScalar
cienaCesSyncPTPClockID = _CienaCesSyncPTPClockID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 8),
    _CienaCesSyncPTPClockID_Type()
)
cienaCesSyncPTPClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPClockID.setStatus("current")
_CienaCesSyncPTPDscp_Type = Unsigned32
_CienaCesSyncPTPDscp_Object = MibScalar
cienaCesSyncPTPDscp = _CienaCesSyncPTPDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 1, 9),
    _CienaCesSyncPTPDscp_Type()
)
cienaCesSyncPTPDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPDscp.setStatus("current")
_CienaCesSyncPTPInputConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncPTPInputConfig = _CienaCesSyncPTPInputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2)
)
_CienaCesSyncPTPInputUnicastReqDuration_Type = Unsigned32
_CienaCesSyncPTPInputUnicastReqDuration_Object = MibScalar
cienaCesSyncPTPInputUnicastReqDuration = _CienaCesSyncPTPInputUnicastReqDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2, 1),
    _CienaCesSyncPTPInputUnicastReqDuration_Type()
)
cienaCesSyncPTPInputUnicastReqDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPInputUnicastReqDuration.setStatus("current")
_CienaCesSyncPTPInputAnnounceRxLossNum_Type = Unsigned32
_CienaCesSyncPTPInputAnnounceRxLossNum_Object = MibScalar
cienaCesSyncPTPInputAnnounceRxLossNum = _CienaCesSyncPTPInputAnnounceRxLossNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2, 2),
    _CienaCesSyncPTPInputAnnounceRxLossNum_Type()
)
cienaCesSyncPTPInputAnnounceRxLossNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPInputAnnounceRxLossNum.setStatus("current")
_CienaCesSyncPTPInputAnnounceTxRateReq_Type = SyncPTPRatePps
_CienaCesSyncPTPInputAnnounceTxRateReq_Object = MibScalar
cienaCesSyncPTPInputAnnounceTxRateReq = _CienaCesSyncPTPInputAnnounceTxRateReq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2, 3),
    _CienaCesSyncPTPInputAnnounceTxRateReq_Type()
)
cienaCesSyncPTPInputAnnounceTxRateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPInputAnnounceTxRateReq.setStatus("current")
_CienaCesSyncPTPInputSyncTxRateReq_Type = SyncPTPRatePps
_CienaCesSyncPTPInputSyncTxRateReq_Object = MibScalar
cienaCesSyncPTPInputSyncTxRateReq = _CienaCesSyncPTPInputSyncTxRateReq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2, 4),
    _CienaCesSyncPTPInputSyncTxRateReq_Type()
)
cienaCesSyncPTPInputSyncTxRateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPInputSyncTxRateReq.setStatus("current")
_CienaCesSyncPTPInputDelayReqTxRate_Type = SyncPTPRatePps
_CienaCesSyncPTPInputDelayReqTxRate_Object = MibScalar
cienaCesSyncPTPInputDelayReqTxRate = _CienaCesSyncPTPInputDelayReqTxRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 2, 5),
    _CienaCesSyncPTPInputDelayReqTxRate_Type()
)
cienaCesSyncPTPInputDelayReqTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPInputDelayReqTxRate.setStatus("current")
_CienaCesSyncPTPOutputConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncPTPOutputConfig = _CienaCesSyncPTPOutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 3)
)
_CienaCesSyncPTPOutputMaxSlaveSessions_Type = Unsigned32
_CienaCesSyncPTPOutputMaxSlaveSessions_Object = MibScalar
cienaCesSyncPTPOutputMaxSlaveSessions = _CienaCesSyncPTPOutputMaxSlaveSessions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 3, 1),
    _CienaCesSyncPTPOutputMaxSlaveSessions_Type()
)
cienaCesSyncPTPOutputMaxSlaveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPOutputMaxSlaveSessions.setStatus("current")


class _CienaCesSyncPTPOutputTimestampMode_Type(Integer32):
    """Custom type cienaCesSyncPTPOutputTimestampMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onestep", 2),
          ("twostep", 3))
    )


_CienaCesSyncPTPOutputTimestampMode_Type.__name__ = "Integer32"
_CienaCesSyncPTPOutputTimestampMode_Object = MibScalar
cienaCesSyncPTPOutputTimestampMode = _CienaCesSyncPTPOutputTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 8, 3, 2),
    _CienaCesSyncPTPOutputTimestampMode_Type()
)
cienaCesSyncPTPOutputTimestampMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncPTPOutputTimestampMode.setStatus("current")
_CienaCesSyncGPSConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncGPSConfig = _CienaCesSyncGPSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 9)
)
_CienaCesSyncGPSOutputConfig_ObjectIdentity = ObjectIdentity
cienaCesSyncGPSOutputConfig = _CienaCesSyncGPSOutputConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 9, 1)
)
_CienaCesSyncGPSOutput1ppsPulseWidth_Type = Unsigned32
_CienaCesSyncGPSOutput1ppsPulseWidth_Object = MibScalar
cienaCesSyncGPSOutput1ppsPulseWidth = _CienaCesSyncGPSOutput1ppsPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 9, 1, 1),
    _CienaCesSyncGPSOutput1ppsPulseWidth_Type()
)
cienaCesSyncGPSOutput1ppsPulseWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncGPSOutput1ppsPulseWidth.setStatus("current")


class _CienaCesSyncHoldoverInterval_Type(Integer32):
    """Custom type cienaCesSyncHoldoverInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("indefinite", 2),
          ("twentyfourhours", 3))
    )


_CienaCesSyncHoldoverInterval_Type.__name__ = "Integer32"
_CienaCesSyncHoldoverInterval_Object = MibScalar
cienaCesSyncHoldoverInterval = _CienaCesSyncHoldoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 10),
    _CienaCesSyncHoldoverInterval_Type()
)
cienaCesSyncHoldoverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesSyncHoldoverInterval.setStatus("current")


class _CienaCesSyncModuleSlotClockStatus_Type(Integer32):
    """Custom type cienaCesSyncModuleSlotClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("lossoflock", 2),
          ("lockedtoprimaryctx", 3),
          ("lockedtosecondaryctx", 4))
    )


_CienaCesSyncModuleSlotClockStatus_Type.__name__ = "Integer32"
_CienaCesSyncModuleSlotClockStatus_Object = MibScalar
cienaCesSyncModuleSlotClockStatus = _CienaCesSyncModuleSlotClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 11),
    _CienaCesSyncModuleSlotClockStatus_Type()
)
cienaCesSyncModuleSlotClockStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesSyncModuleSlotClockStatus.setStatus("current")
_CienaCesTimeSyncMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBNotificationPrefix = _CienaCesTimeSyncMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28)
)
_CienaCesTimeSyncMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesTimeSyncMIBNotifications = _CienaCesTimeSyncMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0)
)

# Managed Objects groups


# Notification objects

cienaCesSyncInputPUStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 1)
)
cienaCesSyncInputPUStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUPGEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceProtocol"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUOperationalStatus"))
)
if mibBuilder.loadTexts:
    cienaCesSyncInputPUStateChangeNotification.setStatus(
        "current"
    )

cienaCesSyncInputProtectionGroupStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 2)
)
cienaCesSyncInputProtectionGroupStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGOperationalStatus"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGSelectedReference"))
)
if mibBuilder.loadTexts:
    cienaCesSyncInputProtectionGroupStateChangeNotification.setStatus(
        "current"
    )

cienaCesSyncModuleSlotClockStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 3)
)
cienaCesSyncModuleSlotClockStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotName"),
        ("CIENA-CES-TIME-SYNC-MIB", "cienaCesSyncModuleSlotClockStatus"))
)
if mibBuilder.loadTexts:
    cienaCesSyncModuleSlotClockStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-TIME-SYNC-MIB",
    **{"SsmStratumLevel": SsmStratumLevel,
       "SyncInterfaceProtocol": SyncInterfaceProtocol,
       "SyncBITSSignalMode": SyncBITSSignalMode,
       "SyncBITSSignalFormat": SyncBITSSignalFormat,
       "SyncBITSSignalEncoding": SyncBITSSignalEncoding,
       "SyncRefOperationalStatus": SyncRefOperationalStatus,
       "SyncTimingType": SyncTimingType,
       "SyncPTPRatePps": SyncPTPRatePps,
       "SyncGPSFreqClock": SyncGPSFreqClock,
       "SyncPTPEncapType": SyncPTPEncapType,
       "cienaCesTimeSyncMIB": cienaCesTimeSyncMIB,
       "cienaCesTimeSyncMIBObjects": cienaCesTimeSyncMIBObjects,
       "cienaCesTimeSyncObjects": cienaCesTimeSyncObjects,
       "cienaCesSyncAdminState": cienaCesSyncAdminState,
       "cienaCesSyncOptionType": cienaCesSyncOptionType,
       "cienaCesSyncRevertiveMode": cienaCesSyncRevertiveMode,
       "cienaCesSyncWaitToRestoreTimer": cienaCesSyncWaitToRestoreTimer,
       "cienaCesSyncInputProtectionGroupTable": cienaCesSyncInputProtectionGroupTable,
       "cienaCesSyncInputProtectionGroupEntry": cienaCesSyncInputProtectionGroupEntry,
       "cienaCesInputPGEntityId": cienaCesInputPGEntityId,
       "cienaCesInputPGEntityName": cienaCesInputPGEntityName,
       "cienaCesInputPGPreferredReference": cienaCesInputPGPreferredReference,
       "cienaCesInputPGSelectedReference": cienaCesInputPGSelectedReference,
       "cienaCesInputPGForcedReference": cienaCesInputPGForcedReference,
       "cienaCesInputPGThresholdQualityLevel": cienaCesInputPGThresholdQualityLevel,
       "cienaCesInputPGState": cienaCesInputPGState,
       "cienaCesInputPGStateDuration": cienaCesInputPGStateDuration,
       "cienaCesInputPGReferenceSwitchCount": cienaCesInputPGReferenceSwitchCount,
       "cienaCesInputPGOperationalStatus": cienaCesInputPGOperationalStatus,
       "cienaCesInputPGTimingType": cienaCesInputPGTimingType,
       "cienaCesInputPGOperationalQualityLevel": cienaCesInputPGOperationalQualityLevel,
       "cienaCesSyncInputProtectionUnitTable": cienaCesSyncInputProtectionUnitTable,
       "cienaCesSyncInputProtectionUnitEntry": cienaCesSyncInputProtectionUnitEntry,
       "cienaCesInputPUEntityId": cienaCesInputPUEntityId,
       "cienaCesInputPUEntityName": cienaCesInputPUEntityName,
       "cienaCesInputPUPGEntityName": cienaCesInputPUPGEntityName,
       "cienaCesInputPUTimingInterfaceName": cienaCesInputPUTimingInterfaceName,
       "cienaCesInputPUTimingInterfaceProtocol": cienaCesInputPUTimingInterfaceProtocol,
       "cienaCesInputPUUserPriority": cienaCesInputPUUserPriority,
       "cienaCesInputPUOperationalQL": cienaCesInputPUOperationalQL,
       "cienaCesInputPUForcedQL": cienaCesInputPUForcedQL,
       "cienaCesInputPUReceivedQL": cienaCesInputPUReceivedQL,
       "cienaCesInputPUSsmEnabled": cienaCesInputPUSsmEnabled,
       "cienaCesInputPUOperationalStatus": cienaCesInputPUOperationalStatus,
       "cienaCesInputPUBITSSignalMode": cienaCesInputPUBITSSignalMode,
       "cienaCesInputPUBITSSignalFormat": cienaCesInputPUBITSSignalFormat,
       "cienaCesInputPUBITSSignalEncoding": cienaCesInputPUBITSSignalEncoding,
       "cienaCesInputPUUserOverridePriority": cienaCesInputPUUserOverridePriority,
       "cienaCesInputPUPTPEncapType": cienaCesInputPUPTPEncapType,
       "cienaCesInputPUGPSClockMode": cienaCesInputPUGPSClockMode,
       "cienaCesInputPUGPSFreqClock": cienaCesInputPUGPSFreqClock,
       "cienaCesInputPUBITSSignalSsmLocation": cienaCesInputPUBITSSignalSsmLocation,
       "cienaCesSyncOutputTable": cienaCesSyncOutputTable,
       "cienaCesSyncOutputEntry": cienaCesSyncOutputEntry,
       "cienaCesOutputEntityId": cienaCesOutputEntityId,
       "cienaCesOutputEntityName": cienaCesOutputEntityName,
       "cienaCesOutputTimingInterfaceName": cienaCesOutputTimingInterfaceName,
       "cienaCesOutputTimingInterfaceProtocol": cienaCesOutputTimingInterfaceProtocol,
       "cienaCesOutputOperationalQL": cienaCesOutputOperationalQL,
       "cienaCesOutputOperationalStatus": cienaCesOutputOperationalStatus,
       "cienaCesOutputBITSSignalMode": cienaCesOutputBITSSignalMode,
       "cienaCesOutputBITSSignalFormat": cienaCesOutputBITSSignalFormat,
       "cienaCesOutputBITSSignalEncoding": cienaCesOutputBITSSignalEncoding,
       "cienaCesOutputBITSSignalLineBuildout": cienaCesOutputBITSSignalLineBuildout,
       "cienaCesOutputBITSSignalSsmLocation": cienaCesOutputBITSSignalSsmLocation,
       "cienaCesOutputGPSClockMode": cienaCesOutputGPSClockMode,
       "cienaCesOutputGPSFreqClock": cienaCesOutputGPSFreqClock,
       "cienaCesOutputPTPEncapType": cienaCesOutputPTPEncapType,
       "cienaCesSyncPTPConfig": cienaCesSyncPTPConfig,
       "cienaCesSyncPTPGlobalConfig": cienaCesSyncPTPGlobalConfig,
       "cienaCesSyncPTPAddrMode": cienaCesSyncPTPAddrMode,
       "cienaCesSyncPTPTagPriority": cienaCesSyncPTPTagPriority,
       "cienaCesSyncPTPProtocolVersion": cienaCesSyncPTPProtocolVersion,
       "cienaCesSyncPTPProfileVersion": cienaCesSyncPTPProfileVersion,
       "cienaCesSyncPTPProfileIdentifier": cienaCesSyncPTPProfileIdentifier,
       "cienaCesSyncPTPDomainNumber": cienaCesSyncPTPDomainNumber,
       "cienaCesSyncPTPClockType": cienaCesSyncPTPClockType,
       "cienaCesSyncPTPClockID": cienaCesSyncPTPClockID,
       "cienaCesSyncPTPDscp": cienaCesSyncPTPDscp,
       "cienaCesSyncPTPInputConfig": cienaCesSyncPTPInputConfig,
       "cienaCesSyncPTPInputUnicastReqDuration": cienaCesSyncPTPInputUnicastReqDuration,
       "cienaCesSyncPTPInputAnnounceRxLossNum": cienaCesSyncPTPInputAnnounceRxLossNum,
       "cienaCesSyncPTPInputAnnounceTxRateReq": cienaCesSyncPTPInputAnnounceTxRateReq,
       "cienaCesSyncPTPInputSyncTxRateReq": cienaCesSyncPTPInputSyncTxRateReq,
       "cienaCesSyncPTPInputDelayReqTxRate": cienaCesSyncPTPInputDelayReqTxRate,
       "cienaCesSyncPTPOutputConfig": cienaCesSyncPTPOutputConfig,
       "cienaCesSyncPTPOutputMaxSlaveSessions": cienaCesSyncPTPOutputMaxSlaveSessions,
       "cienaCesSyncPTPOutputTimestampMode": cienaCesSyncPTPOutputTimestampMode,
       "cienaCesSyncGPSConfig": cienaCesSyncGPSConfig,
       "cienaCesSyncGPSOutputConfig": cienaCesSyncGPSOutputConfig,
       "cienaCesSyncGPSOutput1ppsPulseWidth": cienaCesSyncGPSOutput1ppsPulseWidth,
       "cienaCesSyncHoldoverInterval": cienaCesSyncHoldoverInterval,
       "cienaCesSyncModuleSlotClockStatus": cienaCesSyncModuleSlotClockStatus,
       "cienaCesTimeSyncMIBNotificationPrefix": cienaCesTimeSyncMIBNotificationPrefix,
       "cienaCesTimeSyncMIBNotifications": cienaCesTimeSyncMIBNotifications,
       "cienaCesSyncInputPUStateChangeNotification": cienaCesSyncInputPUStateChangeNotification,
       "cienaCesSyncInputProtectionGroupStateChangeNotification": cienaCesSyncInputProtectionGroupStateChangeNotification,
       "cienaCesSyncModuleSlotClockStateChangeNotification": cienaCesSyncModuleSlotClockStateChangeNotification}
)
