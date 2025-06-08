# SNMP MIB module (MEF-SOAM-FM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mef_15007/MEF-SOAM-FM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:56 2025
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

(EntityAdminState,
 EntityOperState) = mibBuilder.importSymbols(
    "ENTITY-STATE-TC-MIB",
    "EntityAdminState",
    "EntityOperState")

(Dot1agCfmInterfaceStatus,
 Dot1agCfmMDLevel,
 Dot1agCfmMepDefects,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmPortStatus,
 dot1agCfmMaIndex,
 dot1agCfmMaNetEntry,
 dot1agCfmMdIndex,
 dot1agCfmMepActive,
 dot1agCfmMepDbRMepState,
 dot1agCfmMepDefects,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmInterfaceStatus",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepDefects",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmPortStatus",
    "dot1agCfmMaIndex",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMdIndex",
    "dot1agCfmMepActive",
    "dot1agCfmMepDbRMepState",
    "dot1agCfmMepDefects",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(ieee8021CfmConfigErrorListErrorType,
 ieee8021CfmMaCompEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-V2-MIB",
    "ieee8021CfmConfigErrorListErrorType",
    "ieee8021CfmMaCompEntry")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(MefSoamTcConnectivityStatusType,
 MefSoamTcDataPatternType,
 MefSoamTcIntervalTypeAisLck,
 MefSoamTcMegIdType,
 MefSoamTcOperationTimeType,
 MefSoamTcTestPatternType) = mibBuilder.importSymbols(
    "MEF-SOAM-TC-MIB",
    "MefSoamTcConnectivityStatusType",
    "MefSoamTcDataPatternType",
    "MefSoamTcIntervalTypeAisLck",
    "MefSoamTcMegIdType",
    "MefSoamTcOperationTimeType",
    "MefSoamTcTestPatternType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

mefSoamFmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2)
)
if mibBuilder.loadTexts:
    mefSoamFmMib.setRevisions(
        ("2010-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MefSoamFmNotifications_ObjectIdentity = ObjectIdentity
mefSoamFmNotifications = _MefSoamFmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0)
)
_MefSoamFmMibObjects_ObjectIdentity = ObjectIdentity
mefSoamFmMibObjects = _MefSoamFmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1)
)
_MefSoamNet_ObjectIdentity = ObjectIdentity
mefSoamNet = _MefSoamNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1)
)
_MefSoamNetCfgTable_Object = MibTable
mefSoamNetCfgTable = _MefSoamNetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamNetCfgTable.setStatus("current")
_MefSoamNetCfgEntry_Object = MibTableRow
mefSoamNetCfgEntry = _MefSoamNetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamNetCfgEntry.setStatus("current")
_MefSoamNetCfgY1731Compliant_Type = TruthValue
_MefSoamNetCfgY1731Compliant_Object = MibTableColumn
mefSoamNetCfgY1731Compliant = _MefSoamNetCfgY1731Compliant_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1, 1, 1, 1),
    _MefSoamNetCfgY1731Compliant_Type()
)
mefSoamNetCfgY1731Compliant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamNetCfgY1731Compliant.setStatus("current")


class _MefSoamNetCfgMegIdFormat_Type(MefSoamTcMegIdType):
    """Custom type mefSoamNetCfgMegIdFormat based on MefSoamTcMegIdType"""
    defaultValue = 2


_MefSoamNetCfgMegIdFormat_Type.__name__ = "MefSoamTcMegIdType"
_MefSoamNetCfgMegIdFormat_Object = MibTableColumn
mefSoamNetCfgMegIdFormat = _MefSoamNetCfgMegIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1, 1, 1, 2),
    _MefSoamNetCfgMegIdFormat_Type()
)
mefSoamNetCfgMegIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamNetCfgMegIdFormat.setStatus("current")
_MefSoamNetCfgMegLevel_Type = Dot1agCfmMDLevel
_MefSoamNetCfgMegLevel_Object = MibTableColumn
mefSoamNetCfgMegLevel = _MefSoamNetCfgMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 1, 1, 1, 3),
    _MefSoamNetCfgMegLevel_Type()
)
mefSoamNetCfgMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamNetCfgMegLevel.setStatus("current")
_MefSoamMeg_ObjectIdentity = ObjectIdentity
mefSoamMeg = _MefSoamMeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2)
)
_MefSoamMegCfgTable_Object = MibTable
mefSoamMegCfgTable = _MefSoamMegCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamMegCfgTable.setStatus("current")
_MefSoamMegCfgEntry_Object = MibTableRow
mefSoamMegCfgEntry = _MefSoamMegCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamMegCfgEntry.setStatus("current")


class _MefSoamMegCfgConnectivityStatusInterval_Type(Unsigned32):
    """Custom type mefSoamMegCfgConnectivityStatusInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2100000),
    )


_MefSoamMegCfgConnectivityStatusInterval_Type.__name__ = "Unsigned32"
_MefSoamMegCfgConnectivityStatusInterval_Object = MibTableColumn
mefSoamMegCfgConnectivityStatusInterval = _MefSoamMegCfgConnectivityStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1, 1, 1),
    _MefSoamMegCfgConnectivityStatusInterval_Type()
)
mefSoamMegCfgConnectivityStatusInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamMegCfgConnectivityStatusInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamMegCfgConnectivityStatusInterval.setUnits("ms")


class _MefSoamMegCfgPeerMepInfoAgingTime_Type(Unsigned32):
    """Custom type mefSoamMegCfgPeerMepInfoAgingTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_MefSoamMegCfgPeerMepInfoAgingTime_Type.__name__ = "Unsigned32"
_MefSoamMegCfgPeerMepInfoAgingTime_Object = MibTableColumn
mefSoamMegCfgPeerMepInfoAgingTime = _MefSoamMegCfgPeerMepInfoAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1, 1, 2),
    _MefSoamMegCfgPeerMepInfoAgingTime_Type()
)
mefSoamMegCfgPeerMepInfoAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamMegCfgPeerMepInfoAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamMegCfgPeerMepInfoAgingTime.setUnits("seconds")


class _MefSoamMegCfgPortStatusTlvIncluded_Type(TruthValue):
    """Custom type mefSoamMegCfgPortStatusTlvIncluded based on TruthValue"""
    defaultValue = 1


_MefSoamMegCfgPortStatusTlvIncluded_Type.__name__ = "TruthValue"
_MefSoamMegCfgPortStatusTlvIncluded_Object = MibTableColumn
mefSoamMegCfgPortStatusTlvIncluded = _MefSoamMegCfgPortStatusTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1, 1, 3),
    _MefSoamMegCfgPortStatusTlvIncluded_Type()
)
mefSoamMegCfgPortStatusTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamMegCfgPortStatusTlvIncluded.setStatus("current")


class _MefSoamMegCfgInterfaceStatusTlvIncluded_Type(TruthValue):
    """Custom type mefSoamMegCfgInterfaceStatusTlvIncluded based on TruthValue"""
    defaultValue = 1


_MefSoamMegCfgInterfaceStatusTlvIncluded_Type.__name__ = "TruthValue"
_MefSoamMegCfgInterfaceStatusTlvIncluded_Object = MibTableColumn
mefSoamMegCfgInterfaceStatusTlvIncluded = _MefSoamMegCfgInterfaceStatusTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 2, 1, 1, 4),
    _MefSoamMegCfgInterfaceStatusTlvIncluded_Type()
)
mefSoamMegCfgInterfaceStatusTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamMegCfgInterfaceStatusTlvIncluded.setStatus("current")
_MefSoamMep_ObjectIdentity = ObjectIdentity
mefSoamMep = _MefSoamMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3)
)
_MefSoamMepStatusTable_Object = MibTable
mefSoamMepStatusTable = _MefSoamMepStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mefSoamMepStatusTable.setStatus("current")
_MefSoamMepStatusEntry_Object = MibTableRow
mefSoamMepStatusEntry = _MefSoamMepStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamMepStatusEntry.setStatus("current")
_MefSoamMepStatusOperationalState_Type = EntityOperState
_MefSoamMepStatusOperationalState_Object = MibTableColumn
mefSoamMepStatusOperationalState = _MefSoamMepStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 1),
    _MefSoamMepStatusOperationalState_Type()
)
mefSoamMepStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusOperationalState.setStatus("current")
_MefSoamMepStatusConnectivityStatus_Type = MefSoamTcConnectivityStatusType
_MefSoamMepStatusConnectivityStatus_Object = MibTableColumn
mefSoamMepStatusConnectivityStatus = _MefSoamMepStatusConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 2),
    _MefSoamMepStatusConnectivityStatus_Type()
)
mefSoamMepStatusConnectivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusConnectivityStatus.setStatus("current")


