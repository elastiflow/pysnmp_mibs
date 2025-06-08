# SNMP MIB module (TIMETRA-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-RIP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(RouteTag,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "RouteTag")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TPriorityOrUndefined,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TPriorityOrUndefined",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraRipMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    timetraRipMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2002-05-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxRipAuthType(TextualConvention, Integer32):
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
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3),
          ("md20", 4))
    )



class TmnxRipAuthKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxRipMessageSize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 255),
    )



class TmnxRipMetric(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxRipPreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxRipReceive(TextualConvention, Integer32):
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3),
          ("doNotReceive", 4))
    )



class TmnxRipSend(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("ripVersion1", 2),
          ("rip1Compatible", 3),
          ("ripVersion2", 4),
          ("ripUnicast", 6))
    )



class TmnxRipTimerFlush(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )



class TmnxRipTimerTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )



class TmnxRipTimerUpdate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxRipConformance_ObjectIdentity = ObjectIdentity
tmnxRipConformance = _TmnxRipConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9)
)
_TmnxRipCompliances_ObjectIdentity = ObjectIdentity
tmnxRipCompliances = _TmnxRipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 1)
)
_TmnxRipGroups_ObjectIdentity = ObjectIdentity
tmnxRipGroups = _TmnxRipGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2)
)
_VRtrRipObjs_ObjectIdentity = ObjectIdentity
vRtrRipObjs = _VRtrRipObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9)
)
_VRtrRipGlobals_ObjectIdentity = ObjectIdentity
vRtrRipGlobals = _VRtrRipGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 1)
)
_VRtrRipGlobalLearnedRoutes_Type = Counter32
_VRtrRipGlobalLearnedRoutes_Object = MibScalar
vRtrRipGlobalLearnedRoutes = _VRtrRipGlobalLearnedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 1, 1),
    _VRtrRipGlobalLearnedRoutes_Type()
)
vRtrRipGlobalLearnedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipGlobalLearnedRoutes.setStatus("current")
_VRtrRipGlobalTimedoutRoutes_Type = Counter32
_VRtrRipGlobalTimedoutRoutes_Object = MibScalar
vRtrRipGlobalTimedoutRoutes = _VRtrRipGlobalTimedoutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 1, 2),
    _VRtrRipGlobalTimedoutRoutes_Type()
)
vRtrRipGlobalTimedoutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipGlobalTimedoutRoutes.setStatus("current")
_VRtrRipGlobalCurrentMemory_Type = Counter32
_VRtrRipGlobalCurrentMemory_Object = MibScalar
vRtrRipGlobalCurrentMemory = _VRtrRipGlobalCurrentMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 1, 3),
    _VRtrRipGlobalCurrentMemory_Type()
)
vRtrRipGlobalCurrentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipGlobalCurrentMemory.setStatus("current")
_VRtrRipGlobalMaximumMemory_Type = Counter32
_VRtrRipGlobalMaximumMemory_Object = MibScalar
vRtrRipGlobalMaximumMemory = _VRtrRipGlobalMaximumMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 1, 4),
    _VRtrRipGlobalMaximumMemory_Type()
)
vRtrRipGlobalMaximumMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipGlobalMaximumMemory.setStatus("current")
_VRtrRipInstanceTable_Object = MibTable
vRtrRipInstanceTable = _VRtrRipInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    vRtrRipInstanceTable.setStatus("current")
_VRtrRipInstanceEntry_Object = MibTableRow
vRtrRipInstanceEntry = _VRtrRipInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1)
)
vRtrRipInstanceEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrRipInstanceEntry.setStatus("current")


class _VRtrRipInstanceAuthType_Type(TmnxRipAuthType):
    """Custom type vRtrRipInstanceAuthType based on TmnxRipAuthType"""
    defaultValue = 1


_VRtrRipInstanceAuthType_Type.__name__ = "TmnxRipAuthType"
_VRtrRipInstanceAuthType_Object = MibTableColumn
vRtrRipInstanceAuthType = _VRtrRipInstanceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 1),
    _VRtrRipInstanceAuthType_Type()
)
vRtrRipInstanceAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceAuthType.setStatus("current")


class _VRtrRipInstanceAuthKey_Type(TmnxRipAuthKey):
    """Custom type vRtrRipInstanceAuthKey based on TmnxRipAuthKey"""
    defaultHexValue = ""


_VRtrRipInstanceAuthKey_Type.__name__ = "TmnxRipAuthKey"
_VRtrRipInstanceAuthKey_Object = MibTableColumn
vRtrRipInstanceAuthKey = _VRtrRipInstanceAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 2),
    _VRtrRipInstanceAuthKey_Type()
)
vRtrRipInstanceAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceAuthKey.setStatus("current")


class _VRtrRipInstanceCheckZero_Type(TruthValue):
    """Custom type vRtrRipInstanceCheckZero based on TruthValue"""
    defaultValue = 2


_VRtrRipInstanceCheckZero_Type.__name__ = "TruthValue"
_VRtrRipInstanceCheckZero_Object = MibTableColumn
vRtrRipInstanceCheckZero = _VRtrRipInstanceCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 3),
    _VRtrRipInstanceCheckZero_Type()
)
vRtrRipInstanceCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceCheckZero.setStatus("current")


class _VRtrRipInstanceMessageSize_Type(TmnxRipMessageSize):
    """Custom type vRtrRipInstanceMessageSize based on TmnxRipMessageSize"""
    defaultValue = 25


_VRtrRipInstanceMessageSize_Type.__name__ = "TmnxRipMessageSize"
_VRtrRipInstanceMessageSize_Object = MibTableColumn
vRtrRipInstanceMessageSize = _VRtrRipInstanceMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 4),
    _VRtrRipInstanceMessageSize_Type()
)
vRtrRipInstanceMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceMessageSize.setStatus("current")


class _VRtrRipInstanceMetricIn_Type(TmnxRipMetric):
    """Custom type vRtrRipInstanceMetricIn based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipInstanceMetricIn_Type.__name__ = "TmnxRipMetric"
_VRtrRipInstanceMetricIn_Object = MibTableColumn
vRtrRipInstanceMetricIn = _VRtrRipInstanceMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 5),
    _VRtrRipInstanceMetricIn_Type()
)
vRtrRipInstanceMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceMetricIn.setStatus("current")


class _VRtrRipInstanceMetricOut_Type(TmnxRipMetric):
    """Custom type vRtrRipInstanceMetricOut based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipInstanceMetricOut_Type.__name__ = "TmnxRipMetric"
_VRtrRipInstanceMetricOut_Object = MibTableColumn
vRtrRipInstanceMetricOut = _VRtrRipInstanceMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 6),
    _VRtrRipInstanceMetricOut_Type()
)
vRtrRipInstanceMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceMetricOut.setStatus("current")


class _VRtrRipInstancePreference_Type(TmnxRipPreference):
    """Custom type vRtrRipInstancePreference based on TmnxRipPreference"""
    defaultValue = 100


_VRtrRipInstancePreference_Type.__name__ = "TmnxRipPreference"
_VRtrRipInstancePreference_Object = MibTableColumn
vRtrRipInstancePreference = _VRtrRipInstancePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 7),
    _VRtrRipInstancePreference_Type()
)
vRtrRipInstancePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstancePreference.setStatus("current")


class _VRtrRipInstanceReceive_Type(TmnxRipReceive):
    """Custom type vRtrRipInstanceReceive based on TmnxRipReceive"""
    defaultValue = 3


_VRtrRipInstanceReceive_Type.__name__ = "TmnxRipReceive"
_VRtrRipInstanceReceive_Object = MibTableColumn
vRtrRipInstanceReceive = _VRtrRipInstanceReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 8),
    _VRtrRipInstanceReceive_Type()
)
vRtrRipInstanceReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceReceive.setStatus("current")


class _VRtrRipInstanceSend_Type(TmnxRipSend):
    """Custom type vRtrRipInstanceSend based on TmnxRipSend"""
    defaultValue = 3


_VRtrRipInstanceSend_Type.__name__ = "TmnxRipSend"
_VRtrRipInstanceSend_Object = MibTableColumn
vRtrRipInstanceSend = _VRtrRipInstanceSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 9),
    _VRtrRipInstanceSend_Type()
)
vRtrRipInstanceSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceSend.setStatus("current")


class _VRtrRipInstanceSplitHorizon_Type(TruthValue):
    """Custom type vRtrRipInstanceSplitHorizon based on TruthValue"""
    defaultValue = 1


_VRtrRipInstanceSplitHorizon_Type.__name__ = "TruthValue"
_VRtrRipInstanceSplitHorizon_Object = MibTableColumn
vRtrRipInstanceSplitHorizon = _VRtrRipInstanceSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 10),
    _VRtrRipInstanceSplitHorizon_Type()
)
vRtrRipInstanceSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceSplitHorizon.setStatus("current")


class _VRtrRipInstanceTimerFlush_Type(TmnxRipTimerFlush):
    """Custom type vRtrRipInstanceTimerFlush based on TmnxRipTimerFlush"""
    defaultValue = 120


_VRtrRipInstanceTimerFlush_Type.__name__ = "TmnxRipTimerFlush"
_VRtrRipInstanceTimerFlush_Object = MibTableColumn
vRtrRipInstanceTimerFlush = _VRtrRipInstanceTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 11),
    _VRtrRipInstanceTimerFlush_Type()
)
vRtrRipInstanceTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerFlush.setUnits("seconds")


class _VRtrRipInstanceTimerTimeout_Type(TmnxRipTimerTimeout):
    """Custom type vRtrRipInstanceTimerTimeout based on TmnxRipTimerTimeout"""
    defaultValue = 180


_VRtrRipInstanceTimerTimeout_Type.__name__ = "TmnxRipTimerTimeout"
_VRtrRipInstanceTimerTimeout_Object = MibTableColumn
vRtrRipInstanceTimerTimeout = _VRtrRipInstanceTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 12),
    _VRtrRipInstanceTimerTimeout_Type()
)
vRtrRipInstanceTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerTimeout.setUnits("seconds")


class _VRtrRipInstanceTimerUpdate_Type(TmnxRipTimerUpdate):
    """Custom type vRtrRipInstanceTimerUpdate based on TmnxRipTimerUpdate"""
    defaultValue = 30


_VRtrRipInstanceTimerUpdate_Type.__name__ = "TmnxRipTimerUpdate"
_VRtrRipInstanceTimerUpdate_Object = MibTableColumn
vRtrRipInstanceTimerUpdate = _VRtrRipInstanceTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 13),
    _VRtrRipInstanceTimerUpdate_Type()
)
vRtrRipInstanceTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipInstanceTimerUpdate.setUnits("seconds")


class _VRtrRipInstanceImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceImportPolicy1_Object = MibTableColumn
vRtrRipInstanceImportPolicy1 = _VRtrRipInstanceImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 14),
    _VRtrRipInstanceImportPolicy1_Type()
)
vRtrRipInstanceImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceImportPolicy1.setStatus("current")


class _VRtrRipInstanceImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceImportPolicy2_Object = MibTableColumn
vRtrRipInstanceImportPolicy2 = _VRtrRipInstanceImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 15),
    _VRtrRipInstanceImportPolicy2_Type()
)
vRtrRipInstanceImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceImportPolicy2.setStatus("current")


class _VRtrRipInstanceImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceImportPolicy3_Object = MibTableColumn
vRtrRipInstanceImportPolicy3 = _VRtrRipInstanceImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 16),
    _VRtrRipInstanceImportPolicy3_Type()
)
vRtrRipInstanceImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceImportPolicy3.setStatus("current")


class _VRtrRipInstanceImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceImportPolicy4_Object = MibTableColumn
vRtrRipInstanceImportPolicy4 = _VRtrRipInstanceImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 17),
    _VRtrRipInstanceImportPolicy4_Type()
)
vRtrRipInstanceImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceImportPolicy4.setStatus("current")


class _VRtrRipInstanceImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceImportPolicy5_Object = MibTableColumn
vRtrRipInstanceImportPolicy5 = _VRtrRipInstanceImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 18),
    _VRtrRipInstanceImportPolicy5_Type()
)
vRtrRipInstanceImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceImportPolicy5.setStatus("current")


