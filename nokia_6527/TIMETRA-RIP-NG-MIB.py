# SNMP MIB module (TIMETRA-RIP-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-RIP-NG-MIB.mib
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

timetraRipNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 89)
)
if mibBuilder.loadTexts:
    timetraRipNgMIBModule.setRevisions(
        ("2013-04-22 00:00",
         "2013-04-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxRipNgInstVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rip", 1),
          ("ripNg", 2))
    )



class TmnxRipNgPeerVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rip-v1", 1),
          ("rip-v2", 2),
          ("ripNg-v1", 3))
    )



class TmnxRipNgAuthType(TextualConvention, Integer32):
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



class TmnxRipNgAuthKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxRipNgMessageSize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 255),
    )



class TmnxRipNgMetric(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxRipNgPreference(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxRipNgReceive(TextualConvention, Integer32):
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3),
          ("doNotReceive", 4),
          ("ripNg1", 5))
    )



class TmnxRipNgSend(TextualConvention, Integer32):
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
        *(("doNotSend", 1),
          ("ripVersion1", 2),
          ("rip1Compatible", 3),
          ("ripVersion2", 4),
          ("ripNgVersion1", 5),
          ("ripUnicast", 6))
    )



class TmnxRipNgTimerFlush(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )



class TmnxRipNgTimerTimeout(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )



class TmnxRipNgTimerUpdate(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxRipNgConformance_ObjectIdentity = ObjectIdentity
tmnxRipNgConformance = _TmnxRipNgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89)
)
_TmnxRipNgCompliances_ObjectIdentity = ObjectIdentity
tmnxRipNgCompliances = _TmnxRipNgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 1)
)
_TmnxRipNgGroups_ObjectIdentity = ObjectIdentity
tmnxRipNgGroups = _TmnxRipNgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2)
)
_TmnxRipNgObjs_ObjectIdentity = ObjectIdentity
tmnxRipNgObjs = _TmnxRipNgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89)
)
_TmnxRipNgGlobals_ObjectIdentity = ObjectIdentity
tmnxRipNgGlobals = _TmnxRipNgGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 1)
)
_TmnxRipNgGlobalLearnedRoutes_Type = Counter32
_TmnxRipNgGlobalLearnedRoutes_Object = MibScalar
tmnxRipNgGlobalLearnedRoutes = _TmnxRipNgGlobalLearnedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 1, 1),
    _TmnxRipNgGlobalLearnedRoutes_Type()
)
tmnxRipNgGlobalLearnedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgGlobalLearnedRoutes.setStatus("current")
_TmnxRipNgGlobalTimedoutRoutes_Type = Counter32
_TmnxRipNgGlobalTimedoutRoutes_Object = MibScalar
tmnxRipNgGlobalTimedoutRoutes = _TmnxRipNgGlobalTimedoutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 1, 2),
    _TmnxRipNgGlobalTimedoutRoutes_Type()
)
tmnxRipNgGlobalTimedoutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgGlobalTimedoutRoutes.setStatus("current")
_TmnxRipNgGlobalCurrentMemory_Type = Counter32
_TmnxRipNgGlobalCurrentMemory_Object = MibScalar
tmnxRipNgGlobalCurrentMemory = _TmnxRipNgGlobalCurrentMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 1, 3),
    _TmnxRipNgGlobalCurrentMemory_Type()
)
tmnxRipNgGlobalCurrentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgGlobalCurrentMemory.setStatus("current")
_TmnxRipNgGlobalMaximumMemory_Type = Counter32
_TmnxRipNgGlobalMaximumMemory_Object = MibScalar
tmnxRipNgGlobalMaximumMemory = _TmnxRipNgGlobalMaximumMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 1, 4),
    _TmnxRipNgGlobalMaximumMemory_Type()
)
tmnxRipNgGlobalMaximumMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgGlobalMaximumMemory.setStatus("current")
_TmnxRipNgTableObjs_ObjectIdentity = ObjectIdentity
tmnxRipNgTableObjs = _TmnxRipNgTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2)
)
_TmnxRipNgInstTable_Object = MibTable
tmnxRipNgInstTable = _TmnxRipNgInstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxRipNgInstTable.setStatus("current")
_TmnxRipNgInstEntry_Object = MibTableRow
tmnxRipNgInstEntry = _TmnxRipNgInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1)
)
tmnxRipNgInstEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
)
if mibBuilder.loadTexts:
    tmnxRipNgInstEntry.setStatus("current")
_TmnxRipNgInstVersion_Type = TmnxRipNgInstVersion
_TmnxRipNgInstVersion_Object = MibTableColumn
tmnxRipNgInstVersion = _TmnxRipNgInstVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 1),
    _TmnxRipNgInstVersion_Type()
)
tmnxRipNgInstVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgInstVersion.setStatus("current")


class _TmnxRipNgInstAuthType_Type(TmnxRipNgAuthType):
    """Custom type tmnxRipNgInstAuthType based on TmnxRipNgAuthType"""
    defaultValue = 1


_TmnxRipNgInstAuthType_Type.__name__ = "TmnxRipNgAuthType"
_TmnxRipNgInstAuthType_Object = MibTableColumn
tmnxRipNgInstAuthType = _TmnxRipNgInstAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 2),
    _TmnxRipNgInstAuthType_Type()
)
tmnxRipNgInstAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstAuthType.setStatus("current")


class _TmnxRipNgInstAuthKey_Type(TmnxRipNgAuthKey):
    """Custom type tmnxRipNgInstAuthKey based on TmnxRipNgAuthKey"""
    defaultHexValue = ""


_TmnxRipNgInstAuthKey_Type.__name__ = "TmnxRipNgAuthKey"
_TmnxRipNgInstAuthKey_Object = MibTableColumn
tmnxRipNgInstAuthKey = _TmnxRipNgInstAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 3),
    _TmnxRipNgInstAuthKey_Type()
)
tmnxRipNgInstAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstAuthKey.setStatus("current")


class _TmnxRipNgInstCheckZero_Type(TruthValue):
    """Custom type tmnxRipNgInstCheckZero based on TruthValue"""
    defaultValue = 2


_TmnxRipNgInstCheckZero_Type.__name__ = "TruthValue"
_TmnxRipNgInstCheckZero_Object = MibTableColumn
tmnxRipNgInstCheckZero = _TmnxRipNgInstCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 4),
    _TmnxRipNgInstCheckZero_Type()
)
tmnxRipNgInstCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstCheckZero.setStatus("current")


class _TmnxRipNgInstMessageSize_Type(TmnxRipNgMessageSize):
    """Custom type tmnxRipNgInstMessageSize based on TmnxRipNgMessageSize"""
    defaultValue = 25


_TmnxRipNgInstMessageSize_Type.__name__ = "TmnxRipNgMessageSize"
_TmnxRipNgInstMessageSize_Object = MibTableColumn
tmnxRipNgInstMessageSize = _TmnxRipNgInstMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 5),
    _TmnxRipNgInstMessageSize_Type()
)
tmnxRipNgInstMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstMessageSize.setStatus("current")


class _TmnxRipNgInstMetricIn_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgInstMetricIn based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgInstMetricIn_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgInstMetricIn_Object = MibTableColumn
tmnxRipNgInstMetricIn = _TmnxRipNgInstMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 6),
    _TmnxRipNgInstMetricIn_Type()
)
tmnxRipNgInstMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstMetricIn.setStatus("current")


class _TmnxRipNgInstMetricOut_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgInstMetricOut based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgInstMetricOut_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgInstMetricOut_Object = MibTableColumn
tmnxRipNgInstMetricOut = _TmnxRipNgInstMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 7),
    _TmnxRipNgInstMetricOut_Type()
)
tmnxRipNgInstMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstMetricOut.setStatus("current")


class _TmnxRipNgInstPreference_Type(TmnxRipNgPreference):
    """Custom type tmnxRipNgInstPreference based on TmnxRipNgPreference"""
    defaultValue = 100


_TmnxRipNgInstPreference_Type.__name__ = "TmnxRipNgPreference"
_TmnxRipNgInstPreference_Object = MibTableColumn
tmnxRipNgInstPreference = _TmnxRipNgInstPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 8),
    _TmnxRipNgInstPreference_Type()
)
tmnxRipNgInstPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstPreference.setStatus("current")


class _TmnxRipNgInstReceive_Type(TmnxRipNgReceive):
    """Custom type tmnxRipNgInstReceive based on TmnxRipNgReceive"""
    defaultValue = 5


_TmnxRipNgInstReceive_Type.__name__ = "TmnxRipNgReceive"
_TmnxRipNgInstReceive_Object = MibTableColumn
tmnxRipNgInstReceive = _TmnxRipNgInstReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 9),
    _TmnxRipNgInstReceive_Type()
)
tmnxRipNgInstReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstReceive.setStatus("current")


class _TmnxRipNgInstSend_Type(TmnxRipNgSend):
    """Custom type tmnxRipNgInstSend based on TmnxRipNgSend"""
    defaultValue = 5


_TmnxRipNgInstSend_Type.__name__ = "TmnxRipNgSend"
_TmnxRipNgInstSend_Object = MibTableColumn
tmnxRipNgInstSend = _TmnxRipNgInstSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 10),
    _TmnxRipNgInstSend_Type()
)
tmnxRipNgInstSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstSend.setStatus("current")


class _TmnxRipNgInstSplitHorizon_Type(TruthValue):
    """Custom type tmnxRipNgInstSplitHorizon based on TruthValue"""
    defaultValue = 1


_TmnxRipNgInstSplitHorizon_Type.__name__ = "TruthValue"
_TmnxRipNgInstSplitHorizon_Object = MibTableColumn
tmnxRipNgInstSplitHorizon = _TmnxRipNgInstSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 11),
    _TmnxRipNgInstSplitHorizon_Type()
)
tmnxRipNgInstSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstSplitHorizon.setStatus("current")


class _TmnxRipNgInstTimerFlush_Type(TmnxRipNgTimerFlush):
    """Custom type tmnxRipNgInstTimerFlush based on TmnxRipNgTimerFlush"""
    defaultValue = 120


_TmnxRipNgInstTimerFlush_Type.__name__ = "TmnxRipNgTimerFlush"
_TmnxRipNgInstTimerFlush_Object = MibTableColumn
tmnxRipNgInstTimerFlush = _TmnxRipNgInstTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 12),
    _TmnxRipNgInstTimerFlush_Type()
)
tmnxRipNgInstTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerFlush.setUnits("seconds")


class _TmnxRipNgInstTimerTimeout_Type(TmnxRipNgTimerTimeout):
    """Custom type tmnxRipNgInstTimerTimeout based on TmnxRipNgTimerTimeout"""
    defaultValue = 180


_TmnxRipNgInstTimerTimeout_Type.__name__ = "TmnxRipNgTimerTimeout"
_TmnxRipNgInstTimerTimeout_Object = MibTableColumn
tmnxRipNgInstTimerTimeout = _TmnxRipNgInstTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 13),
    _TmnxRipNgInstTimerTimeout_Type()
)
tmnxRipNgInstTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerTimeout.setUnits("seconds")


class _TmnxRipNgInstTimerUpdate_Type(TmnxRipNgTimerUpdate):
    """Custom type tmnxRipNgInstTimerUpdate based on TmnxRipNgTimerUpdate"""
    defaultValue = 30


_TmnxRipNgInstTimerUpdate_Type.__name__ = "TmnxRipNgTimerUpdate"
_TmnxRipNgInstTimerUpdate_Object = MibTableColumn
tmnxRipNgInstTimerUpdate = _TmnxRipNgInstTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 14),
    _TmnxRipNgInstTimerUpdate_Type()
)
tmnxRipNgInstTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgInstTimerUpdate.setUnits("seconds")


class _TmnxRipNgInstImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstImportPolicy1_Object = MibTableColumn
tmnxRipNgInstImportPolicy1 = _TmnxRipNgInstImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 15),
    _TmnxRipNgInstImportPolicy1_Type()
)
tmnxRipNgInstImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstImportPolicy1.setStatus("current")


class _TmnxRipNgInstImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstImportPolicy2_Object = MibTableColumn
tmnxRipNgInstImportPolicy2 = _TmnxRipNgInstImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 16),
    _TmnxRipNgInstImportPolicy2_Type()
)
tmnxRipNgInstImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstImportPolicy2.setStatus("current")


class _TmnxRipNgInstImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstImportPolicy3_Object = MibTableColumn
tmnxRipNgInstImportPolicy3 = _TmnxRipNgInstImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 17),
    _TmnxRipNgInstImportPolicy3_Type()
)
tmnxRipNgInstImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstImportPolicy3.setStatus("current")


class _TmnxRipNgInstImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstImportPolicy4_Object = MibTableColumn
tmnxRipNgInstImportPolicy4 = _TmnxRipNgInstImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 18),
    _TmnxRipNgInstImportPolicy4_Type()
)
tmnxRipNgInstImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstImportPolicy4.setStatus("current")


class _TmnxRipNgInstImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstImportPolicy5_Object = MibTableColumn
tmnxRipNgInstImportPolicy5 = _TmnxRipNgInstImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 19),
    _TmnxRipNgInstImportPolicy5_Type()
)
tmnxRipNgInstImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstImportPolicy5.setStatus("current")


class _TmnxRipNgInstExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstExportPolicy1_Object = MibTableColumn
tmnxRipNgInstExportPolicy1 = _TmnxRipNgInstExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 20),
    _TmnxRipNgInstExportPolicy1_Type()
)
tmnxRipNgInstExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportPolicy1.setStatus("current")


class _TmnxRipNgInstExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstExportPolicy2_Object = MibTableColumn
tmnxRipNgInstExportPolicy2 = _TmnxRipNgInstExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 21),
    _TmnxRipNgInstExportPolicy2_Type()
)
tmnxRipNgInstExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportPolicy2.setStatus("current")