class _MefSoamMepStatusSentPortStatus_Type(Dot1agCfmPortStatus):
    """Custom type mefSoamMepStatusSentPortStatus based on Dot1agCfmPortStatus"""
    defaultValue = 0


_MefSoamMepStatusSentPortStatus_Type.__name__ = "Dot1agCfmPortStatus"
_MefSoamMepStatusSentPortStatus_Object = MibTableColumn
mefSoamMepStatusSentPortStatus = _MefSoamMepStatusSentPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 3),
    _MefSoamMepStatusSentPortStatus_Type()
)
mefSoamMepStatusSentPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusSentPortStatus.setStatus("current")


class _MefSoamMepStatusSentInterfaceStatus_Type(Dot1agCfmInterfaceStatus):
    """Custom type mefSoamMepStatusSentInterfaceStatus based on Dot1agCfmInterfaceStatus"""
    defaultValue = 0


_MefSoamMepStatusSentInterfaceStatus_Type.__name__ = "Dot1agCfmInterfaceStatus"
_MefSoamMepStatusSentInterfaceStatus_Object = MibTableColumn
mefSoamMepStatusSentInterfaceStatus = _MefSoamMepStatusSentInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 4),
    _MefSoamMepStatusSentInterfaceStatus_Type()
)
mefSoamMepStatusSentInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusSentInterfaceStatus.setStatus("current")


class _MefSoamMepStatusLastDefectSentStatus_Type(Dot1agCfmMepDefects):
    """Custom type mefSoamMepStatusLastDefectSentStatus based on Dot1agCfmMepDefects"""
    defaultBinValue = "0"


_MefSoamMepStatusLastDefectSentStatus_Type.__name__ = "Dot1agCfmMepDefects"
_MefSoamMepStatusLastDefectSentStatus_Object = MibTableColumn
mefSoamMepStatusLastDefectSentStatus = _MefSoamMepStatusLastDefectSentStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 5),
    _MefSoamMepStatusLastDefectSentStatus_Type()
)
mefSoamMepStatusLastDefectSentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusLastDefectSentStatus.setStatus("current")


class _MefSoamMepStatusRdiTransmitStatus_Type(TruthValue):
    """Custom type mefSoamMepStatusRdiTransmitStatus based on TruthValue"""
    defaultValue = 1


_MefSoamMepStatusRdiTransmitStatus_Type.__name__ = "TruthValue"
_MefSoamMepStatusRdiTransmitStatus_Object = MibTableColumn
mefSoamMepStatusRdiTransmitStatus = _MefSoamMepStatusRdiTransmitStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 1, 1, 6),
    _MefSoamMepStatusRdiTransmitStatus_Type()
)
mefSoamMepStatusRdiTransmitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepStatusRdiTransmitStatus.setStatus("current")
_MefSoamMepFmStatsTable_Object = MibTable
mefSoamMepFmStatsTable = _MefSoamMepFmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefSoamMepFmStatsTable.setStatus("current")
_MefSoamMepFmStatsEntry_Object = MibTableRow
mefSoamMepFmStatsEntry = _MefSoamMepFmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamMepFmStatsEntry.setStatus("current")
_MefSoamMepFmStatsInOamFramesDiscarded_Type = Counter32
_MefSoamMepFmStatsInOamFramesDiscarded_Object = MibTableColumn
mefSoamMepFmStatsInOamFramesDiscarded = _MefSoamMepFmStatsInOamFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 2, 1, 1),
    _MefSoamMepFmStatsInOamFramesDiscarded_Type()
)
mefSoamMepFmStatsInOamFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepFmStatsInOamFramesDiscarded.setStatus("current")
_MefSoamMepFmStatsInCcmTotal_Type = Counter32
_MefSoamMepFmStatsInCcmTotal_Object = MibTableColumn
mefSoamMepFmStatsInCcmTotal = _MefSoamMepFmStatsInCcmTotal_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 3, 2, 1, 2),
    _MefSoamMepFmStatsInCcmTotal_Type()
)
mefSoamMepFmStatsInCcmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamMepFmStatsInCcmTotal.setStatus("current")
_MefSoamCc_ObjectIdentity = ObjectIdentity
mefSoamCc = _MefSoamCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 4)
)
_MefSoamCcCfgTable_Object = MibTable
mefSoamCcCfgTable = _MefSoamCcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mefSoamCcCfgTable.setStatus("current")
_MefSoamCcCfgEntry_Object = MibTableRow
mefSoamCcCfgEntry = _MefSoamCcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamCcCfgEntry.setStatus("current")


class _MefSoamCcCfgDropEligible_Type(TruthValue):
    """Custom type mefSoamCcCfgDropEligible based on TruthValue"""
    defaultValue = 2


_MefSoamCcCfgDropEligible_Type.__name__ = "TruthValue"
_MefSoamCcCfgDropEligible_Object = MibTableColumn
mefSoamCcCfgDropEligible = _MefSoamCcCfgDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 4, 1, 1, 1),
    _MefSoamCcCfgDropEligible_Type()
)
mefSoamCcCfgDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamCcCfgDropEligible.setStatus("current")
_MefSoamAis_ObjectIdentity = ObjectIdentity
mefSoamAis = _MefSoamAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5)
)
_MefSoamAisCfgTable_Object = MibTable
mefSoamAisCfgTable = _MefSoamAisCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mefSoamAisCfgTable.setStatus("current")
_MefSoamAisCfgEntry_Object = MibTableRow
mefSoamAisCfgEntry = _MefSoamAisCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamAisCfgEntry.setStatus("current")


class _MefSoamAisCfgEnabled_Type(TruthValue):
    """Custom type mefSoamAisCfgEnabled based on TruthValue"""
    defaultValue = 2


_MefSoamAisCfgEnabled_Type.__name__ = "TruthValue"
_MefSoamAisCfgEnabled_Object = MibTableColumn
mefSoamAisCfgEnabled = _MefSoamAisCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1, 1),
    _MefSoamAisCfgEnabled_Type()
)
mefSoamAisCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamAisCfgEnabled.setStatus("current")


class _MefSoamAisCfgInterval_Type(MefSoamTcIntervalTypeAisLck):
    """Custom type mefSoamAisCfgInterval based on MefSoamTcIntervalTypeAisLck"""
    defaultValue = 1


_MefSoamAisCfgInterval_Type.__name__ = "MefSoamTcIntervalTypeAisLck"
_MefSoamAisCfgInterval_Object = MibTableColumn
mefSoamAisCfgInterval = _MefSoamAisCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1, 2),
    _MefSoamAisCfgInterval_Type()
)
mefSoamAisCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamAisCfgInterval.setStatus("current")
_MefSoamAisCfgPriority_Type = IEEE8021PriorityValue
_MefSoamAisCfgPriority_Object = MibTableColumn
mefSoamAisCfgPriority = _MefSoamAisCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1, 3),
    _MefSoamAisCfgPriority_Type()
)
mefSoamAisCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamAisCfgPriority.setStatus("current")


class _MefSoamAisCfgMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type mefSoamAisCfgMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_MefSoamAisCfgMdLevel_Type.__name__ = "Dot1agCfmMDLevel"
_MefSoamAisCfgMdLevel_Object = MibTableColumn
mefSoamAisCfgMdLevel = _MefSoamAisCfgMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1, 4),
    _MefSoamAisCfgMdLevel_Type()
)
mefSoamAisCfgMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamAisCfgMdLevel.setStatus("current")


class _MefSoamAisCfgDropEligible_Type(TruthValue):
    """Custom type mefSoamAisCfgDropEligible based on TruthValue"""
    defaultValue = 2