class _VRtrRipInstanceExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceExportPolicy1_Object = MibTableColumn
vRtrRipInstanceExportPolicy1 = _VRtrRipInstanceExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 19),
    _VRtrRipInstanceExportPolicy1_Type()
)
vRtrRipInstanceExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportPolicy1.setStatus("current")


class _VRtrRipInstanceExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceExportPolicy2_Object = MibTableColumn
vRtrRipInstanceExportPolicy2 = _VRtrRipInstanceExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 20),
    _VRtrRipInstanceExportPolicy2_Type()
)
vRtrRipInstanceExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportPolicy2.setStatus("current")


class _VRtrRipInstanceExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceExportPolicy3_Object = MibTableColumn
vRtrRipInstanceExportPolicy3 = _VRtrRipInstanceExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 21),
    _VRtrRipInstanceExportPolicy3_Type()
)
vRtrRipInstanceExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportPolicy3.setStatus("current")


class _VRtrRipInstanceExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceExportPolicy4_Object = MibTableColumn
vRtrRipInstanceExportPolicy4 = _VRtrRipInstanceExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 22),
    _VRtrRipInstanceExportPolicy4_Type()
)
vRtrRipInstanceExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportPolicy4.setStatus("current")


class _VRtrRipInstanceExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipInstanceExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipInstanceExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipInstanceExportPolicy5_Object = MibTableColumn
vRtrRipInstanceExportPolicy5 = _VRtrRipInstanceExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 23),
    _VRtrRipInstanceExportPolicy5_Type()
)
vRtrRipInstanceExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportPolicy5.setStatus("current")


class _VRtrRipInstanceDescription_Type(TItemDescription):
    """Custom type vRtrRipInstanceDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrRipInstanceDescription_Type.__name__ = "TItemDescription"
_VRtrRipInstanceDescription_Object = MibTableColumn
vRtrRipInstanceDescription = _VRtrRipInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 24),
    _VRtrRipInstanceDescription_Type()
)
vRtrRipInstanceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceDescription.setStatus("current")


class _VRtrRipInstanceAdminStatus_Type(TmnxAdminState):
    """Custom type vRtrRipInstanceAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_VRtrRipInstanceAdminStatus_Type.__name__ = "TmnxAdminState"
_VRtrRipInstanceAdminStatus_Object = MibTableColumn
vRtrRipInstanceAdminStatus = _VRtrRipInstanceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 25),
    _VRtrRipInstanceAdminStatus_Type()
)
vRtrRipInstanceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceAdminStatus.setStatus("current")
_VRtrRipInstanceOperStatus_Type = TmnxOperState
_VRtrRipInstanceOperStatus_Object = MibTableColumn
vRtrRipInstanceOperStatus = _VRtrRipInstanceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 26),
    _VRtrRipInstanceOperStatus_Type()
)
vRtrRipInstanceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipInstanceOperStatus.setStatus("current")


class _VRtrRipInstancePropagateMetric_Type(TruthValue):
    """Custom type vRtrRipInstancePropagateMetric based on TruthValue"""
    defaultValue = 2


_VRtrRipInstancePropagateMetric_Type.__name__ = "TruthValue"
_VRtrRipInstancePropagateMetric_Object = MibTableColumn
vRtrRipInstancePropagateMetric = _VRtrRipInstancePropagateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 27),
    _VRtrRipInstancePropagateMetric_Type()
)
vRtrRipInstancePropagateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstancePropagateMetric.setStatus("current")


class _VRtrRipInstanceExportLimit_Type(Unsigned32):
    """Custom type vRtrRipInstanceExportLimit based on Unsigned32"""
    defaultValue = 0


_VRtrRipInstanceExportLimit_Type.__name__ = "Unsigned32"
_VRtrRipInstanceExportLimit_Object = MibTableColumn
vRtrRipInstanceExportLimit = _VRtrRipInstanceExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 28),
    _VRtrRipInstanceExportLimit_Type()
)
vRtrRipInstanceExportLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExportLimit.setStatus("current")


class _VRtrRipInstanceExpLmtLogPercent_Type(Unsigned32):
    """Custom type vRtrRipInstanceExpLmtLogPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrRipInstanceExpLmtLogPercent_Type.__name__ = "Unsigned32"
_VRtrRipInstanceExpLmtLogPercent_Object = MibTableColumn
vRtrRipInstanceExpLmtLogPercent = _VRtrRipInstanceExpLmtLogPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 29),
    _VRtrRipInstanceExpLmtLogPercent_Type()
)
vRtrRipInstanceExpLmtLogPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipInstanceExpLmtLogPercent.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipInstanceExpLmtLogPercent.setUnits("percentage")
_VRtrRipInstanceTotalExpRoutes_Type = Gauge32
_VRtrRipInstanceTotalExpRoutes_Object = MibTableColumn
vRtrRipInstanceTotalExpRoutes = _VRtrRipInstanceTotalExpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 2, 1, 30),
    _VRtrRipInstanceTotalExpRoutes_Type()
)
vRtrRipInstanceTotalExpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipInstanceTotalExpRoutes.setStatus("current")
_VRtrRipGroupTable_Object = MibTable
vRtrRipGroupTable = _VRtrRipGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    vRtrRipGroupTable.setStatus("current")
_VRtrRipGroupEntry_Object = MibTableRow
vRtrRipGroupEntry = _VRtrRipGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1)
)
vRtrRipGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipGroupName"),
)
if mibBuilder.loadTexts:
    vRtrRipGroupEntry.setStatus("current")
_VRtrRipGroupName_Type = TNamedItem
_VRtrRipGroupName_Object = MibTableColumn
vRtrRipGroupName = _VRtrRipGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 1),
    _VRtrRipGroupName_Type()
)
vRtrRipGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipGroupName.setStatus("current")


class _VRtrRipGroupAuthType_Type(TmnxRipAuthType):
    """Custom type vRtrRipGroupAuthType based on TmnxRipAuthType"""
    defaultValue = 1


_VRtrRipGroupAuthType_Type.__name__ = "TmnxRipAuthType"
_VRtrRipGroupAuthType_Object = MibTableColumn
vRtrRipGroupAuthType = _VRtrRipGroupAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 2),
    _VRtrRipGroupAuthType_Type()
)
vRtrRipGroupAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupAuthType.setStatus("current")


class _VRtrRipGroupAuthKey_Type(TmnxRipAuthKey):
    """Custom type vRtrRipGroupAuthKey based on TmnxRipAuthKey"""
    defaultHexValue = ""


_VRtrRipGroupAuthKey_Type.__name__ = "TmnxRipAuthKey"
_VRtrRipGroupAuthKey_Object = MibTableColumn
vRtrRipGroupAuthKey = _VRtrRipGroupAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 3),
    _VRtrRipGroupAuthKey_Type()
)
vRtrRipGroupAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupAuthKey.setStatus("current")


class _VRtrRipGroupCheckZero_Type(TruthValue):
    """Custom type vRtrRipGroupCheckZero based on TruthValue"""
    defaultValue = 2


_VRtrRipGroupCheckZero_Type.__name__ = "TruthValue"
_VRtrRipGroupCheckZero_Object = MibTableColumn
vRtrRipGroupCheckZero = _VRtrRipGroupCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 4),
    _VRtrRipGroupCheckZero_Type()
)
vRtrRipGroupCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupCheckZero.setStatus("current")


class _VRtrRipGroupMessageSize_Type(TmnxRipMessageSize):
    """Custom type vRtrRipGroupMessageSize based on TmnxRipMessageSize"""
    defaultValue = 25


_VRtrRipGroupMessageSize_Type.__name__ = "TmnxRipMessageSize"
_VRtrRipGroupMessageSize_Object = MibTableColumn
vRtrRipGroupMessageSize = _VRtrRipGroupMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 5),
    _VRtrRipGroupMessageSize_Type()
)
vRtrRipGroupMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupMessageSize.setStatus("current")


class _VRtrRipGroupMetricIn_Type(TmnxRipMetric):
    """Custom type vRtrRipGroupMetricIn based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipGroupMetricIn_Type.__name__ = "TmnxRipMetric"
_VRtrRipGroupMetricIn_Object = MibTableColumn
vRtrRipGroupMetricIn = _VRtrRipGroupMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 6),
    _VRtrRipGroupMetricIn_Type()
)
vRtrRipGroupMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupMetricIn.setStatus("current")