class _TmnxRipNgInstExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstExportPolicy3_Object = MibTableColumn
tmnxRipNgInstExportPolicy3 = _TmnxRipNgInstExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 22),
    _TmnxRipNgInstExportPolicy3_Type()
)
tmnxRipNgInstExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportPolicy3.setStatus("current")


class _TmnxRipNgInstExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstExportPolicy4_Object = MibTableColumn
tmnxRipNgInstExportPolicy4 = _TmnxRipNgInstExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 23),
    _TmnxRipNgInstExportPolicy4_Type()
)
tmnxRipNgInstExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportPolicy4.setStatus("current")


class _TmnxRipNgInstExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgInstExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgInstExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgInstExportPolicy5_Object = MibTableColumn
tmnxRipNgInstExportPolicy5 = _TmnxRipNgInstExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 24),
    _TmnxRipNgInstExportPolicy5_Type()
)
tmnxRipNgInstExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportPolicy5.setStatus("current")


class _TmnxRipNgInstDescription_Type(TItemDescription):
    """Custom type tmnxRipNgInstDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxRipNgInstDescription_Type.__name__ = "TItemDescription"
_TmnxRipNgInstDescription_Object = MibTableColumn
tmnxRipNgInstDescription = _TmnxRipNgInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 25),
    _TmnxRipNgInstDescription_Type()
)
tmnxRipNgInstDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstDescription.setStatus("current")


class _TmnxRipNgInstAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxRipNgInstAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxRipNgInstAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxRipNgInstAdminStatus_Object = MibTableColumn
tmnxRipNgInstAdminStatus = _TmnxRipNgInstAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 26),
    _TmnxRipNgInstAdminStatus_Type()
)
tmnxRipNgInstAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstAdminStatus.setStatus("current")
_TmnxRipNgInstOperStatus_Type = TmnxOperState
_TmnxRipNgInstOperStatus_Object = MibTableColumn
tmnxRipNgInstOperStatus = _TmnxRipNgInstOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 27),
    _TmnxRipNgInstOperStatus_Type()
)
tmnxRipNgInstOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgInstOperStatus.setStatus("current")


class _TmnxRipNgInstPropagateMetric_Type(TruthValue):
    """Custom type tmnxRipNgInstPropagateMetric based on TruthValue"""
    defaultValue = 2


_TmnxRipNgInstPropagateMetric_Type.__name__ = "TruthValue"
_TmnxRipNgInstPropagateMetric_Object = MibTableColumn
tmnxRipNgInstPropagateMetric = _TmnxRipNgInstPropagateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 28),
    _TmnxRipNgInstPropagateMetric_Type()
)
tmnxRipNgInstPropagateMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstPropagateMetric.setStatus("current")


class _TmnxRipNgInstExportLimit_Type(Unsigned32):
    """Custom type tmnxRipNgInstExportLimit based on Unsigned32"""
    defaultValue = 0


_TmnxRipNgInstExportLimit_Type.__name__ = "Unsigned32"
_TmnxRipNgInstExportLimit_Object = MibTableColumn
tmnxRipNgInstExportLimit = _TmnxRipNgInstExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 29),
    _TmnxRipNgInstExportLimit_Type()
)
tmnxRipNgInstExportLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExportLimit.setStatus("current")


class _TmnxRipNgInstExpLmtLogPct_Type(Unsigned32):
    """Custom type tmnxRipNgInstExpLmtLogPct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxRipNgInstExpLmtLogPct_Type.__name__ = "Unsigned32"
_TmnxRipNgInstExpLmtLogPct_Object = MibTableColumn
tmnxRipNgInstExpLmtLogPct = _TmnxRipNgInstExpLmtLogPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 30),
    _TmnxRipNgInstExpLmtLogPct_Type()
)
tmnxRipNgInstExpLmtLogPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgInstExpLmtLogPct.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgInstExpLmtLogPct.setUnits("percentage")
_TmnxRipNgInstTotalExpRoutes_Type = Gauge32
_TmnxRipNgInstTotalExpRoutes_Object = MibTableColumn
tmnxRipNgInstTotalExpRoutes = _TmnxRipNgInstTotalExpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 1, 1, 31),
    _TmnxRipNgInstTotalExpRoutes_Type()
)
tmnxRipNgInstTotalExpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgInstTotalExpRoutes.setStatus("current")
_TmnxRipNgGroupTable_Object = MibTable
tmnxRipNgGroupTable = _TmnxRipNgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxRipNgGroupTable.setStatus("current")
_TmnxRipNgGroupEntry_Object = MibTableRow
tmnxRipNgGroupEntry = _TmnxRipNgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1)
)
tmnxRipNgGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupName"),
)
if mibBuilder.loadTexts:
    tmnxRipNgGroupEntry.setStatus("current")
_TmnxRipNgGroupName_Type = TNamedItem
_TmnxRipNgGroupName_Object = MibTableColumn
tmnxRipNgGroupName = _TmnxRipNgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 1),
    _TmnxRipNgGroupName_Type()
)
tmnxRipNgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgGroupName.setStatus("current")


class _TmnxRipNgGroupAuthType_Type(TmnxRipNgAuthType):
    """Custom type tmnxRipNgGroupAuthType based on TmnxRipNgAuthType"""
    defaultValue = 1


_TmnxRipNgGroupAuthType_Type.__name__ = "TmnxRipNgAuthType"
_TmnxRipNgGroupAuthType_Object = MibTableColumn
tmnxRipNgGroupAuthType = _TmnxRipNgGroupAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 2),
    _TmnxRipNgGroupAuthType_Type()
)
tmnxRipNgGroupAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupAuthType.setStatus("current")


class _TmnxRipNgGroupAuthKey_Type(TmnxRipNgAuthKey):
    """Custom type tmnxRipNgGroupAuthKey based on TmnxRipNgAuthKey"""
    defaultHexValue = ""


_TmnxRipNgGroupAuthKey_Type.__name__ = "TmnxRipNgAuthKey"
_TmnxRipNgGroupAuthKey_Object = MibTableColumn
tmnxRipNgGroupAuthKey = _TmnxRipNgGroupAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 3),
    _TmnxRipNgGroupAuthKey_Type()
)
tmnxRipNgGroupAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupAuthKey.setStatus("current")


class _TmnxRipNgGroupCheckZero_Type(TruthValue):
    """Custom type tmnxRipNgGroupCheckZero based on TruthValue"""
    defaultValue = 2


_TmnxRipNgGroupCheckZero_Type.__name__ = "TruthValue"
_TmnxRipNgGroupCheckZero_Object = MibTableColumn
tmnxRipNgGroupCheckZero = _TmnxRipNgGroupCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 4),
    _TmnxRipNgGroupCheckZero_Type()
)
tmnxRipNgGroupCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupCheckZero.setStatus("current")


class _TmnxRipNgGroupMessageSize_Type(TmnxRipNgMessageSize):
    """Custom type tmnxRipNgGroupMessageSize based on TmnxRipNgMessageSize"""
    defaultValue = 25


_TmnxRipNgGroupMessageSize_Type.__name__ = "TmnxRipNgMessageSize"
_TmnxRipNgGroupMessageSize_Object = MibTableColumn
tmnxRipNgGroupMessageSize = _TmnxRipNgGroupMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 5),
    _TmnxRipNgGroupMessageSize_Type()
)
tmnxRipNgGroupMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupMessageSize.setStatus("current")


class _TmnxRipNgGroupMetricIn_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgGroupMetricIn based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgGroupMetricIn_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgGroupMetricIn_Object = MibTableColumn
tmnxRipNgGroupMetricIn = _TmnxRipNgGroupMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 6),
    _TmnxRipNgGroupMetricIn_Type()
)
tmnxRipNgGroupMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupMetricIn.setStatus("current")


class _TmnxRipNgGroupMetricOut_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgGroupMetricOut based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgGroupMetricOut_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgGroupMetricOut_Object = MibTableColumn
tmnxRipNgGroupMetricOut = _TmnxRipNgGroupMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 7),
    _TmnxRipNgGroupMetricOut_Type()
)
tmnxRipNgGroupMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupMetricOut.setStatus("current")


class _TmnxRipNgGroupPreference_Type(TmnxRipNgPreference):
    """Custom type tmnxRipNgGroupPreference based on TmnxRipNgPreference"""
    defaultValue = 100


_TmnxRipNgGroupPreference_Type.__name__ = "TmnxRipNgPreference"
_TmnxRipNgGroupPreference_Object = MibTableColumn
tmnxRipNgGroupPreference = _TmnxRipNgGroupPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 8),
    _TmnxRipNgGroupPreference_Type()
)
tmnxRipNgGroupPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupPreference.setStatus("current")


class _TmnxRipNgGroupReceive_Type(TmnxRipNgReceive):
    """Custom type tmnxRipNgGroupReceive based on TmnxRipNgReceive"""
    defaultValue = 5


_TmnxRipNgGroupReceive_Type.__name__ = "TmnxRipNgReceive"
_TmnxRipNgGroupReceive_Object = MibTableColumn
tmnxRipNgGroupReceive = _TmnxRipNgGroupReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 9),
    _TmnxRipNgGroupReceive_Type()
)
tmnxRipNgGroupReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupReceive.setStatus("current")


class _TmnxRipNgGroupSend_Type(TmnxRipNgSend):
    """Custom type tmnxRipNgGroupSend based on TmnxRipNgSend"""
    defaultValue = 5


_TmnxRipNgGroupSend_Type.__name__ = "TmnxRipNgSend"
_TmnxRipNgGroupSend_Object = MibTableColumn
tmnxRipNgGroupSend = _TmnxRipNgGroupSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 10),
    _TmnxRipNgGroupSend_Type()
)
tmnxRipNgGroupSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupSend.setStatus("current")


class _TmnxRipNgGroupSplitHorizon_Type(TruthValue):
    """Custom type tmnxRipNgGroupSplitHorizon based on TruthValue"""
    defaultValue = 1


_TmnxRipNgGroupSplitHorizon_Type.__name__ = "TruthValue"
_TmnxRipNgGroupSplitHorizon_Object = MibTableColumn
tmnxRipNgGroupSplitHorizon = _TmnxRipNgGroupSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 11),
    _TmnxRipNgGroupSplitHorizon_Type()
)
tmnxRipNgGroupSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupSplitHorizon.setStatus("current")


class _TmnxRipNgGroupTimerFlush_Type(TmnxRipNgTimerFlush):
    """Custom type tmnxRipNgGroupTimerFlush based on TmnxRipNgTimerFlush"""
    defaultValue = 120


_TmnxRipNgGroupTimerFlush_Type.__name__ = "TmnxRipNgTimerFlush"
_TmnxRipNgGroupTimerFlush_Object = MibTableColumn
tmnxRipNgGroupTimerFlush = _TmnxRipNgGroupTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 12),
    _TmnxRipNgGroupTimerFlush_Type()
)
tmnxRipNgGroupTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerFlush.setUnits("seconds")


class _TmnxRipNgGroupTimerTimeout_Type(TmnxRipNgTimerTimeout):
    """Custom type tmnxRipNgGroupTimerTimeout based on TmnxRipNgTimerTimeout"""
    defaultValue = 180


_TmnxRipNgGroupTimerTimeout_Type.__name__ = "TmnxRipNgTimerTimeout"
_TmnxRipNgGroupTimerTimeout_Object = MibTableColumn
tmnxRipNgGroupTimerTimeout = _TmnxRipNgGroupTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 13),
    _TmnxRipNgGroupTimerTimeout_Type()
)
tmnxRipNgGroupTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerTimeout.setUnits("seconds")


class _TmnxRipNgGroupTimerUpdate_Type(TmnxRipNgTimerUpdate):
    """Custom type tmnxRipNgGroupTimerUpdate based on TmnxRipNgTimerUpdate"""
    defaultValue = 30


_TmnxRipNgGroupTimerUpdate_Type.__name__ = "TmnxRipNgTimerUpdate"
_TmnxRipNgGroupTimerUpdate_Object = MibTableColumn
tmnxRipNgGroupTimerUpdate = _TmnxRipNgGroupTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 14),
    _TmnxRipNgGroupTimerUpdate_Type()
)
tmnxRipNgGroupTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgGroupTimerUpdate.setUnits("seconds")


class _TmnxRipNgGroupImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupImportPolicy1_Object = MibTableColumn
tmnxRipNgGroupImportPolicy1 = _TmnxRipNgGroupImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 15),
    _TmnxRipNgGroupImportPolicy1_Type()
)
tmnxRipNgGroupImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupImportPolicy1.setStatus("current")


class _TmnxRipNgGroupImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupImportPolicy2_Object = MibTableColumn
tmnxRipNgGroupImportPolicy2 = _TmnxRipNgGroupImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 16),
    _TmnxRipNgGroupImportPolicy2_Type()
)
tmnxRipNgGroupImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupImportPolicy2.setStatus("current")


class _TmnxRipNgGroupImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupImportPolicy3_Object = MibTableColumn
tmnxRipNgGroupImportPolicy3 = _TmnxRipNgGroupImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 17),
    _TmnxRipNgGroupImportPolicy3_Type()
)
tmnxRipNgGroupImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupImportPolicy3.setStatus("current")


class _TmnxRipNgGroupImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupImportPolicy4_Object = MibTableColumn
tmnxRipNgGroupImportPolicy4 = _TmnxRipNgGroupImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 18),
    _TmnxRipNgGroupImportPolicy4_Type()
)
tmnxRipNgGroupImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupImportPolicy4.setStatus("current")