_MefSoamAisCfgDropEligible_Type.__name__ = "TruthValue"
_MefSoamAisCfgDropEligible_Object = MibTableColumn
mefSoamAisCfgDropEligible = _MefSoamAisCfgDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 1, 1, 5),
    _MefSoamAisCfgDropEligible_Type()
)
mefSoamAisCfgDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamAisCfgDropEligible.setStatus("current")
_MefSoamAisStatsTable_Object = MibTable
mefSoamAisStatsTable = _MefSoamAisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mefSoamAisStatsTable.setStatus("current")
_MefSoamAisStatsEntry_Object = MibTableRow
mefSoamAisStatsEntry = _MefSoamAisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamAisStatsEntry.setStatus("current")
_MefSoamAisStatsOutStatus_Type = TruthValue
_MefSoamAisStatsOutStatus_Object = MibTableColumn
mefSoamAisStatsOutStatus = _MefSoamAisStatsOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1, 1),
    _MefSoamAisStatsOutStatus_Type()
)
mefSoamAisStatsOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamAisStatsOutStatus.setStatus("current")
_MefSoamAisStatsOutCounter_Type = Counter32
_MefSoamAisStatsOutCounter_Object = MibTableColumn
mefSoamAisStatsOutCounter = _MefSoamAisStatsOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1, 2),
    _MefSoamAisStatsOutCounter_Type()
)
mefSoamAisStatsOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamAisStatsOutCounter.setStatus("current")
_MefSoamAisStatsInStatus_Type = TruthValue
_MefSoamAisStatsInStatus_Object = MibTableColumn
mefSoamAisStatsInStatus = _MefSoamAisStatsInStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1, 3),
    _MefSoamAisStatsInStatus_Type()
)
mefSoamAisStatsInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamAisStatsInStatus.setStatus("current")
_MefSoamAisStatsInCounter_Type = Counter32
_MefSoamAisStatsInCounter_Object = MibTableColumn
mefSoamAisStatsInCounter = _MefSoamAisStatsInCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1, 4),
    _MefSoamAisStatsInCounter_Type()
)
mefSoamAisStatsInCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamAisStatsInCounter.setStatus("current")
_MefSoamAisStatsInMacAddr_Type = MacAddress
_MefSoamAisStatsInMacAddr_Object = MibTableColumn
mefSoamAisStatsInMacAddr = _MefSoamAisStatsInMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 5, 2, 1, 5),
    _MefSoamAisStatsInMacAddr_Type()
)
mefSoamAisStatsInMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamAisStatsInMacAddr.setStatus("current")
_MefSoamLb_ObjectIdentity = ObjectIdentity
mefSoamLb = _MefSoamLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6)
)
_MefSoamLbCfgTable_Object = MibTable
mefSoamLbCfgTable = _MefSoamLbCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mefSoamLbCfgTable.setStatus("current")
_MefSoamLbCfgEntry_Object = MibTableRow
mefSoamLbCfgEntry = _MefSoamLbCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamLbCfgEntry.setStatus("current")


class _MefSoamLbCfgMulticastEnabled_Type(TruthValue):
    """Custom type mefSoamLbCfgMulticastEnabled based on TruthValue"""
    defaultValue = 2


_MefSoamLbCfgMulticastEnabled_Type.__name__ = "TruthValue"
_MefSoamLbCfgMulticastEnabled_Object = MibTableColumn
mefSoamLbCfgMulticastEnabled = _MefSoamLbCfgMulticastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 1),
    _MefSoamLbCfgMulticastEnabled_Type()
)
mefSoamLbCfgMulticastEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgMulticastEnabled.setStatus("current")


class _MefSoamLbCfgInterval_Type(Unsigned32):
    """Custom type mefSoamLbCfgInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_MefSoamLbCfgInterval_Type.__name__ = "Unsigned32"
_MefSoamLbCfgInterval_Object = MibTableColumn
mefSoamLbCfgInterval = _MefSoamLbCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 2),
    _MefSoamLbCfgInterval_Type()
)
mefSoamLbCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLbCfgInterval.setUnits("ms")


class _MefSoamLbCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamLbCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_MefSoamLbCfgFrameSize_Type.__name__ = "Unsigned32"
_MefSoamLbCfgFrameSize_Object = MibTableColumn
mefSoamLbCfgFrameSize = _MefSoamLbCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 3),
    _MefSoamLbCfgFrameSize_Type()
)
mefSoamLbCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLbCfgFrameSize.setUnits("bytes")


class _MefSoamLbCfgDataPattern_Type(MefSoamTcDataPatternType):
    """Custom type mefSoamLbCfgDataPattern based on MefSoamTcDataPatternType"""
    defaultValue = 1


_MefSoamLbCfgDataPattern_Type.__name__ = "MefSoamTcDataPatternType"
_MefSoamLbCfgDataPattern_Object = MibTableColumn
mefSoamLbCfgDataPattern = _MefSoamLbCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 4),
    _MefSoamLbCfgDataPattern_Type()
)
mefSoamLbCfgDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgDataPattern.setStatus("current")


class _MefSoamLbCfgTestTlvIncluded_Type(TruthValue):
    """Custom type mefSoamLbCfgTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_MefSoamLbCfgTestTlvIncluded_Type.__name__ = "TruthValue"
_MefSoamLbCfgTestTlvIncluded_Object = MibTableColumn
mefSoamLbCfgTestTlvIncluded = _MefSoamLbCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 5),
    _MefSoamLbCfgTestTlvIncluded_Type()
)
mefSoamLbCfgTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgTestTlvIncluded.setStatus("current")


class _MefSoamLbCfgTestTlvPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamLbCfgTestTlvPattern based on MefSoamTcTestPatternType"""
    defaultValue = 1


_MefSoamLbCfgTestTlvPattern_Type.__name__ = "MefSoamTcTestPatternType"
_MefSoamLbCfgTestTlvPattern_Object = MibTableColumn
mefSoamLbCfgTestTlvPattern = _MefSoamLbCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 6),
    _MefSoamLbCfgTestTlvPattern_Type()
)
mefSoamLbCfgTestTlvPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgTestTlvPattern.setStatus("current")


class _MefSoamLbCfgTimeout_Type(Unsigned32):
    """Custom type mefSoamLbCfgTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MefSoamLbCfgTimeout_Type.__name__ = "Unsigned32"
_MefSoamLbCfgTimeout_Object = MibTableColumn
mefSoamLbCfgTimeout = _MefSoamLbCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 1, 1, 7),
    _MefSoamLbCfgTimeout_Type()
)
mefSoamLbCfgTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLbCfgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLbCfgTimeout.setUnits("ms")
_MefSoamLbStatsTable_Object = MibTable
mefSoamLbStatsTable = _MefSoamLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mefSoamLbStatsTable.setStatus("current")
_MefSoamLbStatsEntry_Object = MibTableRow
mefSoamLbStatsEntry = _MefSoamLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamLbStatsEntry.setStatus("current")
_MefSoamLbStatsNumLbrInCrcErrors_Type = Counter32
_MefSoamLbStatsNumLbrInCrcErrors_Object = MibTableColumn
mefSoamLbStatsNumLbrInCrcErrors = _MefSoamLbStatsNumLbrInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 2, 1, 1),
    _MefSoamLbStatsNumLbrInCrcErrors_Type()
)
mefSoamLbStatsNumLbrInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLbStatsNumLbrInCrcErrors.setStatus("current")
_MefSoamLbrMulticastTable_Object = MibTable
mefSoamLbrMulticastTable = _MefSoamLbrMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    mefSoamLbrMulticastTable.setStatus("current")
_MefSoamLbrMulticastEntry_Object = MibTableRow
mefSoamLbrMulticastEntry = _MefSoamLbrMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 3, 1)
)
mefSoamLbrMulticastEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-FM-MIB", "mefSoamLbrMulticastTransId"),
    (0, "MEF-SOAM-FM-MIB", "mefSoamLbrMulticastReceiveOrder"),
)
if mibBuilder.loadTexts:
    mefSoamLbrMulticastEntry.setStatus("current")