class _VRtrRipGroupMetricOut_Type(TmnxRipMetric):
    """Custom type vRtrRipGroupMetricOut based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipGroupMetricOut_Type.__name__ = "TmnxRipMetric"
_VRtrRipGroupMetricOut_Object = MibTableColumn
vRtrRipGroupMetricOut = _VRtrRipGroupMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 7),
    _VRtrRipGroupMetricOut_Type()
)
vRtrRipGroupMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupMetricOut.setStatus("current")


class _VRtrRipGroupPreference_Type(TmnxRipPreference):
    """Custom type vRtrRipGroupPreference based on TmnxRipPreference"""
    defaultValue = 100


_VRtrRipGroupPreference_Type.__name__ = "TmnxRipPreference"
_VRtrRipGroupPreference_Object = MibTableColumn
vRtrRipGroupPreference = _VRtrRipGroupPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 8),
    _VRtrRipGroupPreference_Type()
)
vRtrRipGroupPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupPreference.setStatus("current")


class _VRtrRipGroupReceive_Type(TmnxRipReceive):
    """Custom type vRtrRipGroupReceive based on TmnxRipReceive"""
    defaultValue = 3


_VRtrRipGroupReceive_Type.__name__ = "TmnxRipReceive"
_VRtrRipGroupReceive_Object = MibTableColumn
vRtrRipGroupReceive = _VRtrRipGroupReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 9),
    _VRtrRipGroupReceive_Type()
)
vRtrRipGroupReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupReceive.setStatus("current")


class _VRtrRipGroupSend_Type(TmnxRipSend):
    """Custom type vRtrRipGroupSend based on TmnxRipSend"""
    defaultValue = 3


_VRtrRipGroupSend_Type.__name__ = "TmnxRipSend"
_VRtrRipGroupSend_Object = MibTableColumn
vRtrRipGroupSend = _VRtrRipGroupSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 10),
    _VRtrRipGroupSend_Type()
)
vRtrRipGroupSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupSend.setStatus("current")


class _VRtrRipGroupSplitHorizon_Type(TruthValue):
    """Custom type vRtrRipGroupSplitHorizon based on TruthValue"""
    defaultValue = 1


_VRtrRipGroupSplitHorizon_Type.__name__ = "TruthValue"
_VRtrRipGroupSplitHorizon_Object = MibTableColumn
vRtrRipGroupSplitHorizon = _VRtrRipGroupSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 11),
    _VRtrRipGroupSplitHorizon_Type()
)
vRtrRipGroupSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupSplitHorizon.setStatus("current")


class _VRtrRipGroupTimerFlush_Type(TmnxRipTimerFlush):
    """Custom type vRtrRipGroupTimerFlush based on TmnxRipTimerFlush"""
    defaultValue = 120


_VRtrRipGroupTimerFlush_Type.__name__ = "TmnxRipTimerFlush"
_VRtrRipGroupTimerFlush_Object = MibTableColumn
vRtrRipGroupTimerFlush = _VRtrRipGroupTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 12),
    _VRtrRipGroupTimerFlush_Type()
)
vRtrRipGroupTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerFlush.setUnits("seconds")


class _VRtrRipGroupTimerTimeout_Type(TmnxRipTimerTimeout):
    """Custom type vRtrRipGroupTimerTimeout based on TmnxRipTimerTimeout"""
    defaultValue = 180


_VRtrRipGroupTimerTimeout_Type.__name__ = "TmnxRipTimerTimeout"
_VRtrRipGroupTimerTimeout_Object = MibTableColumn
vRtrRipGroupTimerTimeout = _VRtrRipGroupTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 13),
    _VRtrRipGroupTimerTimeout_Type()
)
vRtrRipGroupTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerTimeout.setUnits("seconds")


class _VRtrRipGroupTimerUpdate_Type(TmnxRipTimerUpdate):
    """Custom type vRtrRipGroupTimerUpdate based on TmnxRipTimerUpdate"""
    defaultValue = 30


_VRtrRipGroupTimerUpdate_Type.__name__ = "TmnxRipTimerUpdate"
_VRtrRipGroupTimerUpdate_Object = MibTableColumn
vRtrRipGroupTimerUpdate = _VRtrRipGroupTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 14),
    _VRtrRipGroupTimerUpdate_Type()
)
vRtrRipGroupTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipGroupTimerUpdate.setUnits("seconds")


class _VRtrRipGroupImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupImportPolicy1_Object = MibTableColumn
vRtrRipGroupImportPolicy1 = _VRtrRipGroupImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 15),
    _VRtrRipGroupImportPolicy1_Type()
)
vRtrRipGroupImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupImportPolicy1.setStatus("current")


class _VRtrRipGroupImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupImportPolicy2_Object = MibTableColumn
vRtrRipGroupImportPolicy2 = _VRtrRipGroupImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 16),
    _VRtrRipGroupImportPolicy2_Type()
)
vRtrRipGroupImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupImportPolicy2.setStatus("current")


class _VRtrRipGroupImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupImportPolicy3_Object = MibTableColumn
vRtrRipGroupImportPolicy3 = _VRtrRipGroupImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 17),
    _VRtrRipGroupImportPolicy3_Type()
)
vRtrRipGroupImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupImportPolicy3.setStatus("current")


class _VRtrRipGroupImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupImportPolicy4_Object = MibTableColumn
vRtrRipGroupImportPolicy4 = _VRtrRipGroupImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 18),
    _VRtrRipGroupImportPolicy4_Type()
)
vRtrRipGroupImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupImportPolicy4.setStatus("current")


class _VRtrRipGroupImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupImportPolicy5_Object = MibTableColumn
vRtrRipGroupImportPolicy5 = _VRtrRipGroupImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 19),
    _VRtrRipGroupImportPolicy5_Type()
)
vRtrRipGroupImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupImportPolicy5.setStatus("current")


class _VRtrRipGroupExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupExportPolicy1_Object = MibTableColumn
vRtrRipGroupExportPolicy1 = _VRtrRipGroupExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 20),
    _VRtrRipGroupExportPolicy1_Type()
)
vRtrRipGroupExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupExportPolicy1.setStatus("current")


class _VRtrRipGroupExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupExportPolicy2_Object = MibTableColumn
vRtrRipGroupExportPolicy2 = _VRtrRipGroupExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 21),
    _VRtrRipGroupExportPolicy2_Type()
)
vRtrRipGroupExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupExportPolicy2.setStatus("current")


class _VRtrRipGroupExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupExportPolicy3_Object = MibTableColumn
vRtrRipGroupExportPolicy3 = _VRtrRipGroupExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 22),
    _VRtrRipGroupExportPolicy3_Type()
)
vRtrRipGroupExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupExportPolicy3.setStatus("current")


class _VRtrRipGroupExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupExportPolicy4_Object = MibTableColumn
vRtrRipGroupExportPolicy4 = _VRtrRipGroupExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 23),
    _VRtrRipGroupExportPolicy4_Type()
)
vRtrRipGroupExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupExportPolicy4.setStatus("current")


class _VRtrRipGroupExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipGroupExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipGroupExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipGroupExportPolicy5_Object = MibTableColumn
vRtrRipGroupExportPolicy5 = _VRtrRipGroupExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 24),
    _VRtrRipGroupExportPolicy5_Type()
)
vRtrRipGroupExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupExportPolicy5.setStatus("current")


class _VRtrRipGroupDescription_Type(TItemDescription):
    """Custom type vRtrRipGroupDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrRipGroupDescription_Type.__name__ = "TItemDescription"
_VRtrRipGroupDescription_Object = MibTableColumn
vRtrRipGroupDescription = _VRtrRipGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 25),
    _VRtrRipGroupDescription_Type()
)
vRtrRipGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupDescription.setStatus("current")


class _VRtrRipGroupInheritance_Type(Unsigned32):
    """Custom type vRtrRipGroupInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrRipGroupInheritance_Type.__name__ = "Unsigned32"
_VRtrRipGroupInheritance_Object = MibTableColumn
vRtrRipGroupInheritance = _VRtrRipGroupInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 26),
    _VRtrRipGroupInheritance_Type()
)
vRtrRipGroupInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupInheritance.setStatus("current")


class _VRtrRipGroupAdminStatus_Type(TmnxAdminState):
    """Custom type vRtrRipGroupAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_VRtrRipGroupAdminStatus_Type.__name__ = "TmnxAdminState"
_VRtrRipGroupAdminStatus_Object = MibTableColumn
vRtrRipGroupAdminStatus = _VRtrRipGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 27),
    _VRtrRipGroupAdminStatus_Type()
)
vRtrRipGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupAdminStatus.setStatus("current")
_VRtrRipGroupOperStatus_Type = TmnxOperState
_VRtrRipGroupOperStatus_Object = MibTableColumn
vRtrRipGroupOperStatus = _VRtrRipGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 28),
    _VRtrRipGroupOperStatus_Type()
)
vRtrRipGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipGroupOperStatus.setStatus("current")
_VRtrRipGroupRowStatus_Type = RowStatus
_VRtrRipGroupRowStatus_Object = MibTableColumn
vRtrRipGroupRowStatus = _VRtrRipGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 3, 1, 29),
    _VRtrRipGroupRowStatus_Type()
)
vRtrRipGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipGroupRowStatus.setStatus("current")
_VRtrRipIfTable_Object = MibTable
vRtrRipIfTable = _VRtrRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    vRtrRipIfTable.setStatus("current")
_VRtrRipIfEntry_Object = MibTableRow
vRtrRipIfEntry = _VRtrRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1)
)
vRtrRipIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrRipIfEntry.setStatus("current")
_VRtrRipIfGroupName_Type = TNamedItem
_VRtrRipIfGroupName_Object = MibTableColumn
vRtrRipIfGroupName = _VRtrRipIfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 1),
    _VRtrRipIfGroupName_Type()
)
vRtrRipIfGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfGroupName.setStatus("current")


class _VRtrRipIfAuthType_Type(TmnxRipAuthType):
    """Custom type vRtrRipIfAuthType based on TmnxRipAuthType"""
    defaultValue = 1


_VRtrRipIfAuthType_Type.__name__ = "TmnxRipAuthType"
_VRtrRipIfAuthType_Object = MibTableColumn
vRtrRipIfAuthType = _VRtrRipIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 2),
    _VRtrRipIfAuthType_Type()
)
vRtrRipIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfAuthType.setStatus("current")


class _VRtrRipIfAuthKey_Type(TmnxRipAuthKey):
    """Custom type vRtrRipIfAuthKey based on TmnxRipAuthKey"""
    defaultHexValue = ""


_VRtrRipIfAuthKey_Type.__name__ = "TmnxRipAuthKey"
_VRtrRipIfAuthKey_Object = MibTableColumn
vRtrRipIfAuthKey = _VRtrRipIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 3),
    _VRtrRipIfAuthKey_Type()
)
vRtrRipIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfAuthKey.setStatus("current")


class _VRtrRipIfCheckZero_Type(TruthValue):
    """Custom type vRtrRipIfCheckZero based on TruthValue"""
    defaultValue = 2


_VRtrRipIfCheckZero_Type.__name__ = "TruthValue"
_VRtrRipIfCheckZero_Object = MibTableColumn
vRtrRipIfCheckZero = _VRtrRipIfCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 4),
    _VRtrRipIfCheckZero_Type()
)
vRtrRipIfCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfCheckZero.setStatus("current")


class _VRtrRipIfMessageSize_Type(TmnxRipMessageSize):
    """Custom type vRtrRipIfMessageSize based on TmnxRipMessageSize"""
    defaultValue = 25


_VRtrRipIfMessageSize_Type.__name__ = "TmnxRipMessageSize"
_VRtrRipIfMessageSize_Object = MibTableColumn
vRtrRipIfMessageSize = _VRtrRipIfMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 5),
    _VRtrRipIfMessageSize_Type()
)
vRtrRipIfMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfMessageSize.setStatus("current")


class _VRtrRipIfMetricIn_Type(TmnxRipMetric):
    """Custom type vRtrRipIfMetricIn based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipIfMetricIn_Type.__name__ = "TmnxRipMetric"
_VRtrRipIfMetricIn_Object = MibTableColumn
vRtrRipIfMetricIn = _VRtrRipIfMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 6),
    _VRtrRipIfMetricIn_Type()
)
vRtrRipIfMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfMetricIn.setStatus("current")


class _VRtrRipIfMetricOut_Type(TmnxRipMetric):
    """Custom type vRtrRipIfMetricOut based on TmnxRipMetric"""
    defaultValue = 1


_VRtrRipIfMetricOut_Type.__name__ = "TmnxRipMetric"
_VRtrRipIfMetricOut_Object = MibTableColumn
vRtrRipIfMetricOut = _VRtrRipIfMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 7),
    _VRtrRipIfMetricOut_Type()
)
vRtrRipIfMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfMetricOut.setStatus("current")


class _VRtrRipIfPreference_Type(TmnxRipPreference):
    """Custom type vRtrRipIfPreference based on TmnxRipPreference"""
    defaultValue = 100


_VRtrRipIfPreference_Type.__name__ = "TmnxRipPreference"
_VRtrRipIfPreference_Object = MibTableColumn
vRtrRipIfPreference = _VRtrRipIfPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 8),
    _VRtrRipIfPreference_Type()
)
vRtrRipIfPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfPreference.setStatus("current")


class _VRtrRipIfReceive_Type(TmnxRipReceive):
    """Custom type vRtrRipIfReceive based on TmnxRipReceive"""
    defaultValue = 3


_VRtrRipIfReceive_Type.__name__ = "TmnxRipReceive"
_VRtrRipIfReceive_Object = MibTableColumn
vRtrRipIfReceive = _VRtrRipIfReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 9),
    _VRtrRipIfReceive_Type()
)
vRtrRipIfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfReceive.setStatus("current")


class _VRtrRipIfSend_Type(TmnxRipSend):
    """Custom type vRtrRipIfSend based on TmnxRipSend"""
    defaultValue = 3


_VRtrRipIfSend_Type.__name__ = "TmnxRipSend"
_VRtrRipIfSend_Object = MibTableColumn
vRtrRipIfSend = _VRtrRipIfSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 10),
    _VRtrRipIfSend_Type()
)
vRtrRipIfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfSend.setStatus("current")


class _VRtrRipIfSplitHorizon_Type(TruthValue):
    """Custom type vRtrRipIfSplitHorizon based on TruthValue"""
    defaultValue = 1


_VRtrRipIfSplitHorizon_Type.__name__ = "TruthValue"
_VRtrRipIfSplitHorizon_Object = MibTableColumn
vRtrRipIfSplitHorizon = _VRtrRipIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 11),
    _VRtrRipIfSplitHorizon_Type()
)
vRtrRipIfSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfSplitHorizon.setStatus("current")


class _VRtrRipIfTimerFlush_Type(TmnxRipTimerFlush):
    """Custom type vRtrRipIfTimerFlush based on TmnxRipTimerFlush"""
    defaultValue = 120


_VRtrRipIfTimerFlush_Type.__name__ = "TmnxRipTimerFlush"
_VRtrRipIfTimerFlush_Object = MibTableColumn
vRtrRipIfTimerFlush = _VRtrRipIfTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 12),
    _VRtrRipIfTimerFlush_Type()
)
vRtrRipIfTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipIfTimerFlush.setUnits("seconds")


class _VRtrRipIfTimerTimeout_Type(TmnxRipTimerTimeout):
    """Custom type vRtrRipIfTimerTimeout based on TmnxRipTimerTimeout"""
    defaultValue = 180


_VRtrRipIfTimerTimeout_Type.__name__ = "TmnxRipTimerTimeout"
_VRtrRipIfTimerTimeout_Object = MibTableColumn
vRtrRipIfTimerTimeout = _VRtrRipIfTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 13),
    _VRtrRipIfTimerTimeout_Type()
)
vRtrRipIfTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipIfTimerTimeout.setUnits("seconds")


class _VRtrRipIfTimerUpdate_Type(TmnxRipTimerUpdate):
    """Custom type vRtrRipIfTimerUpdate based on TmnxRipTimerUpdate"""
    defaultValue = 30


_VRtrRipIfTimerUpdate_Type.__name__ = "TmnxRipTimerUpdate"
_VRtrRipIfTimerUpdate_Object = MibTableColumn
vRtrRipIfTimerUpdate = _VRtrRipIfTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 14),
    _VRtrRipIfTimerUpdate_Type()
)
vRtrRipIfTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRipIfTimerUpdate.setUnits("seconds")


class _VRtrRipIfImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfImportPolicy1_Object = MibTableColumn
vRtrRipIfImportPolicy1 = _VRtrRipIfImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 15),
    _VRtrRipIfImportPolicy1_Type()
)
vRtrRipIfImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfImportPolicy1.setStatus("current")


class _VRtrRipIfImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfImportPolicy2_Object = MibTableColumn
vRtrRipIfImportPolicy2 = _VRtrRipIfImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 16),
    _VRtrRipIfImportPolicy2_Type()
)
vRtrRipIfImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfImportPolicy2.setStatus("current")


class _VRtrRipIfImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfImportPolicy3_Object = MibTableColumn
vRtrRipIfImportPolicy3 = _VRtrRipIfImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 17),
    _VRtrRipIfImportPolicy3_Type()
)
vRtrRipIfImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfImportPolicy3.setStatus("current")


class _VRtrRipIfImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfImportPolicy4_Object = MibTableColumn
vRtrRipIfImportPolicy4 = _VRtrRipIfImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 18),
    _VRtrRipIfImportPolicy4_Type()
)
vRtrRipIfImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfImportPolicy4.setStatus("current")


class _VRtrRipIfImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfImportPolicy5_Object = MibTableColumn
vRtrRipIfImportPolicy5 = _VRtrRipIfImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 19),
    _VRtrRipIfImportPolicy5_Type()
)
vRtrRipIfImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfImportPolicy5.setStatus("current")


class _VRtrRipIfExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfExportPolicy1_Object = MibTableColumn
vRtrRipIfExportPolicy1 = _VRtrRipIfExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 20),
    _VRtrRipIfExportPolicy1_Type()
)
vRtrRipIfExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfExportPolicy1.setStatus("current")


class _VRtrRipIfExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfExportPolicy2_Object = MibTableColumn
vRtrRipIfExportPolicy2 = _VRtrRipIfExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 21),
    _VRtrRipIfExportPolicy2_Type()
)
vRtrRipIfExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfExportPolicy2.setStatus("current")


class _VRtrRipIfExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfExportPolicy3_Object = MibTableColumn
vRtrRipIfExportPolicy3 = _VRtrRipIfExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 22),
    _VRtrRipIfExportPolicy3_Type()
)
vRtrRipIfExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfExportPolicy3.setStatus("current")


class _VRtrRipIfExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfExportPolicy4_Object = MibTableColumn
vRtrRipIfExportPolicy4 = _VRtrRipIfExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 23),
    _VRtrRipIfExportPolicy4_Type()
)
vRtrRipIfExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfExportPolicy4.setStatus("current")


class _VRtrRipIfExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrRipIfExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrRipIfExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrRipIfExportPolicy5_Object = MibTableColumn
vRtrRipIfExportPolicy5 = _VRtrRipIfExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 24),
    _VRtrRipIfExportPolicy5_Type()
)
vRtrRipIfExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfExportPolicy5.setStatus("current")


class _VRtrRipIfDescription_Type(TItemDescription):
    """Custom type vRtrRipIfDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrRipIfDescription_Type.__name__ = "TItemDescription"