class _TmnxRipNgGroupImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupImportPolicy5_Object = MibTableColumn
tmnxRipNgGroupImportPolicy5 = _TmnxRipNgGroupImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 19),
    _TmnxRipNgGroupImportPolicy5_Type()
)
tmnxRipNgGroupImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupImportPolicy5.setStatus("current")


class _TmnxRipNgGroupExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupExportPolicy1_Object = MibTableColumn
tmnxRipNgGroupExportPolicy1 = _TmnxRipNgGroupExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 20),
    _TmnxRipNgGroupExportPolicy1_Type()
)
tmnxRipNgGroupExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupExportPolicy1.setStatus("current")


class _TmnxRipNgGroupExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupExportPolicy2_Object = MibTableColumn
tmnxRipNgGroupExportPolicy2 = _TmnxRipNgGroupExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 21),
    _TmnxRipNgGroupExportPolicy2_Type()
)
tmnxRipNgGroupExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupExportPolicy2.setStatus("current")


class _TmnxRipNgGroupExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupExportPolicy3_Object = MibTableColumn
tmnxRipNgGroupExportPolicy3 = _TmnxRipNgGroupExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 22),
    _TmnxRipNgGroupExportPolicy3_Type()
)
tmnxRipNgGroupExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupExportPolicy3.setStatus("current")


class _TmnxRipNgGroupExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupExportPolicy4_Object = MibTableColumn
tmnxRipNgGroupExportPolicy4 = _TmnxRipNgGroupExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 23),
    _TmnxRipNgGroupExportPolicy4_Type()
)
tmnxRipNgGroupExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupExportPolicy4.setStatus("current")


class _TmnxRipNgGroupExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgGroupExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgGroupExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgGroupExportPolicy5_Object = MibTableColumn
tmnxRipNgGroupExportPolicy5 = _TmnxRipNgGroupExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 24),
    _TmnxRipNgGroupExportPolicy5_Type()
)
tmnxRipNgGroupExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupExportPolicy5.setStatus("current")


class _TmnxRipNgGroupDescription_Type(TItemDescription):
    """Custom type tmnxRipNgGroupDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxRipNgGroupDescription_Type.__name__ = "TItemDescription"
_TmnxRipNgGroupDescription_Object = MibTableColumn
tmnxRipNgGroupDescription = _TmnxRipNgGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 25),
    _TmnxRipNgGroupDescription_Type()
)
tmnxRipNgGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupDescription.setStatus("current")


class _TmnxRipNgGroupInheritance_Type(Unsigned32):
    """Custom type tmnxRipNgGroupInheritance based on Unsigned32"""
    defaultValue = 0


_TmnxRipNgGroupInheritance_Type.__name__ = "Unsigned32"
_TmnxRipNgGroupInheritance_Object = MibTableColumn
tmnxRipNgGroupInheritance = _TmnxRipNgGroupInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 26),
    _TmnxRipNgGroupInheritance_Type()
)
tmnxRipNgGroupInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupInheritance.setStatus("current")


class _TmnxRipNgGroupAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxRipNgGroupAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxRipNgGroupAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxRipNgGroupAdminStatus_Object = MibTableColumn
tmnxRipNgGroupAdminStatus = _TmnxRipNgGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 27),
    _TmnxRipNgGroupAdminStatus_Type()
)
tmnxRipNgGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupAdminStatus.setStatus("current")
_TmnxRipNgGroupOperStatus_Type = TmnxOperState
_TmnxRipNgGroupOperStatus_Object = MibTableColumn
tmnxRipNgGroupOperStatus = _TmnxRipNgGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 28),
    _TmnxRipNgGroupOperStatus_Type()
)
tmnxRipNgGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgGroupOperStatus.setStatus("current")
_TmnxRipNgGroupRowStatus_Type = RowStatus
_TmnxRipNgGroupRowStatus_Object = MibTableColumn
tmnxRipNgGroupRowStatus = _TmnxRipNgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 2, 1, 29),
    _TmnxRipNgGroupRowStatus_Type()
)
tmnxRipNgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgGroupRowStatus.setStatus("current")
_TmnxRipNgIfTable_Object = MibTable
tmnxRipNgIfTable = _TmnxRipNgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxRipNgIfTable.setStatus("current")
_TmnxRipNgIfEntry_Object = MibTableRow
tmnxRipNgIfEntry = _TmnxRipNgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1)
)
tmnxRipNgIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxRipNgIfEntry.setStatus("current")
_TmnxRipNgIfGroupName_Type = TNamedItem
_TmnxRipNgIfGroupName_Object = MibTableColumn
tmnxRipNgIfGroupName = _TmnxRipNgIfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 1),
    _TmnxRipNgIfGroupName_Type()
)
tmnxRipNgIfGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfGroupName.setStatus("current")


class _TmnxRipNgIfAuthType_Type(TmnxRipNgAuthType):
    """Custom type tmnxRipNgIfAuthType based on TmnxRipNgAuthType"""
    defaultValue = 1


_TmnxRipNgIfAuthType_Type.__name__ = "TmnxRipNgAuthType"
_TmnxRipNgIfAuthType_Object = MibTableColumn
tmnxRipNgIfAuthType = _TmnxRipNgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 2),
    _TmnxRipNgIfAuthType_Type()
)
tmnxRipNgIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfAuthType.setStatus("current")


class _TmnxRipNgIfAuthKey_Type(TmnxRipNgAuthKey):
    """Custom type tmnxRipNgIfAuthKey based on TmnxRipNgAuthKey"""
    defaultHexValue = ""


_TmnxRipNgIfAuthKey_Type.__name__ = "TmnxRipNgAuthKey"
_TmnxRipNgIfAuthKey_Object = MibTableColumn
tmnxRipNgIfAuthKey = _TmnxRipNgIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 3),
    _TmnxRipNgIfAuthKey_Type()
)
tmnxRipNgIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfAuthKey.setStatus("current")


class _TmnxRipNgIfCheckZero_Type(TruthValue):
    """Custom type tmnxRipNgIfCheckZero based on TruthValue"""
    defaultValue = 2


_TmnxRipNgIfCheckZero_Type.__name__ = "TruthValue"
_TmnxRipNgIfCheckZero_Object = MibTableColumn
tmnxRipNgIfCheckZero = _TmnxRipNgIfCheckZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 4),
    _TmnxRipNgIfCheckZero_Type()
)
tmnxRipNgIfCheckZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfCheckZero.setStatus("current")


class _TmnxRipNgIfMessageSize_Type(TmnxRipNgMessageSize):
    """Custom type tmnxRipNgIfMessageSize based on TmnxRipNgMessageSize"""
    defaultValue = 25


_TmnxRipNgIfMessageSize_Type.__name__ = "TmnxRipNgMessageSize"
_TmnxRipNgIfMessageSize_Object = MibTableColumn
tmnxRipNgIfMessageSize = _TmnxRipNgIfMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 5),
    _TmnxRipNgIfMessageSize_Type()
)
tmnxRipNgIfMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfMessageSize.setStatus("current")


class _TmnxRipNgIfMetricIn_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgIfMetricIn based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgIfMetricIn_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgIfMetricIn_Object = MibTableColumn
tmnxRipNgIfMetricIn = _TmnxRipNgIfMetricIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 6),
    _TmnxRipNgIfMetricIn_Type()
)
tmnxRipNgIfMetricIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfMetricIn.setStatus("current")


class _TmnxRipNgIfMetricOut_Type(TmnxRipNgMetric):
    """Custom type tmnxRipNgIfMetricOut based on TmnxRipNgMetric"""
    defaultValue = 1


_TmnxRipNgIfMetricOut_Type.__name__ = "TmnxRipNgMetric"
_TmnxRipNgIfMetricOut_Object = MibTableColumn
tmnxRipNgIfMetricOut = _TmnxRipNgIfMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 7),
    _TmnxRipNgIfMetricOut_Type()
)
tmnxRipNgIfMetricOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfMetricOut.setStatus("current")


class _TmnxRipNgIfPreference_Type(TmnxRipNgPreference):
    """Custom type tmnxRipNgIfPreference based on TmnxRipNgPreference"""
    defaultValue = 100


_TmnxRipNgIfPreference_Type.__name__ = "TmnxRipNgPreference"
_TmnxRipNgIfPreference_Object = MibTableColumn
tmnxRipNgIfPreference = _TmnxRipNgIfPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 8),
    _TmnxRipNgIfPreference_Type()
)
tmnxRipNgIfPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfPreference.setStatus("current")


class _TmnxRipNgIfReceive_Type(TmnxRipNgReceive):
    """Custom type tmnxRipNgIfReceive based on TmnxRipNgReceive"""
    defaultValue = 5


_TmnxRipNgIfReceive_Type.__name__ = "TmnxRipNgReceive"
_TmnxRipNgIfReceive_Object = MibTableColumn
tmnxRipNgIfReceive = _TmnxRipNgIfReceive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 9),
    _TmnxRipNgIfReceive_Type()
)
tmnxRipNgIfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfReceive.setStatus("current")


class _TmnxRipNgIfSend_Type(TmnxRipNgSend):
    """Custom type tmnxRipNgIfSend based on TmnxRipNgSend"""
    defaultValue = 5


_TmnxRipNgIfSend_Type.__name__ = "TmnxRipNgSend"
_TmnxRipNgIfSend_Object = MibTableColumn
tmnxRipNgIfSend = _TmnxRipNgIfSend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 10),
    _TmnxRipNgIfSend_Type()
)
tmnxRipNgIfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfSend.setStatus("current")


class _TmnxRipNgIfSplitHorizon_Type(TruthValue):
    """Custom type tmnxRipNgIfSplitHorizon based on TruthValue"""
    defaultValue = 1


_TmnxRipNgIfSplitHorizon_Type.__name__ = "TruthValue"
_TmnxRipNgIfSplitHorizon_Object = MibTableColumn
tmnxRipNgIfSplitHorizon = _TmnxRipNgIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 11),
    _TmnxRipNgIfSplitHorizon_Type()
)
tmnxRipNgIfSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfSplitHorizon.setStatus("current")


class _TmnxRipNgIfTimerFlush_Type(TmnxRipNgTimerFlush):
    """Custom type tmnxRipNgIfTimerFlush based on TmnxRipNgTimerFlush"""
    defaultValue = 120


_TmnxRipNgIfTimerFlush_Type.__name__ = "TmnxRipNgTimerFlush"
_TmnxRipNgIfTimerFlush_Object = MibTableColumn
tmnxRipNgIfTimerFlush = _TmnxRipNgIfTimerFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 12),
    _TmnxRipNgIfTimerFlush_Type()
)
tmnxRipNgIfTimerFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerFlush.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerFlush.setUnits("seconds")


class _TmnxRipNgIfTimerTimeout_Type(TmnxRipNgTimerTimeout):
    """Custom type tmnxRipNgIfTimerTimeout based on TmnxRipNgTimerTimeout"""
    defaultValue = 180


_TmnxRipNgIfTimerTimeout_Type.__name__ = "TmnxRipNgTimerTimeout"
_TmnxRipNgIfTimerTimeout_Object = MibTableColumn
tmnxRipNgIfTimerTimeout = _TmnxRipNgIfTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 13),
    _TmnxRipNgIfTimerTimeout_Type()
)
tmnxRipNgIfTimerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerTimeout.setUnits("seconds")


class _TmnxRipNgIfTimerUpdate_Type(TmnxRipNgTimerUpdate):
    """Custom type tmnxRipNgIfTimerUpdate based on TmnxRipNgTimerUpdate"""
    defaultValue = 30


_TmnxRipNgIfTimerUpdate_Type.__name__ = "TmnxRipNgTimerUpdate"
_TmnxRipNgIfTimerUpdate_Object = MibTableColumn
tmnxRipNgIfTimerUpdate = _TmnxRipNgIfTimerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 14),
    _TmnxRipNgIfTimerUpdate_Type()
)
tmnxRipNgIfTimerUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerUpdate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRipNgIfTimerUpdate.setUnits("seconds")


class _TmnxRipNgIfImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfImportPolicy1_Object = MibTableColumn
tmnxRipNgIfImportPolicy1 = _TmnxRipNgIfImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 15),
    _TmnxRipNgIfImportPolicy1_Type()
)
tmnxRipNgIfImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfImportPolicy1.setStatus("current")


class _TmnxRipNgIfImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfImportPolicy2_Object = MibTableColumn
tmnxRipNgIfImportPolicy2 = _TmnxRipNgIfImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 16),
    _TmnxRipNgIfImportPolicy2_Type()
)
tmnxRipNgIfImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfImportPolicy2.setStatus("current")


class _TmnxRipNgIfImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfImportPolicy3_Object = MibTableColumn
tmnxRipNgIfImportPolicy3 = _TmnxRipNgIfImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 17),
    _TmnxRipNgIfImportPolicy3_Type()
)
tmnxRipNgIfImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfImportPolicy3.setStatus("current")


class _TmnxRipNgIfImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfImportPolicy4_Object = MibTableColumn
tmnxRipNgIfImportPolicy4 = _TmnxRipNgIfImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 18),
    _TmnxRipNgIfImportPolicy4_Type()
)
tmnxRipNgIfImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfImportPolicy4.setStatus("current")


class _TmnxRipNgIfImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfImportPolicy5_Object = MibTableColumn
tmnxRipNgIfImportPolicy5 = _TmnxRipNgIfImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 19),
    _TmnxRipNgIfImportPolicy5_Type()
)
tmnxRipNgIfImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfImportPolicy5.setStatus("current")


class _TmnxRipNgIfExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfExportPolicy1_Object = MibTableColumn
tmnxRipNgIfExportPolicy1 = _TmnxRipNgIfExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 20),
    _TmnxRipNgIfExportPolicy1_Type()
)
tmnxRipNgIfExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfExportPolicy1.setStatus("current")


class _TmnxRipNgIfExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfExportPolicy2_Object = MibTableColumn
tmnxRipNgIfExportPolicy2 = _TmnxRipNgIfExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 21),
    _TmnxRipNgIfExportPolicy2_Type()
)
tmnxRipNgIfExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfExportPolicy2.setStatus("current")


class _TmnxRipNgIfExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfExportPolicy3_Object = MibTableColumn
tmnxRipNgIfExportPolicy3 = _TmnxRipNgIfExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 22),
    _TmnxRipNgIfExportPolicy3_Type()
)
tmnxRipNgIfExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfExportPolicy3.setStatus("current")


class _TmnxRipNgIfExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfExportPolicy4_Object = MibTableColumn
tmnxRipNgIfExportPolicy4 = _TmnxRipNgIfExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 23),
    _TmnxRipNgIfExportPolicy4_Type()
)
tmnxRipNgIfExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfExportPolicy4.setStatus("current")


class _TmnxRipNgIfExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxRipNgIfExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxRipNgIfExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxRipNgIfExportPolicy5_Object = MibTableColumn
tmnxRipNgIfExportPolicy5 = _TmnxRipNgIfExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 24),
    _TmnxRipNgIfExportPolicy5_Type()
)
tmnxRipNgIfExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfExportPolicy5.setStatus("current")


class _TmnxRipNgIfDescription_Type(TItemDescription):
    """Custom type tmnxRipNgIfDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxRipNgIfDescription_Type.__name__ = "TItemDescription"