class _MefSoamLbrMulticastTransId_Type(Unsigned32):
    """Custom type mefSoamLbrMulticastTransId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MefSoamLbrMulticastTransId_Type.__name__ = "Unsigned32"
_MefSoamLbrMulticastTransId_Object = MibTableColumn
mefSoamLbrMulticastTransId = _MefSoamLbrMulticastTransId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 3, 1, 1),
    _MefSoamLbrMulticastTransId_Type()
)
mefSoamLbrMulticastTransId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLbrMulticastTransId.setStatus("current")


class _MefSoamLbrMulticastReceiveOrder_Type(Unsigned32):
    """Custom type mefSoamLbrMulticastReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MefSoamLbrMulticastReceiveOrder_Type.__name__ = "Unsigned32"
_MefSoamLbrMulticastReceiveOrder_Object = MibTableColumn
mefSoamLbrMulticastReceiveOrder = _MefSoamLbrMulticastReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 3, 1, 2),
    _MefSoamLbrMulticastReceiveOrder_Type()
)
mefSoamLbrMulticastReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLbrMulticastReceiveOrder.setStatus("current")
_MefSoamLbrMulticastReplyMac_Type = MacAddress
_MefSoamLbrMulticastReplyMac_Object = MibTableColumn
mefSoamLbrMulticastReplyMac = _MefSoamLbrMulticastReplyMac_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 6, 3, 1, 3),
    _MefSoamLbrMulticastReplyMac_Type()
)
mefSoamLbrMulticastReplyMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLbrMulticastReplyMac.setStatus("current")
_MefSoamLt_ObjectIdentity = ObjectIdentity
mefSoamLt = _MefSoamLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7)
)
_MefSoamLtStatsTable_Object = MibTable
mefSoamLtStatsTable = _MefSoamLtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mefSoamLtStatsTable.setStatus("current")
_MefSoamLtStatsEntry_Object = MibTableRow
mefSoamLtStatsEntry = _MefSoamLtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamLtStatsEntry.setStatus("current")
_MefSoamLtLtmTransmitted_Type = Counter32
_MefSoamLtLtmTransmitted_Object = MibTableColumn
mefSoamLtLtmTransmitted = _MefSoamLtLtmTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1, 1, 1),
    _MefSoamLtLtmTransmitted_Type()
)
mefSoamLtLtmTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLtLtmTransmitted.setStatus("current")
_MefSoamLtLtrReceived_Type = Counter32
_MefSoamLtLtrReceived_Object = MibTableColumn
mefSoamLtLtrReceived = _MefSoamLtLtrReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1, 1, 2),
    _MefSoamLtLtrReceived_Type()
)
mefSoamLtLtrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLtLtrReceived.setStatus("current")
_MefSoamLtLtmReceived_Type = Counter32
_MefSoamLtLtmReceived_Object = MibTableColumn
mefSoamLtLtmReceived = _MefSoamLtLtmReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1, 1, 3),
    _MefSoamLtLtmReceived_Type()
)
mefSoamLtLtmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLtLtmReceived.setStatus("current")
_MefSoamLtLtrTransmitted_Type = Counter32
_MefSoamLtLtrTransmitted_Object = MibTableColumn
mefSoamLtLtrTransmitted = _MefSoamLtLtrTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 7, 1, 1, 4),
    _MefSoamLtLtrTransmitted_Type()
)
mefSoamLtLtrTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLtLtrTransmitted.setStatus("current")
_MefSoamLck_ObjectIdentity = ObjectIdentity
mefSoamLck = _MefSoamLck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8)
)
_MefSoamLckCfgTable_Object = MibTable
mefSoamLckCfgTable = _MefSoamLckCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mefSoamLckCfgTable.setStatus("current")
_MefSoamLckCfgEntry_Object = MibTableRow
mefSoamLckCfgEntry = _MefSoamLckCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamLckCfgEntry.setStatus("current")


class _MefSoamLckCfgAdminState_Type(EntityAdminState):
    """Custom type mefSoamLckCfgAdminState based on EntityAdminState"""
    defaultValue = 4


_MefSoamLckCfgAdminState_Type.__name__ = "EntityAdminState"
_MefSoamLckCfgAdminState_Object = MibTableColumn
mefSoamLckCfgAdminState = _MefSoamLckCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1, 1, 1),
    _MefSoamLckCfgAdminState_Type()
)
mefSoamLckCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLckCfgAdminState.setStatus("current")


class _MefSoamLckCfgInterval_Type(MefSoamTcIntervalTypeAisLck):
    """Custom type mefSoamLckCfgInterval based on MefSoamTcIntervalTypeAisLck"""
    defaultValue = 1


_MefSoamLckCfgInterval_Type.__name__ = "MefSoamTcIntervalTypeAisLck"
_MefSoamLckCfgInterval_Object = MibTableColumn
mefSoamLckCfgInterval = _MefSoamLckCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1, 1, 2),
    _MefSoamLckCfgInterval_Type()
)
mefSoamLckCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLckCfgInterval.setStatus("current")
_MefSoamLckCfgPriority_Type = IEEE8021PriorityValue
_MefSoamLckCfgPriority_Object = MibTableColumn
mefSoamLckCfgPriority = _MefSoamLckCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1, 1, 3),
    _MefSoamLckCfgPriority_Type()
)
mefSoamLckCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLckCfgPriority.setStatus("current")


class _MefSoamLckCfgMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type mefSoamLckCfgMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_MefSoamLckCfgMdLevel_Type.__name__ = "Dot1agCfmMDLevel"
_MefSoamLckCfgMdLevel_Object = MibTableColumn
mefSoamLckCfgMdLevel = _MefSoamLckCfgMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 1, 1, 4),
    _MefSoamLckCfgMdLevel_Type()
)
mefSoamLckCfgMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLckCfgMdLevel.setStatus("current")
_MefSoamLckStatsTable_Object = MibTable
mefSoamLckStatsTable = _MefSoamLckStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    mefSoamLckStatsTable.setStatus("current")
_MefSoamLckStatsEntry_Object = MibTableRow
mefSoamLckStatsEntry = _MefSoamLckStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamLckStatsEntry.setStatus("current")
_MefSoamLckStatsInStatus_Type = TruthValue
_MefSoamLckStatsInStatus_Object = MibTableColumn
mefSoamLckStatsInStatus = _MefSoamLckStatsInStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2, 1, 1),
    _MefSoamLckStatsInStatus_Type()
)
mefSoamLckStatsInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLckStatsInStatus.setStatus("current")
_MefSoamLckStatsInCounter_Type = Counter32
_MefSoamLckStatsInCounter_Object = MibTableColumn
mefSoamLckStatsInCounter = _MefSoamLckStatsInCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2, 1, 2),
    _MefSoamLckStatsInCounter_Type()
)
mefSoamLckStatsInCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLckStatsInCounter.setStatus("current")
_MefSoamLckStatsOutStatus_Type = TruthValue
_MefSoamLckStatsOutStatus_Object = MibTableColumn
mefSoamLckStatsOutStatus = _MefSoamLckStatsOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2, 1, 3),
    _MefSoamLckStatsOutStatus_Type()
)
mefSoamLckStatsOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLckStatsOutStatus.setStatus("current")
_MefSoamLckStatsOutCounter_Type = Counter32
_MefSoamLckStatsOutCounter_Object = MibTableColumn
mefSoamLckStatsOutCounter = _MefSoamLckStatsOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 8, 2, 1, 4),
    _MefSoamLckStatsOutCounter_Type()
)
mefSoamLckStatsOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLckStatsOutCounter.setStatus("current")
_MefSoamTest_ObjectIdentity = ObjectIdentity
mefSoamTest = _MefSoamTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9)
)
_MefSoamTestCfgTable_Object = MibTable
mefSoamTestCfgTable = _MefSoamTestCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    mefSoamTestCfgTable.setStatus("current")
_MefSoamTestCfgEntry_Object = MibTableRow
mefSoamTestCfgEntry = _MefSoamTestCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamTestCfgEntry.setStatus("current")