_VRtrRipIfDescription_Object = MibTableColumn
vRtrRipIfDescription = _VRtrRipIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 25),
    _VRtrRipIfDescription_Type()
)
vRtrRipIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfDescription.setStatus("current")


class _VRtrRipIfInheritance_Type(Unsigned32):
    """Custom type vRtrRipIfInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrRipIfInheritance_Type.__name__ = "Unsigned32"
_VRtrRipIfInheritance_Object = MibTableColumn
vRtrRipIfInheritance = _VRtrRipIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 26),
    _VRtrRipIfInheritance_Type()
)
vRtrRipIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfInheritance.setStatus("current")


class _VRtrRipIfAdminStatus_Type(TmnxAdminState):
    """Custom type vRtrRipIfAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_VRtrRipIfAdminStatus_Type.__name__ = "TmnxAdminState"
_VRtrRipIfAdminStatus_Object = MibTableColumn
vRtrRipIfAdminStatus = _VRtrRipIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 27),
    _VRtrRipIfAdminStatus_Type()
)
vRtrRipIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfAdminStatus.setStatus("current")


class _VRtrRipIfOperStatus_Type(TmnxOperState):
    """Custom type vRtrRipIfOperStatus based on TmnxOperState"""
    defaultValue = 2


_VRtrRipIfOperStatus_Type.__name__ = "TmnxOperState"
_VRtrRipIfOperStatus_Object = MibTableColumn
vRtrRipIfOperStatus = _VRtrRipIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 28),
    _VRtrRipIfOperStatus_Type()
)
vRtrRipIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfOperStatus.setStatus("current")
_VRtrRipIfRowStatus_Type = RowStatus
_VRtrRipIfRowStatus_Object = MibTableColumn
vRtrRipIfRowStatus = _VRtrRipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 4, 1, 29),
    _VRtrRipIfRowStatus_Type()
)
vRtrRipIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipIfRowStatus.setStatus("current")
_VRtrRipRouteTable_Object = MibTable
vRtrRipRouteTable = _VRtrRipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    vRtrRipRouteTable.setStatus("current")
_VRtrRipRouteEntry_Object = MibTableRow
vRtrRipRouteEntry = _VRtrRipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1)
)
vRtrRipRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipRouteDest"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipRouteMask"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipRouteIfIndex"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipRoutePeerAddr"),
)
if mibBuilder.loadTexts:
    vRtrRipRouteEntry.setStatus("current")
_VRtrRipRouteDest_Type = IpAddress
_VRtrRipRouteDest_Object = MibTableColumn
vRtrRipRouteDest = _VRtrRipRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 1),
    _VRtrRipRouteDest_Type()
)
vRtrRipRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipRouteDest.setStatus("current")
_VRtrRipRouteMask_Type = IpAddress
_VRtrRipRouteMask_Object = MibTableColumn
vRtrRipRouteMask = _VRtrRipRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 2),
    _VRtrRipRouteMask_Type()
)
vRtrRipRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipRouteMask.setStatus("current")
_VRtrRipRouteIfIndex_Type = InterfaceIndex
_VRtrRipRouteIfIndex_Object = MibTableColumn
vRtrRipRouteIfIndex = _VRtrRipRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 3),
    _VRtrRipRouteIfIndex_Type()
)
vRtrRipRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipRouteIfIndex.setStatus("current")
_VRtrRipRoutePeerAddr_Type = IpAddress
_VRtrRipRoutePeerAddr_Object = MibTableColumn
vRtrRipRoutePeerAddr = _VRtrRipRoutePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 4),
    _VRtrRipRoutePeerAddr_Type()
)
vRtrRipRoutePeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipRoutePeerAddr.setStatus("current")
_VRtrRipRouteNextHop_Type = IpAddress
_VRtrRipRouteNextHop_Object = MibTableColumn
vRtrRipRouteNextHop = _VRtrRipRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 5),
    _VRtrRipRouteNextHop_Type()
)
vRtrRipRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteNextHop.setStatus("current")
_VRtrRipRouteMetric_Type = TmnxRipMetric
_VRtrRipRouteMetric_Object = MibTableColumn
vRtrRipRouteMetric = _VRtrRipRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 6),
    _VRtrRipRouteMetric_Type()
)
vRtrRipRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteMetric.setStatus("current")
_VRtrRipRouteTag_Type = RouteTag
_VRtrRipRouteTag_Object = MibTableColumn
vRtrRipRouteTag = _VRtrRipRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 7),
    _VRtrRipRouteTag_Type()
)
vRtrRipRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteTag.setStatus("current")