_TmnxRipNgIfDescription_Object = MibTableColumn
tmnxRipNgIfDescription = _TmnxRipNgIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 25),
    _TmnxRipNgIfDescription_Type()
)
tmnxRipNgIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfDescription.setStatus("current")


class _TmnxRipNgIfInheritance_Type(Unsigned32):
    """Custom type tmnxRipNgIfInheritance based on Unsigned32"""
    defaultValue = 0


_TmnxRipNgIfInheritance_Type.__name__ = "Unsigned32"
_TmnxRipNgIfInheritance_Object = MibTableColumn
tmnxRipNgIfInheritance = _TmnxRipNgIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 26),
    _TmnxRipNgIfInheritance_Type()
)
tmnxRipNgIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfInheritance.setStatus("current")


class _TmnxRipNgIfAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxRipNgIfAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxRipNgIfAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxRipNgIfAdminStatus_Object = MibTableColumn
tmnxRipNgIfAdminStatus = _TmnxRipNgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 27),
    _TmnxRipNgIfAdminStatus_Type()
)
tmnxRipNgIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfAdminStatus.setStatus("current")


class _TmnxRipNgIfOperStatus_Type(TmnxOperState):
    """Custom type tmnxRipNgIfOperStatus based on TmnxOperState"""
    defaultValue = 2


_TmnxRipNgIfOperStatus_Type.__name__ = "TmnxOperState"
_TmnxRipNgIfOperStatus_Object = MibTableColumn
tmnxRipNgIfOperStatus = _TmnxRipNgIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 28),
    _TmnxRipNgIfOperStatus_Type()
)
tmnxRipNgIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfOperStatus.setStatus("current")
_TmnxRipNgIfRowStatus_Type = RowStatus
_TmnxRipNgIfRowStatus_Object = MibTableColumn
tmnxRipNgIfRowStatus = _TmnxRipNgIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 3, 1, 29),
    _TmnxRipNgIfRowStatus_Type()
)
tmnxRipNgIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfRowStatus.setStatus("current")
_TmnxRipNgRouteTable_Object = MibTable
tmnxRipNgRouteTable = _TmnxRipNgRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxRipNgRouteTable.setStatus("current")
_TmnxRipNgRouteEntry_Object = MibTableRow
tmnxRipNgRouteEntry = _TmnxRipNgRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1)
)
tmnxRipNgRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteDestAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteDestAddress"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteMaskLength"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteIfIndex"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRoutePeerAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgRoutePeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxRipNgRouteEntry.setStatus("current")
_TmnxRipNgRouteDestAddrType_Type = InetAddressType
_TmnxRipNgRouteDestAddrType_Object = MibTableColumn
tmnxRipNgRouteDestAddrType = _TmnxRipNgRouteDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 1),
    _TmnxRipNgRouteDestAddrType_Type()
)
tmnxRipNgRouteDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRouteDestAddrType.setStatus("current")


class _TmnxRipNgRouteDestAddress_Type(InetAddress):
    """Custom type tmnxRipNgRouteDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgRouteDestAddress_Type.__name__ = "InetAddress"
_TmnxRipNgRouteDestAddress_Object = MibTableColumn
tmnxRipNgRouteDestAddress = _TmnxRipNgRouteDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 2),
    _TmnxRipNgRouteDestAddress_Type()
)
tmnxRipNgRouteDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRouteDestAddress.setStatus("current")


class _TmnxRipNgRouteMaskLength_Type(InetAddressPrefixLength):
    """Custom type tmnxRipNgRouteMaskLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxRipNgRouteMaskLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxRipNgRouteMaskLength_Object = MibTableColumn
tmnxRipNgRouteMaskLength = _TmnxRipNgRouteMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 3),
    _TmnxRipNgRouteMaskLength_Type()
)
tmnxRipNgRouteMaskLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRouteMaskLength.setStatus("current")
_TmnxRipNgRouteIfIndex_Type = InterfaceIndex
_TmnxRipNgRouteIfIndex_Object = MibTableColumn
tmnxRipNgRouteIfIndex = _TmnxRipNgRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 4),
    _TmnxRipNgRouteIfIndex_Type()
)
tmnxRipNgRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRouteIfIndex.setStatus("current")
_TmnxRipNgRoutePeerAddrType_Type = InetAddressType
_TmnxRipNgRoutePeerAddrType_Object = MibTableColumn
tmnxRipNgRoutePeerAddrType = _TmnxRipNgRoutePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 5),
    _TmnxRipNgRoutePeerAddrType_Type()
)
tmnxRipNgRoutePeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRoutePeerAddrType.setStatus("current")


class _TmnxRipNgRoutePeerAddress_Type(InetAddress):
    """Custom type tmnxRipNgRoutePeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgRoutePeerAddress_Type.__name__ = "InetAddress"
_TmnxRipNgRoutePeerAddress_Object = MibTableColumn
tmnxRipNgRoutePeerAddress = _TmnxRipNgRoutePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 6),
    _TmnxRipNgRoutePeerAddress_Type()
)
tmnxRipNgRoutePeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgRoutePeerAddress.setStatus("current")
_TmnxRipNgRouteNHAddrType_Type = InetAddressType
_TmnxRipNgRouteNHAddrType_Object = MibTableColumn
tmnxRipNgRouteNHAddrType = _TmnxRipNgRouteNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 7),
    _TmnxRipNgRouteNHAddrType_Type()
)
tmnxRipNgRouteNHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteNHAddrType.setStatus("current")


class _TmnxRipNgRouteNHAddress_Type(InetAddress):
    """Custom type tmnxRipNgRouteNHAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgRouteNHAddress_Type.__name__ = "InetAddress"
_TmnxRipNgRouteNHAddress_Object = MibTableColumn
tmnxRipNgRouteNHAddress = _TmnxRipNgRouteNHAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 8),
    _TmnxRipNgRouteNHAddress_Type()
)
tmnxRipNgRouteNHAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteNHAddress.setStatus("current")
_TmnxRipNgRouteMetric_Type = TmnxRipNgMetric
_TmnxRipNgRouteMetric_Object = MibTableColumn
tmnxRipNgRouteMetric = _TmnxRipNgRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 9),
    _TmnxRipNgRouteMetric_Type()
)
tmnxRipNgRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteMetric.setStatus("current")
_TmnxRipNgRouteTag_Type = RouteTag
_TmnxRipNgRouteTag_Object = MibTableColumn
tmnxRipNgRouteTag = _TmnxRipNgRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 10),
    _TmnxRipNgRouteTag_Type()
)
tmnxRipNgRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteTag.setStatus("current")


class _TmnxRipNgRouteStatus_Type(Integer32):
    """Custom type tmnxRipNgRouteStatus based on Integer32"""
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