class _MefSoamTestCfgOutEnabled_Type(TruthValue):
    """Custom type mefSoamTestCfgOutEnabled based on TruthValue"""
    defaultValue = 2


_MefSoamTestCfgOutEnabled_Type.__name__ = "TruthValue"
_MefSoamTestCfgOutEnabled_Object = MibTableColumn
mefSoamTestCfgOutEnabled = _MefSoamTestCfgOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 1),
    _MefSoamTestCfgOutEnabled_Type()
)
mefSoamTestCfgOutEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgOutEnabled.setStatus("current")


class _MefSoamTestCfgInEnabled_Type(TruthValue):
    """Custom type mefSoamTestCfgInEnabled based on TruthValue"""
    defaultValue = 2


_MefSoamTestCfgInEnabled_Type.__name__ = "TruthValue"
_MefSoamTestCfgInEnabled_Object = MibTableColumn
mefSoamTestCfgInEnabled = _MefSoamTestCfgInEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 2),
    _MefSoamTestCfgInEnabled_Type()
)
mefSoamTestCfgInEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgInEnabled.setStatus("current")


class _MefSoamTestCfgInService_Type(TruthValue):
    """Custom type mefSoamTestCfgInService based on TruthValue"""
    defaultValue = 1


_MefSoamTestCfgInService_Type.__name__ = "TruthValue"
_MefSoamTestCfgInService_Object = MibTableColumn
mefSoamTestCfgInService = _MefSoamTestCfgInService_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 3),
    _MefSoamTestCfgInService_Type()
)
mefSoamTestCfgInService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgInService.setStatus("current")
_MefSoamTestCfgDestMacAddress_Type = MacAddress
_MefSoamTestCfgDestMacAddress_Object = MibTableColumn
mefSoamTestCfgDestMacAddress = _MefSoamTestCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 4),
    _MefSoamTestCfgDestMacAddress_Type()
)
mefSoamTestCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgDestMacAddress.setStatus("current")


class _MefSoamTestCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type mefSoamTestCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_MefSoamTestCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_MefSoamTestCfgDestMepId_Object = MibTableColumn
mefSoamTestCfgDestMepId = _MefSoamTestCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 5),
    _MefSoamTestCfgDestMepId_Type()
)
mefSoamTestCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgDestMepId.setStatus("current")


class _MefSoamTestCfgDestIsMepId_Type(TruthValue):
    """Custom type mefSoamTestCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_MefSoamTestCfgDestIsMepId_Type.__name__ = "TruthValue"
_MefSoamTestCfgDestIsMepId_Object = MibTableColumn
mefSoamTestCfgDestIsMepId = _MefSoamTestCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 6),
    _MefSoamTestCfgDestIsMepId_Type()
)
mefSoamTestCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgDestIsMepId.setStatus("current")


class _MefSoamTestCfgInterval_Type(Unsigned32):
    """Custom type mefSoamTestCfgInterval based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_MefSoamTestCfgInterval_Type.__name__ = "Unsigned32"
_MefSoamTestCfgInterval_Object = MibTableColumn
mefSoamTestCfgInterval = _MefSoamTestCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 7),
    _MefSoamTestCfgInterval_Type()
)
mefSoamTestCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamTestCfgInterval.setUnits("microseconds")


class _MefSoamTestCfgPriority_Type(IEEE8021PriorityValue):
    """Custom type mefSoamTestCfgPriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_MefSoamTestCfgPriority_Type.__name__ = "IEEE8021PriorityValue"
_MefSoamTestCfgPriority_Object = MibTableColumn
mefSoamTestCfgPriority = _MefSoamTestCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 8),
    _MefSoamTestCfgPriority_Type()
)
mefSoamTestCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgPriority.setStatus("current")


class _MefSoamTestCfgDropEligible_Type(TruthValue):
    """Custom type mefSoamTestCfgDropEligible based on TruthValue"""
    defaultValue = 2


_MefSoamTestCfgDropEligible_Type.__name__ = "TruthValue"
_MefSoamTestCfgDropEligible_Object = MibTableColumn
mefSoamTestCfgDropEligible = _MefSoamTestCfgDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 9),
    _MefSoamTestCfgDropEligible_Type()
)
mefSoamTestCfgDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgDropEligible.setStatus("current")


class _MefSoamTestCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamTestCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_MefSoamTestCfgFrameSize_Type.__name__ = "Unsigned32"
_MefSoamTestCfgFrameSize_Object = MibTableColumn
mefSoamTestCfgFrameSize = _MefSoamTestCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 10),
    _MefSoamTestCfgFrameSize_Type()
)
mefSoamTestCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamTestCfgFrameSize.setUnits("bytes")


class _MefSoamTestCfgPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamTestCfgPattern based on MefSoamTcTestPatternType"""
    defaultValue = 1


_MefSoamTestCfgPattern_Type.__name__ = "MefSoamTcTestPatternType"
_MefSoamTestCfgPattern_Object = MibTableColumn
mefSoamTestCfgPattern = _MefSoamTestCfgPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 11),
    _MefSoamTestCfgPattern_Type()
)
mefSoamTestCfgPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgPattern.setStatus("current")


class _MefSoamTestCfgStartTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamTestCfgStartTimeType based on MefSoamTcOperationTimeType"""
    defaultValue = 1


_MefSoamTestCfgStartTimeType_Type.__name__ = "MefSoamTcOperationTimeType"
_MefSoamTestCfgStartTimeType_Object = MibTableColumn
mefSoamTestCfgStartTimeType = _MefSoamTestCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 12),
    _MefSoamTestCfgStartTimeType_Type()
)
mefSoamTestCfgStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgStartTimeType.setStatus("current")


class _MefSoamTestCfgScheduledStartDateAndTime_Type(DateAndTime):
    """Custom type mefSoamTestCfgScheduledStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamTestCfgScheduledStartDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamTestCfgScheduledStartDateAndTime_Object = MibTableColumn
mefSoamTestCfgScheduledStartDateAndTime = _MefSoamTestCfgScheduledStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 13),
    _MefSoamTestCfgScheduledStartDateAndTime_Type()
)
mefSoamTestCfgScheduledStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgScheduledStartDateAndTime.setStatus("current")


class _MefSoamTestCfgScheduledStopDateAndTime_Type(DateAndTime):
    """Custom type mefSoamTestCfgScheduledStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamTestCfgScheduledStopDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamTestCfgScheduledStopDateAndTime_Object = MibTableColumn
mefSoamTestCfgScheduledStopDateAndTime = _MefSoamTestCfgScheduledStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 14),
    _MefSoamTestCfgScheduledStopDateAndTime_Type()
)
mefSoamTestCfgScheduledStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgScheduledStopDateAndTime.setStatus("current")


class _MefSoamTestCfgRelativeStartTime_Type(TimeInterval):
    """Custom type mefSoamTestCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_MefSoamTestCfgRelativeStartTime_Type.__name__ = "TimeInterval"
_MefSoamTestCfgRelativeStartTime_Object = MibTableColumn
mefSoamTestCfgRelativeStartTime = _MefSoamTestCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 15),
    _MefSoamTestCfgRelativeStartTime_Type()
)
mefSoamTestCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgRelativeStartTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamTestCfgRelativeStartTime.setUnits("centi-seconds")


class _MefSoamTestCfgDurationTime_Type(TimeInterval):
    """Custom type mefSoamTestCfgDurationTime based on TimeInterval"""
    defaultValue = 0


_MefSoamTestCfgDurationTime_Type.__name__ = "TimeInterval"
_MefSoamTestCfgDurationTime_Object = MibTableColumn
mefSoamTestCfgDurationTime = _MefSoamTestCfgDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 16),
    _MefSoamTestCfgDurationTime_Type()
)
mefSoamTestCfgDurationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamTestCfgDurationTime.setUnits("centi-seconds")


class _MefSoamTestCfgOutStatus_Type(TruthValue):
    """Custom type mefSoamTestCfgOutStatus based on TruthValue"""
    defaultValue = 2