class _VRtrRipRouteStatus_Type(Integer32):
    """Custom type vRtrRipRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VRtrRipRouteStatus_Type.__name__ = "Integer32"
_VRtrRipRouteStatus_Object = MibTableColumn
vRtrRipRouteStatus = _VRtrRipRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 8),
    _VRtrRipRouteStatus_Type()
)
vRtrRipRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteStatus.setStatus("current")
_VRtrRipRouteTimerRemaining_Type = Unsigned32
_VRtrRipRouteTimerRemaining_Object = MibTableColumn
vRtrRipRouteTimerRemaining = _VRtrRipRouteTimerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 9),
    _VRtrRipRouteTimerRemaining_Type()
)
vRtrRipRouteTimerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteTimerRemaining.setStatus("current")
_VRtrRipRouteFC_Type = TNamedItemOrEmpty
_VRtrRipRouteFC_Object = MibTableColumn
vRtrRipRouteFC = _VRtrRipRouteFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 10),
    _VRtrRipRouteFC_Type()
)
vRtrRipRouteFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteFC.setStatus("current")
_VRtrRipRouteFCPriority_Type = TPriorityOrUndefined
_VRtrRipRouteFCPriority_Object = MibTableColumn
vRtrRipRouteFCPriority = _VRtrRipRouteFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 5, 1, 11),
    _VRtrRipRouteFCPriority_Type()
)
vRtrRipRouteFCPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipRouteFCPriority.setStatus("current")
_VRtrRipIfStatTable_Object = MibTable
vRtrRipIfStatTable = _VRtrRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    vRtrRipIfStatTable.setStatus("current")
_VRtrRipIfStatEntry_Object = MibTableRow
vRtrRipIfStatEntry = _VRtrRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1)
)
vRtrRipIfStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrRipIfStatEntry.setStatus("current")
_VRtrRipIfStatAllSentUpdates_Type = Counter32
_VRtrRipIfStatAllSentUpdates_Object = MibTableColumn
vRtrRipIfStatAllSentUpdates = _VRtrRipIfStatAllSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 1),
    _VRtrRipIfStatAllSentUpdates_Type()
)
vRtrRipIfStatAllSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllSentUpdates.setStatus("current")
_VRtrRipIfStatAllTriggeredUpdates_Type = Counter32
_VRtrRipIfStatAllTriggeredUpdates_Object = MibTableColumn
vRtrRipIfStatAllTriggeredUpdates = _VRtrRipIfStatAllTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 2),
    _VRtrRipIfStatAllTriggeredUpdates_Type()
)
vRtrRipIfStatAllTriggeredUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllTriggeredUpdates.setStatus("current")
_VRtrRipIfStatAllRcvBadPackets_Type = Counter32
_VRtrRipIfStatAllRcvBadPackets_Object = MibTableColumn
vRtrRipIfStatAllRcvBadPackets = _VRtrRipIfStatAllRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 3),
    _VRtrRipIfStatAllRcvBadPackets_Type()
)
vRtrRipIfStatAllRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllRcvBadPackets.setStatus("current")
_VRtrRipIfStatV1RcvUpdates_Type = Counter32
_VRtrRipIfStatV1RcvUpdates_Object = MibTableColumn
vRtrRipIfStatV1RcvUpdates = _VRtrRipIfStatV1RcvUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 4),
    _VRtrRipIfStatV1RcvUpdates_Type()
)
vRtrRipIfStatV1RcvUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvUpdates.setStatus("current")
_VRtrRipIfStatV1RcvRequests_Type = Counter32
_VRtrRipIfStatV1RcvRequests_Object = MibTableColumn
vRtrRipIfStatV1RcvRequests = _VRtrRipIfStatV1RcvRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 5),
    _VRtrRipIfStatV1RcvRequests_Type()
)
vRtrRipIfStatV1RcvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvRequests.setStatus("current")
_VRtrRipIfStatV1BadUpdates_Type = Counter32
_VRtrRipIfStatV1BadUpdates_Object = MibTableColumn
vRtrRipIfStatV1BadUpdates = _VRtrRipIfStatV1BadUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 6),
    _VRtrRipIfStatV1BadUpdates_Type()
)
vRtrRipIfStatV1BadUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadUpdates.setStatus("current")
_VRtrRipIfStatV1BadRequests_Type = Counter32
_VRtrRipIfStatV1BadRequests_Object = MibTableColumn
vRtrRipIfStatV1BadRequests = _VRtrRipIfStatV1BadRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 7),
    _VRtrRipIfStatV1BadRequests_Type()
)
vRtrRipIfStatV1BadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRequests.setStatus("current")
_VRtrRipIfStatV1BadRoutes_Type = Counter32
_VRtrRipIfStatV1BadRoutes_Object = MibTableColumn
vRtrRipIfStatV1BadRoutes = _VRtrRipIfStatV1BadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 8),
    _VRtrRipIfStatV1BadRoutes_Type()
)
vRtrRipIfStatV1BadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRoutes.setStatus("current")
_VRtrRipIfStatV2RcvUpdates_Type = Counter32
_VRtrRipIfStatV2RcvUpdates_Object = MibTableColumn
vRtrRipIfStatV2RcvUpdates = _VRtrRipIfStatV2RcvUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 9),
    _VRtrRipIfStatV2RcvUpdates_Type()
)
vRtrRipIfStatV2RcvUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvUpdates.setStatus("current")
_VRtrRipIfStatV2RcvRequests_Type = Counter32
_VRtrRipIfStatV2RcvRequests_Object = MibTableColumn
vRtrRipIfStatV2RcvRequests = _VRtrRipIfStatV2RcvRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 10),
    _VRtrRipIfStatV2RcvRequests_Type()
)
vRtrRipIfStatV2RcvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvRequests.setStatus("current")
_VRtrRipIfStatV2BadUpdates_Type = Counter32
_VRtrRipIfStatV2BadUpdates_Object = MibTableColumn
vRtrRipIfStatV2BadUpdates = _VRtrRipIfStatV2BadUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 11),
    _VRtrRipIfStatV2BadUpdates_Type()
)
vRtrRipIfStatV2BadUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadUpdates.setStatus("current")
_VRtrRipIfStatV2BadRequests_Type = Counter32
_VRtrRipIfStatV2BadRequests_Object = MibTableColumn
vRtrRipIfStatV2BadRequests = _VRtrRipIfStatV2BadRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 12),
    _VRtrRipIfStatV2BadRequests_Type()
)
vRtrRipIfStatV2BadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRequests.setStatus("current")
_VRtrRipIfStatV2BadRoutes_Type = Counter32
_VRtrRipIfStatV2BadRoutes_Object = MibTableColumn
vRtrRipIfStatV2BadRoutes = _VRtrRipIfStatV2BadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 13),
    _VRtrRipIfStatV2BadRoutes_Type()
)
vRtrRipIfStatV2BadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRoutes.setStatus("current")
_VRtrRipIfStatAuthErrors_Type = Counter32
_VRtrRipIfStatAuthErrors_Object = MibTableColumn
vRtrRipIfStatAuthErrors = _VRtrRipIfStatAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 14),
    _VRtrRipIfStatAuthErrors_Type()
)
vRtrRipIfStatAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAuthErrors.setStatus("current")
_VRtrRipIfStatAllSentUpdates5Min_Type = Counter32
_VRtrRipIfStatAllSentUpdates5Min_Object = MibTableColumn
vRtrRipIfStatAllSentUpdates5Min = _VRtrRipIfStatAllSentUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 15),
    _VRtrRipIfStatAllSentUpdates5Min_Type()
)
vRtrRipIfStatAllSentUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllSentUpdates5Min.setStatus("current")
_VRtrRipIfStatAllTriggeredUpdates5Min_Type = Counter32
_VRtrRipIfStatAllTriggeredUpdates5Min_Object = MibTableColumn
vRtrRipIfStatAllTriggeredUpdates5Min = _VRtrRipIfStatAllTriggeredUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 16),
    _VRtrRipIfStatAllTriggeredUpdates5Min_Type()
)
vRtrRipIfStatAllTriggeredUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllTriggeredUpdates5Min.setStatus("current")
_VRtrRipIfStatAllRcvBadPackets5Min_Type = Counter32
_VRtrRipIfStatAllRcvBadPackets5Min_Object = MibTableColumn
vRtrRipIfStatAllRcvBadPackets5Min = _VRtrRipIfStatAllRcvBadPackets5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 17),
    _VRtrRipIfStatAllRcvBadPackets5Min_Type()
)
vRtrRipIfStatAllRcvBadPackets5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllRcvBadPackets5Min.setStatus("current")
_VRtrRipIfStatV1RcvUpdates5Min_Type = Counter32
_VRtrRipIfStatV1RcvUpdates5Min_Object = MibTableColumn
vRtrRipIfStatV1RcvUpdates5Min = _VRtrRipIfStatV1RcvUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 18),
    _VRtrRipIfStatV1RcvUpdates5Min_Type()
)
vRtrRipIfStatV1RcvUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvUpdates5Min.setStatus("current")
_VRtrRipIfStatV1RcvRequests5Min_Type = Counter32
_VRtrRipIfStatV1RcvRequests5Min_Object = MibTableColumn
vRtrRipIfStatV1RcvRequests5Min = _VRtrRipIfStatV1RcvRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 19),
    _VRtrRipIfStatV1RcvRequests5Min_Type()
)
vRtrRipIfStatV1RcvRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvRequests5Min.setStatus("current")
_VRtrRipIfStatV1BadUpdates5Min_Type = Counter32
_VRtrRipIfStatV1BadUpdates5Min_Object = MibTableColumn
vRtrRipIfStatV1BadUpdates5Min = _VRtrRipIfStatV1BadUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 20),
    _VRtrRipIfStatV1BadUpdates5Min_Type()
)
vRtrRipIfStatV1BadUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadUpdates5Min.setStatus("current")
_VRtrRipIfStatV1BadRequests5Min_Type = Counter32
_VRtrRipIfStatV1BadRequests5Min_Object = MibTableColumn
vRtrRipIfStatV1BadRequests5Min = _VRtrRipIfStatV1BadRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 21),
    _VRtrRipIfStatV1BadRequests5Min_Type()
)
vRtrRipIfStatV1BadRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRequests5Min.setStatus("current")
_VRtrRipIfStatV1BadRoutes5Min_Type = Counter32
_VRtrRipIfStatV1BadRoutes5Min_Object = MibTableColumn
vRtrRipIfStatV1BadRoutes5Min = _VRtrRipIfStatV1BadRoutes5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 22),
    _VRtrRipIfStatV1BadRoutes5Min_Type()
)
vRtrRipIfStatV1BadRoutes5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRoutes5Min.setStatus("current")
_VRtrRipIfStatV2RcvUpdates5Min_Type = Counter32
_VRtrRipIfStatV2RcvUpdates5Min_Object = MibTableColumn
vRtrRipIfStatV2RcvUpdates5Min = _VRtrRipIfStatV2RcvUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 23),
    _VRtrRipIfStatV2RcvUpdates5Min_Type()
)
vRtrRipIfStatV2RcvUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvUpdates5Min.setStatus("current")
_VRtrRipIfStatV2RcvRequests5Min_Type = Counter32
_VRtrRipIfStatV2RcvRequests5Min_Object = MibTableColumn
vRtrRipIfStatV2RcvRequests5Min = _VRtrRipIfStatV2RcvRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 24),
    _VRtrRipIfStatV2RcvRequests5Min_Type()
)
vRtrRipIfStatV2RcvRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvRequests5Min.setStatus("current")
_VRtrRipIfStatV2BadUpdates5Min_Type = Counter32
_VRtrRipIfStatV2BadUpdates5Min_Object = MibTableColumn
vRtrRipIfStatV2BadUpdates5Min = _VRtrRipIfStatV2BadUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 25),
    _VRtrRipIfStatV2BadUpdates5Min_Type()
)
vRtrRipIfStatV2BadUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadUpdates5Min.setStatus("current")
_VRtrRipIfStatV2BadRequests5Min_Type = Counter32
_VRtrRipIfStatV2BadRequests5Min_Object = MibTableColumn
vRtrRipIfStatV2BadRequests5Min = _VRtrRipIfStatV2BadRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 26),
    _VRtrRipIfStatV2BadRequests5Min_Type()
)
vRtrRipIfStatV2BadRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRequests5Min.setStatus("current")
_VRtrRipIfStatV2BadRoutes5Min_Type = Counter32
_VRtrRipIfStatV2BadRoutes5Min_Object = MibTableColumn
vRtrRipIfStatV2BadRoutes5Min = _VRtrRipIfStatV2BadRoutes5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 27),
    _VRtrRipIfStatV2BadRoutes5Min_Type()
)
vRtrRipIfStatV2BadRoutes5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRoutes5Min.setStatus("current")
_VRtrRipIfStatAuthErrors5Min_Type = Counter32
_VRtrRipIfStatAuthErrors5Min_Object = MibTableColumn
vRtrRipIfStatAuthErrors5Min = _VRtrRipIfStatAuthErrors5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 28),
    _VRtrRipIfStatAuthErrors5Min_Type()
)
vRtrRipIfStatAuthErrors5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAuthErrors5Min.setStatus("current")
_VRtrRipIfStatAllSentUpdates1Min_Type = Counter32
_VRtrRipIfStatAllSentUpdates1Min_Object = MibTableColumn
vRtrRipIfStatAllSentUpdates1Min = _VRtrRipIfStatAllSentUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 29),
    _VRtrRipIfStatAllSentUpdates1Min_Type()
)
vRtrRipIfStatAllSentUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllSentUpdates1Min.setStatus("current")
_VRtrRipIfStatAllTriggeredUpdates1Min_Type = Counter32
_VRtrRipIfStatAllTriggeredUpdates1Min_Object = MibTableColumn
vRtrRipIfStatAllTriggeredUpdates1Min = _VRtrRipIfStatAllTriggeredUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 30),
    _VRtrRipIfStatAllTriggeredUpdates1Min_Type()
)
vRtrRipIfStatAllTriggeredUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllTriggeredUpdates1Min.setStatus("current")
_VRtrRipIfStatAllRcvBadPackets1Min_Type = Counter32
_VRtrRipIfStatAllRcvBadPackets1Min_Object = MibTableColumn
vRtrRipIfStatAllRcvBadPackets1Min = _VRtrRipIfStatAllRcvBadPackets1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 31),
    _VRtrRipIfStatAllRcvBadPackets1Min_Type()
)
vRtrRipIfStatAllRcvBadPackets1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAllRcvBadPackets1Min.setStatus("current")
_VRtrRipIfStatV1RcvUpdates1Min_Type = Counter32
_VRtrRipIfStatV1RcvUpdates1Min_Object = MibTableColumn
vRtrRipIfStatV1RcvUpdates1Min = _VRtrRipIfStatV1RcvUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 32),
    _VRtrRipIfStatV1RcvUpdates1Min_Type()
)
vRtrRipIfStatV1RcvUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvUpdates1Min.setStatus("current")
_VRtrRipIfStatV1RcvRequests1Min_Type = Counter32
_VRtrRipIfStatV1RcvRequests1Min_Object = MibTableColumn
vRtrRipIfStatV1RcvRequests1Min = _VRtrRipIfStatV1RcvRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 33),
    _VRtrRipIfStatV1RcvRequests1Min_Type()
)
vRtrRipIfStatV1RcvRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1RcvRequests1Min.setStatus("current")
_VRtrRipIfStatV1BadUpdates1Min_Type = Counter32
_VRtrRipIfStatV1BadUpdates1Min_Object = MibTableColumn
vRtrRipIfStatV1BadUpdates1Min = _VRtrRipIfStatV1BadUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 34),
    _VRtrRipIfStatV1BadUpdates1Min_Type()
)
vRtrRipIfStatV1BadUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadUpdates1Min.setStatus("current")
_VRtrRipIfStatV1BadRequests1Min_Type = Counter32
_VRtrRipIfStatV1BadRequests1Min_Object = MibTableColumn
vRtrRipIfStatV1BadRequests1Min = _VRtrRipIfStatV1BadRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 35),
    _VRtrRipIfStatV1BadRequests1Min_Type()
)
vRtrRipIfStatV1BadRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRequests1Min.setStatus("current")
_VRtrRipIfStatV1BadRoutes1Min_Type = Counter32
_VRtrRipIfStatV1BadRoutes1Min_Object = MibTableColumn
vRtrRipIfStatV1BadRoutes1Min = _VRtrRipIfStatV1BadRoutes1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 36),
    _VRtrRipIfStatV1BadRoutes1Min_Type()
)
vRtrRipIfStatV1BadRoutes1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV1BadRoutes1Min.setStatus("current")
_VRtrRipIfStatV2RcvUpdates1Min_Type = Counter32
_VRtrRipIfStatV2RcvUpdates1Min_Object = MibTableColumn
vRtrRipIfStatV2RcvUpdates1Min = _VRtrRipIfStatV2RcvUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 37),
    _VRtrRipIfStatV2RcvUpdates1Min_Type()
)
vRtrRipIfStatV2RcvUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvUpdates1Min.setStatus("current")
_VRtrRipIfStatV2RcvRequests1Min_Type = Counter32
_VRtrRipIfStatV2RcvRequests1Min_Object = MibTableColumn
vRtrRipIfStatV2RcvRequests1Min = _VRtrRipIfStatV2RcvRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 38),
    _VRtrRipIfStatV2RcvRequests1Min_Type()
)
vRtrRipIfStatV2RcvRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2RcvRequests1Min.setStatus("current")
_VRtrRipIfStatV2BadUpdates1Min_Type = Counter32
_VRtrRipIfStatV2BadUpdates1Min_Object = MibTableColumn
vRtrRipIfStatV2BadUpdates1Min = _VRtrRipIfStatV2BadUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 39),
    _VRtrRipIfStatV2BadUpdates1Min_Type()
)
vRtrRipIfStatV2BadUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadUpdates1Min.setStatus("current")
_VRtrRipIfStatV2BadRequests1Min_Type = Counter32
_VRtrRipIfStatV2BadRequests1Min_Object = MibTableColumn
vRtrRipIfStatV2BadRequests1Min = _VRtrRipIfStatV2BadRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 40),
    _VRtrRipIfStatV2BadRequests1Min_Type()
)
vRtrRipIfStatV2BadRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRequests1Min.setStatus("current")
_VRtrRipIfStatV2BadRoutes1Min_Type = Counter32
_VRtrRipIfStatV2BadRoutes1Min_Object = MibTableColumn
vRtrRipIfStatV2BadRoutes1Min = _VRtrRipIfStatV2BadRoutes1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 41),
    _VRtrRipIfStatV2BadRoutes1Min_Type()
)
vRtrRipIfStatV2BadRoutes1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatV2BadRoutes1Min.setStatus("current")
_VRtrRipIfStatAuthErrors1Min_Type = Counter32
_VRtrRipIfStatAuthErrors1Min_Object = MibTableColumn
vRtrRipIfStatAuthErrors1Min = _VRtrRipIfStatAuthErrors1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 6, 1, 42),
    _VRtrRipIfStatAuthErrors1Min_Type()
)
vRtrRipIfStatAuthErrors1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipIfStatAuthErrors1Min.setStatus("current")
_VRtrRipPeerTable_Object = MibTable
vRtrRipPeerTable = _VRtrRipPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7)
)
if mibBuilder.loadTexts:
    vRtrRipPeerTable.setStatus("current")
_VRtrRipPeerEntry_Object = MibTableRow
vRtrRipPeerEntry = _VRtrRipPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1)
)
vRtrRipPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipPeerIfIndex"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrRipPeerEntry.setStatus("current")
_VRtrRipPeerIfIndex_Type = InterfaceIndex
_VRtrRipPeerIfIndex_Object = MibTableColumn
vRtrRipPeerIfIndex = _VRtrRipPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 1),
    _VRtrRipPeerIfIndex_Type()
)
vRtrRipPeerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipPeerIfIndex.setStatus("current")
_VRtrRipPeerAddress_Type = IpAddress
_VRtrRipPeerAddress_Object = MibTableColumn
vRtrRipPeerAddress = _VRtrRipPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 2),
    _VRtrRipPeerAddress_Type()
)
vRtrRipPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipPeerAddress.setStatus("current")
_VRtrRipPeerLastUpdate_Type = TimeStamp
_VRtrRipPeerLastUpdate_Object = MibTableColumn
vRtrRipPeerLastUpdate = _VRtrRipPeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 3),
    _VRtrRipPeerLastUpdate_Type()
)
vRtrRipPeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipPeerLastUpdate.setStatus("current")


class _VRtrRipPeerVersion_Type(Unsigned32):
    """Custom type vRtrRipPeerVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrRipPeerVersion_Type.__name__ = "Unsigned32"