_TmnxRipNgRouteStatus_Type.__name__ = "Integer32"
_TmnxRipNgRouteStatus_Object = MibTableColumn
tmnxRipNgRouteStatus = _TmnxRipNgRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 11),
    _TmnxRipNgRouteStatus_Type()
)
tmnxRipNgRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteStatus.setStatus("current")
_TmnxRipNgRouteTimerRemaining_Type = Unsigned32
_TmnxRipNgRouteTimerRemaining_Object = MibTableColumn
tmnxRipNgRouteTimerRemaining = _TmnxRipNgRouteTimerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 12),
    _TmnxRipNgRouteTimerRemaining_Type()
)
tmnxRipNgRouteTimerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteTimerRemaining.setStatus("current")
_TmnxRipNgRouteFC_Type = TNamedItemOrEmpty
_TmnxRipNgRouteFC_Object = MibTableColumn
tmnxRipNgRouteFC = _TmnxRipNgRouteFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 13),
    _TmnxRipNgRouteFC_Type()
)
tmnxRipNgRouteFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteFC.setStatus("current")
_TmnxRipNgRouteFCPriority_Type = TPriorityOrUndefined
_TmnxRipNgRouteFCPriority_Object = MibTableColumn
tmnxRipNgRouteFCPriority = _TmnxRipNgRouteFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 4, 1, 14),
    _TmnxRipNgRouteFCPriority_Type()
)
tmnxRipNgRouteFCPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgRouteFCPriority.setStatus("current")
_TmnxRipNgIfStatTable_Object = MibTable
tmnxRipNgIfStatTable = _TmnxRipNgIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxRipNgIfStatTable.setStatus("current")
_TmnxRipNgIfStatEntry_Object = MibTableRow
tmnxRipNgIfStatEntry = _TmnxRipNgIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1)
)
tmnxRipNgIfStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxRipNgIfStatEntry.setStatus("current")
_TmnxRipNgIfStatAllSentUpdates_Type = Counter32
_TmnxRipNgIfStatAllSentUpdates_Object = MibTableColumn
tmnxRipNgIfStatAllSentUpdates = _TmnxRipNgIfStatAllSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 1),
    _TmnxRipNgIfStatAllSentUpdates_Type()
)
tmnxRipNgIfStatAllSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllSentUpdates.setStatus("current")
_TmnxRipNgIfStatAllTrigUpdates_Type = Counter32
_TmnxRipNgIfStatAllTrigUpdates_Object = MibTableColumn
tmnxRipNgIfStatAllTrigUpdates = _TmnxRipNgIfStatAllTrigUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 2),
    _TmnxRipNgIfStatAllTrigUpdates_Type()
)
tmnxRipNgIfStatAllTrigUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllTrigUpdates.setStatus("current")
_TmnxRipNgIfStatAllRcvBadPkts_Type = Counter32
_TmnxRipNgIfStatAllRcvBadPkts_Object = MibTableColumn
tmnxRipNgIfStatAllRcvBadPkts = _TmnxRipNgIfStatAllRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 3),
    _TmnxRipNgIfStatAllRcvBadPkts_Type()
)
tmnxRipNgIfStatAllRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllRcvBadPkts.setStatus("current")
_TmnxRipNgIfStatV1RcvUpdates_Type = Counter32
_TmnxRipNgIfStatV1RcvUpdates_Object = MibTableColumn
tmnxRipNgIfStatV1RcvUpdates = _TmnxRipNgIfStatV1RcvUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 4),
    _TmnxRipNgIfStatV1RcvUpdates_Type()
)
tmnxRipNgIfStatV1RcvUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvUpdates.setStatus("current")
_TmnxRipNgIfStatV1RcvRequests_Type = Counter32
_TmnxRipNgIfStatV1RcvRequests_Object = MibTableColumn
tmnxRipNgIfStatV1RcvRequests = _TmnxRipNgIfStatV1RcvRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 5),
    _TmnxRipNgIfStatV1RcvRequests_Type()
)
tmnxRipNgIfStatV1RcvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvRequests.setStatus("current")
_TmnxRipNgIfStatV1BadUpdates_Type = Counter32
_TmnxRipNgIfStatV1BadUpdates_Object = MibTableColumn
tmnxRipNgIfStatV1BadUpdates = _TmnxRipNgIfStatV1BadUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 6),
    _TmnxRipNgIfStatV1BadUpdates_Type()
)
tmnxRipNgIfStatV1BadUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadUpdates.setStatus("current")
_TmnxRipNgIfStatV1BadRequests_Type = Counter32
_TmnxRipNgIfStatV1BadRequests_Object = MibTableColumn
tmnxRipNgIfStatV1BadRequests = _TmnxRipNgIfStatV1BadRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 7),
    _TmnxRipNgIfStatV1BadRequests_Type()
)
tmnxRipNgIfStatV1BadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRequests.setStatus("current")
_TmnxRipNgIfStatV1BadRoutes_Type = Counter32
_TmnxRipNgIfStatV1BadRoutes_Object = MibTableColumn
tmnxRipNgIfStatV1BadRoutes = _TmnxRipNgIfStatV1BadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 8),
    _TmnxRipNgIfStatV1BadRoutes_Type()
)
tmnxRipNgIfStatV1BadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRoutes.setStatus("current")
_TmnxRipNgIfStatV2RcvUpdates_Type = Counter32
_TmnxRipNgIfStatV2RcvUpdates_Object = MibTableColumn
tmnxRipNgIfStatV2RcvUpdates = _TmnxRipNgIfStatV2RcvUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 9),
    _TmnxRipNgIfStatV2RcvUpdates_Type()
)
tmnxRipNgIfStatV2RcvUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvUpdates.setStatus("current")
_TmnxRipNgIfStatV2RcvRequests_Type = Counter32
_TmnxRipNgIfStatV2RcvRequests_Object = MibTableColumn
tmnxRipNgIfStatV2RcvRequests = _TmnxRipNgIfStatV2RcvRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 10),
    _TmnxRipNgIfStatV2RcvRequests_Type()
)
tmnxRipNgIfStatV2RcvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvRequests.setStatus("current")
_TmnxRipNgIfStatV2BadUpdates_Type = Counter32
_TmnxRipNgIfStatV2BadUpdates_Object = MibTableColumn
tmnxRipNgIfStatV2BadUpdates = _TmnxRipNgIfStatV2BadUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 11),
    _TmnxRipNgIfStatV2BadUpdates_Type()
)
tmnxRipNgIfStatV2BadUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadUpdates.setStatus("current")
_TmnxRipNgIfStatV2BadRequests_Type = Counter32
_TmnxRipNgIfStatV2BadRequests_Object = MibTableColumn
tmnxRipNgIfStatV2BadRequests = _TmnxRipNgIfStatV2BadRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 12),
    _TmnxRipNgIfStatV2BadRequests_Type()
)
tmnxRipNgIfStatV2BadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRequests.setStatus("current")
_TmnxRipNgIfStatV2BadRoutes_Type = Counter32
_TmnxRipNgIfStatV2BadRoutes_Object = MibTableColumn
tmnxRipNgIfStatV2BadRoutes = _TmnxRipNgIfStatV2BadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 13),
    _TmnxRipNgIfStatV2BadRoutes_Type()
)
tmnxRipNgIfStatV2BadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRoutes.setStatus("current")
_TmnxRipNgIfStatAuthErrors_Type = Counter32
_TmnxRipNgIfStatAuthErrors_Object = MibTableColumn
tmnxRipNgIfStatAuthErrors = _TmnxRipNgIfStatAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 14),
    _TmnxRipNgIfStatAuthErrors_Type()
)
tmnxRipNgIfStatAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAuthErrors.setStatus("current")
_TmnxRipNgIfStatAllSentUpdts5Min_Type = Counter32
_TmnxRipNgIfStatAllSentUpdts5Min_Object = MibTableColumn
tmnxRipNgIfStatAllSentUpdts5Min = _TmnxRipNgIfStatAllSentUpdts5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 15),
    _TmnxRipNgIfStatAllSentUpdts5Min_Type()
)
tmnxRipNgIfStatAllSentUpdts5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllSentUpdts5Min.setStatus("current")
_TmnxRipNgIfStatAllTrigUpdts5Min_Type = Counter32
_TmnxRipNgIfStatAllTrigUpdts5Min_Object = MibTableColumn
tmnxRipNgIfStatAllTrigUpdts5Min = _TmnxRipNgIfStatAllTrigUpdts5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 16),
    _TmnxRipNgIfStatAllTrigUpdts5Min_Type()
)
tmnxRipNgIfStatAllTrigUpdts5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllTrigUpdts5Min.setStatus("current")
_TmnxRipNgIfStatAllRcvBadPkts5Min_Type = Counter32
_TmnxRipNgIfStatAllRcvBadPkts5Min_Object = MibTableColumn
tmnxRipNgIfStatAllRcvBadPkts5Min = _TmnxRipNgIfStatAllRcvBadPkts5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 17),
    _TmnxRipNgIfStatAllRcvBadPkts5Min_Type()
)
tmnxRipNgIfStatAllRcvBadPkts5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllRcvBadPkts5Min.setStatus("current")
_TmnxRipNgIfStatV1RcvUpdates5Min_Type = Counter32
_TmnxRipNgIfStatV1RcvUpdates5Min_Object = MibTableColumn
tmnxRipNgIfStatV1RcvUpdates5Min = _TmnxRipNgIfStatV1RcvUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 18),
    _TmnxRipNgIfStatV1RcvUpdates5Min_Type()
)
tmnxRipNgIfStatV1RcvUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvUpdates5Min.setStatus("current")
_TmnxRipNgIfStatV1RcvRequests5Min_Type = Counter32
_TmnxRipNgIfStatV1RcvRequests5Min_Object = MibTableColumn
tmnxRipNgIfStatV1RcvRequests5Min = _TmnxRipNgIfStatV1RcvRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 19),
    _TmnxRipNgIfStatV1RcvRequests5Min_Type()
)
tmnxRipNgIfStatV1RcvRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvRequests5Min.setStatus("current")
_TmnxRipNgIfStatV1BadUpdates5Min_Type = Counter32
_TmnxRipNgIfStatV1BadUpdates5Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadUpdates5Min = _TmnxRipNgIfStatV1BadUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 20),
    _TmnxRipNgIfStatV1BadUpdates5Min_Type()
)
tmnxRipNgIfStatV1BadUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadUpdates5Min.setStatus("current")
_TmnxRipNgIfStatV1BadRequests5Min_Type = Counter32
_TmnxRipNgIfStatV1BadRequests5Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadRequests5Min = _TmnxRipNgIfStatV1BadRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 21),
    _TmnxRipNgIfStatV1BadRequests5Min_Type()
)
tmnxRipNgIfStatV1BadRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRequests5Min.setStatus("current")
_TmnxRipNgIfStatV1BadRoutes5Min_Type = Counter32
_TmnxRipNgIfStatV1BadRoutes5Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadRoutes5Min = _TmnxRipNgIfStatV1BadRoutes5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 22),
    _TmnxRipNgIfStatV1BadRoutes5Min_Type()
)
tmnxRipNgIfStatV1BadRoutes5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRoutes5Min.setStatus("current")
_TmnxRipNgIfStatV2RcvUpdates5Min_Type = Counter32
_TmnxRipNgIfStatV2RcvUpdates5Min_Object = MibTableColumn
tmnxRipNgIfStatV2RcvUpdates5Min = _TmnxRipNgIfStatV2RcvUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 23),
    _TmnxRipNgIfStatV2RcvUpdates5Min_Type()
)
tmnxRipNgIfStatV2RcvUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvUpdates5Min.setStatus("current")
_TmnxRipNgIfStatV2RcvRequests5Min_Type = Counter32
_TmnxRipNgIfStatV2RcvRequests5Min_Object = MibTableColumn
tmnxRipNgIfStatV2RcvRequests5Min = _TmnxRipNgIfStatV2RcvRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 24),
    _TmnxRipNgIfStatV2RcvRequests5Min_Type()
)
tmnxRipNgIfStatV2RcvRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvRequests5Min.setStatus("current")
_TmnxRipNgIfStatV2BadUpdates5Min_Type = Counter32
_TmnxRipNgIfStatV2BadUpdates5Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadUpdates5Min = _TmnxRipNgIfStatV2BadUpdates5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 25),
    _TmnxRipNgIfStatV2BadUpdates5Min_Type()
)
tmnxRipNgIfStatV2BadUpdates5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadUpdates5Min.setStatus("current")
_TmnxRipNgIfStatV2BadRequests5Min_Type = Counter32
_TmnxRipNgIfStatV2BadRequests5Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadRequests5Min = _TmnxRipNgIfStatV2BadRequests5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 26),
    _TmnxRipNgIfStatV2BadRequests5Min_Type()
)
tmnxRipNgIfStatV2BadRequests5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRequests5Min.setStatus("current")
_TmnxRipNgIfStatV2BadRoutes5Min_Type = Counter32
_TmnxRipNgIfStatV2BadRoutes5Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadRoutes5Min = _TmnxRipNgIfStatV2BadRoutes5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 27),
    _TmnxRipNgIfStatV2BadRoutes5Min_Type()
)
tmnxRipNgIfStatV2BadRoutes5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRoutes5Min.setStatus("current")
_TmnxRipNgIfStatAuthErrors5Min_Type = Counter32
_TmnxRipNgIfStatAuthErrors5Min_Object = MibTableColumn
tmnxRipNgIfStatAuthErrors5Min = _TmnxRipNgIfStatAuthErrors5Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 28),
    _TmnxRipNgIfStatAuthErrors5Min_Type()
)
tmnxRipNgIfStatAuthErrors5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAuthErrors5Min.setStatus("current")
_TmnxRipNgIfStatAllSentUpdts1Min_Type = Counter32
_TmnxRipNgIfStatAllSentUpdts1Min_Object = MibTableColumn
tmnxRipNgIfStatAllSentUpdts1Min = _TmnxRipNgIfStatAllSentUpdts1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 29),
    _TmnxRipNgIfStatAllSentUpdts1Min_Type()
)
tmnxRipNgIfStatAllSentUpdts1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllSentUpdts1Min.setStatus("current")
_TmnxRipNgIfStatAllTrigUpdts1Min_Type = Counter32
_TmnxRipNgIfStatAllTrigUpdts1Min_Object = MibTableColumn
tmnxRipNgIfStatAllTrigUpdts1Min = _TmnxRipNgIfStatAllTrigUpdts1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 30),
    _TmnxRipNgIfStatAllTrigUpdts1Min_Type()
)
tmnxRipNgIfStatAllTrigUpdts1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllTrigUpdts1Min.setStatus("current")
_TmnxRipNgIfStatAllRcvBadPkts1Min_Type = Counter32
_TmnxRipNgIfStatAllRcvBadPkts1Min_Object = MibTableColumn
tmnxRipNgIfStatAllRcvBadPkts1Min = _TmnxRipNgIfStatAllRcvBadPkts1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 31),
    _TmnxRipNgIfStatAllRcvBadPkts1Min_Type()
)
tmnxRipNgIfStatAllRcvBadPkts1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAllRcvBadPkts1Min.setStatus("current")
_TmnxRipNgIfStatV1RcvUpdates1Min_Type = Counter32
_TmnxRipNgIfStatV1RcvUpdates1Min_Object = MibTableColumn
tmnxRipNgIfStatV1RcvUpdates1Min = _TmnxRipNgIfStatV1RcvUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 32),
    _TmnxRipNgIfStatV1RcvUpdates1Min_Type()
)
tmnxRipNgIfStatV1RcvUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvUpdates1Min.setStatus("current")
_TmnxRipNgIfStatV1RcvRequests1Min_Type = Counter32
_TmnxRipNgIfStatV1RcvRequests1Min_Object = MibTableColumn
tmnxRipNgIfStatV1RcvRequests1Min = _TmnxRipNgIfStatV1RcvRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 33),
    _TmnxRipNgIfStatV1RcvRequests1Min_Type()
)
tmnxRipNgIfStatV1RcvRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1RcvRequests1Min.setStatus("current")
_TmnxRipNgIfStatV1BadUpdates1Min_Type = Counter32
_TmnxRipNgIfStatV1BadUpdates1Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadUpdates1Min = _TmnxRipNgIfStatV1BadUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 34),
    _TmnxRipNgIfStatV1BadUpdates1Min_Type()
)
tmnxRipNgIfStatV1BadUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadUpdates1Min.setStatus("current")
_TmnxRipNgIfStatV1BadRequests1Min_Type = Counter32
_TmnxRipNgIfStatV1BadRequests1Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadRequests1Min = _TmnxRipNgIfStatV1BadRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 35),
    _TmnxRipNgIfStatV1BadRequests1Min_Type()
)
tmnxRipNgIfStatV1BadRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRequests1Min.setStatus("current")
_TmnxRipNgIfStatV1BadRoutes1Min_Type = Counter32
_TmnxRipNgIfStatV1BadRoutes1Min_Object = MibTableColumn
tmnxRipNgIfStatV1BadRoutes1Min = _TmnxRipNgIfStatV1BadRoutes1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 36),
    _TmnxRipNgIfStatV1BadRoutes1Min_Type()
)
tmnxRipNgIfStatV1BadRoutes1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV1BadRoutes1Min.setStatus("current")
_TmnxRipNgIfStatV2RcvUpdates1Min_Type = Counter32
_TmnxRipNgIfStatV2RcvUpdates1Min_Object = MibTableColumn
tmnxRipNgIfStatV2RcvUpdates1Min = _TmnxRipNgIfStatV2RcvUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 37),
    _TmnxRipNgIfStatV2RcvUpdates1Min_Type()
)
tmnxRipNgIfStatV2RcvUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvUpdates1Min.setStatus("current")
_TmnxRipNgIfStatV2RcvRequests1Min_Type = Counter32
_TmnxRipNgIfStatV2RcvRequests1Min_Object = MibTableColumn
tmnxRipNgIfStatV2RcvRequests1Min = _TmnxRipNgIfStatV2RcvRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 38),
    _TmnxRipNgIfStatV2RcvRequests1Min_Type()
)
tmnxRipNgIfStatV2RcvRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2RcvRequests1Min.setStatus("current")
_TmnxRipNgIfStatV2BadUpdates1Min_Type = Counter32
_TmnxRipNgIfStatV2BadUpdates1Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadUpdates1Min = _TmnxRipNgIfStatV2BadUpdates1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 39),
    _TmnxRipNgIfStatV2BadUpdates1Min_Type()
)
tmnxRipNgIfStatV2BadUpdates1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadUpdates1Min.setStatus("current")
_TmnxRipNgIfStatV2BadRequests1Min_Type = Counter32
_TmnxRipNgIfStatV2BadRequests1Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadRequests1Min = _TmnxRipNgIfStatV2BadRequests1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 40),
    _TmnxRipNgIfStatV2BadRequests1Min_Type()
)
tmnxRipNgIfStatV2BadRequests1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRequests1Min.setStatus("current")
_TmnxRipNgIfStatV2BadRoutes1Min_Type = Counter32
_TmnxRipNgIfStatV2BadRoutes1Min_Object = MibTableColumn
tmnxRipNgIfStatV2BadRoutes1Min = _TmnxRipNgIfStatV2BadRoutes1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 41),
    _TmnxRipNgIfStatV2BadRoutes1Min_Type()
)
tmnxRipNgIfStatV2BadRoutes1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatV2BadRoutes1Min.setStatus("current")
_TmnxRipNgIfStatAuthErrors1Min_Type = Counter32
_TmnxRipNgIfStatAuthErrors1Min_Object = MibTableColumn
tmnxRipNgIfStatAuthErrors1Min = _TmnxRipNgIfStatAuthErrors1Min_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 5, 1, 42),
    _TmnxRipNgIfStatAuthErrors1Min_Type()
)
tmnxRipNgIfStatAuthErrors1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgIfStatAuthErrors1Min.setStatus("current")
_TmnxRipNgPeerTable_Object = MibTable
tmnxRipNgPeerTable = _TmnxRipNgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxRipNgPeerTable.setStatus("current")
_TmnxRipNgPeerEntry_Object = MibTableRow
tmnxRipNgPeerEntry = _TmnxRipNgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1)
)
tmnxRipNgPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerIfIndex"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxRipNgPeerEntry.setStatus("current")
_TmnxRipNgPeerIfIndex_Type = InterfaceIndex
_TmnxRipNgPeerIfIndex_Object = MibTableColumn
tmnxRipNgPeerIfIndex = _TmnxRipNgPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 1),
    _TmnxRipNgPeerIfIndex_Type()
)
tmnxRipNgPeerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgPeerIfIndex.setStatus("current")
_TmnxRipNgPeerAddrType_Type = InetAddressType
_TmnxRipNgPeerAddrType_Object = MibTableColumn
tmnxRipNgPeerAddrType = _TmnxRipNgPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 2),
    _TmnxRipNgPeerAddrType_Type()
)
tmnxRipNgPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgPeerAddrType.setStatus("current")