_MefSoamTestCfgOutStatus_Type.__name__ = "TruthValue"
_MefSoamTestCfgOutStatus_Object = MibTableColumn
mefSoamTestCfgOutStatus = _MefSoamTestCfgOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 1, 1, 17),
    _MefSoamTestCfgOutStatus_Type()
)
mefSoamTestCfgOutStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamTestCfgOutStatus.setStatus("current")
_MefSoamTestStatsTable_Object = MibTable
mefSoamTestStatsTable = _MefSoamTestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    mefSoamTestStatsTable.setStatus("current")
_MefSoamTestStatsEntry_Object = MibTableRow
mefSoamTestStatsEntry = _MefSoamTestStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamTestStatsEntry.setStatus("current")
_MefSoamTestStatsNumIn_Type = Counter64
_MefSoamTestStatsNumIn_Object = MibTableColumn
mefSoamTestStatsNumIn = _MefSoamTestStatsNumIn_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1, 1),
    _MefSoamTestStatsNumIn_Type()
)
mefSoamTestStatsNumIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamTestStatsNumIn.setStatus("current")
_MefSoamTestStatsNumInOutOfOrder_Type = Counter64
_MefSoamTestStatsNumInOutOfOrder_Object = MibTableColumn
mefSoamTestStatsNumInOutOfOrder = _MefSoamTestStatsNumInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1, 2),
    _MefSoamTestStatsNumInOutOfOrder_Type()
)
mefSoamTestStatsNumInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamTestStatsNumInOutOfOrder.setStatus("current")
_MefSoamTestStatsNumInCrcErrors_Type = Counter64
_MefSoamTestStatsNumInCrcErrors_Object = MibTableColumn
mefSoamTestStatsNumInCrcErrors = _MefSoamTestStatsNumInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1, 3),
    _MefSoamTestStatsNumInCrcErrors_Type()
)
mefSoamTestStatsNumInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamTestStatsNumInCrcErrors.setStatus("current")
_MefSoamTestStatsNumInBerErrors_Type = Counter64
_MefSoamTestStatsNumInBerErrors_Object = MibTableColumn
mefSoamTestStatsNumInBerErrors = _MefSoamTestStatsNumInBerErrors_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1, 4),
    _MefSoamTestStatsNumInBerErrors_Type()
)
mefSoamTestStatsNumInBerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamTestStatsNumInBerErrors.setStatus("current")
_MefSoamTestStatsNumOut_Type = Counter64
_MefSoamTestStatsNumOut_Object = MibTableColumn
mefSoamTestStatsNumOut = _MefSoamTestStatsNumOut_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 9, 2, 1, 5),
    _MefSoamTestStatsNumOut_Type()
)
mefSoamTestStatsNumOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamTestStatsNumOut.setStatus("current")
_MefSoamFmNotificationCfg_ObjectIdentity = ObjectIdentity
mefSoamFmNotificationCfg = _MefSoamFmNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 10)
)


class _MefSoamAlarmInterval_Type(Unsigned32):
    """Custom type mefSoamAlarmInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MefSoamAlarmInterval_Type.__name__ = "Unsigned32"
_MefSoamAlarmInterval_Object = MibScalar
mefSoamAlarmInterval = _MefSoamAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 10, 1),
    _MefSoamAlarmInterval_Type()
)
mefSoamAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamAlarmInterval.setUnits("Seconds")


class _MefSoamAlarmEnable_Type(Bits):
    """Custom type mefSoamAlarmEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bCfmFaultAlarm", 0),
          ("bMepDefectAlarm", 1),
          ("bConfigErrorAssertAlarm", 2),
          ("bConfigErrorClearAlarm", 3),
          ("bMepOperStatusAlarm", 4),
          ("bLckAlarm", 5),
          ("bAisAlarm", 6))
    )

_MefSoamAlarmEnable_Type.__name__ = "Bits"
_MefSoamAlarmEnable_Object = MibScalar
mefSoamAlarmEnable = _MefSoamAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 1, 10, 2),
    _MefSoamAlarmEnable_Type()
)
mefSoamAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamAlarmEnable.setStatus("current")
_MefSoamFmMibConformance_ObjectIdentity = ObjectIdentity
mefSoamFmMibConformance = _MefSoamFmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2)
)
_MefSoamFmMibCompliances_ObjectIdentity = ObjectIdentity
mefSoamFmMibCompliances = _MefSoamFmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 1)
)
_MefSoamFmMibGroups_ObjectIdentity = ObjectIdentity
mefSoamFmMibGroups = _MefSoamFmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2)
)
dot1agCfmMaNetEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamNetCfgEntry")
)
mefSoamNetCfgEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
ieee8021CfmMaCompEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamMegCfgEntry")
)
mefSoamMegCfgEntry.setIndexNames(*ieee8021CfmMaCompEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamMepStatusEntry")
)
mefSoamMepStatusEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamMepFmStatsEntry")
)
mefSoamMepFmStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamCcCfgEntry")
)
mefSoamCcCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamAisCfgEntry")
)
mefSoamAisCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamAisStatsEntry")
)
mefSoamAisStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamLbCfgEntry")
)
mefSoamLbCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamLbStatsEntry")
)
mefSoamLbStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamLtStatsEntry")
)
mefSoamLtStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamLckCfgEntry")
)
mefSoamLckCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamLckStatsEntry")
)
mefSoamLckStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamTestCfgEntry")
)
mefSoamTestCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-FM-MIB",
     "mefSoamTestStatsEntry")
)
mefSoamTestStatsEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

mefSoamMegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 1)
)
mefSoamMegGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMegCfgConnectivityStatusInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamMegCfgPeerMepInfoAgingTime"),
        ("MEF-SOAM-FM-MIB", "mefSoamMegCfgPortStatusTlvIncluded"),
        ("MEF-SOAM-FM-MIB", "mefSoamMegCfgInterfaceStatusTlvIncluded"),
        ("MEF-SOAM-FM-MIB", "mefSoamNetCfgY1731Compliant"),
        ("MEF-SOAM-FM-MIB", "mefSoamNetCfgMegIdFormat"),
        ("MEF-SOAM-FM-MIB", "mefSoamNetCfgMegLevel"))
)
if mibBuilder.loadTexts:
    mefSoamMegGroup.setStatus("current")

mefSoamMepMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 2)
)
mefSoamMepMandatoryGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMepStatusOperationalState"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusConnectivityStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusSentPortStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusSentInterfaceStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusLastDefectSentStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusRdiTransmitStatus"))
)
if mibBuilder.loadTexts:
    mefSoamMepMandatoryGroup.setStatus("current")

mefSoamMepOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 3)
)
mefSoamMepOptionalGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMepFmStatsInOamFramesDiscarded"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepFmStatsInCcmTotal"))
)
if mibBuilder.loadTexts:
    mefSoamMepOptionalGroup.setStatus("current")

mefSoamCcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 4)
)
mefSoamCcGroup.setObjects(
    ("MEF-SOAM-FM-MIB", "mefSoamCcCfgDropEligible")
)
if mibBuilder.loadTexts:
    mefSoamCcGroup.setStatus("current")

mefSoamAisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 5)
)
mefSoamAisGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamAisCfgEnabled"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisCfgInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisCfgPriority"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisCfgMdLevel"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisCfgDropEligible"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsOutStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsOutCounter"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsInStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsInCounter"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsInMacAddr"))
)
if mibBuilder.loadTexts:
    mefSoamAisGroup.setStatus("current")

mefSoamLbMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 6)
)
mefSoamLbMandatoryGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLbCfgMulticastEnabled"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbCfgInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbCfgFrameSize"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbCfgDataPattern"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbStatsNumLbrInCrcErrors"))
)
if mibBuilder.loadTexts:
    mefSoamLbMandatoryGroup.setStatus("current")

mefSoamLbOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 7)
)
mefSoamLbOptionalGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLbCfgTestTlvIncluded"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbCfgTestTlvPattern"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbrMulticastReplyMac"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbCfgTimeout"))
)
if mibBuilder.loadTexts:
    mefSoamLbOptionalGroup.setStatus("current")

mefSoamLtMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 8)
)
mefSoamLtMandatoryGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLtLtmTransmitted"),
        ("MEF-SOAM-FM-MIB", "mefSoamLtLtrReceived"))
)
if mibBuilder.loadTexts:
    mefSoamLtMandatoryGroup.setStatus("current")

mefSoamLtOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 9)
)
mefSoamLtOptionalGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLtLtmReceived"),
        ("MEF-SOAM-FM-MIB", "mefSoamLtLtrTransmitted"))
)
if mibBuilder.loadTexts:
    mefSoamLtOptionalGroup.setStatus("current")

mefSoamLckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 10)
)
mefSoamLckGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLckCfgAdminState"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckCfgInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckCfgPriority"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckCfgMdLevel"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckStatsInStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckStatsInCounter"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckStatsOutStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckStatsOutCounter"))
)
if mibBuilder.loadTexts:
    mefSoamLckGroup.setStatus("current")

mefSoamTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 11)
)
mefSoamTestGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamTestCfgOutEnabled"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgInEnabled"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgInService"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgDestMacAddress"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgDestMepId"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgDestIsMepId"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgPriority"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgDropEligible"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgFrameSize"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgPattern"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgStartTimeType"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgScheduledStartDateAndTime"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgScheduledStopDateAndTime"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgRelativeStartTime"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgDurationTime"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestStatsNumIn"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestStatsNumInOutOfOrder"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestStatsNumInCrcErrors"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestStatsNumInBerErrors"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestStatsNumOut"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestCfgOutStatus"))
)
if mibBuilder.loadTexts:
    mefSoamTestGroup.setStatus("current")

mefSoamFmNotificationCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 13)
)
mefSoamFmNotificationCfgGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamAlarmInterval"),
        ("MEF-SOAM-FM-MIB", "mefSoamAlarmEnable"))
)
if mibBuilder.loadTexts:
    mefSoamFmNotificationCfgGroup.setStatus("current")


# Notification objects

mefSoamMepDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 1)
)
mefSoamMepDefectAlarm.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepDefects"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepStatusLastDefectSentStatus"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"))
)
if mibBuilder.loadTexts:
    mefSoamMepDefectAlarm.setStatus(
        "current"
    )

mefSoamConfigErrorAssertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 2)
)
mefSoamConfigErrorAssertAlarm.setObjects(
    ("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    mefSoamConfigErrorAssertAlarm.setStatus(
        "current"
    )

mefSoamConfigErrorClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 3)
)
mefSoamConfigErrorClearAlarm.setObjects(
    ("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    mefSoamConfigErrorClearAlarm.setStatus(
        "current"
    )

mefSoamMepOperStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 4)
)
mefSoamMepOperStatusAlarm.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMepStatusOperationalState"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepActive"))
)
if mibBuilder.loadTexts:
    mefSoamMepOperStatusAlarm.setStatus(
        "current"
    )

mefSoamLckAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 5)
)
mefSoamLckAlarm.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLckStatsInStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckStatsOutStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLckAlarm.setStatus(
        "current"
    )

mefSoamAisAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 0, 6)
)
mefSoamAisAlarm.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamAisStatsOutStatus"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisStatsInStatus"))
)
if mibBuilder.loadTexts:
    mefSoamAisAlarm.setStatus(
        "current"
    )


# Notifications groups

mefSoamFmNotificationsMandatoryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 12)
)
mefSoamFmNotificationsMandatoryGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMepDefectAlarm"),
        ("MEF-SOAM-FM-MIB", "mefSoamConfigErrorAssertAlarm"),
        ("MEF-SOAM-FM-MIB", "mefSoamConfigErrorClearAlarm"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepOperStatusAlarm"))
)
if mibBuilder.loadTexts:
    mefSoamFmNotificationsMandatoryGroup.setStatus(
        "current"
    )

mefSoamFmNotificationsOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 2, 14)
)
mefSoamFmNotificationsOptionalGroup.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamLckAlarm"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisAlarm"))
)
if mibBuilder.loadTexts:
    mefSoamFmNotificationsOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mefSoamFmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 1, 2, 2, 1, 1)
)
mefSoamFmMibCompliance.setObjects(
      *(("MEF-SOAM-FM-MIB", "mefSoamMegGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepMandatoryGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbMandatoryGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamLtMandatoryGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamFmNotificationsMandatoryGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamMepOptionalGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamCcGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamAisGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamLbOptionalGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamLtOptionalGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamLckGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamTestGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamFmNotificationCfgGroup"),
        ("MEF-SOAM-FM-MIB", "mefSoamFmNotificationsOptionalGroup"))
)
if mibBuilder.loadTexts:
    mefSoamFmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-SOAM-FM-MIB",
    **{"mefSoamFmMib": mefSoamFmMib,
       "mefSoamFmNotifications": mefSoamFmNotifications,
       "mefSoamMepDefectAlarm": mefSoamMepDefectAlarm,
       "mefSoamConfigErrorAssertAlarm": mefSoamConfigErrorAssertAlarm,
       "mefSoamConfigErrorClearAlarm": mefSoamConfigErrorClearAlarm,
       "mefSoamMepOperStatusAlarm": mefSoamMepOperStatusAlarm,
       "mefSoamLckAlarm": mefSoamLckAlarm,
       "mefSoamAisAlarm": mefSoamAisAlarm,
       "mefSoamFmMibObjects": mefSoamFmMibObjects,
       "mefSoamNet": mefSoamNet,
       "mefSoamNetCfgTable": mefSoamNetCfgTable,
       "mefSoamNetCfgEntry": mefSoamNetCfgEntry,
       "mefSoamNetCfgY1731Compliant": mefSoamNetCfgY1731Compliant,
       "mefSoamNetCfgMegIdFormat": mefSoamNetCfgMegIdFormat,
       "mefSoamNetCfgMegLevel": mefSoamNetCfgMegLevel,
       "mefSoamMeg": mefSoamMeg,
       "mefSoamMegCfgTable": mefSoamMegCfgTable,
       "mefSoamMegCfgEntry": mefSoamMegCfgEntry,
       "mefSoamMegCfgConnectivityStatusInterval": mefSoamMegCfgConnectivityStatusInterval,
       "mefSoamMegCfgPeerMepInfoAgingTime": mefSoamMegCfgPeerMepInfoAgingTime,
       "mefSoamMegCfgPortStatusTlvIncluded": mefSoamMegCfgPortStatusTlvIncluded,
       "mefSoamMegCfgInterfaceStatusTlvIncluded": mefSoamMegCfgInterfaceStatusTlvIncluded,
       "mefSoamMep": mefSoamMep,
       "mefSoamMepStatusTable": mefSoamMepStatusTable,
       "mefSoamMepStatusEntry": mefSoamMepStatusEntry,
       "mefSoamMepStatusOperationalState": mefSoamMepStatusOperationalState,
       "mefSoamMepStatusConnectivityStatus": mefSoamMepStatusConnectivityStatus,
       "mefSoamMepStatusSentPortStatus": mefSoamMepStatusSentPortStatus,
       "mefSoamMepStatusSentInterfaceStatus": mefSoamMepStatusSentInterfaceStatus,
       "mefSoamMepStatusLastDefectSentStatus": mefSoamMepStatusLastDefectSentStatus,
       "mefSoamMepStatusRdiTransmitStatus": mefSoamMepStatusRdiTransmitStatus,
       "mefSoamMepFmStatsTable": mefSoamMepFmStatsTable,
       "mefSoamMepFmStatsEntry": mefSoamMepFmStatsEntry,
       "mefSoamMepFmStatsInOamFramesDiscarded": mefSoamMepFmStatsInOamFramesDiscarded,
       "mefSoamMepFmStatsInCcmTotal": mefSoamMepFmStatsInCcmTotal,
       "mefSoamCc": mefSoamCc,
       "mefSoamCcCfgTable": mefSoamCcCfgTable,
       "mefSoamCcCfgEntry": mefSoamCcCfgEntry,
       "mefSoamCcCfgDropEligible": mefSoamCcCfgDropEligible,
       "mefSoamAis": mefSoamAis,
       "mefSoamAisCfgTable": mefSoamAisCfgTable,
       "mefSoamAisCfgEntry": mefSoamAisCfgEntry,
       "mefSoamAisCfgEnabled": mefSoamAisCfgEnabled,
       "mefSoamAisCfgInterval": mefSoamAisCfgInterval,
       "mefSoamAisCfgPriority": mefSoamAisCfgPriority,
       "mefSoamAisCfgMdLevel": mefSoamAisCfgMdLevel,
       "mefSoamAisCfgDropEligible": mefSoamAisCfgDropEligible,
       "mefSoamAisStatsTable": mefSoamAisStatsTable,
       "mefSoamAisStatsEntry": mefSoamAisStatsEntry,
       "mefSoamAisStatsOutStatus": mefSoamAisStatsOutStatus,
       "mefSoamAisStatsOutCounter": mefSoamAisStatsOutCounter,
       "mefSoamAisStatsInStatus": mefSoamAisStatsInStatus,
       "mefSoamAisStatsInCounter": mefSoamAisStatsInCounter,
       "mefSoamAisStatsInMacAddr": mefSoamAisStatsInMacAddr,
       "mefSoamLb": mefSoamLb,
       "mefSoamLbCfgTable": mefSoamLbCfgTable,
       "mefSoamLbCfgEntry": mefSoamLbCfgEntry,
       "mefSoamLbCfgMulticastEnabled": mefSoamLbCfgMulticastEnabled,
       "mefSoamLbCfgInterval": mefSoamLbCfgInterval,
       "mefSoamLbCfgFrameSize": mefSoamLbCfgFrameSize,
       "mefSoamLbCfgDataPattern": mefSoamLbCfgDataPattern,
       "mefSoamLbCfgTestTlvIncluded": mefSoamLbCfgTestTlvIncluded,
       "mefSoamLbCfgTestTlvPattern": mefSoamLbCfgTestTlvPattern,
       "mefSoamLbCfgTimeout": mefSoamLbCfgTimeout,
       "mefSoamLbStatsTable": mefSoamLbStatsTable,
       "mefSoamLbStatsEntry": mefSoamLbStatsEntry,
       "mefSoamLbStatsNumLbrInCrcErrors": mefSoamLbStatsNumLbrInCrcErrors,
       "mefSoamLbrMulticastTable": mefSoamLbrMulticastTable,
       "mefSoamLbrMulticastEntry": mefSoamLbrMulticastEntry,
       "mefSoamLbrMulticastTransId": mefSoamLbrMulticastTransId,
       "mefSoamLbrMulticastReceiveOrder": mefSoamLbrMulticastReceiveOrder,
       "mefSoamLbrMulticastReplyMac": mefSoamLbrMulticastReplyMac,
       "mefSoamLt": mefSoamLt,
       "mefSoamLtStatsTable": mefSoamLtStatsTable,
       "mefSoamLtStatsEntry": mefSoamLtStatsEntry,
       "mefSoamLtLtmTransmitted": mefSoamLtLtmTransmitted,
       "mefSoamLtLtrReceived": mefSoamLtLtrReceived,
       "mefSoamLtLtmReceived": mefSoamLtLtmReceived,
       "mefSoamLtLtrTransmitted": mefSoamLtLtrTransmitted,
       "mefSoamLck": mefSoamLck,
       "mefSoamLckCfgTable": mefSoamLckCfgTable,
       "mefSoamLckCfgEntry": mefSoamLckCfgEntry,
       "mefSoamLckCfgAdminState": mefSoamLckCfgAdminState,
       "mefSoamLckCfgInterval": mefSoamLckCfgInterval,
       "mefSoamLckCfgPriority": mefSoamLckCfgPriority,
       "mefSoamLckCfgMdLevel": mefSoamLckCfgMdLevel,
       "mefSoamLckStatsTable": mefSoamLckStatsTable,
       "mefSoamLckStatsEntry": mefSoamLckStatsEntry,
       "mefSoamLckStatsInStatus": mefSoamLckStatsInStatus,
       "mefSoamLckStatsInCounter": mefSoamLckStatsInCounter,
       "mefSoamLckStatsOutStatus": mefSoamLckStatsOutStatus,
       "mefSoamLckStatsOutCounter": mefSoamLckStatsOutCounter,
       "mefSoamTest": mefSoamTest,
       "mefSoamTestCfgTable": mefSoamTestCfgTable,
       "mefSoamTestCfgEntry": mefSoamTestCfgEntry,
       "mefSoamTestCfgOutEnabled": mefSoamTestCfgOutEnabled,
       "mefSoamTestCfgInEnabled": mefSoamTestCfgInEnabled,
       "mefSoamTestCfgInService": mefSoamTestCfgInService,
       "mefSoamTestCfgDestMacAddress": mefSoamTestCfgDestMacAddress,
       "mefSoamTestCfgDestMepId": mefSoamTestCfgDestMepId,
       "mefSoamTestCfgDestIsMepId": mefSoamTestCfgDestIsMepId,
       "mefSoamTestCfgInterval": mefSoamTestCfgInterval,
       "mefSoamTestCfgPriority": mefSoamTestCfgPriority,
       "mefSoamTestCfgDropEligible": mefSoamTestCfgDropEligible,
       "mefSoamTestCfgFrameSize": mefSoamTestCfgFrameSize,
       "mefSoamTestCfgPattern": mefSoamTestCfgPattern,
       "mefSoamTestCfgStartTimeType": mefSoamTestCfgStartTimeType,
       "mefSoamTestCfgScheduledStartDateAndTime": mefSoamTestCfgScheduledStartDateAndTime,
       "mefSoamTestCfgScheduledStopDateAndTime": mefSoamTestCfgScheduledStopDateAndTime,
       "mefSoamTestCfgRelativeStartTime": mefSoamTestCfgRelativeStartTime,
       "mefSoamTestCfgDurationTime": mefSoamTestCfgDurationTime,
       "mefSoamTestCfgOutStatus": mefSoamTestCfgOutStatus,
       "mefSoamTestStatsTable": mefSoamTestStatsTable,
       "mefSoamTestStatsEntry": mefSoamTestStatsEntry,
       "mefSoamTestStatsNumIn": mefSoamTestStatsNumIn,
       "mefSoamTestStatsNumInOutOfOrder": mefSoamTestStatsNumInOutOfOrder,
       "mefSoamTestStatsNumInCrcErrors": mefSoamTestStatsNumInCrcErrors,
       "mefSoamTestStatsNumInBerErrors": mefSoamTestStatsNumInBerErrors,
       "mefSoamTestStatsNumOut": mefSoamTestStatsNumOut,
       "mefSoamFmNotificationCfg": mefSoamFmNotificationCfg,
       "mefSoamAlarmInterval": mefSoamAlarmInterval,
       "mefSoamAlarmEnable": mefSoamAlarmEnable,
       "mefSoamFmMibConformance": mefSoamFmMibConformance,
       "mefSoamFmMibCompliances": mefSoamFmMibCompliances,
       "mefSoamFmMibCompliance": mefSoamFmMibCompliance,
       "mefSoamFmMibGroups": mefSoamFmMibGroups,
       "mefSoamMegGroup": mefSoamMegGroup,
       "mefSoamMepMandatoryGroup": mefSoamMepMandatoryGroup,
       "mefSoamMepOptionalGroup": mefSoamMepOptionalGroup,
       "mefSoamCcGroup": mefSoamCcGroup,
       "mefSoamAisGroup": mefSoamAisGroup,
       "mefSoamLbMandatoryGroup": mefSoamLbMandatoryGroup,
       "mefSoamLbOptionalGroup": mefSoamLbOptionalGroup,
       "mefSoamLtMandatoryGroup": mefSoamLtMandatoryGroup,
       "mefSoamLtOptionalGroup": mefSoamLtOptionalGroup,
       "mefSoamLckGroup": mefSoamLckGroup,
       "mefSoamTestGroup": mefSoamTestGroup,
       "mefSoamFmNotificationsMandatoryGroup": mefSoamFmNotificationsMandatoryGroup,
       "mefSoamFmNotificationCfgGroup": mefSoamFmNotificationCfgGroup,
       "mefSoamFmNotificationsOptionalGroup": mefSoamFmNotificationsOptionalGroup}
)