_VRtrRipPeerVersion_Object = MibTableColumn
vRtrRipPeerVersion = _VRtrRipPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 4),
    _VRtrRipPeerVersion_Type()
)
vRtrRipPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipPeerVersion.setStatus("current")
_VRtrRipPeerRcvBadPackets_Type = Counter32
_VRtrRipPeerRcvBadPackets_Object = MibTableColumn
vRtrRipPeerRcvBadPackets = _VRtrRipPeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 5),
    _VRtrRipPeerRcvBadPackets_Type()
)
vRtrRipPeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipPeerRcvBadPackets.setStatus("current")
_VRtrRipPeerRcvBadRoutes_Type = Counter32
_VRtrRipPeerRcvBadRoutes_Object = MibTableColumn
vRtrRipPeerRcvBadRoutes = _VRtrRipPeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 7, 1, 6),
    _VRtrRipPeerRcvBadRoutes_Type()
)
vRtrRipPeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipPeerRcvBadRoutes.setStatus("current")
_VRtrRipAdvertisedRouteTable_Object = MibTable
vRtrRipAdvertisedRouteTable = _VRtrRipAdvertisedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8)
)
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteTable.setStatus("current")
_VRtrRipAdvertisedRouteEntry_Object = MibTableRow
vRtrRipAdvertisedRouteEntry = _VRtrRipAdvertisedRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1)
)
vRtrRipAdvertisedRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteDest"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteMask"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteIfIndex"),
    (0, "TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteIfAddr"),
)
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteEntry.setStatus("current")
_VRtrRipAdvertisedRouteDest_Type = IpAddress
_VRtrRipAdvertisedRouteDest_Object = MibTableColumn
vRtrRipAdvertisedRouteDest = _VRtrRipAdvertisedRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 1),
    _VRtrRipAdvertisedRouteDest_Type()
)
vRtrRipAdvertisedRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteDest.setStatus("current")
_VRtrRipAdvertisedRouteMask_Type = IpAddress
_VRtrRipAdvertisedRouteMask_Object = MibTableColumn
vRtrRipAdvertisedRouteMask = _VRtrRipAdvertisedRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 2),
    _VRtrRipAdvertisedRouteMask_Type()
)
vRtrRipAdvertisedRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteMask.setStatus("current")
_VRtrRipAdvertisedRouteIfIndex_Type = InterfaceIndex
_VRtrRipAdvertisedRouteIfIndex_Object = MibTableColumn
vRtrRipAdvertisedRouteIfIndex = _VRtrRipAdvertisedRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 3),
    _VRtrRipAdvertisedRouteIfIndex_Type()
)
vRtrRipAdvertisedRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteIfIndex.setStatus("current")
_VRtrRipAdvertisedRouteIfAddr_Type = IpAddress
_VRtrRipAdvertisedRouteIfAddr_Object = MibTableColumn
vRtrRipAdvertisedRouteIfAddr = _VRtrRipAdvertisedRouteIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 4),
    _VRtrRipAdvertisedRouteIfAddr_Type()
)
vRtrRipAdvertisedRouteIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteIfAddr.setStatus("current")
_VRtrRipAdvertisedRouteNextHop_Type = IpAddress
_VRtrRipAdvertisedRouteNextHop_Object = MibTableColumn
vRtrRipAdvertisedRouteNextHop = _VRtrRipAdvertisedRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 5),
    _VRtrRipAdvertisedRouteNextHop_Type()
)
vRtrRipAdvertisedRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteNextHop.setStatus("current")