class _TmnxRipNgPeerAddress_Type(InetAddress):
    """Custom type tmnxRipNgPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgPeerAddress_Type.__name__ = "InetAddress"
_TmnxRipNgPeerAddress_Object = MibTableColumn
tmnxRipNgPeerAddress = _TmnxRipNgPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 3),
    _TmnxRipNgPeerAddress_Type()
)
tmnxRipNgPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgPeerAddress.setStatus("current")
_TmnxRipNgPeerLastUpdate_Type = TimeStamp
_TmnxRipNgPeerLastUpdate_Object = MibTableColumn
tmnxRipNgPeerLastUpdate = _TmnxRipNgPeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 4),
    _TmnxRipNgPeerLastUpdate_Type()
)
tmnxRipNgPeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgPeerLastUpdate.setStatus("current")
_TmnxRipNgPeerVersion_Type = TmnxRipNgPeerVersion
_TmnxRipNgPeerVersion_Object = MibTableColumn
tmnxRipNgPeerVersion = _TmnxRipNgPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 5),
    _TmnxRipNgPeerVersion_Type()
)
tmnxRipNgPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgPeerVersion.setStatus("current")
_TmnxRipNgPeerRcvBadPackets_Type = Counter32
_TmnxRipNgPeerRcvBadPackets_Object = MibTableColumn
tmnxRipNgPeerRcvBadPackets = _TmnxRipNgPeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 6),
    _TmnxRipNgPeerRcvBadPackets_Type()
)
tmnxRipNgPeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgPeerRcvBadPackets.setStatus("current")
_TmnxRipNgPeerRcvBadRoutes_Type = Counter32
_TmnxRipNgPeerRcvBadRoutes_Object = MibTableColumn
tmnxRipNgPeerRcvBadRoutes = _TmnxRipNgPeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 6, 1, 7),
    _TmnxRipNgPeerRcvBadRoutes_Type()
)
tmnxRipNgPeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgPeerRcvBadRoutes.setStatus("current")
_TmnxRipNgAdvRouteTable_Object = MibTable
tmnxRipNgAdvRouteTable = _TmnxRipNgAdvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteTable.setStatus("current")
_TmnxRipNgAdvRouteEntry_Object = MibTableRow
tmnxRipNgAdvRouteEntry = _TmnxRipNgAdvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1)
)
tmnxRipNgAdvRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteDestAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteDestAddress"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteMaskLength"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteIfIndex"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteIfAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteIfAddress"),
)
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteEntry.setStatus("current")
_TmnxRipNgAdvRouteDestAddrType_Type = InetAddressType
_TmnxRipNgAdvRouteDestAddrType_Object = MibTableColumn
tmnxRipNgAdvRouteDestAddrType = _TmnxRipNgAdvRouteDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 1),
    _TmnxRipNgAdvRouteDestAddrType_Type()
)
tmnxRipNgAdvRouteDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteDestAddrType.setStatus("current")


class _TmnxRipNgAdvRouteDestAddress_Type(InetAddress):
    """Custom type tmnxRipNgAdvRouteDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgAdvRouteDestAddress_Type.__name__ = "InetAddress"
_TmnxRipNgAdvRouteDestAddress_Object = MibTableColumn
tmnxRipNgAdvRouteDestAddress = _TmnxRipNgAdvRouteDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 2),
    _TmnxRipNgAdvRouteDestAddress_Type()
)
tmnxRipNgAdvRouteDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteDestAddress.setStatus("current")


class _TmnxRipNgAdvRouteMaskLength_Type(InetAddressPrefixLength):
    """Custom type tmnxRipNgAdvRouteMaskLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxRipNgAdvRouteMaskLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxRipNgAdvRouteMaskLength_Object = MibTableColumn
tmnxRipNgAdvRouteMaskLength = _TmnxRipNgAdvRouteMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 3),
    _TmnxRipNgAdvRouteMaskLength_Type()
)
tmnxRipNgAdvRouteMaskLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteMaskLength.setStatus("current")
_TmnxRipNgAdvRouteIfIndex_Type = InterfaceIndex
_TmnxRipNgAdvRouteIfIndex_Object = MibTableColumn
tmnxRipNgAdvRouteIfIndex = _TmnxRipNgAdvRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 4),
    _TmnxRipNgAdvRouteIfIndex_Type()
)
tmnxRipNgAdvRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteIfIndex.setStatus("current")
_TmnxRipNgAdvRouteIfAddrType_Type = InetAddressType
_TmnxRipNgAdvRouteIfAddrType_Object = MibTableColumn
tmnxRipNgAdvRouteIfAddrType = _TmnxRipNgAdvRouteIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 5),
    _TmnxRipNgAdvRouteIfAddrType_Type()
)
tmnxRipNgAdvRouteIfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteIfAddrType.setStatus("current")


class _TmnxRipNgAdvRouteIfAddress_Type(InetAddress):
    """Custom type tmnxRipNgAdvRouteIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgAdvRouteIfAddress_Type.__name__ = "InetAddress"
_TmnxRipNgAdvRouteIfAddress_Object = MibTableColumn
tmnxRipNgAdvRouteIfAddress = _TmnxRipNgAdvRouteIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 6),
    _TmnxRipNgAdvRouteIfAddress_Type()
)
tmnxRipNgAdvRouteIfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteIfAddress.setStatus("current")
_TmnxRipNgAdvRouteNHAddrType_Type = InetAddressType
_TmnxRipNgAdvRouteNHAddrType_Object = MibTableColumn
tmnxRipNgAdvRouteNHAddrType = _TmnxRipNgAdvRouteNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 7),
    _TmnxRipNgAdvRouteNHAddrType_Type()
)
tmnxRipNgAdvRouteNHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteNHAddrType.setStatus("current")


class _TmnxRipNgAdvRouteNHAddress_Type(InetAddress):
    """Custom type tmnxRipNgAdvRouteNHAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgAdvRouteNHAddress_Type.__name__ = "InetAddress"
_TmnxRipNgAdvRouteNHAddress_Object = MibTableColumn
tmnxRipNgAdvRouteNHAddress = _TmnxRipNgAdvRouteNHAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 8),
    _TmnxRipNgAdvRouteNHAddress_Type()
)
tmnxRipNgAdvRouteNHAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteNHAddress.setStatus("current")


class _TmnxRipNgAdvRouteMetric_Type(Unsigned32):
    """Custom type tmnxRipNgAdvRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxRipNgAdvRouteMetric_Type.__name__ = "Unsigned32"
_TmnxRipNgAdvRouteMetric_Object = MibTableColumn
tmnxRipNgAdvRouteMetric = _TmnxRipNgAdvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 9),
    _TmnxRipNgAdvRouteMetric_Type()
)
tmnxRipNgAdvRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteMetric.setStatus("current")
_TmnxRipNgAdvRouteTag_Type = RouteTag
_TmnxRipNgAdvRouteTag_Object = MibTableColumn
tmnxRipNgAdvRouteTag = _TmnxRipNgAdvRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 10),
    _TmnxRipNgAdvRouteTag_Type()
)
tmnxRipNgAdvRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteTag.setStatus("current")
_TmnxRipNgAdvRouteTimerRem_Type = Integer32
_TmnxRipNgAdvRouteTimerRem_Object = MibTableColumn
tmnxRipNgAdvRouteTimerRem = _TmnxRipNgAdvRouteTimerRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 7, 1, 11),
    _TmnxRipNgAdvRouteTimerRem_Type()
)
tmnxRipNgAdvRouteTimerRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRipNgAdvRouteTimerRem.setStatus("current")
_TmnxRipNgIfUcastTable_Object = MibTable
tmnxRipNgIfUcastTable = _TmnxRipNgIfUcastTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastTable.setStatus("current")
_TmnxRipNgIfUcastEntry_Object = MibTableRow
tmnxRipNgIfUcastEntry = _TmnxRipNgIfUcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 8, 1)
)
tmnxRipNgIfUcastEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgInstVersion"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgIfUcastAddrType"),
    (0, "TIMETRA-RIP-NG-MIB", "tmnxRipNgIfUcastAddress"),
)
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastEntry.setStatus("current")
_TmnxRipNgIfUcastAddrType_Type = InetAddressType
_TmnxRipNgIfUcastAddrType_Object = MibTableColumn
tmnxRipNgIfUcastAddrType = _TmnxRipNgIfUcastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 8, 1, 1),
    _TmnxRipNgIfUcastAddrType_Type()
)
tmnxRipNgIfUcastAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastAddrType.setStatus("current")


class _TmnxRipNgIfUcastAddress_Type(InetAddress):
    """Custom type tmnxRipNgIfUcastAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRipNgIfUcastAddress_Type.__name__ = "InetAddress"
_TmnxRipNgIfUcastAddress_Object = MibTableColumn
tmnxRipNgIfUcastAddress = _TmnxRipNgIfUcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 8, 1, 2),
    _TmnxRipNgIfUcastAddress_Type()
)
tmnxRipNgIfUcastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastAddress.setStatus("current")
_TmnxRipNgIfUcastRowStatus_Type = RowStatus
_TmnxRipNgIfUcastRowStatus_Object = MibTableColumn
tmnxRipNgIfUcastRowStatus = _TmnxRipNgIfUcastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 2, 8, 1, 3),
    _TmnxRipNgIfUcastRowStatus_Type()
)
tmnxRipNgIfUcastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastRowStatus.setStatus("current")
_TmnxRipNgNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxRipNgNotificationObjs = _TmnxRipNgNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 3)
)
_TmnxRipNgNotifySrcAddrType_Type = InetAddressType
_TmnxRipNgNotifySrcAddrType_Object = MibScalar
tmnxRipNgNotifySrcAddrType = _TmnxRipNgNotifySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 3, 1),
    _TmnxRipNgNotifySrcAddrType_Type()
)
tmnxRipNgNotifySrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRipNgNotifySrcAddrType.setStatus("current")
_TmnxRipNgNotifySrcAddr_Type = InetAddress
_TmnxRipNgNotifySrcAddr_Object = MibScalar
tmnxRipNgNotifySrcAddr = _TmnxRipNgNotifySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 3, 2),
    _TmnxRipNgNotifySrcAddr_Type()
)
tmnxRipNgNotifySrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRipNgNotifySrcAddr.setStatus("current")


class _TmnxRipNgNotifyReason_Type(DisplayString):
    """Custom type tmnxRipNgNotifyReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxRipNgNotifyReason_Type.__name__ = "DisplayString"
_TmnxRipNgNotifyReason_Object = MibScalar
tmnxRipNgNotifyReason = _TmnxRipNgNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 89, 3, 3),
    _TmnxRipNgNotifyReason_Type()
)
tmnxRipNgNotifyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRipNgNotifyReason.setStatus("current")
_TmnxRipNgNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxRipNgNotifyPrefix = _TmnxRipNgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89)
)
_TmnxRipNgNotifications_ObjectIdentity = ObjectIdentity
tmnxRipNgNotifications = _TmnxRipNgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0)
)

# Managed Objects groups

tmnxRipNgGlobalV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 1)
)
tmnxRipNgGlobalV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgGlobalLearnedRoutes"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGlobalTimedoutRoutes"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGlobalCurrentMemory"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGlobalMaximumMemory"))
)
if mibBuilder.loadTexts:
    tmnxRipNgGlobalV12v0Group.setStatus("current")

tmnxRipNgInstanceV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 2)
)
tmnxRipNgInstanceV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstAuthType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstAuthKey"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstCheckZero"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstMessageSize"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstMetricIn"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstMetricOut"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstPreference"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstReceive"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstSend"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstSplitHorizon"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstTimerFlush"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstTimerTimeout"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstTimerUpdate"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstImportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstImportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstImportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstImportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstImportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstDescription"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstAdminStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstOperStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstPropagateMetric"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportLimit"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExpLmtLogPct"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstTotalExpRoutes"))
)
if mibBuilder.loadTexts:
    tmnxRipNgInstanceV12v0Group.setStatus("current")

tmnxRipNgGroupV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 3)
)
tmnxRipNgGroupV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupAuthType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupAuthKey"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupCheckZero"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupMessageSize"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupMetricIn"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupMetricOut"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupPreference"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupReceive"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupSend"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupSplitHorizon"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupTimerFlush"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupTimerTimeout"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupTimerUpdate"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupImportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupImportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupImportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupImportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupImportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupExportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupExportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupExportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupExportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupExportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupDescription"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupInheritance"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupAdminStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupOperStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRipNgGroupV12v0Group.setStatus("current")

tmnxRipNgInterfaceV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 4)
)
tmnxRipNgInterfaceV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfGroupName"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfAuthType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfAuthKey"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfCheckZero"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfMessageSize"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfMetricIn"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfMetricOut"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfPreference"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfReceive"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfSend"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfSplitHorizon"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfTimerFlush"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfTimerTimeout"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfTimerUpdate"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfImportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfImportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfImportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfImportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfImportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfExportPolicy1"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfExportPolicy2"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfExportPolicy3"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfExportPolicy4"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfExportPolicy5"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfDescription"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfInheritance"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfAdminStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfOperStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfRowStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllSentUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllTrigUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllRcvBadPkts"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvRequests"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRequests"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRoutes"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvRequests"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadUpdates"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRequests"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRoutes"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAuthErrors"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllSentUpdts5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllTrigUpdts5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllRcvBadPkts5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvUpdates5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvRequests5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadUpdates5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRequests5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRoutes5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvUpdates5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvRequests5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadUpdates5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRequests5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRoutes5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAuthErrors5Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllSentUpdts1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllTrigUpdts1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAllRcvBadPkts1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvUpdates1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1RcvRequests1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadUpdates1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRequests1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV1BadRoutes1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvUpdates1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2RcvRequests1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadUpdates1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRequests1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatV2BadRoutes1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfStatAuthErrors1Min"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfUcastRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRipNgInterfaceV12v0Group.setStatus("current")

tmnxRipNgRoutesV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 5)
)
tmnxRipNgRoutesV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteNHAddrType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteNHAddress"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteMetric"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteTag"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteTimerRemaining"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteFC"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRouteFCPriority"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteNHAddrType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteNHAddress"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteMetric"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteTag"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAdvRouteTimerRem"))
)
if mibBuilder.loadTexts:
    tmnxRipNgRoutesV12v0Group.setStatus("current")

tmnxRipNgPeerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 6)
)
tmnxRipNgPeerV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerLastUpdate"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerVersion"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerRcvBadPackets"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerRcvBadRoutes"))
)
if mibBuilder.loadTexts:
    tmnxRipNgPeerV12v0Group.setStatus("current")

tmnxRipNgNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 7)
)
tmnxRipNgNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgNotifySrcAddrType"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgNotifySrcAddr"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxRipNgNotifyObjsV12v0Group.setStatus("current")


# Notification objects

tmnxRipNgAuthTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 1)
)
tmnxRipNgAuthTypeMismatch.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerLastUpdate")
)
if mibBuilder.loadTexts:
    tmnxRipNgAuthTypeMismatch.setStatus(
        "current"
    )

tmnxRipNgAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 2)
)
tmnxRipNgAuthFailure.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerLastUpdate")
)
if mibBuilder.loadTexts:
    tmnxRipNgAuthFailure.setStatus(
        "current"
    )

tmnxRipNgInstShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 3)
)
tmnxRipNgInstShuttingDown.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstOperStatus"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxRipNgInstShuttingDown.setStatus(
        "current"
    )

tmnxRipNgInstRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 4)
)
tmnxRipNgInstRestarted.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstOperStatus")
)
if mibBuilder.loadTexts:
    tmnxRipNgInstRestarted.setStatus(
        "current"
    )

tmnxRipNgInstExpLmtReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 5)
)
tmnxRipNgInstExpLmtReached.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportLimit")
)
if mibBuilder.loadTexts:
    tmnxRipNgInstExpLmtReached.setStatus(
        "current"
    )

tmnxRipNgInstExpLmtWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 6)
)
tmnxRipNgInstExpLmtWarning.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportLimit"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExpLmtLogPct"))
)
if mibBuilder.loadTexts:
    tmnxRipNgInstExpLmtWarning.setStatus(
        "current"
    )

tmnxRipNgInstRtsExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 7)
)
tmnxRipNgInstRtsExpLmtDropped.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExportLimit")
)
if mibBuilder.loadTexts:
    tmnxRipNgInstRtsExpLmtDropped.setStatus(
        "current"
    )

tmnxRipNgIfUcastAddrNotUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 89, 0, 8)
)
tmnxRipNgIfUcastAddrNotUsed.setObjects(
    ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfRowStatus")
)
if mibBuilder.loadTexts:
    tmnxRipNgIfUcastAddrNotUsed.setStatus(
        "current"
    )


# Notifications groups