class _VRtrRipAdvertisedRouteMetric_Type(Unsigned32):
    """Custom type vRtrRipAdvertisedRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VRtrRipAdvertisedRouteMetric_Type.__name__ = "Unsigned32"
_VRtrRipAdvertisedRouteMetric_Object = MibTableColumn
vRtrRipAdvertisedRouteMetric = _VRtrRipAdvertisedRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 6),
    _VRtrRipAdvertisedRouteMetric_Type()
)
vRtrRipAdvertisedRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteMetric.setStatus("current")
_VRtrRipAdvertisedRouteTag_Type = RouteTag
_VRtrRipAdvertisedRouteTag_Object = MibTableColumn
vRtrRipAdvertisedRouteTag = _VRtrRipAdvertisedRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 7),
    _VRtrRipAdvertisedRouteTag_Type()
)
vRtrRipAdvertisedRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteTag.setStatus("current")
_VRtrRipAdvertisedRouteTimerRemaining_Type = Integer32
_VRtrRipAdvertisedRouteTimerRemaining_Object = MibTableColumn
vRtrRipAdvertisedRouteTimerRemaining = _VRtrRipAdvertisedRouteTimerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 9, 8, 1, 8),
    _VRtrRipAdvertisedRouteTimerRemaining_Type()
)
vRtrRipAdvertisedRouteTimerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRipAdvertisedRouteTimerRemaining.setStatus("current")
_VRtrRipNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrRipNotifyPrefix = _VRtrRipNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9)
)
_VRtrRipNotifications_ObjectIdentity = ObjectIdentity
vRtrRipNotifications = _VRtrRipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0)
)

# Managed Objects groups

tmnxRipGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 1)
)
tmnxRipGlobalGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipGlobalLearnedRoutes"),
        ("TIMETRA-RIP-MIB", "vRtrRipGlobalTimedoutRoutes"),
        ("TIMETRA-RIP-MIB", "vRtrRipGlobalCurrentMemory"),
        ("TIMETRA-RIP-MIB", "vRtrRipGlobalMaximumMemory"))
)
if mibBuilder.loadTexts:
    tmnxRipGlobalGroup.setStatus("current")

tmnxRipInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 2)
)
tmnxRipInstanceGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipInstanceAuthType"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceAuthKey"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceCheckZero"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceMessageSize"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceMetricIn"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceMetricOut"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstancePreference"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceReceive"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceSend"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceSplitHorizon"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceTimerFlush"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceTimerTimeout"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceTimerUpdate"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceImportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceImportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceImportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceImportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceImportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceDescription"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceAdminStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxRipInstanceGroup.setStatus("current")

tmnxRipGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 3)
)
tmnxRipGroupGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipGroupAuthType"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupAuthKey"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupCheckZero"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupMessageSize"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupMetricIn"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupMetricOut"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupPreference"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupReceive"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupSend"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupSplitHorizon"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupTimerFlush"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupTimerTimeout"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupTimerUpdate"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupImportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupImportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupImportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupImportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupImportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupExportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupExportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupExportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupExportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupExportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupDescription"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupInheritance"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupAdminStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupOperStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipGroupRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRipGroupGroup.setStatus("current")

tmnxRipInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 4)
)
tmnxRipInterfaceGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipIfGroupName"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfAuthType"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfAuthKey"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfCheckZero"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfMessageSize"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfMetricIn"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfMetricOut"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfPreference"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfReceive"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfSend"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfSplitHorizon"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfTimerFlush"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfTimerTimeout"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfTimerUpdate"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfImportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfImportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfImportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfImportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfImportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfExportPolicy1"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfExportPolicy2"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfExportPolicy3"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfExportPolicy4"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfExportPolicy5"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfDescription"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfInheritance"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfAdminStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfOperStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfRowStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllSentUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllTriggeredUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllRcvBadPackets"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvRequests"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRequests"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRoutes"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvRequests"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadUpdates"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRequests"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRoutes"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAuthErrors"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllSentUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllTriggeredUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllRcvBadPackets5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvRequests5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRequests5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRoutes5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvRequests5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadUpdates5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRequests5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRoutes5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAuthErrors5Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllSentUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllTriggeredUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAllRcvBadPackets1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1RcvRequests1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRequests1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV1BadRoutes1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2RcvRequests1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadUpdates1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRequests1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatV2BadRoutes1Min"),
        ("TIMETRA-RIP-MIB", "vRtrRipIfStatAuthErrors1Min"))
)
if mibBuilder.loadTexts:
    tmnxRipInterfaceGroup.setStatus("current")

tmnxRipRoutesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 5)
)
tmnxRipRoutesGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipRouteNextHop"),
        ("TIMETRA-RIP-MIB", "vRtrRipRouteMetric"),
        ("TIMETRA-RIP-MIB", "vRtrRipRouteTag"),
        ("TIMETRA-RIP-MIB", "vRtrRipRouteStatus"),
        ("TIMETRA-RIP-MIB", "vRtrRipRouteTimerRemaining"),
        ("TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteNextHop"),
        ("TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteMetric"),
        ("TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteTag"),
        ("TIMETRA-RIP-MIB", "vRtrRipAdvertisedRouteTimerRemaining"))
)
if mibBuilder.loadTexts:
    tmnxRipRoutesGroup.setStatus("current")

tmnxRipPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 6)
)
tmnxRipPeerGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipPeerLastUpdate"),
        ("TIMETRA-RIP-MIB", "vRtrRipPeerVersion"),
        ("TIMETRA-RIP-MIB", "vRtrRipPeerRcvBadPackets"),
        ("TIMETRA-RIP-MIB", "vRtrRipPeerRcvBadRoutes"))
)
if mibBuilder.loadTexts:
    tmnxRipPeerGroup.setStatus("current")

tmnxRipV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 9)
)
tmnxRipV6v1Group.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipInstancePropagateMetric")
)
if mibBuilder.loadTexts:
    tmnxRipV6v1Group.setStatus("current")

tmnxRipV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 10)
)
tmnxRipV7v0Group.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipInstanceExportLimit"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExpLmtLogPercent"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceTotalExpRoutes"))
)
if mibBuilder.loadTexts:
    tmnxRipV7v0Group.setStatus("current")

tmnxRipRoutesV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 12)
)
tmnxRipRoutesV9v0R4Group.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipRouteFC"),
        ("TIMETRA-RIP-MIB", "vRtrRipRouteFCPriority"))
)
if mibBuilder.loadTexts:
    tmnxRipRoutesV9v0R4Group.setStatus("current")


# Notification objects

vRtrRipAuthTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 1)
)
vRtrRipAuthTypeMismatch.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipPeerLastUpdate")
)
if mibBuilder.loadTexts:
    vRtrRipAuthTypeMismatch.setStatus(
        "current"
    )

vRtrRipAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 2)
)
vRtrRipAuthFailure.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipPeerLastUpdate")
)
if mibBuilder.loadTexts:
    vRtrRipAuthFailure.setStatus(
        "current"
    )

vRtrRipInstanceShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 3)
)
vRtrRipInstanceShuttingDown.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipInstanceOperStatus")
)
if mibBuilder.loadTexts:
    vRtrRipInstanceShuttingDown.setStatus(
        "current"
    )

vRtrRipInstanceRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 4)
)
vRtrRipInstanceRestarted.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipInstanceOperStatus")
)
if mibBuilder.loadTexts:
    vRtrRipInstanceRestarted.setStatus(
        "current"
    )

vRtrRipInstanceExpLmtReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 5)
)
vRtrRipInstanceExpLmtReached.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportLimit")
)
if mibBuilder.loadTexts:
    vRtrRipInstanceExpLmtReached.setStatus(
        "current"
    )

vRtrRipInstanceExpLmtWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 6)
)
vRtrRipInstanceExpLmtWarning.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipInstanceExportLimit"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExpLmtLogPercent"))
)
if mibBuilder.loadTexts:
    vRtrRipInstanceExpLmtWarning.setStatus(
        "current"
    )

vRtrRipInstanceRtsExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 9, 0, 7)
)
vRtrRipInstanceRtsExpLmtDropped.setObjects(
    ("TIMETRA-RIP-MIB", "vRtrRipInstanceExportLimit")
)
if mibBuilder.loadTexts:
    vRtrRipInstanceRtsExpLmtDropped.setStatus(
        "current"
    )


# Notifications groups

tmnxRipNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 8)
)
tmnxRipNotificationGroup.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipAuthTypeMismatch"),
        ("TIMETRA-RIP-MIB", "vRtrRipAuthFailure"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceShuttingDown"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceRestarted"))
)
if mibBuilder.loadTexts:
    tmnxRipNotificationGroup.setStatus(
        "current"
    )

tmnxRipNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 2, 11)
)
tmnxRipNotificationV7v0Group.setObjects(
      *(("TIMETRA-RIP-MIB", "vRtrRipInstanceExpLmtReached"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceExpLmtWarning"),
        ("TIMETRA-RIP-MIB", "vRtrRipInstanceRtsExpLmtDropped"))
)
if mibBuilder.loadTexts:
    tmnxRipNotificationV7v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxRipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 9, 1, 1)
)
tmnxRipCompliance.setObjects(
      *(("TIMETRA-RIP-MIB", "tmnxRipGlobalGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipInstanceGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipGroupGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipInterfaceGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipRoutesGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipPeerGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipNotificationGroup"),
        ("TIMETRA-RIP-MIB", "tmnxRipV6v1Group"),
        ("TIMETRA-RIP-MIB", "tmnxRipV7v0Group"),
        ("TIMETRA-RIP-MIB", "tmnxRipNotificationV7v0Group"),
        ("TIMETRA-RIP-MIB", "tmnxRipRoutesV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxRipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-RIP-MIB",
    **{"TmnxRipAuthType": TmnxRipAuthType,
       "TmnxRipAuthKey": TmnxRipAuthKey,
       "TmnxRipMessageSize": TmnxRipMessageSize,
       "TmnxRipMetric": TmnxRipMetric,
       "TmnxRipPreference": TmnxRipPreference,
       "TmnxRipReceive": TmnxRipReceive,
       "TmnxRipSend": TmnxRipSend,
       "TmnxRipTimerFlush": TmnxRipTimerFlush,
       "TmnxRipTimerTimeout": TmnxRipTimerTimeout,
       "TmnxRipTimerUpdate": TmnxRipTimerUpdate,
       "timetraRipMIBModule": timetraRipMIBModule,
       "tmnxRipConformance": tmnxRipConformance,
       "tmnxRipCompliances": tmnxRipCompliances,
       "tmnxRipCompliance": tmnxRipCompliance,
       "tmnxRipGroups": tmnxRipGroups,
       "tmnxRipGlobalGroup": tmnxRipGlobalGroup,
       "tmnxRipInstanceGroup": tmnxRipInstanceGroup,
       "tmnxRipGroupGroup": tmnxRipGroupGroup,
       "tmnxRipInterfaceGroup": tmnxRipInterfaceGroup,
       "tmnxRipRoutesGroup": tmnxRipRoutesGroup,
       "tmnxRipPeerGroup": tmnxRipPeerGroup,
       "tmnxRipNotificationGroup": tmnxRipNotificationGroup,
       "tmnxRipV6v1Group": tmnxRipV6v1Group,
       "tmnxRipV7v0Group": tmnxRipV7v0Group,
       "tmnxRipNotificationV7v0Group": tmnxRipNotificationV7v0Group,
       "tmnxRipRoutesV9v0R4Group": tmnxRipRoutesV9v0R4Group,
       "vRtrRipObjs": vRtrRipObjs,
       "vRtrRipGlobals": vRtrRipGlobals,
       "vRtrRipGlobalLearnedRoutes": vRtrRipGlobalLearnedRoutes,
       "vRtrRipGlobalTimedoutRoutes": vRtrRipGlobalTimedoutRoutes,
       "vRtrRipGlobalCurrentMemory": vRtrRipGlobalCurrentMemory,
       "vRtrRipGlobalMaximumMemory": vRtrRipGlobalMaximumMemory,
       "vRtrRipInstanceTable": vRtrRipInstanceTable,
       "vRtrRipInstanceEntry": vRtrRipInstanceEntry,
       "vRtrRipInstanceAuthType": vRtrRipInstanceAuthType,
       "vRtrRipInstanceAuthKey": vRtrRipInstanceAuthKey,
       "vRtrRipInstanceCheckZero": vRtrRipInstanceCheckZero,
       "vRtrRipInstanceMessageSize": vRtrRipInstanceMessageSize,
       "vRtrRipInstanceMetricIn": vRtrRipInstanceMetricIn,
       "vRtrRipInstanceMetricOut": vRtrRipInstanceMetricOut,
       "vRtrRipInstancePreference": vRtrRipInstancePreference,
       "vRtrRipInstanceReceive": vRtrRipInstanceReceive,
       "vRtrRipInstanceSend": vRtrRipInstanceSend,
       "vRtrRipInstanceSplitHorizon": vRtrRipInstanceSplitHorizon,
       "vRtrRipInstanceTimerFlush": vRtrRipInstanceTimerFlush,
       "vRtrRipInstanceTimerTimeout": vRtrRipInstanceTimerTimeout,
       "vRtrRipInstanceTimerUpdate": vRtrRipInstanceTimerUpdate,
       "vRtrRipInstanceImportPolicy1": vRtrRipInstanceImportPolicy1,
       "vRtrRipInstanceImportPolicy2": vRtrRipInstanceImportPolicy2,
       "vRtrRipInstanceImportPolicy3": vRtrRipInstanceImportPolicy3,
       "vRtrRipInstanceImportPolicy4": vRtrRipInstanceImportPolicy4,
       "vRtrRipInstanceImportPolicy5": vRtrRipInstanceImportPolicy5,
       "vRtrRipInstanceExportPolicy1": vRtrRipInstanceExportPolicy1,
       "vRtrRipInstanceExportPolicy2": vRtrRipInstanceExportPolicy2,
       "vRtrRipInstanceExportPolicy3": vRtrRipInstanceExportPolicy3,
       "vRtrRipInstanceExportPolicy4": vRtrRipInstanceExportPolicy4,
       "vRtrRipInstanceExportPolicy5": vRtrRipInstanceExportPolicy5,
       "vRtrRipInstanceDescription": vRtrRipInstanceDescription,
       "vRtrRipInstanceAdminStatus": vRtrRipInstanceAdminStatus,
       "vRtrRipInstanceOperStatus": vRtrRipInstanceOperStatus,
       "vRtrRipInstancePropagateMetric": vRtrRipInstancePropagateMetric,
       "vRtrRipInstanceExportLimit": vRtrRipInstanceExportLimit,
       "vRtrRipInstanceExpLmtLogPercent": vRtrRipInstanceExpLmtLogPercent,
       "vRtrRipInstanceTotalExpRoutes": vRtrRipInstanceTotalExpRoutes,
       "vRtrRipGroupTable": vRtrRipGroupTable,
       "vRtrRipGroupEntry": vRtrRipGroupEntry,
       "vRtrRipGroupName": vRtrRipGroupName,
       "vRtrRipGroupAuthType": vRtrRipGroupAuthType,
       "vRtrRipGroupAuthKey": vRtrRipGroupAuthKey,
       "vRtrRipGroupCheckZero": vRtrRipGroupCheckZero,
       "vRtrRipGroupMessageSize": vRtrRipGroupMessageSize,
       "vRtrRipGroupMetricIn": vRtrRipGroupMetricIn,
       "vRtrRipGroupMetricOut": vRtrRipGroupMetricOut,
       "vRtrRipGroupPreference": vRtrRipGroupPreference,
       "vRtrRipGroupReceive": vRtrRipGroupReceive,
       "vRtrRipGroupSend": vRtrRipGroupSend,
       "vRtrRipGroupSplitHorizon": vRtrRipGroupSplitHorizon,
       "vRtrRipGroupTimerFlush": vRtrRipGroupTimerFlush,
       "vRtrRipGroupTimerTimeout": vRtrRipGroupTimerTimeout,
       "vRtrRipGroupTimerUpdate": vRtrRipGroupTimerUpdate,
       "vRtrRipGroupImportPolicy1": vRtrRipGroupImportPolicy1,
       "vRtrRipGroupImportPolicy2": vRtrRipGroupImportPolicy2,
       "vRtrRipGroupImportPolicy3": vRtrRipGroupImportPolicy3,
       "vRtrRipGroupImportPolicy4": vRtrRipGroupImportPolicy4,
       "vRtrRipGroupImportPolicy5": vRtrRipGroupImportPolicy5,
       "vRtrRipGroupExportPolicy1": vRtrRipGroupExportPolicy1,
       "vRtrRipGroupExportPolicy2": vRtrRipGroupExportPolicy2,
       "vRtrRipGroupExportPolicy3": vRtrRipGroupExportPolicy3,
       "vRtrRipGroupExportPolicy4": vRtrRipGroupExportPolicy4,
       "vRtrRipGroupExportPolicy5": vRtrRipGroupExportPolicy5,
       "vRtrRipGroupDescription": vRtrRipGroupDescription,
       "vRtrRipGroupInheritance": vRtrRipGroupInheritance,
       "vRtrRipGroupAdminStatus": vRtrRipGroupAdminStatus,
       "vRtrRipGroupOperStatus": vRtrRipGroupOperStatus,
       "vRtrRipGroupRowStatus": vRtrRipGroupRowStatus,
       "vRtrRipIfTable": vRtrRipIfTable,
       "vRtrRipIfEntry": vRtrRipIfEntry,
       "vRtrRipIfGroupName": vRtrRipIfGroupName,
       "vRtrRipIfAuthType": vRtrRipIfAuthType,
       "vRtrRipIfAuthKey": vRtrRipIfAuthKey,
       "vRtrRipIfCheckZero": vRtrRipIfCheckZero,
       "vRtrRipIfMessageSize": vRtrRipIfMessageSize,
       "vRtrRipIfMetricIn": vRtrRipIfMetricIn,
       "vRtrRipIfMetricOut": vRtrRipIfMetricOut,
       "vRtrRipIfPreference": vRtrRipIfPreference,
       "vRtrRipIfReceive": vRtrRipIfReceive,
       "vRtrRipIfSend": vRtrRipIfSend,
       "vRtrRipIfSplitHorizon": vRtrRipIfSplitHorizon,
       "vRtrRipIfTimerFlush": vRtrRipIfTimerFlush,
       "vRtrRipIfTimerTimeout": vRtrRipIfTimerTimeout,
       "vRtrRipIfTimerUpdate": vRtrRipIfTimerUpdate,
       "vRtrRipIfImportPolicy1": vRtrRipIfImportPolicy1,
       "vRtrRipIfImportPolicy2": vRtrRipIfImportPolicy2,
       "vRtrRipIfImportPolicy3": vRtrRipIfImportPolicy3,
       "vRtrRipIfImportPolicy4": vRtrRipIfImportPolicy4,
       "vRtrRipIfImportPolicy5": vRtrRipIfImportPolicy5,
       "vRtrRipIfExportPolicy1": vRtrRipIfExportPolicy1,
       "vRtrRipIfExportPolicy2": vRtrRipIfExportPolicy2,
       "vRtrRipIfExportPolicy3": vRtrRipIfExportPolicy3,
       "vRtrRipIfExportPolicy4": vRtrRipIfExportPolicy4,
       "vRtrRipIfExportPolicy5": vRtrRipIfExportPolicy5,
       "vRtrRipIfDescription": vRtrRipIfDescription,
       "vRtrRipIfInheritance": vRtrRipIfInheritance,
       "vRtrRipIfAdminStatus": vRtrRipIfAdminStatus,
       "vRtrRipIfOperStatus": vRtrRipIfOperStatus,
       "vRtrRipIfRowStatus": vRtrRipIfRowStatus,
       "vRtrRipRouteTable": vRtrRipRouteTable,
       "vRtrRipRouteEntry": vRtrRipRouteEntry,
       "vRtrRipRouteDest": vRtrRipRouteDest,
       "vRtrRipRouteMask": vRtrRipRouteMask,
       "vRtrRipRouteIfIndex": vRtrRipRouteIfIndex,
       "vRtrRipRoutePeerAddr": vRtrRipRoutePeerAddr,
       "vRtrRipRouteNextHop": vRtrRipRouteNextHop,
       "vRtrRipRouteMetric": vRtrRipRouteMetric,
       "vRtrRipRouteTag": vRtrRipRouteTag,
       "vRtrRipRouteStatus": vRtrRipRouteStatus,
       "vRtrRipRouteTimerRemaining": vRtrRipRouteTimerRemaining,
       "vRtrRipRouteFC": vRtrRipRouteFC,
       "vRtrRipRouteFCPriority": vRtrRipRouteFCPriority,
       "vRtrRipIfStatTable": vRtrRipIfStatTable,
       "vRtrRipIfStatEntry": vRtrRipIfStatEntry,
       "vRtrRipIfStatAllSentUpdates": vRtrRipIfStatAllSentUpdates,
       "vRtrRipIfStatAllTriggeredUpdates": vRtrRipIfStatAllTriggeredUpdates,
       "vRtrRipIfStatAllRcvBadPackets": vRtrRipIfStatAllRcvBadPackets,
       "vRtrRipIfStatV1RcvUpdates": vRtrRipIfStatV1RcvUpdates,
       "vRtrRipIfStatV1RcvRequests": vRtrRipIfStatV1RcvRequests,
       "vRtrRipIfStatV1BadUpdates": vRtrRipIfStatV1BadUpdates,
       "vRtrRipIfStatV1BadRequests": vRtrRipIfStatV1BadRequests,
       "vRtrRipIfStatV1BadRoutes": vRtrRipIfStatV1BadRoutes,
       "vRtrRipIfStatV2RcvUpdates": vRtrRipIfStatV2RcvUpdates,
       "vRtrRipIfStatV2RcvRequests": vRtrRipIfStatV2RcvRequests,
       "vRtrRipIfStatV2BadUpdates": vRtrRipIfStatV2BadUpdates,
       "vRtrRipIfStatV2BadRequests": vRtrRipIfStatV2BadRequests,
       "vRtrRipIfStatV2BadRoutes": vRtrRipIfStatV2BadRoutes,
       "vRtrRipIfStatAuthErrors": vRtrRipIfStatAuthErrors,
       "vRtrRipIfStatAllSentUpdates5Min": vRtrRipIfStatAllSentUpdates5Min,
       "vRtrRipIfStatAllTriggeredUpdates5Min": vRtrRipIfStatAllTriggeredUpdates5Min,
       "vRtrRipIfStatAllRcvBadPackets5Min": vRtrRipIfStatAllRcvBadPackets5Min,
       "vRtrRipIfStatV1RcvUpdates5Min": vRtrRipIfStatV1RcvUpdates5Min,
       "vRtrRipIfStatV1RcvRequests5Min": vRtrRipIfStatV1RcvRequests5Min,
       "vRtrRipIfStatV1BadUpdates5Min": vRtrRipIfStatV1BadUpdates5Min,
       "vRtrRipIfStatV1BadRequests5Min": vRtrRipIfStatV1BadRequests5Min,
       "vRtrRipIfStatV1BadRoutes5Min": vRtrRipIfStatV1BadRoutes5Min,
       "vRtrRipIfStatV2RcvUpdates5Min": vRtrRipIfStatV2RcvUpdates5Min,
       "vRtrRipIfStatV2RcvRequests5Min": vRtrRipIfStatV2RcvRequests5Min,
       "vRtrRipIfStatV2BadUpdates5Min": vRtrRipIfStatV2BadUpdates5Min,
       "vRtrRipIfStatV2BadRequests5Min": vRtrRipIfStatV2BadRequests5Min,
       "vRtrRipIfStatV2BadRoutes5Min": vRtrRipIfStatV2BadRoutes5Min,
       "vRtrRipIfStatAuthErrors5Min": vRtrRipIfStatAuthErrors5Min,
       "vRtrRipIfStatAllSentUpdates1Min": vRtrRipIfStatAllSentUpdates1Min,
       "vRtrRipIfStatAllTriggeredUpdates1Min": vRtrRipIfStatAllTriggeredUpdates1Min,
       "vRtrRipIfStatAllRcvBadPackets1Min": vRtrRipIfStatAllRcvBadPackets1Min,
       "vRtrRipIfStatV1RcvUpdates1Min": vRtrRipIfStatV1RcvUpdates1Min,
       "vRtrRipIfStatV1RcvRequests1Min": vRtrRipIfStatV1RcvRequests1Min,
       "vRtrRipIfStatV1BadUpdates1Min": vRtrRipIfStatV1BadUpdates1Min,
       "vRtrRipIfStatV1BadRequests1Min": vRtrRipIfStatV1BadRequests1Min,
       "vRtrRipIfStatV1BadRoutes1Min": vRtrRipIfStatV1BadRoutes1Min,
       "vRtrRipIfStatV2RcvUpdates1Min": vRtrRipIfStatV2RcvUpdates1Min,
       "vRtrRipIfStatV2RcvRequests1Min": vRtrRipIfStatV2RcvRequests1Min,
       "vRtrRipIfStatV2BadUpdates1Min": vRtrRipIfStatV2BadUpdates1Min,
       "vRtrRipIfStatV2BadRequests1Min": vRtrRipIfStatV2BadRequests1Min,
       "vRtrRipIfStatV2BadRoutes1Min": vRtrRipIfStatV2BadRoutes1Min,
       "vRtrRipIfStatAuthErrors1Min": vRtrRipIfStatAuthErrors1Min,
       "vRtrRipPeerTable": vRtrRipPeerTable,
       "vRtrRipPeerEntry": vRtrRipPeerEntry,
       "vRtrRipPeerIfIndex": vRtrRipPeerIfIndex,
       "vRtrRipPeerAddress": vRtrRipPeerAddress,
       "vRtrRipPeerLastUpdate": vRtrRipPeerLastUpdate,
       "vRtrRipPeerVersion": vRtrRipPeerVersion,
       "vRtrRipPeerRcvBadPackets": vRtrRipPeerRcvBadPackets,
       "vRtrRipPeerRcvBadRoutes": vRtrRipPeerRcvBadRoutes,
       "vRtrRipAdvertisedRouteTable": vRtrRipAdvertisedRouteTable,
       "vRtrRipAdvertisedRouteEntry": vRtrRipAdvertisedRouteEntry,
       "vRtrRipAdvertisedRouteDest": vRtrRipAdvertisedRouteDest,
       "vRtrRipAdvertisedRouteMask": vRtrRipAdvertisedRouteMask,
       "vRtrRipAdvertisedRouteIfIndex": vRtrRipAdvertisedRouteIfIndex,
       "vRtrRipAdvertisedRouteIfAddr": vRtrRipAdvertisedRouteIfAddr,
       "vRtrRipAdvertisedRouteNextHop": vRtrRipAdvertisedRouteNextHop,
       "vRtrRipAdvertisedRouteMetric": vRtrRipAdvertisedRouteMetric,
       "vRtrRipAdvertisedRouteTag": vRtrRipAdvertisedRouteTag,
       "vRtrRipAdvertisedRouteTimerRemaining": vRtrRipAdvertisedRouteTimerRemaining,
       "vRtrRipNotifyPrefix": vRtrRipNotifyPrefix,
       "vRtrRipNotifications": vRtrRipNotifications,
       "vRtrRipAuthTypeMismatch": vRtrRipAuthTypeMismatch,
       "vRtrRipAuthFailure": vRtrRipAuthFailure,
       "vRtrRipInstanceShuttingDown": vRtrRipInstanceShuttingDown,
       "vRtrRipInstanceRestarted": vRtrRipInstanceRestarted,
       "vRtrRipInstanceExpLmtReached": vRtrRipInstanceExpLmtReached,
       "vRtrRipInstanceExpLmtWarning": vRtrRipInstanceExpLmtWarning,
       "vRtrRipInstanceRtsExpLmtDropped": vRtrRipInstanceRtsExpLmtDropped}
)