tmnxRipNgNotificationV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 2, 8)
)
tmnxRipNgNotificationV12v0Group.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgAuthTypeMismatch"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgAuthFailure"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstShuttingDown"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstRestarted"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExpLmtReached"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstExpLmtWarning"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstRtsExpLmtDropped"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgIfUcastAddrNotUsed"))
)
if mibBuilder.loadTexts:
    tmnxRipNgNotificationV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxRipNgV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 89, 1, 1)
)
tmnxRipNgV12v0Compliance.setObjects(
      *(("TIMETRA-RIP-NG-MIB", "tmnxRipNgGlobalV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInstanceV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgGroupV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgInterfaceV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgRoutesV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgPeerV12v0Group"),
        ("TIMETRA-RIP-NG-MIB", "tmnxRipNgNotificationV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxRipNgV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-RIP-NG-MIB",
    **{"TmnxRipNgInstVersion": TmnxRipNgInstVersion,
       "TmnxRipNgPeerVersion": TmnxRipNgPeerVersion,
       "TmnxRipNgAuthType": TmnxRipNgAuthType,
       "TmnxRipNgAuthKey": TmnxRipNgAuthKey,
       "TmnxRipNgMessageSize": TmnxRipNgMessageSize,
       "TmnxRipNgMetric": TmnxRipNgMetric,
       "TmnxRipNgPreference": TmnxRipNgPreference,
       "TmnxRipNgReceive": TmnxRipNgReceive,
       "TmnxRipNgSend": TmnxRipNgSend,
       "TmnxRipNgTimerFlush": TmnxRipNgTimerFlush,
       "TmnxRipNgTimerTimeout": TmnxRipNgTimerTimeout,
       "TmnxRipNgTimerUpdate": TmnxRipNgTimerUpdate,
       "timetraRipNgMIBModule": timetraRipNgMIBModule,
       "tmnxRipNgConformance": tmnxRipNgConformance,
       "tmnxRipNgCompliances": tmnxRipNgCompliances,
       "tmnxRipNgV12v0Compliance": tmnxRipNgV12v0Compliance,
       "tmnxRipNgGroups": tmnxRipNgGroups,
       "tmnxRipNgGlobalV12v0Group": tmnxRipNgGlobalV12v0Group,
       "tmnxRipNgInstanceV12v0Group": tmnxRipNgInstanceV12v0Group,
       "tmnxRipNgGroupV12v0Group": tmnxRipNgGroupV12v0Group,
       "tmnxRipNgInterfaceV12v0Group": tmnxRipNgInterfaceV12v0Group,
       "tmnxRipNgRoutesV12v0Group": tmnxRipNgRoutesV12v0Group,
       "tmnxRipNgPeerV12v0Group": tmnxRipNgPeerV12v0Group,
       "tmnxRipNgNotifyObjsV12v0Group": tmnxRipNgNotifyObjsV12v0Group,
       "tmnxRipNgNotificationV12v0Group": tmnxRipNgNotificationV12v0Group,
       "tmnxRipNgObjs": tmnxRipNgObjs,
       "tmnxRipNgGlobals": tmnxRipNgGlobals,
       "tmnxRipNgGlobalLearnedRoutes": tmnxRipNgGlobalLearnedRoutes,
       "tmnxRipNgGlobalTimedoutRoutes": tmnxRipNgGlobalTimedoutRoutes,
       "tmnxRipNgGlobalCurrentMemory": tmnxRipNgGlobalCurrentMemory,
       "tmnxRipNgGlobalMaximumMemory": tmnxRipNgGlobalMaximumMemory,
       "tmnxRipNgTableObjs": tmnxRipNgTableObjs,
       "tmnxRipNgInstTable": tmnxRipNgInstTable,
       "tmnxRipNgInstEntry": tmnxRipNgInstEntry,
       "tmnxRipNgInstVersion": tmnxRipNgInstVersion,
       "tmnxRipNgInstAuthType": tmnxRipNgInstAuthType,
       "tmnxRipNgInstAuthKey": tmnxRipNgInstAuthKey,
       "tmnxRipNgInstCheckZero": tmnxRipNgInstCheckZero,
       "tmnxRipNgInstMessageSize": tmnxRipNgInstMessageSize,
       "tmnxRipNgInstMetricIn": tmnxRipNgInstMetricIn,
       "tmnxRipNgInstMetricOut": tmnxRipNgInstMetricOut,
       "tmnxRipNgInstPreference": tmnxRipNgInstPreference,
       "tmnxRipNgInstReceive": tmnxRipNgInstReceive,
       "tmnxRipNgInstSend": tmnxRipNgInstSend,
       "tmnxRipNgInstSplitHorizon": tmnxRipNgInstSplitHorizon,
       "tmnxRipNgInstTimerFlush": tmnxRipNgInstTimerFlush,
       "tmnxRipNgInstTimerTimeout": tmnxRipNgInstTimerTimeout,
       "tmnxRipNgInstTimerUpdate": tmnxRipNgInstTimerUpdate,
       "tmnxRipNgInstImportPolicy1": tmnxRipNgInstImportPolicy1,
       "tmnxRipNgInstImportPolicy2": tmnxRipNgInstImportPolicy2,
       "tmnxRipNgInstImportPolicy3": tmnxRipNgInstImportPolicy3,
       "tmnxRipNgInstImportPolicy4": tmnxRipNgInstImportPolicy4,
       "tmnxRipNgInstImportPolicy5": tmnxRipNgInstImportPolicy5,
       "tmnxRipNgInstExportPolicy1": tmnxRipNgInstExportPolicy1,
       "tmnxRipNgInstExportPolicy2": tmnxRipNgInstExportPolicy2,
       "tmnxRipNgInstExportPolicy3": tmnxRipNgInstExportPolicy3,
       "tmnxRipNgInstExportPolicy4": tmnxRipNgInstExportPolicy4,
       "tmnxRipNgInstExportPolicy5": tmnxRipNgInstExportPolicy5,
       "tmnxRipNgInstDescription": tmnxRipNgInstDescription,
       "tmnxRipNgInstAdminStatus": tmnxRipNgInstAdminStatus,
       "tmnxRipNgInstOperStatus": tmnxRipNgInstOperStatus,
       "tmnxRipNgInstPropagateMetric": tmnxRipNgInstPropagateMetric,
       "tmnxRipNgInstExportLimit": tmnxRipNgInstExportLimit,
       "tmnxRipNgInstExpLmtLogPct": tmnxRipNgInstExpLmtLogPct,
       "tmnxRipNgInstTotalExpRoutes": tmnxRipNgInstTotalExpRoutes,
       "tmnxRipNgGroupTable": tmnxRipNgGroupTable,
       "tmnxRipNgGroupEntry": tmnxRipNgGroupEntry,
       "tmnxRipNgGroupName": tmnxRipNgGroupName,
       "tmnxRipNgGroupAuthType": tmnxRipNgGroupAuthType,
       "tmnxRipNgGroupAuthKey": tmnxRipNgGroupAuthKey,
       "tmnxRipNgGroupCheckZero": tmnxRipNgGroupCheckZero,
       "tmnxRipNgGroupMessageSize": tmnxRipNgGroupMessageSize,
       "tmnxRipNgGroupMetricIn": tmnxRipNgGroupMetricIn,
       "tmnxRipNgGroupMetricOut": tmnxRipNgGroupMetricOut,
       "tmnxRipNgGroupPreference": tmnxRipNgGroupPreference,
       "tmnxRipNgGroupReceive": tmnxRipNgGroupReceive,
       "tmnxRipNgGroupSend": tmnxRipNgGroupSend,
       "tmnxRipNgGroupSplitHorizon": tmnxRipNgGroupSplitHorizon,
       "tmnxRipNgGroupTimerFlush": tmnxRipNgGroupTimerFlush,
       "tmnxRipNgGroupTimerTimeout": tmnxRipNgGroupTimerTimeout,
       "tmnxRipNgGroupTimerUpdate": tmnxRipNgGroupTimerUpdate,
       "tmnxRipNgGroupImportPolicy1": tmnxRipNgGroupImportPolicy1,
       "tmnxRipNgGroupImportPolicy2": tmnxRipNgGroupImportPolicy2,
       "tmnxRipNgGroupImportPolicy3": tmnxRipNgGroupImportPolicy3,
       "tmnxRipNgGroupImportPolicy4": tmnxRipNgGroupImportPolicy4,
       "tmnxRipNgGroupImportPolicy5": tmnxRipNgGroupImportPolicy5,
       "tmnxRipNgGroupExportPolicy1": tmnxRipNgGroupExportPolicy1,
       "tmnxRipNgGroupExportPolicy2": tmnxRipNgGroupExportPolicy2,
       "tmnxRipNgGroupExportPolicy3": tmnxRipNgGroupExportPolicy3,
       "tmnxRipNgGroupExportPolicy4": tmnxRipNgGroupExportPolicy4,
       "tmnxRipNgGroupExportPolicy5": tmnxRipNgGroupExportPolicy5,
       "tmnxRipNgGroupDescription": tmnxRipNgGroupDescription,
       "tmnxRipNgGroupInheritance": tmnxRipNgGroupInheritance,
       "tmnxRipNgGroupAdminStatus": tmnxRipNgGroupAdminStatus,
       "tmnxRipNgGroupOperStatus": tmnxRipNgGroupOperStatus,
       "tmnxRipNgGroupRowStatus": tmnxRipNgGroupRowStatus,
       "tmnxRipNgIfTable": tmnxRipNgIfTable,
       "tmnxRipNgIfEntry": tmnxRipNgIfEntry,
       "tmnxRipNgIfGroupName": tmnxRipNgIfGroupName,
       "tmnxRipNgIfAuthType": tmnxRipNgIfAuthType,
       "tmnxRipNgIfAuthKey": tmnxRipNgIfAuthKey,
       "tmnxRipNgIfCheckZero": tmnxRipNgIfCheckZero,
       "tmnxRipNgIfMessageSize": tmnxRipNgIfMessageSize,
       "tmnxRipNgIfMetricIn": tmnxRipNgIfMetricIn,
       "tmnxRipNgIfMetricOut": tmnxRipNgIfMetricOut,
       "tmnxRipNgIfPreference": tmnxRipNgIfPreference,
       "tmnxRipNgIfReceive": tmnxRipNgIfReceive,
       "tmnxRipNgIfSend": tmnxRipNgIfSend,
       "tmnxRipNgIfSplitHorizon": tmnxRipNgIfSplitHorizon,
       "tmnxRipNgIfTimerFlush": tmnxRipNgIfTimerFlush,
       "tmnxRipNgIfTimerTimeout": tmnxRipNgIfTimerTimeout,
       "tmnxRipNgIfTimerUpdate": tmnxRipNgIfTimerUpdate,
       "tmnxRipNgIfImportPolicy1": tmnxRipNgIfImportPolicy1,
       "tmnxRipNgIfImportPolicy2": tmnxRipNgIfImportPolicy2,
       "tmnxRipNgIfImportPolicy3": tmnxRipNgIfImportPolicy3,
       "tmnxRipNgIfImportPolicy4": tmnxRipNgIfImportPolicy4,
       "tmnxRipNgIfImportPolicy5": tmnxRipNgIfImportPolicy5,
       "tmnxRipNgIfExportPolicy1": tmnxRipNgIfExportPolicy1,
       "tmnxRipNgIfExportPolicy2": tmnxRipNgIfExportPolicy2,
       "tmnxRipNgIfExportPolicy3": tmnxRipNgIfExportPolicy3,
       "tmnxRipNgIfExportPolicy4": tmnxRipNgIfExportPolicy4,
       "tmnxRipNgIfExportPolicy5": tmnxRipNgIfExportPolicy5,
       "tmnxRipNgIfDescription": tmnxRipNgIfDescription,
       "tmnxRipNgIfInheritance": tmnxRipNgIfInheritance,
       "tmnxRipNgIfAdminStatus": tmnxRipNgIfAdminStatus,
       "tmnxRipNgIfOperStatus": tmnxRipNgIfOperStatus,
       "tmnxRipNgIfRowStatus": tmnxRipNgIfRowStatus,
       "tmnxRipNgRouteTable": tmnxRipNgRouteTable,
       "tmnxRipNgRouteEntry": tmnxRipNgRouteEntry,
       "tmnxRipNgRouteDestAddrType": tmnxRipNgRouteDestAddrType,
       "tmnxRipNgRouteDestAddress": tmnxRipNgRouteDestAddress,
       "tmnxRipNgRouteMaskLength": tmnxRipNgRouteMaskLength,
       "tmnxRipNgRouteIfIndex": tmnxRipNgRouteIfIndex,
       "tmnxRipNgRoutePeerAddrType": tmnxRipNgRoutePeerAddrType,
       "tmnxRipNgRoutePeerAddress": tmnxRipNgRoutePeerAddress,
       "tmnxRipNgRouteNHAddrType": tmnxRipNgRouteNHAddrType,
       "tmnxRipNgRouteNHAddress": tmnxRipNgRouteNHAddress,
       "tmnxRipNgRouteMetric": tmnxRipNgRouteMetric,
       "tmnxRipNgRouteTag": tmnxRipNgRouteTag,
       "tmnxRipNgRouteStatus": tmnxRipNgRouteStatus,
       "tmnxRipNgRouteTimerRemaining": tmnxRipNgRouteTimerRemaining,
       "tmnxRipNgRouteFC": tmnxRipNgRouteFC,
       "tmnxRipNgRouteFCPriority": tmnxRipNgRouteFCPriority,
       "tmnxRipNgIfStatTable": tmnxRipNgIfStatTable,
       "tmnxRipNgIfStatEntry": tmnxRipNgIfStatEntry,
       "tmnxRipNgIfStatAllSentUpdates": tmnxRipNgIfStatAllSentUpdates,
       "tmnxRipNgIfStatAllTrigUpdates": tmnxRipNgIfStatAllTrigUpdates,
       "tmnxRipNgIfStatAllRcvBadPkts": tmnxRipNgIfStatAllRcvBadPkts,
       "tmnxRipNgIfStatV1RcvUpdates": tmnxRipNgIfStatV1RcvUpdates,
       "tmnxRipNgIfStatV1RcvRequests": tmnxRipNgIfStatV1RcvRequests,
       "tmnxRipNgIfStatV1BadUpdates": tmnxRipNgIfStatV1BadUpdates,
       "tmnxRipNgIfStatV1BadRequests": tmnxRipNgIfStatV1BadRequests,
       "tmnxRipNgIfStatV1BadRoutes": tmnxRipNgIfStatV1BadRoutes,
       "tmnxRipNgIfStatV2RcvUpdates": tmnxRipNgIfStatV2RcvUpdates,
       "tmnxRipNgIfStatV2RcvRequests": tmnxRipNgIfStatV2RcvRequests,
       "tmnxRipNgIfStatV2BadUpdates": tmnxRipNgIfStatV2BadUpdates,
       "tmnxRipNgIfStatV2BadRequests": tmnxRipNgIfStatV2BadRequests,
       "tmnxRipNgIfStatV2BadRoutes": tmnxRipNgIfStatV2BadRoutes,
       "tmnxRipNgIfStatAuthErrors": tmnxRipNgIfStatAuthErrors,
       "tmnxRipNgIfStatAllSentUpdts5Min": tmnxRipNgIfStatAllSentUpdts5Min,
       "tmnxRipNgIfStatAllTrigUpdts5Min": tmnxRipNgIfStatAllTrigUpdts5Min,
       "tmnxRipNgIfStatAllRcvBadPkts5Min": tmnxRipNgIfStatAllRcvBadPkts5Min,
       "tmnxRipNgIfStatV1RcvUpdates5Min": tmnxRipNgIfStatV1RcvUpdates5Min,
       "tmnxRipNgIfStatV1RcvRequests5Min": tmnxRipNgIfStatV1RcvRequests5Min,
       "tmnxRipNgIfStatV1BadUpdates5Min": tmnxRipNgIfStatV1BadUpdates5Min,
       "tmnxRipNgIfStatV1BadRequests5Min": tmnxRipNgIfStatV1BadRequests5Min,
       "tmnxRipNgIfStatV1BadRoutes5Min": tmnxRipNgIfStatV1BadRoutes5Min,
       "tmnxRipNgIfStatV2RcvUpdates5Min": tmnxRipNgIfStatV2RcvUpdates5Min,
       "tmnxRipNgIfStatV2RcvRequests5Min": tmnxRipNgIfStatV2RcvRequests5Min,
       "tmnxRipNgIfStatV2BadUpdates5Min": tmnxRipNgIfStatV2BadUpdates5Min,
       "tmnxRipNgIfStatV2BadRequests5Min": tmnxRipNgIfStatV2BadRequests5Min,
       "tmnxRipNgIfStatV2BadRoutes5Min": tmnxRipNgIfStatV2BadRoutes5Min,
       "tmnxRipNgIfStatAuthErrors5Min": tmnxRipNgIfStatAuthErrors5Min,
       "tmnxRipNgIfStatAllSentUpdts1Min": tmnxRipNgIfStatAllSentUpdts1Min,
       "tmnxRipNgIfStatAllTrigUpdts1Min": tmnxRipNgIfStatAllTrigUpdts1Min,
       "tmnxRipNgIfStatAllRcvBadPkts1Min": tmnxRipNgIfStatAllRcvBadPkts1Min,
       "tmnxRipNgIfStatV1RcvUpdates1Min": tmnxRipNgIfStatV1RcvUpdates1Min,
       "tmnxRipNgIfStatV1RcvRequests1Min": tmnxRipNgIfStatV1RcvRequests1Min,
       "tmnxRipNgIfStatV1BadUpdates1Min": tmnxRipNgIfStatV1BadUpdates1Min,
       "tmnxRipNgIfStatV1BadRequests1Min": tmnxRipNgIfStatV1BadRequests1Min,
       "tmnxRipNgIfStatV1BadRoutes1Min": tmnxRipNgIfStatV1BadRoutes1Min,
       "tmnxRipNgIfStatV2RcvUpdates1Min": tmnxRipNgIfStatV2RcvUpdates1Min,
       "tmnxRipNgIfStatV2RcvRequests1Min": tmnxRipNgIfStatV2RcvRequests1Min,
       "tmnxRipNgIfStatV2BadUpdates1Min": tmnxRipNgIfStatV2BadUpdates1Min,
       "tmnxRipNgIfStatV2BadRequests1Min": tmnxRipNgIfStatV2BadRequests1Min,
       "tmnxRipNgIfStatV2BadRoutes1Min": tmnxRipNgIfStatV2BadRoutes1Min,
       "tmnxRipNgIfStatAuthErrors1Min": tmnxRipNgIfStatAuthErrors1Min,
       "tmnxRipNgPeerTable": tmnxRipNgPeerTable,
       "tmnxRipNgPeerEntry": tmnxRipNgPeerEntry,
       "tmnxRipNgPeerIfIndex": tmnxRipNgPeerIfIndex,
       "tmnxRipNgPeerAddrType": tmnxRipNgPeerAddrType,
       "tmnxRipNgPeerAddress": tmnxRipNgPeerAddress,
       "tmnxRipNgPeerLastUpdate": tmnxRipNgPeerLastUpdate,
       "tmnxRipNgPeerVersion": tmnxRipNgPeerVersion,
       "tmnxRipNgPeerRcvBadPackets": tmnxRipNgPeerRcvBadPackets,
       "tmnxRipNgPeerRcvBadRoutes": tmnxRipNgPeerRcvBadRoutes,
       "tmnxRipNgAdvRouteTable": tmnxRipNgAdvRouteTable,
       "tmnxRipNgAdvRouteEntry": tmnxRipNgAdvRouteEntry,
       "tmnxRipNgAdvRouteDestAddrType": tmnxRipNgAdvRouteDestAddrType,
       "tmnxRipNgAdvRouteDestAddress": tmnxRipNgAdvRouteDestAddress,
       "tmnxRipNgAdvRouteMaskLength": tmnxRipNgAdvRouteMaskLength,
       "tmnxRipNgAdvRouteIfIndex": tmnxRipNgAdvRouteIfIndex,
       "tmnxRipNgAdvRouteIfAddrType": tmnxRipNgAdvRouteIfAddrType,
       "tmnxRipNgAdvRouteIfAddress": tmnxRipNgAdvRouteIfAddress,
       "tmnxRipNgAdvRouteNHAddrType": tmnxRipNgAdvRouteNHAddrType,
       "tmnxRipNgAdvRouteNHAddress": tmnxRipNgAdvRouteNHAddress,
       "tmnxRipNgAdvRouteMetric": tmnxRipNgAdvRouteMetric,
       "tmnxRipNgAdvRouteTag": tmnxRipNgAdvRouteTag,
       "tmnxRipNgAdvRouteTimerRem": tmnxRipNgAdvRouteTimerRem,
       "tmnxRipNgIfUcastTable": tmnxRipNgIfUcastTable,
       "tmnxRipNgIfUcastEntry": tmnxRipNgIfUcastEntry,
       "tmnxRipNgIfUcastAddrType": tmnxRipNgIfUcastAddrType,
       "tmnxRipNgIfUcastAddress": tmnxRipNgIfUcastAddress,
       "tmnxRipNgIfUcastRowStatus": tmnxRipNgIfUcastRowStatus,
       "tmnxRipNgNotificationObjs": tmnxRipNgNotificationObjs,
       "tmnxRipNgNotifySrcAddrType": tmnxRipNgNotifySrcAddrType,
       "tmnxRipNgNotifySrcAddr": tmnxRipNgNotifySrcAddr,
       "tmnxRipNgNotifyReason": tmnxRipNgNotifyReason,
       "tmnxRipNgNotifyPrefix": tmnxRipNgNotifyPrefix,
       "tmnxRipNgNotifications": tmnxRipNgNotifications,
       "tmnxRipNgAuthTypeMismatch": tmnxRipNgAuthTypeMismatch,
       "tmnxRipNgAuthFailure": tmnxRipNgAuthFailure,
       "tmnxRipNgInstShuttingDown": tmnxRipNgInstShuttingDown,
       "tmnxRipNgInstRestarted": tmnxRipNgInstRestarted,
       "tmnxRipNgInstExpLmtReached": tmnxRipNgInstExpLmtReached,
       "tmnxRipNgInstExpLmtWarning": tmnxRipNgInstExpLmtWarning,
       "tmnxRipNgInstRtsExpLmtDropped": tmnxRipNgInstRtsExpLmtDropped,
       "tmnxRipNgIfUcastAddrNotUsed": tmnxRipNgIfUcastAddrNotUsed}
)
