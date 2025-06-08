# SNMP MIB module (TIMETRA-MCAST-PATH-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MCAST-PATH-MGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(TmnxChassisIndex,
 TmnxSlotNum,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndex",
    "TmnxSlotNum",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

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
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledOrInherit,
 TmnxVdoAnalyzerAlarm,
 TmnxVdoFccServerMode,
 TmnxVdoGrpId,
 TmnxVdoGrpIdOrInherit,
 TmnxVdoPortNumber) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledOrInherit",
    "TmnxVdoAnalyzerAlarm",
    "TmnxVdoFccServerMode",
    "TmnxVdoGrpId",
    "TmnxVdoGrpIdOrInherit",
    "TmnxVdoPortNumber")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMcastPathMgmtMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 54)
)
if mibBuilder.loadTexts:
    timetraMcastPathMgmtMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMcPathChlSfPathTypeTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2),
          ("ancillary", 3),
          ("blackhole", 4))
    )



class TmnxMcPathBwActivityTc(TextualConvention, Integer32):
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
          ("use-admin-bw", 1),
          ("dynamic", 2))
    )



class TmnxMcPathRtrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vRtr", 0),
          ("service", 1))
    )



class TmnxMcPathVdoChlType(TextualConvention, Integer32):
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
        *(("default", 1),
          ("hd", 2),
          ("sd", 3),
          ("pip", 4))
    )



class TmnxMcPathVdoChlTypeOrInherit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 0),
          ("default", 1),
          ("hd", 2),
          ("sd", 3),
          ("pip", 4))
    )



class TmnxMcPathVdoPayloadType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 33),
        ValueRangeConstraint(96, 127),
    )



class TmnxMcPathVdoBufferSize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8000),
    )



class TmnxMcPathVdoBwLimit(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxMcPathVdoReorderAudio(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class TmnxMcPathVdoFccMinDuration(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 8000),
    )



class TmnxMcPathVdoFccMinDurationOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 8000),
    )



class TmnxMcPathKeepAliveOverrideTimer(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMcPathConformance_ObjectIdentity = ObjectIdentity
tmnxMcPathConformance = _TmnxMcPathConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54)
)
_TmnxMcPathCompliances_ObjectIdentity = ObjectIdentity
tmnxMcPathCompliances = _TmnxMcPathCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1)
)
_TmnxMcPathGroups_ObjectIdentity = ObjectIdentity
tmnxMcPathGroups = _TmnxMcPathGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2)
)
_TmnxMcPathObjs_ObjectIdentity = ObjectIdentity
tmnxMcPathObjs = _TmnxMcPathObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54)
)
_TmnxMcPathGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxMcPathGlobalObjs = _TmnxMcPathGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1)
)
_TmnxMcPathBwPlcyTableLastChanged_Type = TimeStamp
_TmnxMcPathBwPlcyTableLastChanged_Object = MibScalar
tmnxMcPathBwPlcyTableLastChanged = _TmnxMcPathBwPlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 1),
    _TmnxMcPathBwPlcyTableLastChanged_Type()
)
tmnxMcPathBwPlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyTableLastChanged.setStatus("current")
_TmnxMcPathPlcyTableLastChanged_Type = TimeStamp
_TmnxMcPathPlcyTableLastChanged_Object = MibScalar
tmnxMcPathPlcyTableLastChanged = _TmnxMcPathPlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 2),
    _TmnxMcPathPlcyTableLastChanged_Type()
)
tmnxMcPathPlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathPlcyTableLastChanged.setStatus("current")
_TmnxMcPathBdlTableLastChanged_Type = TimeStamp
_TmnxMcPathBdlTableLastChanged_Object = MibScalar
tmnxMcPathBdlTableLastChanged = _TmnxMcPathBdlTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 3),
    _TmnxMcPathBdlTableLastChanged_Type()
)
tmnxMcPathBdlTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlTableLastChanged.setStatus("current")
_TmnxMcPathBdlChlTblLastChanged_Type = TimeStamp
_TmnxMcPathBdlChlTblLastChanged_Object = MibScalar
tmnxMcPathBdlChlTblLastChanged = _TmnxMcPathBdlChlTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 4),
    _TmnxMcPathBdlChlTblLastChanged_Type()
)
tmnxMcPathBdlChlTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlTblLastChanged.setStatus("current")
_TmnxMcPathChlSrcTableLastChanged_Type = TimeStamp
_TmnxMcPathChlSrcTableLastChanged_Object = MibScalar
tmnxMcPathChlSrcTableLastChanged = _TmnxMcPathChlSrcTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 5),
    _TmnxMcPathChlSrcTableLastChanged_Type()
)
tmnxMcPathChlSrcTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcTableLastChanged.setStatus("current")
_TmnxMcPathChassisLevelInfo_ObjectIdentity = ObjectIdentity
tmnxMcPathChassisLevelInfo = _TmnxMcPathChassisLevelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6)
)


class _TmnxMcPathChassisPlaneLimit_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlaneLimit based on Unsigned32"""
    defaultValue = 2000


_TmnxMcPathChassisPlaneLimit_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlaneLimit_Object = MibScalar
tmnxMcPathChassisPlaneLimit = _TmnxMcPathChassisPlaneLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 1),
    _TmnxMcPathChassisPlaneLimit_Type()
)
tmnxMcPathChassisPlaneLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlaneLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlaneLimit.setUnits("mega-bits-per-second")


class _TmnxMcPathChassisSecPlaneLimit_Type(Unsigned32):
    """Custom type tmnxMcPathChassisSecPlaneLimit based on Unsigned32"""
    defaultValue = 1800


_TmnxMcPathChassisSecPlaneLimit_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisSecPlaneLimit_Object = MibScalar
tmnxMcPathChassisSecPlaneLimit = _TmnxMcPathChassisSecPlaneLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 2),
    _TmnxMcPathChassisSecPlaneLimit_Type()
)
tmnxMcPathChassisSecPlaneLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisSecPlaneLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisSecPlaneLimit.setUnits("mega-bits-per-second")


class _TmnxMcPathChassisDualPlaneLimit_Type(Unsigned32):
    """Custom type tmnxMcPathChassisDualPlaneLimit based on Unsigned32"""
    defaultValue = 2000


_TmnxMcPathChassisDualPlaneLimit_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisDualPlaneLimit_Object = MibScalar
tmnxMcPathChassisDualPlaneLimit = _TmnxMcPathChassisDualPlaneLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 3),
    _TmnxMcPathChassisDualPlaneLimit_Type()
)
tmnxMcPathChassisDualPlaneLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisDualPlaneLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisDualPlaneLimit.setUnits("mega-bits-per-second")


class _TmnxMcPathChassisDualSecPlaneLmt_Type(Unsigned32):
    """Custom type tmnxMcPathChassisDualSecPlaneLmt based on Unsigned32"""
    defaultValue = 1800


_TmnxMcPathChassisDualSecPlaneLmt_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisDualSecPlaneLmt_Object = MibScalar
tmnxMcPathChassisDualSecPlaneLmt = _TmnxMcPathChassisDualSecPlaneLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 4),
    _TmnxMcPathChassisDualSecPlaneLmt_Type()
)
tmnxMcPathChassisDualSecPlaneLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisDualSecPlaneLmt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisDualSecPlaneLmt.setUnits("mega-bits-per-second")


class _TmnxMcPathChassisMmrpAdminMode_Type(TruthValue):
    """Custom type tmnxMcPathChassisMmrpAdminMode based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChassisMmrpAdminMode_Type.__name__ = "TruthValue"
_TmnxMcPathChassisMmrpAdminMode_Object = MibScalar
tmnxMcPathChassisMmrpAdminMode = _TmnxMcPathChassisMmrpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 5),
    _TmnxMcPathChassisMmrpAdminMode_Type()
)
tmnxMcPathChassisMmrpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisMmrpAdminMode.setStatus("current")
_TmnxMcPathChassisMmrpOperMode_Type = TruthValue
_TmnxMcPathChassisMmrpOperMode_Object = MibScalar
tmnxMcPathChassisMmrpOperMode = _TmnxMcPathChassisMmrpOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 6),
    _TmnxMcPathChassisMmrpOperMode_Type()
)
tmnxMcPathChassisMmrpOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChassisMmrpOperMode.setStatus("current")


class _TmnxMcPathChassisRRInactiveRec_Type(TruthValue):
    """Custom type tmnxMcPathChassisRRInactiveRec based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChassisRRInactiveRec_Type.__name__ = "TruthValue"
_TmnxMcPathChassisRRInactiveRec_Object = MibScalar
tmnxMcPathChassisRRInactiveRec = _TmnxMcPathChassisRRInactiveRec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 7),
    _TmnxMcPathChassisRRInactiveRec_Type()
)
tmnxMcPathChassisRRInactiveRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisRRInactiveRec.setStatus("current")


class _TmnxMcPathChassisPlnLimTotal_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimTotal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2000),
        ValueRangeConstraint(4000, 4000),
        ValueRangeConstraint(5250, 5250),
        ValueRangeConstraint(8250, 8250),
    )


_TmnxMcPathChassisPlnLimTotal_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimTotal_Object = MibScalar
tmnxMcPathChassisPlnLimTotal = _TmnxMcPathChassisPlnLimTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 8),
    _TmnxMcPathChassisPlnLimTotal_Type()
)
tmnxMcPathChassisPlnLimTotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimTotal.setStatus("current")


class _TmnxMcPathChassisPlnLimDynTotal_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimDynTotal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2000),
        ValueRangeConstraint(4000, 4000),
    )


_TmnxMcPathChassisPlnLimDynTotal_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimDynTotal_Object = MibScalar
tmnxMcPathChassisPlnLimDynTotal = _TmnxMcPathChassisPlnLimDynTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 9),
    _TmnxMcPathChassisPlnLimDynTotal_Type()
)
tmnxMcPathChassisPlnLimDynTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimDynTotal.setStatus("current")


class _TmnxMcPathChassisPlnLimPriCap_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimPriCap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxMcPathChassisPlnLimPriCap_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimPriCap_Object = MibScalar
tmnxMcPathChassisPlnLimPriCap = _TmnxMcPathChassisPlnLimPriCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 10),
    _TmnxMcPathChassisPlnLimPriCap_Type()
)
tmnxMcPathChassisPlnLimPriCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimPriCap.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimPriCap.setUnits("hundredths of a percent")


class _TmnxMcPathChassisPlnLimSecCap_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimSecCap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxMcPathChassisPlnLimSecCap_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimSecCap_Object = MibScalar
tmnxMcPathChassisPlnLimSecCap = _TmnxMcPathChassisPlnLimSecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 11),
    _TmnxMcPathChassisPlnLimSecCap_Type()
)
tmnxMcPathChassisPlnLimSecCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimSecCap.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimSecCap.setUnits("hundredths of a percent")


class _TmnxMcPathChassisPlnLimPriCapRed_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimPriCapRed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxMcPathChassisPlnLimPriCapRed_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimPriCapRed_Object = MibScalar
tmnxMcPathChassisPlnLimPriCapRed = _TmnxMcPathChassisPlnLimPriCapRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 12),
    _TmnxMcPathChassisPlnLimPriCapRed_Type()
)
tmnxMcPathChassisPlnLimPriCapRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimPriCapRed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimPriCapRed.setUnits("hundredths of a percent")


class _TmnxMcPathChassisPlnLimSecCapRed_Type(Unsigned32):
    """Custom type tmnxMcPathChassisPlnLimSecCapRed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxMcPathChassisPlnLimSecCapRed_Type.__name__ = "Unsigned32"
_TmnxMcPathChassisPlnLimSecCapRed_Object = MibScalar
tmnxMcPathChassisPlnLimSecCapRed = _TmnxMcPathChassisPlnLimSecCapRed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 6, 13),
    _TmnxMcPathChassisPlnLimSecCapRed_Type()
)
tmnxMcPathChassisPlnLimSecCapRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimSecCapRed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChassisPlnLimSecCapRed.setUnits("hundredths of a percent")
_TmnxMcPathVdoPlcyTblLastChanged_Type = TimeStamp
_TmnxMcPathVdoPlcyTblLastChanged_Object = MibScalar
tmnxMcPathVdoPlcyTblLastChanged = _TmnxMcPathVdoPlcyTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 7),
    _TmnxMcPathVdoPlcyTblLastChanged_Type()
)
tmnxMcPathVdoPlcyTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyTblLastChanged.setStatus("current")
_TmnxMcPathBdlExtTableLastChgd_Type = TimeStamp
_TmnxMcPathBdlExtTableLastChgd_Object = MibScalar
tmnxMcPathBdlExtTableLastChgd = _TmnxMcPathBdlExtTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 8),
    _TmnxMcPathBdlExtTableLastChgd_Type()
)
tmnxMcPathBdlExtTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlExtTableLastChgd.setStatus("current")
_TmnxMcPathBdlChlExtTableLastChgd_Type = TimeStamp
_TmnxMcPathBdlChlExtTableLastChgd_Object = MibScalar
tmnxMcPathBdlChlExtTableLastChgd = _TmnxMcPathBdlChlExtTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 9),
    _TmnxMcPathBdlChlExtTableLastChgd_Type()
)
tmnxMcPathBdlChlExtTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlExtTableLastChgd.setStatus("current")
_TmnxMcPathChlSrcExtTableLastChgd_Type = TimeStamp
_TmnxMcPathChlSrcExtTableLastChgd_Object = MibScalar
tmnxMcPathChlSrcExtTableLastChgd = _TmnxMcPathChlSrcExtTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 10),
    _TmnxMcPathChlSrcExtTableLastChgd_Type()
)
tmnxMcPathChlSrcExtTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcExtTableLastChgd.setStatus("current")
_TmnxMcPathRprtDestTblLastChanged_Type = TimeStamp
_TmnxMcPathRprtDestTblLastChanged_Object = MibScalar
tmnxMcPathRprtDestTblLastChanged = _TmnxMcPathRprtDestTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 1, 11),
    _TmnxMcPathRprtDestTblLastChanged_Type()
)
tmnxMcPathRprtDestTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestTblLastChanged.setStatus("current")
_TmnxMcPathNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxMcPathNotifyObjs = _TmnxMcPathNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2)
)
_TmnxMcPathChlGrpAddrType_Type = InetAddressType
_TmnxMcPathChlGrpAddrType_Object = MibScalar
tmnxMcPathChlGrpAddrType = _TmnxMcPathChlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 1),
    _TmnxMcPathChlGrpAddrType_Type()
)
tmnxMcPathChlGrpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlGrpAddrType.setStatus("current")


class _TmnxMcPathChlGrpAddr_Type(InetAddress):
    """Custom type tmnxMcPathChlGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathChlGrpAddr_Type.__name__ = "InetAddress"
_TmnxMcPathChlGrpAddr_Object = MibScalar
tmnxMcPathChlGrpAddr = _TmnxMcPathChlGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 2),
    _TmnxMcPathChlGrpAddr_Type()
)
tmnxMcPathChlGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlGrpAddr.setStatus("current")
_TmnxMcPathChlSrcAddrType_Type = InetAddressType
_TmnxMcPathChlSrcAddrType_Object = MibScalar
tmnxMcPathChlSrcAddrType = _TmnxMcPathChlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 3),
    _TmnxMcPathChlSrcAddrType_Type()
)
tmnxMcPathChlSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcAddrType.setStatus("current")


class _TmnxMcPathChlSrcAddr_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathChlSrcAddr_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcAddr_Object = MibScalar
tmnxMcPathChlSrcAddr = _TmnxMcPathChlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 4),
    _TmnxMcPathChlSrcAddr_Type()
)
tmnxMcPathChlSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcAddr.setStatus("current")
_TmnxMcPathChlPathType_Type = TmnxMcPathChlSfPathTypeTc
_TmnxMcPathChlPathType_Object = MibScalar
tmnxMcPathChlPathType = _TmnxMcPathChlPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 5),
    _TmnxMcPathChlPathType_Type()
)
tmnxMcPathChlPathType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlPathType.setStatus("current")
_TmnxMcPathChassisIndex_Type = TmnxChassisIndex
_TmnxMcPathChassisIndex_Object = MibScalar
tmnxMcPathChassisIndex = _TmnxMcPathChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 6),
    _TmnxMcPathChassisIndex_Type()
)
tmnxMcPathChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChassisIndex.setStatus("current")
_TmnxMcPathCardSlotNum_Type = TmnxSlotNum
_TmnxMcPathCardSlotNum_Object = MibScalar
tmnxMcPathCardSlotNum = _TmnxMcPathCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 7),
    _TmnxMcPathCardSlotNum_Type()
)
tmnxMcPathCardSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathCardSlotNum.setStatus("current")


class _TmnxMcPathMDASlotNum_Type(Unsigned32):
    """Custom type tmnxMcPathMDASlotNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxMcPathMDASlotNum_Type.__name__ = "Unsigned32"
_TmnxMcPathMDASlotNum_Object = MibScalar
tmnxMcPathMDASlotNum = _TmnxMcPathMDASlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 8),
    _TmnxMcPathMDASlotNum_Type()
)
tmnxMcPathMDASlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathMDASlotNum.setStatus("current")
_TmnxMcPathChlRtrType_Type = TmnxMcPathRtrType
_TmnxMcPathChlRtrType_Object = MibScalar
tmnxMcPathChlRtrType = _TmnxMcPathChlRtrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 2, 9),
    _TmnxMcPathChlRtrType_Type()
)
tmnxMcPathChlRtrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPathChlRtrType.setStatus("current")
_TmnxMcPathBwPlcyTable_Object = MibTable
tmnxMcPathBwPlcyTable = _TmnxMcPathBwPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3)
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyTable.setStatus("current")
_TmnxMcPathBwPlcyEntry_Object = MibTableRow
tmnxMcPathBwPlcyEntry = _TmnxMcPathBwPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1)
)
tmnxMcPathBwPlcyEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyEntry.setStatus("current")
_TmnxMcPathBwPlcyName_Type = TNamedItem
_TmnxMcPathBwPlcyName_Object = MibTableColumn
tmnxMcPathBwPlcyName = _TmnxMcPathBwPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 1),
    _TmnxMcPathBwPlcyName_Type()
)
tmnxMcPathBwPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyName.setStatus("current")
_TmnxMcPathBwPlcyRowStatus_Type = RowStatus
_TmnxMcPathBwPlcyRowStatus_Object = MibTableColumn
tmnxMcPathBwPlcyRowStatus = _TmnxMcPathBwPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 2),
    _TmnxMcPathBwPlcyRowStatus_Type()
)
tmnxMcPathBwPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyRowStatus.setStatus("current")
_TmnxMcPathBwPlcyLastChanged_Type = TimeStamp
_TmnxMcPathBwPlcyLastChanged_Object = MibTableColumn
tmnxMcPathBwPlcyLastChanged = _TmnxMcPathBwPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 3),
    _TmnxMcPathBwPlcyLastChanged_Type()
)
tmnxMcPathBwPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyLastChanged.setStatus("current")


class _TmnxMcPathBwPlcyDescription_Type(TItemDescription):
    """Custom type tmnxMcPathBwPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcPathBwPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxMcPathBwPlcyDescription_Object = MibTableColumn
tmnxMcPathBwPlcyDescription = _TmnxMcPathBwPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 4),
    _TmnxMcPathBwPlcyDescription_Type()
)
tmnxMcPathBwPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyDescription.setStatus("current")


class _TmnxMcPathBwPlcyFallPercentReset_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyFallPercentReset based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMcPathBwPlcyFallPercentReset_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyFallPercentReset_Object = MibTableColumn
tmnxMcPathBwPlcyFallPercentReset = _TmnxMcPathBwPlcyFallPercentReset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 5),
    _TmnxMcPathBwPlcyFallPercentReset_Type()
)
tmnxMcPathBwPlcyFallPercentReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyFallPercentReset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyFallPercentReset.setUnits("percentage")


class _TmnxMcPathBwPlcyAdminBwThd_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyAdminBwThd based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40000000),
    )


_TmnxMcPathBwPlcyAdminBwThd_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyAdminBwThd_Object = MibTableColumn
tmnxMcPathBwPlcyAdminBwThd = _TmnxMcPathBwPlcyAdminBwThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 6),
    _TmnxMcPathBwPlcyAdminBwThd_Type()
)
tmnxMcPathBwPlcyAdminBwThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyAdminBwThd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyAdminBwThd.setUnits("kbps")


class _TmnxMcPathBwPlcyMcPoolPercentTot_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyMcPoolPercentTot based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxMcPathBwPlcyMcPoolPercentTot_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyMcPoolPercentTot_Object = MibTableColumn
tmnxMcPathBwPlcyMcPoolPercentTot = _TmnxMcPathBwPlcyMcPoolPercentTot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 7),
    _TmnxMcPathBwPlcyMcPoolPercentTot_Type()
)
tmnxMcPathBwPlcyMcPoolPercentTot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyMcPoolPercentTot.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyMcPoolPercentTot.setUnits("percentage")


class _TmnxMcPathBwPlcyMcPoolResvCbs_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyMcPoolResvCbs based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMcPathBwPlcyMcPoolResvCbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyMcPoolResvCbs_Object = MibTableColumn
tmnxMcPathBwPlcyMcPoolResvCbs = _TmnxMcPathBwPlcyMcPoolResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 8),
    _TmnxMcPathBwPlcyMcPoolResvCbs_Type()
)
tmnxMcPathBwPlcyMcPoolResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyMcPoolResvCbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyMcPoolResvCbs.setUnits("percentage")


class _TmnxMcPathBwPlcyMcPoolSlopePlcy_Type(TNamedItem):
    """Custom type tmnxMcPathBwPlcyMcPoolSlopePlcy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxMcPathBwPlcyMcPoolSlopePlcy_Type.__name__ = "TNamedItem"
_TmnxMcPathBwPlcyMcPoolSlopePlcy_Object = MibTableColumn
tmnxMcPathBwPlcyMcPoolSlopePlcy = _TmnxMcPathBwPlcyMcPoolSlopePlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 3, 1, 9),
    _TmnxMcPathBwPlcyMcPoolSlopePlcy_Type()
)
tmnxMcPathBwPlcyMcPoolSlopePlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyMcPoolSlopePlcy.setStatus("current")
_TmnxMcPathBwPlcyPathTable_Object = MibTable
tmnxMcPathBwPlcyPathTable = _TmnxMcPathBwPlcyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4)
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathTable.setStatus("current")
_TmnxMcPathBwPlcyPathEntry_Object = MibTableRow
tmnxMcPathBwPlcyPathEntry = _TmnxMcPathBwPlcyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1)
)
tmnxMcPathBwPlcyPathEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyPathType"),
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathEntry.setStatus("current")
_TmnxMcPathBwPlcyPathType_Type = TmnxMcPathChlSfPathTypeTc
_TmnxMcPathBwPlcyPathType_Object = MibTableColumn
tmnxMcPathBwPlcyPathType = _TmnxMcPathBwPlcyPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1, 1),
    _TmnxMcPathBwPlcyPathType_Type()
)
tmnxMcPathBwPlcyPathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathType.setStatus("current")


class _TmnxMcPathBwPlcyPathLimit_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyPathLimit based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_TmnxMcPathBwPlcyPathLimit_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyPathLimit_Object = MibTableColumn
tmnxMcPathBwPlcyPathLimit = _TmnxMcPathBwPlcyPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1, 2),
    _TmnxMcPathBwPlcyPathLimit_Type()
)
tmnxMcPathBwPlcyPathLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathLimit.setUnits("mega-bits-per-second")


class _TmnxMcPathBwPlcyPathCbs_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyPathCbs based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxMcPathBwPlcyPathCbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyPathCbs_Object = MibTableColumn
tmnxMcPathBwPlcyPathCbs = _TmnxMcPathBwPlcyPathCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1, 3),
    _TmnxMcPathBwPlcyPathCbs_Type()
)
tmnxMcPathBwPlcyPathCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathCbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathCbs.setUnits("hundredths of a percent")


class _TmnxMcPathBwPlcyPathMbs_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyPathMbs based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxMcPathBwPlcyPathMbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyPathMbs_Object = MibTableColumn
tmnxMcPathBwPlcyPathMbs = _TmnxMcPathBwPlcyPathMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1, 4),
    _TmnxMcPathBwPlcyPathMbs_Type()
)
tmnxMcPathBwPlcyPathMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathMbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathMbs.setUnits("hundredths of a percent")


class _TmnxMcPathBwPlcyPathHighPrio_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyPathHighPrio based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMcPathBwPlcyPathHighPrio_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyPathHighPrio_Object = MibTableColumn
tmnxMcPathBwPlcyPathHighPrio = _TmnxMcPathBwPlcyPathHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 4, 1, 5),
    _TmnxMcPathBwPlcyPathHighPrio_Type()
)
tmnxMcPathBwPlcyPathHighPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathHighPrio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyPathHighPrio.setUnits("percentage")
_TmnxMcPathPlcyTable_Object = MibTable
tmnxMcPathPlcyTable = _TmnxMcPathPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5)
)
if mibBuilder.loadTexts:
    tmnxMcPathPlcyTable.setStatus("current")
_TmnxMcPathPlcyEntry_Object = MibTableRow
tmnxMcPathPlcyEntry = _TmnxMcPathPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5, 1)
)
tmnxMcPathPlcyEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxMcPathPlcyEntry.setStatus("current")
_TmnxMcPathPlcyName_Type = TNamedItem
_TmnxMcPathPlcyName_Object = MibTableColumn
tmnxMcPathPlcyName = _TmnxMcPathPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5, 1, 1),
    _TmnxMcPathPlcyName_Type()
)
tmnxMcPathPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathPlcyName.setStatus("current")
_TmnxMcPathPlcyRowStatus_Type = RowStatus
_TmnxMcPathPlcyRowStatus_Object = MibTableColumn
tmnxMcPathPlcyRowStatus = _TmnxMcPathPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5, 1, 2),
    _TmnxMcPathPlcyRowStatus_Type()
)
tmnxMcPathPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathPlcyRowStatus.setStatus("current")
_TmnxMcPathPlcyLastChanged_Type = TimeStamp
_TmnxMcPathPlcyLastChanged_Object = MibTableColumn
tmnxMcPathPlcyLastChanged = _TmnxMcPathPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5, 1, 3),
    _TmnxMcPathPlcyLastChanged_Type()
)
tmnxMcPathPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathPlcyLastChanged.setStatus("current")


class _TmnxMcPathPlcyDescription_Type(TItemDescription):
    """Custom type tmnxMcPathPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcPathPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxMcPathPlcyDescription_Object = MibTableColumn
tmnxMcPathPlcyDescription = _TmnxMcPathPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 5, 1, 4),
    _TmnxMcPathPlcyDescription_Type()
)
tmnxMcPathPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathPlcyDescription.setStatus("current")
_TmnxMcPathBdlTable_Object = MibTable
tmnxMcPathBdlTable = _TmnxMcPathBdlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlTable.setStatus("current")
_TmnxMcPathBdlEntry_Object = MibTableRow
tmnxMcPathBdlEntry = _TmnxMcPathBdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1)
)
tmnxMcPathBdlEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlName"),
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlEntry.setStatus("current")
_TmnxMcPathBdlName_Type = TNamedItem
_TmnxMcPathBdlName_Object = MibTableColumn
tmnxMcPathBdlName = _TmnxMcPathBdlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 1),
    _TmnxMcPathBdlName_Type()
)
tmnxMcPathBdlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBdlName.setStatus("current")
_TmnxMcPathBdlStatus_Type = RowStatus
_TmnxMcPathBdlStatus_Object = MibTableColumn
tmnxMcPathBdlStatus = _TmnxMcPathBdlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 2),
    _TmnxMcPathBdlStatus_Type()
)
tmnxMcPathBdlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlStatus.setStatus("current")
_TmnxMcPathBdlLastChanged_Type = TimeStamp
_TmnxMcPathBdlLastChanged_Object = MibTableColumn
tmnxMcPathBdlLastChanged = _TmnxMcPathBdlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 3),
    _TmnxMcPathBdlLastChanged_Type()
)
tmnxMcPathBdlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlLastChanged.setStatus("current")


class _TmnxMcPathBdlDescription_Type(TItemDescription):
    """Custom type tmnxMcPathBdlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcPathBdlDescription_Type.__name__ = "TItemDescription"
_TmnxMcPathBdlDescription_Object = MibTableColumn
tmnxMcPathBdlDescription = _TmnxMcPathBdlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 4),
    _TmnxMcPathBdlDescription_Type()
)
tmnxMcPathBdlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDescription.setStatus("current")


class _TmnxMcPathBdlCongPriorityThd_Type(Unsigned32):
    """Custom type tmnxMcPathBdlCongPriorityThd based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxMcPathBdlCongPriorityThd_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlCongPriorityThd_Object = MibTableColumn
tmnxMcPathBdlCongPriorityThd = _TmnxMcPathBdlCongPriorityThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 5),
    _TmnxMcPathBdlCongPriorityThd_Type()
)
tmnxMcPathBdlCongPriorityThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlCongPriorityThd.setStatus("current")


class _TmnxMcPathBdlEcmpOptThd_Type(Unsigned32):
    """Custom type tmnxMcPathBdlEcmpOptThd based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxMcPathBdlEcmpOptThd_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlEcmpOptThd_Object = MibTableColumn
tmnxMcPathBdlEcmpOptThd = _TmnxMcPathBdlEcmpOptThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 6),
    _TmnxMcPathBdlEcmpOptThd_Type()
)
tmnxMcPathBdlEcmpOptThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlEcmpOptThd.setStatus("current")


class _TmnxMcPathBdlDefChlAdminBw_Type(Unsigned32):
    """Custom type tmnxMcPathBdlDefChlAdminBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_TmnxMcPathBdlDefChlAdminBw_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlDefChlAdminBw_Object = MibTableColumn
tmnxMcPathBdlDefChlAdminBw = _TmnxMcPathBdlDefChlAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 7),
    _TmnxMcPathBdlDefChlAdminBw_Type()
)
tmnxMcPathBdlDefChlAdminBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlAdminBw.setUnits("kbps")


class _TmnxMcPathBdlDefChlPref_Type(Unsigned32):
    """Custom type tmnxMcPathBdlDefChlPref based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxMcPathBdlDefChlPref_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlDefChlPref_Object = MibTableColumn
tmnxMcPathBdlDefChlPref = _TmnxMcPathBdlDefChlPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 8),
    _TmnxMcPathBdlDefChlPref_Type()
)
tmnxMcPathBdlDefChlPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlPref.setStatus("current")


class _TmnxMcPathBdlDefChlBwActivity_Type(TmnxMcPathBwActivityTc):
    """Custom type tmnxMcPathBdlDefChlBwActivity based on TmnxMcPathBwActivityTc"""
    defaultValue = 2


_TmnxMcPathBdlDefChlBwActivity_Type.__name__ = "TmnxMcPathBwActivityTc"
_TmnxMcPathBdlDefChlBwActivity_Object = MibTableColumn
tmnxMcPathBdlDefChlBwActivity = _TmnxMcPathBdlDefChlBwActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 10),
    _TmnxMcPathBdlDefChlBwActivity_Type()
)
tmnxMcPathBdlDefChlBwActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlBwActivity.setStatus("current")


class _TmnxMcPathBdlDefChlBwFallDelay_Type(Unsigned32):
    """Custom type tmnxMcPathBdlDefChlBwFallDelay based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_TmnxMcPathBdlDefChlBwFallDelay_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlDefChlBwFallDelay_Object = MibTableColumn
tmnxMcPathBdlDefChlBwFallDelay = _TmnxMcPathBdlDefChlBwFallDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 11),
    _TmnxMcPathBdlDefChlBwFallDelay_Type()
)
tmnxMcPathBdlDefChlBwFallDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlBwFallDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlBwFallDelay.setUnits("seconds")


class _TmnxMcPathBdlDefChlBwBlackHoleRt_Type(Unsigned32):
    """Custom type tmnxMcPathBdlDefChlBwBlackHoleRt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 40000000),
    )


_TmnxMcPathBdlDefChlBwBlackHoleRt_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlDefChlBwBlackHoleRt_Object = MibTableColumn
tmnxMcPathBdlDefChlBwBlackHoleRt = _TmnxMcPathBdlDefChlBwBlackHoleRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 12),
    _TmnxMcPathBdlDefChlBwBlackHoleRt_Type()
)
tmnxMcPathBdlDefChlBwBlackHoleRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlBwBlackHoleRt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlBwBlackHoleRt.setUnits("kbps")


class _TmnxMcPathBdlDefChlExSfPath_Type(TmnxMcPathChlSfPathTypeTc):
    """Custom type tmnxMcPathBdlDefChlExSfPath based on TmnxMcPathChlSfPathTypeTc"""
    defaultValue = 0


_TmnxMcPathBdlDefChlExSfPath_Type.__name__ = "TmnxMcPathChlSfPathTypeTc"
_TmnxMcPathBdlDefChlExSfPath_Object = MibTableColumn
tmnxMcPathBdlDefChlExSfPath = _TmnxMcPathBdlDefChlExSfPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 13),
    _TmnxMcPathBdlDefChlExSfPath_Type()
)
tmnxMcPathBdlDefChlExSfPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlDefChlExSfPath.setStatus("current")


class _TmnxMcPathBdlVdoFCCState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMcPathBdlVdoFCCState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMcPathBdlVdoFCCState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMcPathBdlVdoFCCState_Object = MibTableColumn
tmnxMcPathBdlVdoFCCState = _TmnxMcPathBdlVdoFCCState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 14),
    _TmnxMcPathBdlVdoFCCState_Type()
)
tmnxMcPathBdlVdoFCCState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoFCCState.setStatus("current")


class _TmnxMcPathBdlVdoRTState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMcPathBdlVdoRTState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMcPathBdlVdoRTState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMcPathBdlVdoRTState_Object = MibTableColumn
tmnxMcPathBdlVdoRTState = _TmnxMcPathBdlVdoRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 15),
    _TmnxMcPathBdlVdoRTState_Type()
)
tmnxMcPathBdlVdoRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTState.setStatus("current")


class _TmnxMcPathBdlVdoChlType_Type(TmnxMcPathVdoChlType):
    """Custom type tmnxMcPathBdlVdoChlType based on TmnxMcPathVdoChlType"""
    defaultValue = 2


_TmnxMcPathBdlVdoChlType_Type.__name__ = "TmnxMcPathVdoChlType"
_TmnxMcPathBdlVdoChlType_Object = MibTableColumn
tmnxMcPathBdlVdoChlType = _TmnxMcPathBdlVdoChlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 16),
    _TmnxMcPathBdlVdoChlType_Type()
)
tmnxMcPathBdlVdoChlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoChlType.setStatus("current")


class _TmnxMcPathBdlVdoRTAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathBdlVdoRTAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlVdoRTAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlVdoRTAddrType_Object = MibTableColumn
tmnxMcPathBdlVdoRTAddrType = _TmnxMcPathBdlVdoRTAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 17),
    _TmnxMcPathBdlVdoRTAddrType_Type()
)
tmnxMcPathBdlVdoRTAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTAddrType.setStatus("current")


class _TmnxMcPathBdlVdoRTAddress_Type(InetAddress):
    """Custom type tmnxMcPathBdlVdoRTAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlVdoRTAddress_Type.__name__ = "InetAddress"
_TmnxMcPathBdlVdoRTAddress_Object = MibTableColumn
tmnxMcPathBdlVdoRTAddress = _TmnxMcPathBdlVdoRTAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 18),
    _TmnxMcPathBdlVdoRTAddress_Type()
)
tmnxMcPathBdlVdoRTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTAddress.setStatus("current")


class _TmnxMcPathBdlVdoRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlVdoRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathBdlVdoRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlVdoRTPort_Object = MibTableColumn
tmnxMcPathBdlVdoRTPort = _TmnxMcPathBdlVdoRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 19),
    _TmnxMcPathBdlVdoRTPort_Type()
)
tmnxMcPathBdlVdoRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTPort.setStatus("current")


class _TmnxMcPathBdlVdoRTBufferSize_Type(TmnxMcPathVdoBufferSize):
    """Custom type tmnxMcPathBdlVdoRTBufferSize based on TmnxMcPathVdoBufferSize"""
    defaultValue = 300


_TmnxMcPathBdlVdoRTBufferSize_Type.__name__ = "TmnxMcPathVdoBufferSize"
_TmnxMcPathBdlVdoRTBufferSize_Object = MibTableColumn
tmnxMcPathBdlVdoRTBufferSize = _TmnxMcPathBdlVdoRTBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 20),
    _TmnxMcPathBdlVdoRTBufferSize_Type()
)
tmnxMcPathBdlVdoRTBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoRTBufferSize.setUnits("milliseconds")


class _TmnxMcPathBdlVdoLocalRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlVdoLocalRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathBdlVdoLocalRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlVdoLocalRTPort_Object = MibTableColumn
tmnxMcPathBdlVdoLocalRTPort = _TmnxMcPathBdlVdoLocalRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 21),
    _TmnxMcPathBdlVdoLocalRTPort_Type()
)
tmnxMcPathBdlVdoLocalRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoLocalRTPort.setStatus("current")


class _TmnxMcPathBdlVdoLocalFccPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlVdoLocalFccPort based on TmnxVdoPortNumber"""
    defaultValue = 4098


_TmnxMcPathBdlVdoLocalFccPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlVdoLocalFccPort_Object = MibTableColumn
tmnxMcPathBdlVdoLocalFccPort = _TmnxMcPathBdlVdoLocalFccPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 22),
    _TmnxMcPathBdlVdoLocalFccPort_Type()
)
tmnxMcPathBdlVdoLocalFccPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoLocalFccPort.setStatus("current")


class _TmnxMcPathBdlVdoGroupId_Type(TmnxVdoGrpId):
    """Custom type tmnxMcPathBdlVdoGroupId based on TmnxVdoGrpId"""
    defaultValue = 0


_TmnxMcPathBdlVdoGroupId_Type.__name__ = "TmnxVdoGrpId"
_TmnxMcPathBdlVdoGroupId_Object = MibTableColumn
tmnxMcPathBdlVdoGroupId = _TmnxMcPathBdlVdoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 23),
    _TmnxMcPathBdlVdoGroupId_Type()
)
tmnxMcPathBdlVdoGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoGroupId.setStatus("current")


class _TmnxMcPathBdlTunnelIfLspName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlTunnelIfLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlTunnelIfLspName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlTunnelIfLspName_Object = MibTableColumn
tmnxMcPathBdlTunnelIfLspName = _TmnxMcPathBdlTunnelIfLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 24),
    _TmnxMcPathBdlTunnelIfLspName_Type()
)
tmnxMcPathBdlTunnelIfLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlTunnelIfLspName.setStatus("current")


class _TmnxMcPathBdlTunIfSdAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathBdlTunIfSdAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlTunIfSdAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlTunIfSdAddrType_Object = MibTableColumn
tmnxMcPathBdlTunIfSdAddrType = _TmnxMcPathBdlTunIfSdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 25),
    _TmnxMcPathBdlTunIfSdAddrType_Type()
)
tmnxMcPathBdlTunIfSdAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlTunIfSdAddrType.setStatus("current")


class _TmnxMcPathBdlTunIfSdAddr_Type(InetAddress):
    """Custom type tmnxMcPathBdlTunIfSdAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlTunIfSdAddr_Type.__name__ = "InetAddress"
_TmnxMcPathBdlTunIfSdAddr_Object = MibTableColumn
tmnxMcPathBdlTunIfSdAddr = _TmnxMcPathBdlTunIfSdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 26),
    _TmnxMcPathBdlTunIfSdAddr_Type()
)
tmnxMcPathBdlTunIfSdAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlTunIfSdAddr.setStatus("current")


class _TmnxMcPathBdlVdoSourcePort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlVdoSourcePort based on TmnxVdoPortNumber"""
    defaultValue = 4097


_TmnxMcPathBdlVdoSourcePort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlVdoSourcePort_Object = MibTableColumn
tmnxMcPathBdlVdoSourcePort = _TmnxMcPathBdlVdoSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 27),
    _TmnxMcPathBdlVdoSourcePort_Type()
)
tmnxMcPathBdlVdoSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoSourcePort.setStatus("obsolete")


class _TmnxMcPathBdlVdoLocalRTState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMcPathBdlVdoLocalRTState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMcPathBdlVdoLocalRTState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMcPathBdlVdoLocalRTState_Object = MibTableColumn
tmnxMcPathBdlVdoLocalRTState = _TmnxMcPathBdlVdoLocalRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 28),
    _TmnxMcPathBdlVdoLocalRTState_Type()
)
tmnxMcPathBdlVdoLocalRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoLocalRTState.setStatus("current")


class _TmnxMcPathBdlVdoReorderAudio_Type(TmnxMcPathVdoReorderAudio):
    """Custom type tmnxMcPathBdlVdoReorderAudio based on TmnxMcPathVdoReorderAudio"""
    defaultValue = 0


_TmnxMcPathBdlVdoReorderAudio_Type.__name__ = "TmnxMcPathVdoReorderAudio"
_TmnxMcPathBdlVdoReorderAudio_Object = MibTableColumn
tmnxMcPathBdlVdoReorderAudio = _TmnxMcPathBdlVdoReorderAudio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 29),
    _TmnxMcPathBdlVdoReorderAudio_Type()
)
tmnxMcPathBdlVdoReorderAudio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoReorderAudio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoReorderAudio.setUnits("milliseconds")


class _TmnxMcPathBdlVdoFccMinDuration_Type(TmnxMcPathVdoFccMinDuration):
    """Custom type tmnxMcPathBdlVdoFccMinDuration based on TmnxMcPathVdoFccMinDuration"""
    defaultValue = 300


_TmnxMcPathBdlVdoFccMinDuration_Type.__name__ = "TmnxMcPathVdoFccMinDuration"
_TmnxMcPathBdlVdoFccMinDuration_Object = MibTableColumn
tmnxMcPathBdlVdoFccMinDuration = _TmnxMcPathBdlVdoFccMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 30),
    _TmnxMcPathBdlVdoFccMinDuration_Type()
)
tmnxMcPathBdlVdoFccMinDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoFccMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoFccMinDuration.setUnits("milliseconds")


class _TmnxMcPathBdlKAOverrideTimer_Type(TmnxMcPathKeepAliveOverrideTimer):
    """Custom type tmnxMcPathBdlKAOverrideTimer based on TmnxMcPathKeepAliveOverrideTimer"""
    defaultValue = 0


_TmnxMcPathBdlKAOverrideTimer_Type.__name__ = "TmnxMcPathKeepAliveOverrideTimer"
_TmnxMcPathBdlKAOverrideTimer_Object = MibTableColumn
tmnxMcPathBdlKAOverrideTimer = _TmnxMcPathBdlKAOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 31),
    _TmnxMcPathBdlKAOverrideTimer_Type()
)
tmnxMcPathBdlKAOverrideTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlKAOverrideTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlKAOverrideTimer.setUnits("seconds")


class _TmnxMcPathBdlP2MPId_Type(Unsigned32):
    """Custom type tmnxMcPathBdlP2MPId based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathBdlP2MPId_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlP2MPId_Object = MibTableColumn
tmnxMcPathBdlP2MPId = _TmnxMcPathBdlP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 32),
    _TmnxMcPathBdlP2MPId_Type()
)
tmnxMcPathBdlP2MPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlP2MPId.setStatus("current")


class _TmnxMcPathBdlVdoAnalyzer_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoAnalyzer based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoAnalyzer_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoAnalyzer_Object = MibTableColumn
tmnxMcPathBdlVdoAnalyzer = _TmnxMcPathBdlVdoAnalyzer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 33),
    _TmnxMcPathBdlVdoAnalyzer_Type()
)
tmnxMcPathBdlVdoAnalyzer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoAnalyzer.setStatus("current")


class _TmnxMcPathBdlVdoAnalyzerDesc_Type(TItemDescription):
    """Custom type tmnxMcPathBdlVdoAnalyzerDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMcPathBdlVdoAnalyzerDesc_Type.__name__ = "TItemDescription"
_TmnxMcPathBdlVdoAnalyzerDesc_Object = MibTableColumn
tmnxMcPathBdlVdoAnalyzerDesc = _TmnxMcPathBdlVdoAnalyzerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 34),
    _TmnxMcPathBdlVdoAnalyzerDesc_Type()
)
tmnxMcPathBdlVdoAnalyzerDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoAnalyzerDesc.setStatus("current")


class _TmnxMcPathBdlVdoStrSelSrc1Type_Type(InetAddressType):
    """Custom type tmnxMcPathBdlVdoStrSelSrc1Type based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlVdoStrSelSrc1Type_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlVdoStrSelSrc1Type_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelSrc1Type = _TmnxMcPathBdlVdoStrSelSrc1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 35),
    _TmnxMcPathBdlVdoStrSelSrc1Type_Type()
)
tmnxMcPathBdlVdoStrSelSrc1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelSrc1Type.setStatus("current")


class _TmnxMcPathBdlVdoStrSelSrc1_Type(InetAddress):
    """Custom type tmnxMcPathBdlVdoStrSelSrc1 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlVdoStrSelSrc1_Type.__name__ = "InetAddress"
_TmnxMcPathBdlVdoStrSelSrc1_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelSrc1 = _TmnxMcPathBdlVdoStrSelSrc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 36),
    _TmnxMcPathBdlVdoStrSelSrc1_Type()
)
tmnxMcPathBdlVdoStrSelSrc1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelSrc1.setStatus("current")


class _TmnxMcPathBdlVdoStrSelIntf1_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlVdoStrSelIntf1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlVdoStrSelIntf1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlVdoStrSelIntf1_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelIntf1 = _TmnxMcPathBdlVdoStrSelIntf1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 37),
    _TmnxMcPathBdlVdoStrSelIntf1_Type()
)
tmnxMcPathBdlVdoStrSelIntf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelIntf1.setStatus("current")


class _TmnxMcPathBdlVdoStrSelSrc2Type_Type(InetAddressType):
    """Custom type tmnxMcPathBdlVdoStrSelSrc2Type based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlVdoStrSelSrc2Type_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlVdoStrSelSrc2Type_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelSrc2Type = _TmnxMcPathBdlVdoStrSelSrc2Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 38),
    _TmnxMcPathBdlVdoStrSelSrc2Type_Type()
)
tmnxMcPathBdlVdoStrSelSrc2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelSrc2Type.setStatus("current")


class _TmnxMcPathBdlVdoStrSelSrc2_Type(InetAddress):
    """Custom type tmnxMcPathBdlVdoStrSelSrc2 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlVdoStrSelSrc2_Type.__name__ = "InetAddress"
_TmnxMcPathBdlVdoStrSelSrc2_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelSrc2 = _TmnxMcPathBdlVdoStrSelSrc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 39),
    _TmnxMcPathBdlVdoStrSelSrc2_Type()
)
tmnxMcPathBdlVdoStrSelSrc2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelSrc2.setStatus("current")


class _TmnxMcPathBdlVdoStrSelIntf2_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlVdoStrSelIntf2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlVdoStrSelIntf2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlVdoStrSelIntf2_Object = MibTableColumn
tmnxMcPathBdlVdoStrSelIntf2 = _TmnxMcPathBdlVdoStrSelIntf2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 7, 1, 40),
    _TmnxMcPathBdlVdoStrSelIntf2_Type()
)
tmnxMcPathBdlVdoStrSelIntf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoStrSelIntf2.setStatus("current")
_TmnxMcPathBdlChlTable_Object = MibTable
tmnxMcPathBdlChlTable = _TmnxMcPathBdlChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlTable.setStatus("current")
_TmnxMcPathBdlChlEntry_Object = MibTableRow
tmnxMcPathBdlChlEntry = _TmnxMcPathBdlChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1)
)
tmnxMcPathBdlChlEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlStartAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlStartAddr"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlEndAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlEndAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlEntry.setStatus("current")
_TmnxMcPathBdlChlStartAddrType_Type = InetAddressType
_TmnxMcPathBdlChlStartAddrType_Object = MibTableColumn
tmnxMcPathBdlChlStartAddrType = _TmnxMcPathBdlChlStartAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 1),
    _TmnxMcPathBdlChlStartAddrType_Type()
)
tmnxMcPathBdlChlStartAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlStartAddrType.setStatus("current")


class _TmnxMcPathBdlChlStartAddr_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlStartAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathBdlChlStartAddr_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlStartAddr_Object = MibTableColumn
tmnxMcPathBdlChlStartAddr = _TmnxMcPathBdlChlStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 2),
    _TmnxMcPathBdlChlStartAddr_Type()
)
tmnxMcPathBdlChlStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlStartAddr.setStatus("current")
_TmnxMcPathBdlChlEndAddrType_Type = InetAddressType
_TmnxMcPathBdlChlEndAddrType_Object = MibTableColumn
tmnxMcPathBdlChlEndAddrType = _TmnxMcPathBdlChlEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 3),
    _TmnxMcPathBdlChlEndAddrType_Type()
)
tmnxMcPathBdlChlEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlEndAddrType.setStatus("current")


class _TmnxMcPathBdlChlEndAddr_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathBdlChlEndAddr_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlEndAddr_Object = MibTableColumn
tmnxMcPathBdlChlEndAddr = _TmnxMcPathBdlChlEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 4),
    _TmnxMcPathBdlChlEndAddr_Type()
)
tmnxMcPathBdlChlEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlEndAddr.setStatus("current")
_TmnxMcPathBdlChlRowStatus_Type = RowStatus
_TmnxMcPathBdlChlRowStatus_Object = MibTableColumn
tmnxMcPathBdlChlRowStatus = _TmnxMcPathBdlChlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 5),
    _TmnxMcPathBdlChlRowStatus_Type()
)
tmnxMcPathBdlChlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlRowStatus.setStatus("current")
_TmnxMcPathBdlChlLastChanged_Type = TimeStamp
_TmnxMcPathBdlChlLastChanged_Object = MibTableColumn
tmnxMcPathBdlChlLastChanged = _TmnxMcPathBdlChlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 6),
    _TmnxMcPathBdlChlLastChanged_Type()
)
tmnxMcPathBdlChlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlLastChanged.setStatus("current")


class _TmnxMcPathBdlChlAdminBw_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlAdminBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_TmnxMcPathBdlChlAdminBw_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlAdminBw_Object = MibTableColumn
tmnxMcPathBdlChlAdminBw = _TmnxMcPathBdlChlAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 7),
    _TmnxMcPathBdlChlAdminBw_Type()
)
tmnxMcPathBdlChlAdminBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlAdminBw.setUnits("kbps")


class _TmnxMcPathBdlChlPref_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlPref based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxMcPathBdlChlPref_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlPref_Object = MibTableColumn
tmnxMcPathBdlChlPref = _TmnxMcPathBdlChlPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 8),
    _TmnxMcPathBdlChlPref_Type()
)
tmnxMcPathBdlChlPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlPref.setStatus("current")


class _TmnxMcPathBdlChlBwActivity_Type(TmnxMcPathBwActivityTc):
    """Custom type tmnxMcPathBdlChlBwActivity based on TmnxMcPathBwActivityTc"""
    defaultValue = 0


_TmnxMcPathBdlChlBwActivity_Type.__name__ = "TmnxMcPathBwActivityTc"
_TmnxMcPathBdlChlBwActivity_Object = MibTableColumn
tmnxMcPathBdlChlBwActivity = _TmnxMcPathBdlChlBwActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 10),
    _TmnxMcPathBdlChlBwActivity_Type()
)
tmnxMcPathBdlChlBwActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlBwActivity.setStatus("current")


class _TmnxMcPathBdlChlBwFallDelay_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlBwFallDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_TmnxMcPathBdlChlBwFallDelay_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlBwFallDelay_Object = MibTableColumn
tmnxMcPathBdlChlBwFallDelay = _TmnxMcPathBdlChlBwFallDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 11),
    _TmnxMcPathBdlChlBwFallDelay_Type()
)
tmnxMcPathBdlChlBwFallDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlBwFallDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlBwFallDelay.setUnits("seconds")


class _TmnxMcPathBdlChlBwBlackHoleRt_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlBwBlackHoleRt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_TmnxMcPathBdlChlBwBlackHoleRt_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlBwBlackHoleRt_Object = MibTableColumn
tmnxMcPathBdlChlBwBlackHoleRt = _TmnxMcPathBdlChlBwBlackHoleRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 12),
    _TmnxMcPathBdlChlBwBlackHoleRt_Type()
)
tmnxMcPathBdlChlBwBlackHoleRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlBwBlackHoleRt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlBwBlackHoleRt.setUnits("kbps")


class _TmnxMcPathBdlChlExSfPath_Type(TmnxMcPathChlSfPathTypeTc):
    """Custom type tmnxMcPathBdlChlExSfPath based on TmnxMcPathChlSfPathTypeTc"""
    defaultValue = 0


_TmnxMcPathBdlChlExSfPath_Type.__name__ = "TmnxMcPathChlSfPathTypeTc"
_TmnxMcPathBdlChlExSfPath_Object = MibTableColumn
tmnxMcPathBdlChlExSfPath = _TmnxMcPathBdlChlExSfPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 13),
    _TmnxMcPathBdlChlExSfPath_Type()
)
tmnxMcPathBdlChlExSfPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlExSfPath.setStatus("current")


class _TmnxMcPathBdlChlVdoFCCState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathBdlChlVdoFCCState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathBdlChlVdoFCCState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathBdlChlVdoFCCState_Object = MibTableColumn
tmnxMcPathBdlChlVdoFCCState = _TmnxMcPathBdlChlVdoFCCState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 14),
    _TmnxMcPathBdlChlVdoFCCState_Type()
)
tmnxMcPathBdlChlVdoFCCState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoFCCState.setStatus("current")


class _TmnxMcPathBdlChlVdoRTState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathBdlChlVdoRTState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathBdlChlVdoRTState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathBdlChlVdoRTState_Object = MibTableColumn
tmnxMcPathBdlChlVdoRTState = _TmnxMcPathBdlChlVdoRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 15),
    _TmnxMcPathBdlChlVdoRTState_Type()
)
tmnxMcPathBdlChlVdoRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTState.setStatus("current")


class _TmnxMcPathBdlChlVdoChlType_Type(TmnxMcPathVdoChlTypeOrInherit):
    """Custom type tmnxMcPathBdlChlVdoChlType based on TmnxMcPathVdoChlTypeOrInherit"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoChlType_Type.__name__ = "TmnxMcPathVdoChlTypeOrInherit"
_TmnxMcPathBdlChlVdoChlType_Object = MibTableColumn
tmnxMcPathBdlChlVdoChlType = _TmnxMcPathBdlChlVdoChlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 16),
    _TmnxMcPathBdlChlVdoChlType_Type()
)
tmnxMcPathBdlChlVdoChlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoChlType.setStatus("current")


class _TmnxMcPathBdlChlVdoRTAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathBdlChlVdoRTAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoRTAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlChlVdoRTAddrType_Object = MibTableColumn
tmnxMcPathBdlChlVdoRTAddrType = _TmnxMcPathBdlChlVdoRTAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 17),
    _TmnxMcPathBdlChlVdoRTAddrType_Type()
)
tmnxMcPathBdlChlVdoRTAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTAddrType.setStatus("current")


class _TmnxMcPathBdlChlVdoRTAddress_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlVdoRTAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlChlVdoRTAddress_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlVdoRTAddress_Object = MibTableColumn
tmnxMcPathBdlChlVdoRTAddress = _TmnxMcPathBdlChlVdoRTAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 18),
    _TmnxMcPathBdlChlVdoRTAddress_Type()
)
tmnxMcPathBdlChlVdoRTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTAddress.setStatus("current")


class _TmnxMcPathBdlChlVdoRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlChlVdoRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathBdlChlVdoRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlChlVdoRTPort_Object = MibTableColumn
tmnxMcPathBdlChlVdoRTPort = _TmnxMcPathBdlChlVdoRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 19),
    _TmnxMcPathBdlChlVdoRTPort_Type()
)
tmnxMcPathBdlChlVdoRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTPort.setStatus("current")


class _TmnxMcPathBdlChlVdoRTBufferSize_Type(TmnxMcPathVdoBufferSize):
    """Custom type tmnxMcPathBdlChlVdoRTBufferSize based on TmnxMcPathVdoBufferSize"""
    defaultValue = 300


_TmnxMcPathBdlChlVdoRTBufferSize_Type.__name__ = "TmnxMcPathVdoBufferSize"
_TmnxMcPathBdlChlVdoRTBufferSize_Object = MibTableColumn
tmnxMcPathBdlChlVdoRTBufferSize = _TmnxMcPathBdlChlVdoRTBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 20),
    _TmnxMcPathBdlChlVdoRTBufferSize_Type()
)
tmnxMcPathBdlChlVdoRTBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoRTBufferSize.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoLocalRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlChlVdoLocalRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathBdlChlVdoLocalRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlChlVdoLocalRTPort_Object = MibTableColumn
tmnxMcPathBdlChlVdoLocalRTPort = _TmnxMcPathBdlChlVdoLocalRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 21),
    _TmnxMcPathBdlChlVdoLocalRTPort_Type()
)
tmnxMcPathBdlChlVdoLocalRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoLocalRTPort.setStatus("obsolete")


class _TmnxMcPathBdlChlVdoLocalFccPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathBdlChlVdoLocalFccPort based on TmnxVdoPortNumber"""
    defaultValue = 4098


_TmnxMcPathBdlChlVdoLocalFccPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathBdlChlVdoLocalFccPort_Object = MibTableColumn
tmnxMcPathBdlChlVdoLocalFccPort = _TmnxMcPathBdlChlVdoLocalFccPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 22),
    _TmnxMcPathBdlChlVdoLocalFccPort_Type()
)
tmnxMcPathBdlChlVdoLocalFccPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoLocalFccPort.setStatus("obsolete")


class _TmnxMcPathBdlChlVdoGroupId_Type(TmnxVdoGrpIdOrInherit):
    """Custom type tmnxMcPathBdlChlVdoGroupId based on TmnxVdoGrpIdOrInherit"""
    defaultValue = -1


_TmnxMcPathBdlChlVdoGroupId_Type.__name__ = "TmnxVdoGrpIdOrInherit"
_TmnxMcPathBdlChlVdoGroupId_Object = MibTableColumn
tmnxMcPathBdlChlVdoGroupId = _TmnxMcPathBdlChlVdoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 23),
    _TmnxMcPathBdlChlVdoGroupId_Type()
)
tmnxMcPathBdlChlVdoGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoGroupId.setStatus("current")


class _TmnxMcPathBdlChlTunnelIfLspName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlChlTunnelIfLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlChlTunnelIfLspName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlChlTunnelIfLspName_Object = MibTableColumn
tmnxMcPathBdlChlTunnelIfLspName = _TmnxMcPathBdlChlTunnelIfLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 24),
    _TmnxMcPathBdlChlTunnelIfLspName_Type()
)
tmnxMcPathBdlChlTunnelIfLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlTunnelIfLspName.setStatus("current")


class _TmnxMcPathBdlChlTunIfSdAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathBdlChlTunIfSdAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlChlTunIfSdAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlChlTunIfSdAddrType_Object = MibTableColumn
tmnxMcPathBdlChlTunIfSdAddrType = _TmnxMcPathBdlChlTunIfSdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 25),
    _TmnxMcPathBdlChlTunIfSdAddrType_Type()
)
tmnxMcPathBdlChlTunIfSdAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlTunIfSdAddrType.setStatus("current")


class _TmnxMcPathBdlChlTunIfSdAddr_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlTunIfSdAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlChlTunIfSdAddr_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlTunIfSdAddr_Object = MibTableColumn
tmnxMcPathBdlChlTunIfSdAddr = _TmnxMcPathBdlChlTunIfSdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 26),
    _TmnxMcPathBdlChlTunIfSdAddr_Type()
)
tmnxMcPathBdlChlTunIfSdAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlTunIfSdAddr.setStatus("current")


class _TmnxMcPathBdlChlVdoLocalRTState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathBdlChlVdoLocalRTState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathBdlChlVdoLocalRTState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathBdlChlVdoLocalRTState_Object = MibTableColumn
tmnxMcPathBdlChlVdoLocalRTState = _TmnxMcPathBdlChlVdoLocalRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 27),
    _TmnxMcPathBdlChlVdoLocalRTState_Type()
)
tmnxMcPathBdlChlVdoLocalRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoLocalRTState.setStatus("current")


class _TmnxMcPathBdlChlVdoReorderAudio_Type(TmnxMcPathVdoReorderAudio):
    """Custom type tmnxMcPathBdlChlVdoReorderAudio based on TmnxMcPathVdoReorderAudio"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoReorderAudio_Type.__name__ = "TmnxMcPathVdoReorderAudio"
_TmnxMcPathBdlChlVdoReorderAudio_Object = MibTableColumn
tmnxMcPathBdlChlVdoReorderAudio = _TmnxMcPathBdlChlVdoReorderAudio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 28),
    _TmnxMcPathBdlChlVdoReorderAudio_Type()
)
tmnxMcPathBdlChlVdoReorderAudio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoReorderAudio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoReorderAudio.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoFccMinDuratn_Type(TmnxMcPathVdoFccMinDurationOrZero):
    """Custom type tmnxMcPathBdlChlVdoFccMinDuratn based on TmnxMcPathVdoFccMinDurationOrZero"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoFccMinDuratn_Type.__name__ = "TmnxMcPathVdoFccMinDurationOrZero"
_TmnxMcPathBdlChlVdoFccMinDuratn_Object = MibTableColumn
tmnxMcPathBdlChlVdoFccMinDuratn = _TmnxMcPathBdlChlVdoFccMinDuratn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 29),
    _TmnxMcPathBdlChlVdoFccMinDuratn_Type()
)
tmnxMcPathBdlChlVdoFccMinDuratn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoFccMinDuratn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoFccMinDuratn.setUnits("milliseconds")


class _TmnxMcPathBdlChlKAOverrideTimer_Type(TmnxMcPathKeepAliveOverrideTimer):
    """Custom type tmnxMcPathBdlChlKAOverrideTimer based on TmnxMcPathKeepAliveOverrideTimer"""
    defaultValue = 0


_TmnxMcPathBdlChlKAOverrideTimer_Type.__name__ = "TmnxMcPathKeepAliveOverrideTimer"
_TmnxMcPathBdlChlKAOverrideTimer_Object = MibTableColumn
tmnxMcPathBdlChlKAOverrideTimer = _TmnxMcPathBdlChlKAOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 30),
    _TmnxMcPathBdlChlKAOverrideTimer_Type()
)
tmnxMcPathBdlChlKAOverrideTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlKAOverrideTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlKAOverrideTimer.setUnits("seconds")


class _TmnxMcPathBdlChlP2MPId_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlP2MPId based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathBdlChlP2MPId_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlP2MPId_Object = MibTableColumn
tmnxMcPathBdlChlP2MPId = _TmnxMcPathBdlChlP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 31),
    _TmnxMcPathBdlChlP2MPId_Type()
)
tmnxMcPathBdlChlP2MPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlP2MPId.setStatus("current")


class _TmnxMcPathBdlChlVdoAnalyzer_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoAnalyzer based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoAnalyzer_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoAnalyzer_Object = MibTableColumn
tmnxMcPathBdlChlVdoAnalyzer = _TmnxMcPathBdlChlVdoAnalyzer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 32),
    _TmnxMcPathBdlChlVdoAnalyzer_Type()
)
tmnxMcPathBdlChlVdoAnalyzer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoAnalyzer.setStatus("current")


class _TmnxMcPathBdlChlVdoAnalyzerDesc_Type(TItemDescription):
    """Custom type tmnxMcPathBdlChlVdoAnalyzerDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMcPathBdlChlVdoAnalyzerDesc_Type.__name__ = "TItemDescription"
_TmnxMcPathBdlChlVdoAnalyzerDesc_Object = MibTableColumn
tmnxMcPathBdlChlVdoAnalyzerDesc = _TmnxMcPathBdlChlVdoAnalyzerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 33),
    _TmnxMcPathBdlChlVdoAnalyzerDesc_Type()
)
tmnxMcPathBdlChlVdoAnalyzerDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoAnalyzerDesc.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelSrc1Typ_Type(InetAddressType):
    """Custom type tmnxMcPathBdlChlVdoStrSelSrc1Typ based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoStrSelSrc1Typ_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlChlVdoStrSelSrc1Typ_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelSrc1Typ = _TmnxMcPathBdlChlVdoStrSelSrc1Typ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 34),
    _TmnxMcPathBdlChlVdoStrSelSrc1Typ_Type()
)
tmnxMcPathBdlChlVdoStrSelSrc1Typ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelSrc1Typ.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelSrc1_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlVdoStrSelSrc1 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlChlVdoStrSelSrc1_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlVdoStrSelSrc1_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelSrc1 = _TmnxMcPathBdlChlVdoStrSelSrc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 35),
    _TmnxMcPathBdlChlVdoStrSelSrc1_Type()
)
tmnxMcPathBdlChlVdoStrSelSrc1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelSrc1.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelIntf1_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlChlVdoStrSelIntf1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlChlVdoStrSelIntf1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlChlVdoStrSelIntf1_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelIntf1 = _TmnxMcPathBdlChlVdoStrSelIntf1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 36),
    _TmnxMcPathBdlChlVdoStrSelIntf1_Type()
)
tmnxMcPathBdlChlVdoStrSelIntf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelIntf1.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelSrc2Typ_Type(InetAddressType):
    """Custom type tmnxMcPathBdlChlVdoStrSelSrc2Typ based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoStrSelSrc2Typ_Type.__name__ = "InetAddressType"
_TmnxMcPathBdlChlVdoStrSelSrc2Typ_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelSrc2Typ = _TmnxMcPathBdlChlVdoStrSelSrc2Typ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 37),
    _TmnxMcPathBdlChlVdoStrSelSrc2Typ_Type()
)
tmnxMcPathBdlChlVdoStrSelSrc2Typ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelSrc2Typ.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelSrc2_Type(InetAddress):
    """Custom type tmnxMcPathBdlChlVdoStrSelSrc2 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathBdlChlVdoStrSelSrc2_Type.__name__ = "InetAddress"
_TmnxMcPathBdlChlVdoStrSelSrc2_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelSrc2 = _TmnxMcPathBdlChlVdoStrSelSrc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 38),
    _TmnxMcPathBdlChlVdoStrSelSrc2_Type()
)
tmnxMcPathBdlChlVdoStrSelSrc2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelSrc2.setStatus("current")


class _TmnxMcPathBdlChlVdoStrSelIntf2_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathBdlChlVdoStrSelIntf2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathBdlChlVdoStrSelIntf2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathBdlChlVdoStrSelIntf2_Object = MibTableColumn
tmnxMcPathBdlChlVdoStrSelIntf2 = _TmnxMcPathBdlChlVdoStrSelIntf2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 9, 1, 39),
    _TmnxMcPathBdlChlVdoStrSelIntf2_Type()
)
tmnxMcPathBdlChlVdoStrSelIntf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoStrSelIntf2.setStatus("current")
_TmnxMcPathChlSrcTable_Object = MibTable
tmnxMcPathChlSrcTable = _TmnxMcPathChlSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11)
)
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcTable.setStatus("current")
_TmnxMcPathChlSrcEntry_Object = MibTableRow
tmnxMcPathChlSrcEntry = _TmnxMcPathChlSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1)
)
tmnxMcPathChlSrcEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlStartAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlStartAddr"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlEndAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlEndAddr"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcSourceAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcEntry.setStatus("current")
_TmnxMcPathChlSrcSourceAddrType_Type = InetAddressType
_TmnxMcPathChlSrcSourceAddrType_Object = MibTableColumn
tmnxMcPathChlSrcSourceAddrType = _TmnxMcPathChlSrcSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 1),
    _TmnxMcPathChlSrcSourceAddrType_Type()
)
tmnxMcPathChlSrcSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcSourceAddrType.setStatus("current")


class _TmnxMcPathChlSrcSourceAddr_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathChlSrcSourceAddr_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcSourceAddr_Object = MibTableColumn
tmnxMcPathChlSrcSourceAddr = _TmnxMcPathChlSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 2),
    _TmnxMcPathChlSrcSourceAddr_Type()
)
tmnxMcPathChlSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcSourceAddr.setStatus("current")
_TmnxMcPathChlSrcRowStatus_Type = RowStatus
_TmnxMcPathChlSrcRowStatus_Object = MibTableColumn
tmnxMcPathChlSrcRowStatus = _TmnxMcPathChlSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 3),
    _TmnxMcPathChlSrcRowStatus_Type()
)
tmnxMcPathChlSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcRowStatus.setStatus("current")
_TmnxMcPathChlSrcLastChanged_Type = TimeStamp
_TmnxMcPathChlSrcLastChanged_Object = MibTableColumn
tmnxMcPathChlSrcLastChanged = _TmnxMcPathChlSrcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 4),
    _TmnxMcPathChlSrcLastChanged_Type()
)
tmnxMcPathChlSrcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcLastChanged.setStatus("current")


class _TmnxMcPathChlSrcAdminBw_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcAdminBw based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_TmnxMcPathChlSrcAdminBw_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcAdminBw_Object = MibTableColumn
tmnxMcPathChlSrcAdminBw = _TmnxMcPathChlSrcAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 5),
    _TmnxMcPathChlSrcAdminBw_Type()
)
tmnxMcPathChlSrcAdminBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcAdminBw.setUnits("kbps")


class _TmnxMcPathChlSrcPref_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcPref based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxMcPathChlSrcPref_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcPref_Object = MibTableColumn
tmnxMcPathChlSrcPref = _TmnxMcPathChlSrcPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 6),
    _TmnxMcPathChlSrcPref_Type()
)
tmnxMcPathChlSrcPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcPref.setStatus("current")


class _TmnxMcPathChlSrcBwActivity_Type(TmnxMcPathBwActivityTc):
    """Custom type tmnxMcPathChlSrcBwActivity based on TmnxMcPathBwActivityTc"""
    defaultValue = 0


_TmnxMcPathChlSrcBwActivity_Type.__name__ = "TmnxMcPathBwActivityTc"
_TmnxMcPathChlSrcBwActivity_Object = MibTableColumn
tmnxMcPathChlSrcBwActivity = _TmnxMcPathChlSrcBwActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 8),
    _TmnxMcPathChlSrcBwActivity_Type()
)
tmnxMcPathChlSrcBwActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcBwActivity.setStatus("current")


class _TmnxMcPathChlSrcBwFallDelay_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcBwFallDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_TmnxMcPathChlSrcBwFallDelay_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcBwFallDelay_Object = MibTableColumn
tmnxMcPathChlSrcBwFallDelay = _TmnxMcPathChlSrcBwFallDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 9),
    _TmnxMcPathChlSrcBwFallDelay_Type()
)
tmnxMcPathChlSrcBwFallDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcBwFallDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcBwFallDelay.setUnits("seconds")


class _TmnxMcPathChlSrcBwBlackHoleRt_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcBwBlackHoleRt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_TmnxMcPathChlSrcBwBlackHoleRt_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcBwBlackHoleRt_Object = MibTableColumn
tmnxMcPathChlSrcBwBlackHoleRt = _TmnxMcPathChlSrcBwBlackHoleRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 10),
    _TmnxMcPathChlSrcBwBlackHoleRt_Type()
)
tmnxMcPathChlSrcBwBlackHoleRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcBwBlackHoleRt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcBwBlackHoleRt.setUnits("kbps")


class _TmnxMcPathChlSrcExSfPath_Type(TmnxMcPathChlSfPathTypeTc):
    """Custom type tmnxMcPathChlSrcExSfPath based on TmnxMcPathChlSfPathTypeTc"""
    defaultValue = 0


_TmnxMcPathChlSrcExSfPath_Type.__name__ = "TmnxMcPathChlSfPathTypeTc"
_TmnxMcPathChlSrcExSfPath_Object = MibTableColumn
tmnxMcPathChlSrcExSfPath = _TmnxMcPathChlSrcExSfPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 11),
    _TmnxMcPathChlSrcExSfPath_Type()
)
tmnxMcPathChlSrcExSfPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcExSfPath.setStatus("current")


class _TmnxMcPathChlSrcVdoFCCState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathChlSrcVdoFCCState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathChlSrcVdoFCCState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathChlSrcVdoFCCState_Object = MibTableColumn
tmnxMcPathChlSrcVdoFCCState = _TmnxMcPathChlSrcVdoFCCState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 12),
    _TmnxMcPathChlSrcVdoFCCState_Type()
)
tmnxMcPathChlSrcVdoFCCState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoFCCState.setStatus("current")


class _TmnxMcPathChlSrcVdoRTState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathChlSrcVdoRTState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathChlSrcVdoRTState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathChlSrcVdoRTState_Object = MibTableColumn
tmnxMcPathChlSrcVdoRTState = _TmnxMcPathChlSrcVdoRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 13),
    _TmnxMcPathChlSrcVdoRTState_Type()
)
tmnxMcPathChlSrcVdoRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTState.setStatus("current")


class _TmnxMcPathChlSrcVdoChlType_Type(TmnxMcPathVdoChlTypeOrInherit):
    """Custom type tmnxMcPathChlSrcVdoChlType based on TmnxMcPathVdoChlTypeOrInherit"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoChlType_Type.__name__ = "TmnxMcPathVdoChlTypeOrInherit"
_TmnxMcPathChlSrcVdoChlType_Object = MibTableColumn
tmnxMcPathChlSrcVdoChlType = _TmnxMcPathChlSrcVdoChlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 14),
    _TmnxMcPathChlSrcVdoChlType_Type()
)
tmnxMcPathChlSrcVdoChlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoChlType.setStatus("current")


class _TmnxMcPathChlSrcVdoRTAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathChlSrcVdoRTAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoRTAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathChlSrcVdoRTAddrType_Object = MibTableColumn
tmnxMcPathChlSrcVdoRTAddrType = _TmnxMcPathChlSrcVdoRTAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 15),
    _TmnxMcPathChlSrcVdoRTAddrType_Type()
)
tmnxMcPathChlSrcVdoRTAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTAddrType.setStatus("current")


class _TmnxMcPathChlSrcVdoRTAddress_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcVdoRTAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathChlSrcVdoRTAddress_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcVdoRTAddress_Object = MibTableColumn
tmnxMcPathChlSrcVdoRTAddress = _TmnxMcPathChlSrcVdoRTAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 16),
    _TmnxMcPathChlSrcVdoRTAddress_Type()
)
tmnxMcPathChlSrcVdoRTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTAddress.setStatus("current")


class _TmnxMcPathChlSrcVdoRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathChlSrcVdoRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathChlSrcVdoRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathChlSrcVdoRTPort_Object = MibTableColumn
tmnxMcPathChlSrcVdoRTPort = _TmnxMcPathChlSrcVdoRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 17),
    _TmnxMcPathChlSrcVdoRTPort_Type()
)
tmnxMcPathChlSrcVdoRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTPort.setStatus("current")


class _TmnxMcPathChlSrcVdoRTBufferSize_Type(TmnxMcPathVdoBufferSize):
    """Custom type tmnxMcPathChlSrcVdoRTBufferSize based on TmnxMcPathVdoBufferSize"""
    defaultValue = 300


_TmnxMcPathChlSrcVdoRTBufferSize_Type.__name__ = "TmnxMcPathVdoBufferSize"
_TmnxMcPathChlSrcVdoRTBufferSize_Object = MibTableColumn
tmnxMcPathChlSrcVdoRTBufferSize = _TmnxMcPathChlSrcVdoRTBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 18),
    _TmnxMcPathChlSrcVdoRTBufferSize_Type()
)
tmnxMcPathChlSrcVdoRTBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoRTBufferSize.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoLocalRTPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathChlSrcVdoLocalRTPort based on TmnxVdoPortNumber"""
    defaultValue = 4096


_TmnxMcPathChlSrcVdoLocalRTPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathChlSrcVdoLocalRTPort_Object = MibTableColumn
tmnxMcPathChlSrcVdoLocalRTPort = _TmnxMcPathChlSrcVdoLocalRTPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 19),
    _TmnxMcPathChlSrcVdoLocalRTPort_Type()
)
tmnxMcPathChlSrcVdoLocalRTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoLocalRTPort.setStatus("obsolete")


class _TmnxMcPathChlSrcVdoLocalFccPort_Type(TmnxVdoPortNumber):
    """Custom type tmnxMcPathChlSrcVdoLocalFccPort based on TmnxVdoPortNumber"""
    defaultValue = 4098


_TmnxMcPathChlSrcVdoLocalFccPort_Type.__name__ = "TmnxVdoPortNumber"
_TmnxMcPathChlSrcVdoLocalFccPort_Object = MibTableColumn
tmnxMcPathChlSrcVdoLocalFccPort = _TmnxMcPathChlSrcVdoLocalFccPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 20),
    _TmnxMcPathChlSrcVdoLocalFccPort_Type()
)
tmnxMcPathChlSrcVdoLocalFccPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoLocalFccPort.setStatus("obsolete")


class _TmnxMcPathChlSrcVdoGroupId_Type(TmnxVdoGrpIdOrInherit):
    """Custom type tmnxMcPathChlSrcVdoGroupId based on TmnxVdoGrpIdOrInherit"""
    defaultValue = -1


_TmnxMcPathChlSrcVdoGroupId_Type.__name__ = "TmnxVdoGrpIdOrInherit"
_TmnxMcPathChlSrcVdoGroupId_Object = MibTableColumn
tmnxMcPathChlSrcVdoGroupId = _TmnxMcPathChlSrcVdoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 21),
    _TmnxMcPathChlSrcVdoGroupId_Type()
)
tmnxMcPathChlSrcVdoGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoGroupId.setStatus("current")


class _TmnxMcPathChlSrcTunnelIfLspName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathChlSrcTunnelIfLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathChlSrcTunnelIfLspName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathChlSrcTunnelIfLspName_Object = MibTableColumn
tmnxMcPathChlSrcTunnelIfLspName = _TmnxMcPathChlSrcTunnelIfLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 22),
    _TmnxMcPathChlSrcTunnelIfLspName_Type()
)
tmnxMcPathChlSrcTunnelIfLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcTunnelIfLspName.setStatus("current")


class _TmnxMcPathChlSrcTunIfSdAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathChlSrcTunIfSdAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathChlSrcTunIfSdAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathChlSrcTunIfSdAddrType_Object = MibTableColumn
tmnxMcPathChlSrcTunIfSdAddrType = _TmnxMcPathChlSrcTunIfSdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 23),
    _TmnxMcPathChlSrcTunIfSdAddrType_Type()
)
tmnxMcPathChlSrcTunIfSdAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcTunIfSdAddrType.setStatus("current")


class _TmnxMcPathChlSrcTunIfSdAddr_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcTunIfSdAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathChlSrcTunIfSdAddr_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcTunIfSdAddr_Object = MibTableColumn
tmnxMcPathChlSrcTunIfSdAddr = _TmnxMcPathChlSrcTunIfSdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 24),
    _TmnxMcPathChlSrcTunIfSdAddr_Type()
)
tmnxMcPathChlSrcTunIfSdAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcTunIfSdAddr.setStatus("current")


class _TmnxMcPathChlSrcVdoLocalRTState_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMcPathChlSrcVdoLocalRTState based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMcPathChlSrcVdoLocalRTState_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMcPathChlSrcVdoLocalRTState_Object = MibTableColumn
tmnxMcPathChlSrcVdoLocalRTState = _TmnxMcPathChlSrcVdoLocalRTState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 25),
    _TmnxMcPathChlSrcVdoLocalRTState_Type()
)
tmnxMcPathChlSrcVdoLocalRTState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoLocalRTState.setStatus("current")


class _TmnxMcPathChlSrcVdoReorderAudio_Type(TmnxMcPathVdoReorderAudio):
    """Custom type tmnxMcPathChlSrcVdoReorderAudio based on TmnxMcPathVdoReorderAudio"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoReorderAudio_Type.__name__ = "TmnxMcPathVdoReorderAudio"
_TmnxMcPathChlSrcVdoReorderAudio_Object = MibTableColumn
tmnxMcPathChlSrcVdoReorderAudio = _TmnxMcPathChlSrcVdoReorderAudio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 26),
    _TmnxMcPathChlSrcVdoReorderAudio_Type()
)
tmnxMcPathChlSrcVdoReorderAudio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoReorderAudio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoReorderAudio.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoFccMinDuratn_Type(TmnxMcPathVdoFccMinDurationOrZero):
    """Custom type tmnxMcPathChlSrcVdoFccMinDuratn based on TmnxMcPathVdoFccMinDurationOrZero"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoFccMinDuratn_Type.__name__ = "TmnxMcPathVdoFccMinDurationOrZero"
_TmnxMcPathChlSrcVdoFccMinDuratn_Object = MibTableColumn
tmnxMcPathChlSrcVdoFccMinDuratn = _TmnxMcPathChlSrcVdoFccMinDuratn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 27),
    _TmnxMcPathChlSrcVdoFccMinDuratn_Type()
)
tmnxMcPathChlSrcVdoFccMinDuratn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoFccMinDuratn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoFccMinDuratn.setUnits("milliseconds")


class _TmnxMcPathChlSrcKAOverrideTimer_Type(TmnxMcPathKeepAliveOverrideTimer):
    """Custom type tmnxMcPathChlSrcKAOverrideTimer based on TmnxMcPathKeepAliveOverrideTimer"""
    defaultValue = 0


_TmnxMcPathChlSrcKAOverrideTimer_Type.__name__ = "TmnxMcPathKeepAliveOverrideTimer"
_TmnxMcPathChlSrcKAOverrideTimer_Object = MibTableColumn
tmnxMcPathChlSrcKAOverrideTimer = _TmnxMcPathChlSrcKAOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 28),
    _TmnxMcPathChlSrcKAOverrideTimer_Type()
)
tmnxMcPathChlSrcKAOverrideTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcKAOverrideTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcKAOverrideTimer.setUnits("seconds")


class _TmnxMcPathChlSrcP2MPId_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcP2MPId based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathChlSrcP2MPId_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcP2MPId_Object = MibTableColumn
tmnxMcPathChlSrcP2MPId = _TmnxMcPathChlSrcP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 29),
    _TmnxMcPathChlSrcP2MPId_Type()
)
tmnxMcPathChlSrcP2MPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcP2MPId.setStatus("current")


class _TmnxMcPathChlSrcVdoAnalyzer_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoAnalyzer based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoAnalyzer_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoAnalyzer_Object = MibTableColumn
tmnxMcPathChlSrcVdoAnalyzer = _TmnxMcPathChlSrcVdoAnalyzer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 30),
    _TmnxMcPathChlSrcVdoAnalyzer_Type()
)
tmnxMcPathChlSrcVdoAnalyzer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoAnalyzer.setStatus("current")


class _TmnxMcPathChlSrcVdoAnalyzerDesc_Type(TItemDescription):
    """Custom type tmnxMcPathChlSrcVdoAnalyzerDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxMcPathChlSrcVdoAnalyzerDesc_Type.__name__ = "TItemDescription"
_TmnxMcPathChlSrcVdoAnalyzerDesc_Object = MibTableColumn
tmnxMcPathChlSrcVdoAnalyzerDesc = _TmnxMcPathChlSrcVdoAnalyzerDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 31),
    _TmnxMcPathChlSrcVdoAnalyzerDesc_Type()
)
tmnxMcPathChlSrcVdoAnalyzerDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoAnalyzerDesc.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeSrc1Type_Type(InetAddressType):
    """Custom type tmnxMcPathChlSrcVdoStSeSrc1Type based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoStSeSrc1Type_Type.__name__ = "InetAddressType"
_TmnxMcPathChlSrcVdoStSeSrc1Type_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeSrc1Type = _TmnxMcPathChlSrcVdoStSeSrc1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 32),
    _TmnxMcPathChlSrcVdoStSeSrc1Type_Type()
)
tmnxMcPathChlSrcVdoStSeSrc1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeSrc1Type.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeSrc1_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcVdoStSeSrc1 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathChlSrcVdoStSeSrc1_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcVdoStSeSrc1_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeSrc1 = _TmnxMcPathChlSrcVdoStSeSrc1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 33),
    _TmnxMcPathChlSrcVdoStSeSrc1_Type()
)
tmnxMcPathChlSrcVdoStSeSrc1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeSrc1.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeIntf1_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathChlSrcVdoStSeIntf1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathChlSrcVdoStSeIntf1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathChlSrcVdoStSeIntf1_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeIntf1 = _TmnxMcPathChlSrcVdoStSeIntf1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 34),
    _TmnxMcPathChlSrcVdoStSeIntf1_Type()
)
tmnxMcPathChlSrcVdoStSeIntf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeIntf1.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeSrc2Type_Type(InetAddressType):
    """Custom type tmnxMcPathChlSrcVdoStSeSrc2Type based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoStSeSrc2Type_Type.__name__ = "InetAddressType"
_TmnxMcPathChlSrcVdoStSeSrc2Type_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeSrc2Type = _TmnxMcPathChlSrcVdoStSeSrc2Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 35),
    _TmnxMcPathChlSrcVdoStSeSrc2Type_Type()
)
tmnxMcPathChlSrcVdoStSeSrc2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeSrc2Type.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeSrc2_Type(InetAddress):
    """Custom type tmnxMcPathChlSrcVdoStSeSrc2 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathChlSrcVdoStSeSrc2_Type.__name__ = "InetAddress"
_TmnxMcPathChlSrcVdoStSeSrc2_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeSrc2 = _TmnxMcPathChlSrcVdoStSeSrc2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 36),
    _TmnxMcPathChlSrcVdoStSeSrc2_Type()
)
tmnxMcPathChlSrcVdoStSeSrc2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeSrc2.setStatus("current")


class _TmnxMcPathChlSrcVdoStSeIntf2_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPathChlSrcVdoStSeIntf2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPathChlSrcVdoStSeIntf2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPathChlSrcVdoStSeIntf2_Object = MibTableColumn
tmnxMcPathChlSrcVdoStSeIntf2 = _TmnxMcPathChlSrcVdoStSeIntf2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 11, 1, 37),
    _TmnxMcPathChlSrcVdoStSeIntf2_Type()
)
tmnxMcPathChlSrcVdoStSeIntf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoStSeIntf2.setStatus("current")
_TmnxMcPathOperChlTable_Object = MibTable
tmnxMcPathOperChlTable = _TmnxMcPathOperChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12)
)
if mibBuilder.loadTexts:
    tmnxMcPathOperChlTable.setStatus("current")
_TmnxMcPathOperChlEntry_Object = MibTableRow
tmnxMcPathOperChlEntry = _TmnxMcPathOperChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1)
)
tmnxMcPathOperChlEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlRtrType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlGrpAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlGrpAddr"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlSrcAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlSrcAddr"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMcPathOperChlEntry.setStatus("current")
_TmnxMcPathOperChlRtrType_Type = TmnxMcPathRtrType
_TmnxMcPathOperChlRtrType_Object = MibTableColumn
tmnxMcPathOperChlRtrType = _TmnxMcPathOperChlRtrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 1),
    _TmnxMcPathOperChlRtrType_Type()
)
tmnxMcPathOperChlRtrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlRtrType.setStatus("current")
_TmnxMcPathOperChlGrpAddrType_Type = InetAddressType
_TmnxMcPathOperChlGrpAddrType_Object = MibTableColumn
tmnxMcPathOperChlGrpAddrType = _TmnxMcPathOperChlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 2),
    _TmnxMcPathOperChlGrpAddrType_Type()
)
tmnxMcPathOperChlGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlGrpAddrType.setStatus("current")


class _TmnxMcPathOperChlGrpAddr_Type(InetAddress):
    """Custom type tmnxMcPathOperChlGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathOperChlGrpAddr_Type.__name__ = "InetAddress"
_TmnxMcPathOperChlGrpAddr_Object = MibTableColumn
tmnxMcPathOperChlGrpAddr = _TmnxMcPathOperChlGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 3),
    _TmnxMcPathOperChlGrpAddr_Type()
)
tmnxMcPathOperChlGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlGrpAddr.setStatus("current")
_TmnxMcPathOperChlSrcAddrType_Type = InetAddressType
_TmnxMcPathOperChlSrcAddrType_Object = MibTableColumn
tmnxMcPathOperChlSrcAddrType = _TmnxMcPathOperChlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 4),
    _TmnxMcPathOperChlSrcAddrType_Type()
)
tmnxMcPathOperChlSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlSrcAddrType.setStatus("current")


class _TmnxMcPathOperChlSrcAddr_Type(InetAddress):
    """Custom type tmnxMcPathOperChlSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathOperChlSrcAddr_Type.__name__ = "InetAddress"
_TmnxMcPathOperChlSrcAddr_Object = MibTableColumn
tmnxMcPathOperChlSrcAddr = _TmnxMcPathOperChlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 5),
    _TmnxMcPathOperChlSrcAddr_Type()
)
tmnxMcPathOperChlSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlSrcAddr.setStatus("current")
_TmnxMcPathOperChlBandwidth_Type = Gauge32
_TmnxMcPathOperChlBandwidth_Object = MibTableColumn
tmnxMcPathOperChlBandwidth = _TmnxMcPathOperChlBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 6),
    _TmnxMcPathOperChlBandwidth_Type()
)
tmnxMcPathOperChlBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlBandwidth.setUnits("kbps")
_TmnxMcPathOperChlCurrentPath_Type = TmnxMcPathChlSfPathTypeTc
_TmnxMcPathOperChlCurrentPath_Object = MibTableColumn
tmnxMcPathOperChlCurrentPath = _TmnxMcPathOperChlCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 7),
    _TmnxMcPathOperChlCurrentPath_Type()
)
tmnxMcPathOperChlCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlCurrentPath.setStatus("current")
_TmnxMcPathOperChlExplicit_Type = TruthValue
_TmnxMcPathOperChlExplicit_Object = MibTableColumn
tmnxMcPathOperChlExplicit = _TmnxMcPathOperChlExplicit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 8),
    _TmnxMcPathOperChlExplicit_Type()
)
tmnxMcPathOperChlExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlExplicit.setStatus("current")
_TmnxMcPathOperChlAdminBw_Type = Gauge32
_TmnxMcPathOperChlAdminBw_Object = MibTableColumn
tmnxMcPathOperChlAdminBw = _TmnxMcPathOperChlAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 9),
    _TmnxMcPathOperChlAdminBw_Type()
)
tmnxMcPathOperChlAdminBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlAdminBw.setUnits("kbps")
_TmnxMcPathOperChlPref_Type = Gauge32
_TmnxMcPathOperChlPref_Object = MibTableColumn
tmnxMcPathOperChlPref = _TmnxMcPathOperChlPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 10),
    _TmnxMcPathOperChlPref_Type()
)
tmnxMcPathOperChlPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlPref.setStatus("current")
_TmnxMcPathOperChlBwBlackHole_Type = TruthValue
_TmnxMcPathOperChlBwBlackHole_Object = MibTableColumn
tmnxMcPathOperChlBwBlackHole = _TmnxMcPathOperChlBwBlackHole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 11),
    _TmnxMcPathOperChlBwBlackHole_Type()
)
tmnxMcPathOperChlBwBlackHole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlBwBlackHole.setStatus("current")
_TmnxMcPathOperChlBwBlackHoleRt_Type = Gauge32
_TmnxMcPathOperChlBwBlackHoleRt_Object = MibTableColumn
tmnxMcPathOperChlBwBlackHoleRt = _TmnxMcPathOperChlBwBlackHoleRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 12),
    _TmnxMcPathOperChlBwBlackHoleRt_Type()
)
tmnxMcPathOperChlBwBlackHoleRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlBwBlackHoleRt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlBwBlackHoleRt.setUnits("kbps")
_TmnxMcPathOperChlIngLastHighest_Type = Gauge32
_TmnxMcPathOperChlIngLastHighest_Object = MibTableColumn
tmnxMcPathOperChlIngLastHighest = _TmnxMcPathOperChlIngLastHighest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 13),
    _TmnxMcPathOperChlIngLastHighest_Type()
)
tmnxMcPathOperChlIngLastHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlIngLastHighest.setStatus("current")
_TmnxMcPathOperChlIngSecHighest_Type = Gauge32
_TmnxMcPathOperChlIngSecHighest_Object = MibTableColumn
tmnxMcPathOperChlIngSecHighest = _TmnxMcPathOperChlIngSecHighest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 14),
    _TmnxMcPathOperChlIngSecHighest_Type()
)
tmnxMcPathOperChlIngSecHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlIngSecHighest.setStatus("current")
_TmnxMcPathOperChlTimeRemaining_Type = Unsigned32
_TmnxMcPathOperChlTimeRemaining_Object = MibTableColumn
tmnxMcPathOperChlTimeRemaining = _TmnxMcPathOperChlTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 15),
    _TmnxMcPathOperChlTimeRemaining_Type()
)
tmnxMcPathOperChlTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlTimeRemaining.setUnits("seconds")
_TmnxMcPathOperChlCurrentPlane_Type = Unsigned32
_TmnxMcPathOperChlCurrentPlane_Object = MibTableColumn
tmnxMcPathOperChlCurrentPlane = _TmnxMcPathOperChlCurrentPlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 12, 1, 16),
    _TmnxMcPathOperChlCurrentPlane_Type()
)
tmnxMcPathOperChlCurrentPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathOperChlCurrentPlane.setStatus("current")
_TmnxMcPathMdaOperChlTable_Object = MibTable
tmnxMcPathMdaOperChlTable = _TmnxMcPathMdaOperChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13)
)
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlTable.setStatus("current")
_TmnxMcPathMdaOperChlEntry_Object = MibTableRow
tmnxMcPathMdaOperChlEntry = _TmnxMcPathMdaOperChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1)
)
tmnxMcPathMdaOperChlEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlRtrType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlGrpAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlGrpAddr"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlSrcAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlSrcAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlEntry.setStatus("current")
_TmnxMcPathMdaOperChlRtrType_Type = TmnxMcPathRtrType
_TmnxMcPathMdaOperChlRtrType_Object = MibTableColumn
tmnxMcPathMdaOperChlRtrType = _TmnxMcPathMdaOperChlRtrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 1),
    _TmnxMcPathMdaOperChlRtrType_Type()
)
tmnxMcPathMdaOperChlRtrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlRtrType.setStatus("current")
_TmnxMcPathMdaOperChlGrpAddrType_Type = InetAddressType
_TmnxMcPathMdaOperChlGrpAddrType_Object = MibTableColumn
tmnxMcPathMdaOperChlGrpAddrType = _TmnxMcPathMdaOperChlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 2),
    _TmnxMcPathMdaOperChlGrpAddrType_Type()
)
tmnxMcPathMdaOperChlGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlGrpAddrType.setStatus("current")


class _TmnxMcPathMdaOperChlGrpAddr_Type(InetAddress):
    """Custom type tmnxMcPathMdaOperChlGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathMdaOperChlGrpAddr_Type.__name__ = "InetAddress"
_TmnxMcPathMdaOperChlGrpAddr_Object = MibTableColumn
tmnxMcPathMdaOperChlGrpAddr = _TmnxMcPathMdaOperChlGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 3),
    _TmnxMcPathMdaOperChlGrpAddr_Type()
)
tmnxMcPathMdaOperChlGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlGrpAddr.setStatus("current")
_TmnxMcPathMdaOperChlSrcAddrType_Type = InetAddressType
_TmnxMcPathMdaOperChlSrcAddrType_Object = MibTableColumn
tmnxMcPathMdaOperChlSrcAddrType = _TmnxMcPathMdaOperChlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 4),
    _TmnxMcPathMdaOperChlSrcAddrType_Type()
)
tmnxMcPathMdaOperChlSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlSrcAddrType.setStatus("current")


class _TmnxMcPathMdaOperChlSrcAddr_Type(InetAddress):
    """Custom type tmnxMcPathMdaOperChlSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPathMdaOperChlSrcAddr_Type.__name__ = "InetAddress"
_TmnxMcPathMdaOperChlSrcAddr_Object = MibTableColumn
tmnxMcPathMdaOperChlSrcAddr = _TmnxMcPathMdaOperChlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 5),
    _TmnxMcPathMdaOperChlSrcAddr_Type()
)
tmnxMcPathMdaOperChlSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlSrcAddr.setStatus("current")
_TmnxMcPathMdaOperChlBandwidth_Type = Gauge32
_TmnxMcPathMdaOperChlBandwidth_Object = MibTableColumn
tmnxMcPathMdaOperChlBandwidth = _TmnxMcPathMdaOperChlBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 6),
    _TmnxMcPathMdaOperChlBandwidth_Type()
)
tmnxMcPathMdaOperChlBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlBandwidth.setUnits("kbps")
_TmnxMcPathMdaOperChlCurrentPath_Type = TmnxMcPathChlSfPathTypeTc
_TmnxMcPathMdaOperChlCurrentPath_Object = MibTableColumn
tmnxMcPathMdaOperChlCurrentPath = _TmnxMcPathMdaOperChlCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 7),
    _TmnxMcPathMdaOperChlCurrentPath_Type()
)
tmnxMcPathMdaOperChlCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlCurrentPath.setStatus("current")
_TmnxMcPathMdaOperChlExplicit_Type = TruthValue
_TmnxMcPathMdaOperChlExplicit_Object = MibTableColumn
tmnxMcPathMdaOperChlExplicit = _TmnxMcPathMdaOperChlExplicit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 8),
    _TmnxMcPathMdaOperChlExplicit_Type()
)
tmnxMcPathMdaOperChlExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlExplicit.setStatus("current")
_TmnxMcPathMdaOperChlAdminBw_Type = Gauge32
_TmnxMcPathMdaOperChlAdminBw_Object = MibTableColumn
tmnxMcPathMdaOperChlAdminBw = _TmnxMcPathMdaOperChlAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 9),
    _TmnxMcPathMdaOperChlAdminBw_Type()
)
tmnxMcPathMdaOperChlAdminBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlAdminBw.setUnits("kbps")
_TmnxMcPathMdaOperChlPref_Type = Gauge32
_TmnxMcPathMdaOperChlPref_Object = MibTableColumn
tmnxMcPathMdaOperChlPref = _TmnxMcPathMdaOperChlPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 10),
    _TmnxMcPathMdaOperChlPref_Type()
)
tmnxMcPathMdaOperChlPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlPref.setStatus("current")
_TmnxMcPathMdaOperChlBwBlackHole_Type = TruthValue
_TmnxMcPathMdaOperChlBwBlackHole_Object = MibTableColumn
tmnxMcPathMdaOperChlBwBlackHole = _TmnxMcPathMdaOperChlBwBlackHole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 11),
    _TmnxMcPathMdaOperChlBwBlackHole_Type()
)
tmnxMcPathMdaOperChlBwBlackHole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlBwBlackHole.setStatus("current")
_TmnxMcPathMdaOperChlBwBlackHoleRt_Type = Gauge32
_TmnxMcPathMdaOperChlBwBlackHoleRt_Object = MibTableColumn
tmnxMcPathMdaOperChlBwBlackHoleRt = _TmnxMcPathMdaOperChlBwBlackHoleRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 12),
    _TmnxMcPathMdaOperChlBwBlackHoleRt_Type()
)
tmnxMcPathMdaOperChlBwBlackHoleRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlBwBlackHoleRt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlBwBlackHoleRt.setUnits("kbps")
_TmnxMcPathMdaOperChlIngLastHigh_Type = Gauge32
_TmnxMcPathMdaOperChlIngLastHigh_Object = MibTableColumn
tmnxMcPathMdaOperChlIngLastHigh = _TmnxMcPathMdaOperChlIngLastHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 13),
    _TmnxMcPathMdaOperChlIngLastHigh_Type()
)
tmnxMcPathMdaOperChlIngLastHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlIngLastHigh.setStatus("current")
_TmnxMcPathMdaOperChlIngSecHigh_Type = Gauge32
_TmnxMcPathMdaOperChlIngSecHigh_Object = MibTableColumn
tmnxMcPathMdaOperChlIngSecHigh = _TmnxMcPathMdaOperChlIngSecHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 14),
    _TmnxMcPathMdaOperChlIngSecHigh_Type()
)
tmnxMcPathMdaOperChlIngSecHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlIngSecHigh.setStatus("current")
_TmnxMcPathMdaOperChlTimeRemain_Type = Unsigned32
_TmnxMcPathMdaOperChlTimeRemain_Object = MibTableColumn
tmnxMcPathMdaOperChlTimeRemain = _TmnxMcPathMdaOperChlTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 15),
    _TmnxMcPathMdaOperChlTimeRemain_Type()
)
tmnxMcPathMdaOperChlTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlTimeRemain.setUnits("seconds")
_TmnxMcPathMdaOperChlCurrentPlane_Type = Unsigned32
_TmnxMcPathMdaOperChlCurrentPlane_Object = MibTableColumn
tmnxMcPathMdaOperChlCurrentPlane = _TmnxMcPathMdaOperChlCurrentPlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 13, 1, 16),
    _TmnxMcPathMdaOperChlCurrentPlane_Type()
)
tmnxMcPathMdaOperChlCurrentPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathMdaOperChlCurrentPlane.setStatus("current")
_TmnxMcPathBwPlcyT2PathTable_Object = MibTable
tmnxMcPathBwPlcyT2PathTable = _TmnxMcPathBwPlcyT2PathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14)
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathTable.setStatus("current")
_TmnxMcPathBwPlcyT2PathEntry_Object = MibTableRow
tmnxMcPathBwPlcyT2PathEntry = _TmnxMcPathBwPlcyT2PathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1)
)
tmnxMcPathBwPlcyT2PathEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathType"),
)
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathEntry.setStatus("current")
_TmnxMcPathBwPlcyT2PathType_Type = TmnxMcPathChlSfPathTypeTc
_TmnxMcPathBwPlcyT2PathType_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathType = _TmnxMcPathBwPlcyT2PathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 1),
    _TmnxMcPathBwPlcyT2PathType_Type()
)
tmnxMcPathBwPlcyT2PathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathType.setStatus("current")


class _TmnxMcPathBwPlcyT2PathCbs_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyT2PathCbs based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxMcPathBwPlcyT2PathCbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyT2PathCbs_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathCbs = _TmnxMcPathBwPlcyT2PathCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 2),
    _TmnxMcPathBwPlcyT2PathCbs_Type()
)
tmnxMcPathBwPlcyT2PathCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathCbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathCbs.setUnits("hundredths of a percent")


class _TmnxMcPathBwPlcyT2PathMbs_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyT2PathMbs based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxMcPathBwPlcyT2PathMbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyT2PathMbs_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathMbs = _TmnxMcPathBwPlcyT2PathMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 3),
    _TmnxMcPathBwPlcyT2PathMbs_Type()
)
tmnxMcPathBwPlcyT2PathMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathMbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathMbs.setUnits("hundredths of a percent")


class _TmnxMcPathBwPlcyT2PathHighPrio_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyT2PathHighPrio based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMcPathBwPlcyT2PathHighPrio_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyT2PathHighPrio_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathHighPrio = _TmnxMcPathBwPlcyT2PathHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 4),
    _TmnxMcPathBwPlcyT2PathHighPrio_Type()
)
tmnxMcPathBwPlcyT2PathHighPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathHighPrio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathHighPrio.setUnits("percentage")


class _TmnxMcPathBwPlcyT2PathPaths_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyT2PathPaths based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TmnxMcPathBwPlcyT2PathPaths_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyT2PathPaths_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathPaths = _TmnxMcPathBwPlcyT2PathPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 5),
    _TmnxMcPathBwPlcyT2PathPaths_Type()
)
tmnxMcPathBwPlcyT2PathPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathPaths.setStatus("current")


class _TmnxMcPathBwPlcyT2PathDualPaths_Type(Unsigned32):
    """Custom type tmnxMcPathBwPlcyT2PathDualPaths based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TmnxMcPathBwPlcyT2PathDualPaths_Type.__name__ = "Unsigned32"
_TmnxMcPathBwPlcyT2PathDualPaths_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathDualPaths = _TmnxMcPathBwPlcyT2PathDualPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 6),
    _TmnxMcPathBwPlcyT2PathDualPaths_Type()
)
tmnxMcPathBwPlcyT2PathDualPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathDualPaths.setStatus("current")
_TmnxMcPathBwPlcyT2PathLastChanged_Type = TimeStamp
_TmnxMcPathBwPlcyT2PathLastChanged_Object = MibTableColumn
tmnxMcPathBwPlcyT2PathLastChanged = _TmnxMcPathBwPlcyT2PathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 14, 1, 7),
    _TmnxMcPathBwPlcyT2PathLastChanged_Type()
)
tmnxMcPathBwPlcyT2PathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBwPlcyT2PathLastChanged.setStatus("current")
_TmnxMcPathVdoPlcyTable_Object = MibTable
tmnxMcPathVdoPlcyTable = _TmnxMcPathVdoPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15)
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyTable.setStatus("current")
_TmnxMcPathVdoPlcyEntry_Object = MibTableRow
tmnxMcPathVdoPlcyEntry = _TmnxMcPathVdoPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1)
)
tmnxMcPathVdoPlcyEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyName"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyIfAddrType"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyIfAddress"),
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyChlType"),
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyEntry.setStatus("current")
_TmnxMcPathVdoPlcyIfAddrType_Type = InetAddressType
_TmnxMcPathVdoPlcyIfAddrType_Object = MibTableColumn
tmnxMcPathVdoPlcyIfAddrType = _TmnxMcPathVdoPlcyIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 1),
    _TmnxMcPathVdoPlcyIfAddrType_Type()
)
tmnxMcPathVdoPlcyIfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyIfAddrType.setStatus("current")


class _TmnxMcPathVdoPlcyIfAddress_Type(InetAddress):
    """Custom type tmnxMcPathVdoPlcyIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathVdoPlcyIfAddress_Type.__name__ = "InetAddress"
_TmnxMcPathVdoPlcyIfAddress_Object = MibTableColumn
tmnxMcPathVdoPlcyIfAddress = _TmnxMcPathVdoPlcyIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 2),
    _TmnxMcPathVdoPlcyIfAddress_Type()
)
tmnxMcPathVdoPlcyIfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyIfAddress.setStatus("current")
_TmnxMcPathVdoPlcyChlType_Type = TmnxMcPathVdoChlType
_TmnxMcPathVdoPlcyChlType_Object = MibTableColumn
tmnxMcPathVdoPlcyChlType = _TmnxMcPathVdoPlcyChlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 3),
    _TmnxMcPathVdoPlcyChlType_Type()
)
tmnxMcPathVdoPlcyChlType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyChlType.setStatus("current")
_TmnxMcPathVdoPlcyRowStatus_Type = RowStatus
_TmnxMcPathVdoPlcyRowStatus_Object = MibTableColumn
tmnxMcPathVdoPlcyRowStatus = _TmnxMcPathVdoPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 4),
    _TmnxMcPathVdoPlcyRowStatus_Type()
)
tmnxMcPathVdoPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyRowStatus.setStatus("current")
_TmnxMcPathVdoPlcyLastChanged_Type = TimeStamp
_TmnxMcPathVdoPlcyLastChanged_Object = MibTableColumn
tmnxMcPathVdoPlcyLastChanged = _TmnxMcPathVdoPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 5),
    _TmnxMcPathVdoPlcyLastChanged_Type()
)
tmnxMcPathVdoPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyLastChanged.setStatus("current")


class _TmnxMcPathVdoPlcyLclRTSvrState_Type(TruthValue):
    """Custom type tmnxMcPathVdoPlcyLclRTSvrState based on TruthValue"""
    defaultValue = 2


_TmnxMcPathVdoPlcyLclRTSvrState_Type.__name__ = "TruthValue"
_TmnxMcPathVdoPlcyLclRTSvrState_Object = MibTableColumn
tmnxMcPathVdoPlcyLclRTSvrState = _TmnxMcPathVdoPlcyLclRTSvrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 6),
    _TmnxMcPathVdoPlcyLclRTSvrState_Type()
)
tmnxMcPathVdoPlcyLclRTSvrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyLclRTSvrState.setStatus("current")


class _TmnxMcPathVdoPlcyRTRate_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyRTRate based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMcPathVdoPlcyRTRate_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyRTRate_Object = MibTableColumn
tmnxMcPathVdoPlcyRTRate = _TmnxMcPathVdoPlcyRTRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 7),
    _TmnxMcPathVdoPlcyRTRate_Type()
)
tmnxMcPathVdoPlcyRTRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyRTRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyRTRate.setUnits("percent")


class _TmnxMcPathVdoPlcySubBwLimit_Type(TmnxMcPathVdoBwLimit):
    """Custom type tmnxMcPathVdoPlcySubBwLimit based on TmnxMcPathVdoBwLimit"""
    defaultValue = 4294967295


_TmnxMcPathVdoPlcySubBwLimit_Type.__name__ = "TmnxMcPathVdoBwLimit"
_TmnxMcPathVdoPlcySubBwLimit_Object = MibTableColumn
tmnxMcPathVdoPlcySubBwLimit = _TmnxMcPathVdoPlcySubBwLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 8),
    _TmnxMcPathVdoPlcySubBwLimit_Type()
)
tmnxMcPathVdoPlcySubBwLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcySubBwLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcySubBwLimit.setUnits("kbps")


class _TmnxMcPathVdoPlcyFCCSvrMode_Type(TmnxVdoFccServerMode):
    """Custom type tmnxMcPathVdoPlcyFCCSvrMode based on TmnxVdoFccServerMode"""
    defaultValue = 0


_TmnxMcPathVdoPlcyFCCSvrMode_Type.__name__ = "TmnxVdoFccServerMode"
_TmnxMcPathVdoPlcyFCCSvrMode_Object = MibTableColumn
tmnxMcPathVdoPlcyFCCSvrMode = _TmnxMcPathVdoPlcyFCCSvrMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 9),
    _TmnxMcPathVdoPlcyFCCSvrMode_Type()
)
tmnxMcPathVdoPlcyFCCSvrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCSvrMode.setStatus("current")


class _TmnxMcPathVdoPlcyFCCBurst_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyFCCBurst based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxMcPathVdoPlcyFCCBurst_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyFCCBurst_Object = MibTableColumn
tmnxMcPathVdoPlcyFCCBurst = _TmnxMcPathVdoPlcyFCCBurst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 10),
    _TmnxMcPathVdoPlcyFCCBurst_Type()
)
tmnxMcPathVdoPlcyFCCBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCBurst.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCBurst.setUnits("percent")


class _TmnxMcPathVdoPlcyFCCMcHandover_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyFCCMcHandover based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxMcPathVdoPlcyFCCMcHandover_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyFCCMcHandover_Object = MibTableColumn
tmnxMcPathVdoPlcyFCCMcHandover = _TmnxMcPathVdoPlcyFCCMcHandover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 11),
    _TmnxMcPathVdoPlcyFCCMcHandover_Type()
)
tmnxMcPathVdoPlcyFCCMcHandover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCMcHandover.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCMcHandover.setUnits("percent")


class _TmnxMcPathVdoPlcyFCCDentThd_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyFCCDentThd based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxMcPathVdoPlcyFCCDentThd_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyFCCDentThd_Object = MibTableColumn
tmnxMcPathVdoPlcyFCCDentThd = _TmnxMcPathVdoPlcyFCCDentThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 12),
    _TmnxMcPathVdoPlcyFCCDentThd_Type()
)
tmnxMcPathVdoPlcyFCCDentThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyFCCDentThd.setStatus("current")


class _TmnxMcPathVdoPlcyRTPayloadType_Type(TmnxMcPathVdoPayloadType):
    """Custom type tmnxMcPathVdoPlcyRTPayloadType based on TmnxMcPathVdoPayloadType"""
    defaultValue = 99


_TmnxMcPathVdoPlcyRTPayloadType_Type.__name__ = "TmnxMcPathVdoPayloadType"
_TmnxMcPathVdoPlcyRTPayloadType_Object = MibTableColumn
tmnxMcPathVdoPlcyRTPayloadType = _TmnxMcPathVdoPlcyRTPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 13),
    _TmnxMcPathVdoPlcyRTPayloadType_Type()
)
tmnxMcPathVdoPlcyRTPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyRTPayloadType.setStatus("current")


class _TmnxMcPathVdoPlcyMaxClntSessions_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyMaxClntSessions based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_TmnxMcPathVdoPlcyMaxClntSessions_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyMaxClntSessions_Object = MibTableColumn
tmnxMcPathVdoPlcyMaxClntSessions = _TmnxMcPathVdoPlcyMaxClntSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 14),
    _TmnxMcPathVdoPlcyMaxClntSessions_Type()
)
tmnxMcPathVdoPlcyMaxClntSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyMaxClntSessions.setStatus("current")


class _TmnxMcPathVdoPlcyMaxIgmpLatency_Type(Unsigned32):
    """Custom type tmnxMcPathVdoPlcyMaxIgmpLatency based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxMcPathVdoPlcyMaxIgmpLatency_Type.__name__ = "Unsigned32"
_TmnxMcPathVdoPlcyMaxIgmpLatency_Object = MibTableColumn
tmnxMcPathVdoPlcyMaxIgmpLatency = _TmnxMcPathVdoPlcyMaxIgmpLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 15, 1, 15),
    _TmnxMcPathVdoPlcyMaxIgmpLatency_Type()
)
tmnxMcPathVdoPlcyMaxIgmpLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyMaxIgmpLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathVdoPlcyMaxIgmpLatency.setUnits("milliseconds")
_TmnxMcPathBdlExtTable_Object = MibTable
tmnxMcPathBdlExtTable = _TmnxMcPathBdlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlExtTable.setStatus("current")
_TmnxMcPathBdlExtEntry_Object = MibTableRow
tmnxMcPathBdlExtEntry = _TmnxMcPathBdlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlExtEntry.setStatus("current")
_TmnxMcPathBdlVdoLastChanged_Type = TimeStamp
_TmnxMcPathBdlVdoLastChanged_Object = MibTableColumn
tmnxMcPathBdlVdoLastChanged = _TmnxMcPathBdlVdoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 1),
    _TmnxMcPathBdlVdoLastChanged_Type()
)
tmnxMcPathBdlVdoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoLastChanged.setStatus("current")


class _TmnxMcPathBdlVdoCcError_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoCcError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoCcError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoCcError_Object = MibTableColumn
tmnxMcPathBdlVdoCcError = _TmnxMcPathBdlVdoCcError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 2),
    _TmnxMcPathBdlVdoCcError_Type()
)
tmnxMcPathBdlVdoCcError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoCcError.setStatus("current")


class _TmnxMcPathBdlVdoPatRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPatRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPatRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPatRepError_Object = MibTableColumn
tmnxMcPathBdlVdoPatRepError = _TmnxMcPathBdlVdoPatRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 3),
    _TmnxMcPathBdlVdoPatRepError_Type()
)
tmnxMcPathBdlVdoPatRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPatRepError.setStatus("current")


class _TmnxMcPathBdlVdoTncPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoTncPatRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathBdlVdoTncPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoTncPatRep_Object = MibTableColumn
tmnxMcPathBdlVdoTncPatRep = _TmnxMcPathBdlVdoTncPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 4),
    _TmnxMcPathBdlVdoTncPatRep_Type()
)
tmnxMcPathBdlVdoTncPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoQosPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoQosPatRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathBdlVdoQosPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoQosPatRep_Object = MibTableColumn
tmnxMcPathBdlVdoQosPatRep = _TmnxMcPathBdlVdoQosPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 5),
    _TmnxMcPathBdlVdoQosPatRep_Type()
)
tmnxMcPathBdlVdoQosPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPoaPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoPoaPatRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathBdlVdoPoaPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoPoaPatRep_Object = MibTableColumn
tmnxMcPathBdlVdoPoaPatRep = _TmnxMcPathBdlVdoPoaPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 6),
    _TmnxMcPathBdlVdoPoaPatRep_Type()
)
tmnxMcPathBdlVdoPoaPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPatSyntax_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPatSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPatSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPatSyntax_Object = MibTableColumn
tmnxMcPathBdlVdoPatSyntax = _TmnxMcPathBdlVdoPatSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 7),
    _TmnxMcPathBdlVdoPatSyntax_Type()
)
tmnxMcPathBdlVdoPatSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPatSyntax.setStatus("current")


class _TmnxMcPathBdlVdoPcrRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPcrRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPcrRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPcrRepError_Object = MibTableColumn
tmnxMcPathBdlVdoPcrRepError = _TmnxMcPathBdlVdoPcrRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 8),
    _TmnxMcPathBdlVdoPcrRepError_Type()
)
tmnxMcPathBdlVdoPcrRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPcrRepError.setStatus("current")


class _TmnxMcPathBdlVdoTncPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoTncPcrRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathBdlVdoTncPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoTncPcrRep_Object = MibTableColumn
tmnxMcPathBdlVdoTncPcrRep = _TmnxMcPathBdlVdoTncPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 9),
    _TmnxMcPathBdlVdoTncPcrRep_Type()
)
tmnxMcPathBdlVdoTncPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoQosPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoQosPcrRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathBdlVdoQosPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoQosPcrRep_Object = MibTableColumn
tmnxMcPathBdlVdoQosPcrRep = _TmnxMcPathBdlVdoQosPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 10),
    _TmnxMcPathBdlVdoQosPcrRep_Type()
)
tmnxMcPathBdlVdoQosPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPoaPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoPoaPcrRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathBdlVdoPoaPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoPoaPcrRep_Object = MibTableColumn
tmnxMcPathBdlVdoPoaPcrRep = _TmnxMcPathBdlVdoPoaPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 11),
    _TmnxMcPathBdlVdoPoaPcrRep_Type()
)
tmnxMcPathBdlVdoPoaPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoVidPIDAbsent_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoVidPIDAbsent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathBdlVdoVidPIDAbsent_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoVidPIDAbsent_Object = MibTableColumn
tmnxMcPathBdlVdoVidPIDAbsent = _TmnxMcPathBdlVdoVidPIDAbsent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 12),
    _TmnxMcPathBdlVdoVidPIDAbsent_Type()
)
tmnxMcPathBdlVdoVidPIDAbsent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoVidPIDAbsent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoVidPIDAbsent.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPIDPmtUnref_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPIDPmtUnref based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPIDPmtUnref_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPIDPmtUnref_Object = MibTableColumn
tmnxMcPathBdlVdoPIDPmtUnref = _TmnxMcPathBdlVdoPIDPmtUnref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 13),
    _TmnxMcPathBdlVdoPIDPmtUnref_Type()
)
tmnxMcPathBdlVdoPIDPmtUnref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPIDPmtUnref.setStatus("current")


class _TmnxMcPathBdlVdoPmtRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPmtRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPmtRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPmtRepError_Object = MibTableColumn
tmnxMcPathBdlVdoPmtRepError = _TmnxMcPathBdlVdoPmtRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 14),
    _TmnxMcPathBdlVdoPmtRepError_Type()
)
tmnxMcPathBdlVdoPmtRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPmtRepError.setStatus("current")


class _TmnxMcPathBdlVdoTncPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoTncPmtRep based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4800),
    )


_TmnxMcPathBdlVdoTncPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoTncPmtRep_Object = MibTableColumn
tmnxMcPathBdlVdoTncPmtRep = _TmnxMcPathBdlVdoTncPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 15),
    _TmnxMcPathBdlVdoTncPmtRep_Type()
)
tmnxMcPathBdlVdoTncPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTncPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoQosPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoQosPmtRep based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4900),
    )


_TmnxMcPathBdlVdoQosPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoQosPmtRep_Object = MibTableColumn
tmnxMcPathBdlVdoQosPmtRep = _TmnxMcPathBdlVdoQosPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 16),
    _TmnxMcPathBdlVdoQosPmtRep_Type()
)
tmnxMcPathBdlVdoQosPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoQosPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPoaPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoPoaPmtRep based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 5000),
    )


_TmnxMcPathBdlVdoPoaPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoPoaPmtRep_Object = MibTableColumn
tmnxMcPathBdlVdoPoaPmtRep = _TmnxMcPathBdlVdoPoaPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 17),
    _TmnxMcPathBdlVdoPoaPmtRep_Type()
)
tmnxMcPathBdlVdoPoaPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPoaPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlVdoPmtSyntax_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoPmtSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoPmtSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoPmtSyntax_Object = MibTableColumn
tmnxMcPathBdlVdoPmtSyntax = _TmnxMcPathBdlVdoPmtSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 18),
    _TmnxMcPathBdlVdoPmtSyntax_Type()
)
tmnxMcPathBdlVdoPmtSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoPmtSyntax.setStatus("current")


class _TmnxMcPathBdlVdoScte35Error_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoScte35Error based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoScte35Error_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoScte35Error_Object = MibTableColumn
tmnxMcPathBdlVdoScte35Error = _TmnxMcPathBdlVdoScte35Error_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 19),
    _TmnxMcPathBdlVdoScte35Error_Type()
)
tmnxMcPathBdlVdoScte35Error.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoScte35Error.setStatus("obsolete")


class _TmnxMcPathBdlVdoTeiError_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoTeiError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoTeiError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoTeiError_Object = MibTableColumn
tmnxMcPathBdlVdoTeiError = _TmnxMcPathBdlVdoTeiError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 20),
    _TmnxMcPathBdlVdoTeiError_Type()
)
tmnxMcPathBdlVdoTeiError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTeiError.setStatus("current")


class _TmnxMcPathBdlVdoTsSyncLoss_Type(TruthValue):
    """Custom type tmnxMcPathBdlVdoTsSyncLoss based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlVdoTsSyncLoss_Type.__name__ = "TruthValue"
_TmnxMcPathBdlVdoTsSyncLoss_Object = MibTableColumn
tmnxMcPathBdlVdoTsSyncLoss = _TmnxMcPathBdlVdoTsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 21),
    _TmnxMcPathBdlVdoTsSyncLoss_Type()
)
tmnxMcPathBdlVdoTsSyncLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoTsSyncLoss.setStatus("current")


class _TmnxMcPathBdlVdoNonVidPIDAbsent_Type(Unsigned32):
    """Custom type tmnxMcPathBdlVdoNonVidPIDAbsent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathBdlVdoNonVidPIDAbsent_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlVdoNonVidPIDAbsent_Object = MibTableColumn
tmnxMcPathBdlVdoNonVidPIDAbsent = _TmnxMcPathBdlVdoNonVidPIDAbsent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 22),
    _TmnxMcPathBdlVdoNonVidPIDAbsent_Type()
)
tmnxMcPathBdlVdoNonVidPIDAbsent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoNonVidPIDAbsent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoNonVidPIDAbsent.setUnits("milliseconds")


class _TmnxMcPathBdlVdoReportAlarm_Type(TmnxVdoAnalyzerAlarm):
    """Custom type tmnxMcPathBdlVdoReportAlarm based on TmnxVdoAnalyzerAlarm"""
    defaultValue = 0


_TmnxMcPathBdlVdoReportAlarm_Type.__name__ = "TmnxVdoAnalyzerAlarm"
_TmnxMcPathBdlVdoReportAlarm_Object = MibTableColumn
tmnxMcPathBdlVdoReportAlarm = _TmnxMcPathBdlVdoReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 16, 1, 23),
    _TmnxMcPathBdlVdoReportAlarm_Type()
)
tmnxMcPathBdlVdoReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlVdoReportAlarm.setStatus("current")
_TmnxMcPathBdlChlExtTable_Object = MibTable
tmnxMcPathBdlChlExtTable = _TmnxMcPathBdlChlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlExtTable.setStatus("current")
_TmnxMcPathBdlChlExtEntry_Object = MibTableRow
tmnxMcPathBdlChlExtEntry = _TmnxMcPathBdlChlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlExtEntry.setStatus("current")
_TmnxMcPathBdlChlVdoLastChanged_Type = TimeStamp
_TmnxMcPathBdlChlVdoLastChanged_Object = MibTableColumn
tmnxMcPathBdlChlVdoLastChanged = _TmnxMcPathBdlChlVdoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 1),
    _TmnxMcPathBdlChlVdoLastChanged_Type()
)
tmnxMcPathBdlChlVdoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoLastChanged.setStatus("current")


class _TmnxMcPathBdlChlVdoCcError_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoCcError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoCcError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoCcError_Object = MibTableColumn
tmnxMcPathBdlChlVdoCcError = _TmnxMcPathBdlChlVdoCcError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 2),
    _TmnxMcPathBdlChlVdoCcError_Type()
)
tmnxMcPathBdlChlVdoCcError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoCcError.setStatus("current")


class _TmnxMcPathBdlChlVdoPatRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPatRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPatRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPatRepError_Object = MibTableColumn
tmnxMcPathBdlChlVdoPatRepError = _TmnxMcPathBdlChlVdoPatRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 3),
    _TmnxMcPathBdlChlVdoPatRepError_Type()
)
tmnxMcPathBdlChlVdoPatRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPatRepError.setStatus("current")


class _TmnxMcPathBdlChlVdoTncPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoTncPatRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathBdlChlVdoTncPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoTncPatRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoTncPatRep = _TmnxMcPathBdlChlVdoTncPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 4),
    _TmnxMcPathBdlChlVdoTncPatRep_Type()
)
tmnxMcPathBdlChlVdoTncPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoQosPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoQosPatRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathBdlChlVdoQosPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoQosPatRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoQosPatRep = _TmnxMcPathBdlChlVdoQosPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 5),
    _TmnxMcPathBdlChlVdoQosPatRep_Type()
)
tmnxMcPathBdlChlVdoQosPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPoaPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoPoaPatRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathBdlChlVdoPoaPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoPoaPatRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoPoaPatRep = _TmnxMcPathBdlChlVdoPoaPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 6),
    _TmnxMcPathBdlChlVdoPoaPatRep_Type()
)
tmnxMcPathBdlChlVdoPoaPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPatRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPatSyntax_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPatSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPatSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPatSyntax_Object = MibTableColumn
tmnxMcPathBdlChlVdoPatSyntax = _TmnxMcPathBdlChlVdoPatSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 7),
    _TmnxMcPathBdlChlVdoPatSyntax_Type()
)
tmnxMcPathBdlChlVdoPatSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPatSyntax.setStatus("current")


class _TmnxMcPathBdlChlVdoPcrRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPcrRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPcrRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPcrRepError_Object = MibTableColumn
tmnxMcPathBdlChlVdoPcrRepError = _TmnxMcPathBdlChlVdoPcrRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 8),
    _TmnxMcPathBdlChlVdoPcrRepError_Type()
)
tmnxMcPathBdlChlVdoPcrRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPcrRepError.setStatus("current")


class _TmnxMcPathBdlChlVdoTncPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoTncPcrRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathBdlChlVdoTncPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoTncPcrRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoTncPcrRep = _TmnxMcPathBdlChlVdoTncPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 9),
    _TmnxMcPathBdlChlVdoTncPcrRep_Type()
)
tmnxMcPathBdlChlVdoTncPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoQosPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoQosPcrRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathBdlChlVdoQosPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoQosPcrRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoQosPcrRep = _TmnxMcPathBdlChlVdoQosPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 10),
    _TmnxMcPathBdlChlVdoQosPcrRep_Type()
)
tmnxMcPathBdlChlVdoQosPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPoaPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoPoaPcrRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathBdlChlVdoPoaPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoPoaPcrRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoPoaPcrRep = _TmnxMcPathBdlChlVdoPoaPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 11),
    _TmnxMcPathBdlChlVdoPoaPcrRep_Type()
)
tmnxMcPathBdlChlVdoPoaPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPcrRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoVidPIDAbs_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoVidPIDAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathBdlChlVdoVidPIDAbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoVidPIDAbs_Object = MibTableColumn
tmnxMcPathBdlChlVdoVidPIDAbs = _TmnxMcPathBdlChlVdoVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 12),
    _TmnxMcPathBdlChlVdoVidPIDAbs_Type()
)
tmnxMcPathBdlChlVdoVidPIDAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoVidPIDAbs.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPIDPmtUnref_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPIDPmtUnref based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPIDPmtUnref_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPIDPmtUnref_Object = MibTableColumn
tmnxMcPathBdlChlVdoPIDPmtUnref = _TmnxMcPathBdlChlVdoPIDPmtUnref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 13),
    _TmnxMcPathBdlChlVdoPIDPmtUnref_Type()
)
tmnxMcPathBdlChlVdoPIDPmtUnref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPIDPmtUnref.setStatus("current")


class _TmnxMcPathBdlChlVdoPmtRepError_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPmtRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPmtRepError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPmtRepError_Object = MibTableColumn
tmnxMcPathBdlChlVdoPmtRepError = _TmnxMcPathBdlChlVdoPmtRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 14),
    _TmnxMcPathBdlChlVdoPmtRepError_Type()
)
tmnxMcPathBdlChlVdoPmtRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPmtRepError.setStatus("current")


class _TmnxMcPathBdlChlVdoTncPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoTncPmtRep based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4800),
    )


_TmnxMcPathBdlChlVdoTncPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoTncPmtRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoTncPmtRep = _TmnxMcPathBdlChlVdoTncPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 15),
    _TmnxMcPathBdlChlVdoTncPmtRep_Type()
)
tmnxMcPathBdlChlVdoTncPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTncPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoQosPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoQosPmtRep based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4900),
    )


_TmnxMcPathBdlChlVdoQosPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoQosPmtRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoQosPmtRep = _TmnxMcPathBdlChlVdoQosPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 16),
    _TmnxMcPathBdlChlVdoQosPmtRep_Type()
)
tmnxMcPathBdlChlVdoQosPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoQosPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPoaPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoPoaPmtRep based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 5000),
    )


_TmnxMcPathBdlChlVdoPoaPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoPoaPmtRep_Object = MibTableColumn
tmnxMcPathBdlChlVdoPoaPmtRep = _TmnxMcPathBdlChlVdoPoaPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 17),
    _TmnxMcPathBdlChlVdoPoaPmtRep_Type()
)
tmnxMcPathBdlChlVdoPoaPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPoaPmtRep.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoPmtSyntax_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoPmtSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoPmtSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoPmtSyntax_Object = MibTableColumn
tmnxMcPathBdlChlVdoPmtSyntax = _TmnxMcPathBdlChlVdoPmtSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 18),
    _TmnxMcPathBdlChlVdoPmtSyntax_Type()
)
tmnxMcPathBdlChlVdoPmtSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoPmtSyntax.setStatus("current")


class _TmnxMcPathBdlChlVdoScte35Error_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoScte35Error based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoScte35Error_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoScte35Error_Object = MibTableColumn
tmnxMcPathBdlChlVdoScte35Error = _TmnxMcPathBdlChlVdoScte35Error_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 19),
    _TmnxMcPathBdlChlVdoScte35Error_Type()
)
tmnxMcPathBdlChlVdoScte35Error.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoScte35Error.setStatus("obsolete")


class _TmnxMcPathBdlChlVdoTeiError_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoTeiError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoTeiError_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoTeiError_Object = MibTableColumn
tmnxMcPathBdlChlVdoTeiError = _TmnxMcPathBdlChlVdoTeiError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 20),
    _TmnxMcPathBdlChlVdoTeiError_Type()
)
tmnxMcPathBdlChlVdoTeiError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTeiError.setStatus("current")


class _TmnxMcPathBdlChlVdoTsSyncLoss_Type(TruthValue):
    """Custom type tmnxMcPathBdlChlVdoTsSyncLoss based on TruthValue"""
    defaultValue = 2


_TmnxMcPathBdlChlVdoTsSyncLoss_Type.__name__ = "TruthValue"
_TmnxMcPathBdlChlVdoTsSyncLoss_Object = MibTableColumn
tmnxMcPathBdlChlVdoTsSyncLoss = _TmnxMcPathBdlChlVdoTsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 21),
    _TmnxMcPathBdlChlVdoTsSyncLoss_Type()
)
tmnxMcPathBdlChlVdoTsSyncLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoTsSyncLoss.setStatus("current")


class _TmnxMcPathBdlChlVdoNonVidPIDAbs_Type(Unsigned32):
    """Custom type tmnxMcPathBdlChlVdoNonVidPIDAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathBdlChlVdoNonVidPIDAbs_Type.__name__ = "Unsigned32"
_TmnxMcPathBdlChlVdoNonVidPIDAbs_Object = MibTableColumn
tmnxMcPathBdlChlVdoNonVidPIDAbs = _TmnxMcPathBdlChlVdoNonVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 22),
    _TmnxMcPathBdlChlVdoNonVidPIDAbs_Type()
)
tmnxMcPathBdlChlVdoNonVidPIDAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoNonVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoNonVidPIDAbs.setUnits("milliseconds")


class _TmnxMcPathBdlChlVdoReportAlarm_Type(TmnxVdoAnalyzerAlarm):
    """Custom type tmnxMcPathBdlChlVdoReportAlarm based on TmnxVdoAnalyzerAlarm"""
    defaultValue = 0


_TmnxMcPathBdlChlVdoReportAlarm_Type.__name__ = "TmnxVdoAnalyzerAlarm"
_TmnxMcPathBdlChlVdoReportAlarm_Object = MibTableColumn
tmnxMcPathBdlChlVdoReportAlarm = _TmnxMcPathBdlChlVdoReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 17, 1, 23),
    _TmnxMcPathBdlChlVdoReportAlarm_Type()
)
tmnxMcPathBdlChlVdoReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlVdoReportAlarm.setStatus("current")
_TmnxMcPathChlSrcExtTable_Object = MibTable
tmnxMcPathChlSrcExtTable = _TmnxMcPathChlSrcExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18)
)
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcExtTable.setStatus("current")
_TmnxMcPathChlSrcExtEntry_Object = MibTableRow
tmnxMcPathChlSrcExtEntry = _TmnxMcPathChlSrcExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1)
)
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcExtEntry.setStatus("current")
_TmnxMcPathChlSrcVdoLastChanged_Type = TimeStamp
_TmnxMcPathChlSrcVdoLastChanged_Object = MibTableColumn
tmnxMcPathChlSrcVdoLastChanged = _TmnxMcPathChlSrcVdoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 1),
    _TmnxMcPathChlSrcVdoLastChanged_Type()
)
tmnxMcPathChlSrcVdoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoLastChanged.setStatus("current")


class _TmnxMcPathChlSrcVdoCcError_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoCcError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoCcError_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoCcError_Object = MibTableColumn
tmnxMcPathChlSrcVdoCcError = _TmnxMcPathChlSrcVdoCcError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 2),
    _TmnxMcPathChlSrcVdoCcError_Type()
)
tmnxMcPathChlSrcVdoCcError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoCcError.setStatus("current")


class _TmnxMcPathChlSrcVdoPatRepError_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPatRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPatRepError_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPatRepError_Object = MibTableColumn
tmnxMcPathChlSrcVdoPatRepError = _TmnxMcPathChlSrcVdoPatRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 3),
    _TmnxMcPathChlSrcVdoPatRepError_Type()
)
tmnxMcPathChlSrcVdoPatRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPatRepError.setStatus("current")


class _TmnxMcPathChlSrcVdoTncPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoTncPatRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathChlSrcVdoTncPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoTncPatRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoTncPatRep = _TmnxMcPathChlSrcVdoTncPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 4),
    _TmnxMcPathChlSrcVdoTncPatRep_Type()
)
tmnxMcPathChlSrcVdoTncPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPatRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoQosPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoQosPatRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathChlSrcVdoQosPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoQosPatRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoQosPatRep = _TmnxMcPathChlSrcVdoQosPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 5),
    _TmnxMcPathChlSrcVdoQosPatRep_Type()
)
tmnxMcPathChlSrcVdoQosPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPatRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPoaPatRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoPoaPatRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathChlSrcVdoPoaPatRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoPoaPatRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoPoaPatRep = _TmnxMcPathChlSrcVdoPoaPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 6),
    _TmnxMcPathChlSrcVdoPoaPatRep_Type()
)
tmnxMcPathChlSrcVdoPoaPatRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPatRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPatSyntax_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPatSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPatSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPatSyntax_Object = MibTableColumn
tmnxMcPathChlSrcVdoPatSyntax = _TmnxMcPathChlSrcVdoPatSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 7),
    _TmnxMcPathChlSrcVdoPatSyntax_Type()
)
tmnxMcPathChlSrcVdoPatSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPatSyntax.setStatus("current")


class _TmnxMcPathChlSrcVdoPcrRepError_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPcrRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPcrRepError_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPcrRepError_Object = MibTableColumn
tmnxMcPathChlSrcVdoPcrRepError = _TmnxMcPathChlSrcVdoPcrRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 8),
    _TmnxMcPathChlSrcVdoPcrRepError_Type()
)
tmnxMcPathChlSrcVdoPcrRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPcrRepError.setStatus("current")


class _TmnxMcPathChlSrcVdoTncPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoTncPcrRep based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_TmnxMcPathChlSrcVdoTncPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoTncPcrRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoTncPcrRep = _TmnxMcPathChlSrcVdoTncPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 9),
    _TmnxMcPathChlSrcVdoTncPcrRep_Type()
)
tmnxMcPathChlSrcVdoTncPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPcrRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoQosPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoQosPcrRep based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 900),
    )


_TmnxMcPathChlSrcVdoQosPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoQosPcrRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoQosPcrRep = _TmnxMcPathChlSrcVdoQosPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 10),
    _TmnxMcPathChlSrcVdoQosPcrRep_Type()
)
tmnxMcPathChlSrcVdoQosPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPcrRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPoaPcrRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoPoaPcrRep based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1000),
    )


_TmnxMcPathChlSrcVdoPoaPcrRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoPoaPcrRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoPoaPcrRep = _TmnxMcPathChlSrcVdoPoaPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 11),
    _TmnxMcPathChlSrcVdoPoaPcrRep_Type()
)
tmnxMcPathChlSrcVdoPoaPcrRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPcrRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoVidPIDAbs_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoVidPIDAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathChlSrcVdoVidPIDAbs_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoVidPIDAbs_Object = MibTableColumn
tmnxMcPathChlSrcVdoVidPIDAbs = _TmnxMcPathChlSrcVdoVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 12),
    _TmnxMcPathChlSrcVdoVidPIDAbs_Type()
)
tmnxMcPathChlSrcVdoVidPIDAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoVidPIDAbs.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPIDPmtUnref_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPIDPmtUnref based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPIDPmtUnref_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPIDPmtUnref_Object = MibTableColumn
tmnxMcPathChlSrcVdoPIDPmtUnref = _TmnxMcPathChlSrcVdoPIDPmtUnref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 13),
    _TmnxMcPathChlSrcVdoPIDPmtUnref_Type()
)
tmnxMcPathChlSrcVdoPIDPmtUnref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPIDPmtUnref.setStatus("current")


class _TmnxMcPathChlSrcVdoPmtRepError_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPmtRepError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPmtRepError_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPmtRepError_Object = MibTableColumn
tmnxMcPathChlSrcVdoPmtRepError = _TmnxMcPathChlSrcVdoPmtRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 14),
    _TmnxMcPathChlSrcVdoPmtRepError_Type()
)
tmnxMcPathChlSrcVdoPmtRepError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPmtRepError.setStatus("current")


class _TmnxMcPathChlSrcVdoTncPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoTncPmtRep based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4800),
    )


_TmnxMcPathChlSrcVdoTncPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoTncPmtRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoTncPmtRep = _TmnxMcPathChlSrcVdoTncPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 15),
    _TmnxMcPathChlSrcVdoTncPmtRep_Type()
)
tmnxMcPathChlSrcVdoTncPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTncPmtRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoQosPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoQosPmtRep based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4900),
    )


_TmnxMcPathChlSrcVdoQosPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoQosPmtRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoQosPmtRep = _TmnxMcPathChlSrcVdoQosPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 16),
    _TmnxMcPathChlSrcVdoQosPmtRep_Type()
)
tmnxMcPathChlSrcVdoQosPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoQosPmtRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPoaPmtRep_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoPoaPmtRep based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 5000),
    )


_TmnxMcPathChlSrcVdoPoaPmtRep_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoPoaPmtRep_Object = MibTableColumn
tmnxMcPathChlSrcVdoPoaPmtRep = _TmnxMcPathChlSrcVdoPoaPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 17),
    _TmnxMcPathChlSrcVdoPoaPmtRep_Type()
)
tmnxMcPathChlSrcVdoPoaPmtRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPoaPmtRep.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoPmtSyntax_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoPmtSyntax based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoPmtSyntax_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoPmtSyntax_Object = MibTableColumn
tmnxMcPathChlSrcVdoPmtSyntax = _TmnxMcPathChlSrcVdoPmtSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 18),
    _TmnxMcPathChlSrcVdoPmtSyntax_Type()
)
tmnxMcPathChlSrcVdoPmtSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoPmtSyntax.setStatus("current")


class _TmnxMcPathChlSrcVdoScte35Error_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoScte35Error based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoScte35Error_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoScte35Error_Object = MibTableColumn
tmnxMcPathChlSrcVdoScte35Error = _TmnxMcPathChlSrcVdoScte35Error_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 19),
    _TmnxMcPathChlSrcVdoScte35Error_Type()
)
tmnxMcPathChlSrcVdoScte35Error.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoScte35Error.setStatus("obsolete")


class _TmnxMcPathChlSrcVdoTeiError_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoTeiError based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoTeiError_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoTeiError_Object = MibTableColumn
tmnxMcPathChlSrcVdoTeiError = _TmnxMcPathChlSrcVdoTeiError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 20),
    _TmnxMcPathChlSrcVdoTeiError_Type()
)
tmnxMcPathChlSrcVdoTeiError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTeiError.setStatus("current")


class _TmnxMcPathChlSrcVdoTsSyncLoss_Type(TruthValue):
    """Custom type tmnxMcPathChlSrcVdoTsSyncLoss based on TruthValue"""
    defaultValue = 2


_TmnxMcPathChlSrcVdoTsSyncLoss_Type.__name__ = "TruthValue"
_TmnxMcPathChlSrcVdoTsSyncLoss_Object = MibTableColumn
tmnxMcPathChlSrcVdoTsSyncLoss = _TmnxMcPathChlSrcVdoTsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 21),
    _TmnxMcPathChlSrcVdoTsSyncLoss_Type()
)
tmnxMcPathChlSrcVdoTsSyncLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoTsSyncLoss.setStatus("current")


class _TmnxMcPathChlSrcVdoNonVidPIDAbs_Type(Unsigned32):
    """Custom type tmnxMcPathChlSrcVdoNonVidPIDAbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxMcPathChlSrcVdoNonVidPIDAbs_Type.__name__ = "Unsigned32"
_TmnxMcPathChlSrcVdoNonVidPIDAbs_Object = MibTableColumn
tmnxMcPathChlSrcVdoNonVidPIDAbs = _TmnxMcPathChlSrcVdoNonVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 22),
    _TmnxMcPathChlSrcVdoNonVidPIDAbs_Type()
)
tmnxMcPathChlSrcVdoNonVidPIDAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoNonVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoNonVidPIDAbs.setUnits("milliseconds")


class _TmnxMcPathChlSrcVdoReportAlarm_Type(TmnxVdoAnalyzerAlarm):
    """Custom type tmnxMcPathChlSrcVdoReportAlarm based on TmnxVdoAnalyzerAlarm"""
    defaultValue = 0


_TmnxMcPathChlSrcVdoReportAlarm_Type.__name__ = "TmnxVdoAnalyzerAlarm"
_TmnxMcPathChlSrcVdoReportAlarm_Object = MibTableColumn
tmnxMcPathChlSrcVdoReportAlarm = _TmnxMcPathChlSrcVdoReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 18, 1, 23),
    _TmnxMcPathChlSrcVdoReportAlarm_Type()
)
tmnxMcPathChlSrcVdoReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcVdoReportAlarm.setStatus("current")
_TmnxMcPathRprtDestTable_Object = MibTable
tmnxMcPathRprtDestTable = _TmnxMcPathRprtDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19)
)
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestTable.setStatus("current")
_TmnxMcPathRprtDestEntry_Object = MibTableRow
tmnxMcPathRprtDestEntry = _TmnxMcPathRprtDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1)
)
tmnxMcPathRprtDestEntry.setIndexNames(
    (0, "TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestName"),
)
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestEntry.setStatus("current")
_TmnxMcPathRprtDestName_Type = TNamedItem
_TmnxMcPathRprtDestName_Object = MibTableColumn
tmnxMcPathRprtDestName = _TmnxMcPathRprtDestName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 1),
    _TmnxMcPathRprtDestName_Type()
)
tmnxMcPathRprtDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestName.setStatus("current")
_TmnxMcPathRprtDestRowStatus_Type = RowStatus
_TmnxMcPathRprtDestRowStatus_Object = MibTableColumn
tmnxMcPathRprtDestRowStatus = _TmnxMcPathRprtDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 2),
    _TmnxMcPathRprtDestRowStatus_Type()
)
tmnxMcPathRprtDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestRowStatus.setStatus("current")
_TmnxMcPathRprtDestLastChanged_Type = TimeStamp
_TmnxMcPathRprtDestLastChanged_Object = MibTableColumn
tmnxMcPathRprtDestLastChanged = _TmnxMcPathRprtDestLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 3),
    _TmnxMcPathRprtDestLastChanged_Type()
)
tmnxMcPathRprtDestLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestLastChanged.setStatus("current")


class _TmnxMcPathRprtDestDescription_Type(TItemDescription):
    """Custom type tmnxMcPathRprtDestDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcPathRprtDestDescription_Type.__name__ = "TItemDescription"
_TmnxMcPathRprtDestDescription_Object = MibTableColumn
tmnxMcPathRprtDestDescription = _TmnxMcPathRprtDestDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 4),
    _TmnxMcPathRprtDestDescription_Type()
)
tmnxMcPathRprtDestDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestDescription.setStatus("current")


class _TmnxMcPathRprtDestAddrType_Type(InetAddressType):
    """Custom type tmnxMcPathRprtDestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPathRprtDestAddrType_Type.__name__ = "InetAddressType"
_TmnxMcPathRprtDestAddrType_Object = MibTableColumn
tmnxMcPathRprtDestAddrType = _TmnxMcPathRprtDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 5),
    _TmnxMcPathRprtDestAddrType_Type()
)
tmnxMcPathRprtDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestAddrType.setStatus("current")


class _TmnxMcPathRprtDestAddress_Type(InetAddress):
    """Custom type tmnxMcPathRprtDestAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcPathRprtDestAddress_Type.__name__ = "InetAddress"
_TmnxMcPathRprtDestAddress_Object = MibTableColumn
tmnxMcPathRprtDestAddress = _TmnxMcPathRprtDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 6),
    _TmnxMcPathRprtDestAddress_Type()
)
tmnxMcPathRprtDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestAddress.setStatus("current")


class _TmnxMcPathRprtDestUdpDstPort_Type(InetPortNumber):
    """Custom type tmnxMcPathRprtDestUdpDstPort based on InetPortNumber"""
    defaultValue = 1037


_TmnxMcPathRprtDestUdpDstPort_Type.__name__ = "InetPortNumber"
_TmnxMcPathRprtDestUdpDstPort_Object = MibTableColumn
tmnxMcPathRprtDestUdpDstPort = _TmnxMcPathRprtDestUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 7),
    _TmnxMcPathRprtDestUdpDstPort_Type()
)
tmnxMcPathRprtDestUdpDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestUdpDstPort.setStatus("current")


class _TmnxMcPathRprtDestMaxTxDelay_Type(Unsigned32):
    """Custom type tmnxMcPathRprtDestMaxTxDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMcPathRprtDestMaxTxDelay_Type.__name__ = "Unsigned32"
_TmnxMcPathRprtDestMaxTxDelay_Object = MibTableColumn
tmnxMcPathRprtDestMaxTxDelay = _TmnxMcPathRprtDestMaxTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 8),
    _TmnxMcPathRprtDestMaxTxDelay_Type()
)
tmnxMcPathRprtDestMaxTxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestMaxTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestMaxTxDelay.setUnits("deci-seconds")


class _TmnxMcPathRprtDestAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPathRprtDestAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPathRprtDestAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPathRprtDestAdminState_Object = MibTableColumn
tmnxMcPathRprtDestAdminState = _TmnxMcPathRprtDestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 9),
    _TmnxMcPathRprtDestAdminState_Type()
)
tmnxMcPathRprtDestAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestAdminState.setStatus("current")


class _TmnxMcPathRprtDestFrmsSent_Type(Unsigned32):
    """Custom type tmnxMcPathRprtDestFrmsSent based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathRprtDestFrmsSent_Type.__name__ = "Unsigned32"
_TmnxMcPathRprtDestFrmsSent_Object = MibTableColumn
tmnxMcPathRprtDestFrmsSent = _TmnxMcPathRprtDestFrmsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 10),
    _TmnxMcPathRprtDestFrmsSent_Type()
)
tmnxMcPathRprtDestFrmsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestFrmsSent.setStatus("current")


class _TmnxMcPathRprtDestFrmsLost_Type(Unsigned32):
    """Custom type tmnxMcPathRprtDestFrmsLost based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathRprtDestFrmsLost_Type.__name__ = "Unsigned32"
_TmnxMcPathRprtDestFrmsLost_Object = MibTableColumn
tmnxMcPathRprtDestFrmsLost = _TmnxMcPathRprtDestFrmsLost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 11),
    _TmnxMcPathRprtDestFrmsLost_Type()
)
tmnxMcPathRprtDestFrmsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestFrmsLost.setStatus("current")


class _TmnxMcPathRprtDestRecsSent_Type(Unsigned32):
    """Custom type tmnxMcPathRprtDestRecsSent based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathRprtDestRecsSent_Type.__name__ = "Unsigned32"
_TmnxMcPathRprtDestRecsSent_Object = MibTableColumn
tmnxMcPathRprtDestRecsSent = _TmnxMcPathRprtDestRecsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 12),
    _TmnxMcPathRprtDestRecsSent_Type()
)
tmnxMcPathRprtDestRecsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestRecsSent.setStatus("current")


class _TmnxMcPathRprtDestRecsLost_Type(Unsigned32):
    """Custom type tmnxMcPathRprtDestRecsLost based on Unsigned32"""
    defaultValue = 0


_TmnxMcPathRprtDestRecsLost_Type.__name__ = "Unsigned32"
_TmnxMcPathRprtDestRecsLost_Object = MibTableColumn
tmnxMcPathRprtDestRecsLost = _TmnxMcPathRprtDestRecsLost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 54, 19, 1, 13),
    _TmnxMcPathRprtDestRecsLost_Type()
)
tmnxMcPathRprtDestRecsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestRecsLost.setStatus("current")
_TmnxMcPathNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMcPathNotifyPrefix = _TmnxMcPathNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54)
)
_TmnxMcPathNotifications_ObjectIdentity = ObjectIdentity
tmnxMcPathNotifications = _TmnxMcPathNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54, 0)
)
tmnxMcPathBdlEntry.registerAugmentions(
    ("TIMETRA-MCAST-PATH-MGMT-MIB",
     "tmnxMcPathBdlExtEntry")
)
tmnxMcPathBdlExtEntry.setIndexNames(*tmnxMcPathBdlEntry.getIndexNames())
tmnxMcPathBdlChlEntry.registerAugmentions(
    ("TIMETRA-MCAST-PATH-MGMT-MIB",
     "tmnxMcPathBdlChlExtEntry")
)
tmnxMcPathBdlChlExtEntry.setIndexNames(*tmnxMcPathBdlChlEntry.getIndexNames())
tmnxMcPathChlSrcEntry.registerAugmentions(
    ("TIMETRA-MCAST-PATH-MGMT-MIB",
     "tmnxMcPathChlSrcExtEntry")
)
tmnxMcPathChlSrcExtEntry.setIndexNames(*tmnxMcPathChlSrcEntry.getIndexNames())

# Managed Objects groups

tmnxMcPathGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 1)
)
tmnxMcPathGlobalGroup.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyTableLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyTableLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlTableLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlTblLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcTableLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalGroup.setStatus("current")

tmnxMcPathPlcyV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 2)
)
tmnxMcPathPlcyV6v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyDescription"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyFallPercentReset"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyAdminBwThd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyMcPoolPercentTot"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyMcPoolResvCbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyMcPoolSlopePlcy"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyPathLimit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyPathCbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyPathMbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyPathHighPrio"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyDescription"))
)
if mibBuilder.loadTexts:
    tmnxMcPathPlcyV6v0Group.setStatus("current")

tmnxMcPathBdlV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 3)
)
tmnxMcPathBdlV6v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDescription"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlCongPriorityThd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlEcmpOptThd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlAdminBw"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlPref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlBwActivity"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlBwFallDelay"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlBwBlackHoleRt"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlDefChlExSfPath"))
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlV6v0Group.setStatus("current")

tmnxMcPathBdlChlV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 4)
)
tmnxMcPathBdlChlV6v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlAdminBw"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlPref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlBwActivity"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlBwFallDelay"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlBwBlackHoleRt"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlExSfPath"))
)
if mibBuilder.loadTexts:
    tmnxMcPathBdlChlV6v0Group.setStatus("current")

tmnxMcPathChlSrcV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 5)
)
tmnxMcPathChlSrcV6v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAdminBw"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcPref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcBwActivity"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcBwFallDelay"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcBwBlackHoleRt"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcExSfPath"))
)
if mibBuilder.loadTexts:
    tmnxMcPathChlSrcV6v0Group.setStatus("current")

tmnxMcPathOperChlV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 6)
)
tmnxMcPathOperChlV6v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlBandwidth"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlCurrentPath"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlExplicit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlAdminBw"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlPref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlBwBlackHole"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlBwBlackHoleRt"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlIngLastHighest"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlIngSecHighest"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlTimeRemaining"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlBandwidth"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlCurrentPath"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlExplicit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlAdminBw"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlPref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlBwBlackHole"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlBwBlackHoleRt"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlIngLastHigh"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlIngSecHigh"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlTimeRemain"))
)
if mibBuilder.loadTexts:
    tmnxMcPathOperChlV6v0Group.setStatus("current")

tmnxMcPathNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 8)
)
tmnxMcPathNotifyObjsGroup.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlPathType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisIndex"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathCardSlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMDASlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlRtrType"))
)
if mibBuilder.loadTexts:
    tmnxMcPathNotifyObjsGroup.setStatus("current")

tmnxMcPathGlobalV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 9)
)
tmnxMcPathGlobalV6v1Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlaneLimit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisSecPlaneLimit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisDualPlaneLimit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisDualSecPlaneLmt"))
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalV6v1Group.setStatus("current")

tmnxMcPathPlcyV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 10)
)
tmnxMcPathPlcyV6v1Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathCbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathMbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathHighPrio"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathPaths"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathDualPaths"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBwPlcyT2PathLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcPathPlcyV6v1Group.setStatus("current")

tmnxMcPathVdoV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 11)
)
tmnxMcPathVdoV7v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoFCCState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoChlType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoRTAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoRTAddress"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoRTBufferSize"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoLocalRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoLocalFccPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoGroupId"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoFCCState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoChlType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoRTAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoRTAddress"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoRTBufferSize"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoGroupId"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoFCCState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoChlType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoRTAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoRTAddress"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoRTBufferSize"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoGroupId"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyLclRTSvrState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyRTRate"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcySubBwLimit"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyFCCSvrMode"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyFCCBurst"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyFCCMcHandover"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyFCCDentThd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyTblLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoLocalRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoLocalRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoLocalRTState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoReorderAudio"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoReorderAudio"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoReorderAudio"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoFccMinDuration"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoFccMinDuratn"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoFccMinDuratn"))
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoV7v0Group.setStatus("current")

tmnxMcPathTunnelIfV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 12)
)
tmnxMcPathTunnelIfV7v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlTunnelIfLspName"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlTunIfSdAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlTunIfSdAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlTunnelIfLspName"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlTunIfSdAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlTunIfSdAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcTunnelIfLspName"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcTunIfSdAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcTunIfSdAddr"))
)
if mibBuilder.loadTexts:
    tmnxMcPathTunnelIfV7v0Group.setStatus("current")

tmnxMcPathGlobalV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 13)
)
tmnxMcPathGlobalV7v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisMmrpAdminMode"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisMmrpOperMode"))
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalV7v0Group.setStatus("current")

tmnxMcPathObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 14)
)
tmnxMcPathObsoleteV7v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoLocalRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoLocalFccPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoLocalRTPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoLocalFccPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoSourcePort"))
)
if mibBuilder.loadTexts:
    tmnxMcPathObsoleteV7v0Group.setStatus("current")

tmnxMcPathGlobalV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 15)
)
tmnxMcPathGlobalV8v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlKAOverrideTimer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcKAOverrideTimer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlKAOverrideTimer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlP2MPId"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlP2MPId"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcP2MPId"))
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalV8v0Group.setStatus("current")

tmnxMcPathVdoV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 16)
)
tmnxMcPathVdoV8v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyRTPayloadType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyMaxClntSessions"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyMaxIgmpLatency"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc1Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc2Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoVidPIDAbsent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoScte35Error"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoNonVidPIDAbsent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoReportAlarm"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc1Typ"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc2Typ"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoScte35Error"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoNonVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoReportAlarm"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc1Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc2Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoScte35Error"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoNonVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoReportAlarm"))
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoV8v0Group.setStatus("obsolete")

tmnxMcPathGlobalExtV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 17)
)
tmnxMcPathGlobalExtV6v1Group.setObjects(
    ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisRRInactiveRec")
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalExtV6v1Group.setStatus("current")

tmnxMcPathGlobalV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 18)
)
tmnxMcPathGlobalV9v0Group.setObjects(
    ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestTblLastChanged")
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalV9v0Group.setStatus("current")

tmnxMcPathRprtDestV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 19)
)
tmnxMcPathRprtDestV9v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestRowStatus"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestDescription"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestAddress"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestUdpDstPort"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestMaxTxDelay"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestAdminState"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestFrmsSent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestFrmsLost"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestRecsSent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestRecsLost"))
)
if mibBuilder.loadTexts:
    tmnxMcPathRprtDestV9v0Group.setStatus("current")

tmnxMcPathVdoV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 20)
)
tmnxMcPathVdoV9v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyRTPayloadType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyMaxClntSessions"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoPlcyMaxIgmpLatency"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc1Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc2Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoStrSelIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoVidPIDAbsent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoNonVidPIDAbsent"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoReportAlarm"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc1Typ"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc2Typ"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoStrSelIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoNonVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoReportAlarm"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoAnalyzer"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoAnalyzerDesc"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc1Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeIntf1"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc2Type"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeSrc2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoStSeIntf2"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcExtTableLastChgd"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoLastChanged"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoCcError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPatRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPatRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPatSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPcrRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPcrRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPIDPmtUnref"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPmtRepError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTncPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoQosPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPoaPmtRep"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoPmtSyntax"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTeiError"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoTsSyncLoss"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoNonVidPIDAbs"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoReportAlarm"))
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoV9v0Group.setStatus("current")

tmnxMcPathVdoObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 21)
)
tmnxMcPathVdoObsoletedV9v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlVdoScte35Error"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlVdoScte35Error"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcVdoScte35Error"))
)
if mibBuilder.loadTexts:
    tmnxMcPathVdoObsoletedV9v0Group.setStatus("current")

tmnxMcPathSwPlaneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 22)
)
tmnxMcPathSwPlaneGroup.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlCurrentPlane"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMdaOperChlCurrentPlane"))
)
if mibBuilder.loadTexts:
    tmnxMcPathSwPlaneGroup.setStatus("current")

tmnxMcPathGlobalV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 23)
)
tmnxMcPathGlobalV10v0Group.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimTotal"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimDynTotal"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimPriCap"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimSecCap"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimPriCapRed"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisPlnLimSecCapRed"))
)
if mibBuilder.loadTexts:
    tmnxMcPathGlobalV10v0Group.setStatus("current")


# Notification objects

tmnxMcPathSrcGrpBlkHole = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54, 0, 1)
)
tmnxMcPathSrcGrpBlkHole.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlRtrType"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisIndex"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathCardSlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMDASlotNum"))
)
if mibBuilder.loadTexts:
    tmnxMcPathSrcGrpBlkHole.setStatus(
        "current"
    )

tmnxMcPathSrcGrpBlkHoleClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54, 0, 2)
)
tmnxMcPathSrcGrpBlkHoleClear.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlGrpAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddrType"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcAddr"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlRtrType"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisIndex"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathCardSlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMDASlotNum"))
)
if mibBuilder.loadTexts:
    tmnxMcPathSrcGrpBlkHoleClear.setStatus(
        "current"
    )

tmnxMcPathAvailBwLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54, 0, 3)
)
tmnxMcPathAvailBwLimitReached.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisIndex"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathCardSlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMDASlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlPathType"))
)
if mibBuilder.loadTexts:
    tmnxMcPathAvailBwLimitReached.setStatus(
        "current"
    )

tmnxMcPathAvailBwValWithinRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 54, 0, 4)
)
tmnxMcPathAvailBwValWithinRange.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChassisIndex"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathCardSlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathMDASlotNum"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlPathType"))
)
if mibBuilder.loadTexts:
    tmnxMcPathAvailBwValWithinRange.setStatus(
        "current"
    )


# Notifications groups

tmnxMcPathNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 2, 7)
)
tmnxMcPathNotificationGroup.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathSrcGrpBlkHole"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathSrcGrpBlkHoleClear"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathAvailBwLimitReached"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathAvailBwValWithinRange"))
)
if mibBuilder.loadTexts:
    tmnxMcPathNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMcPathV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 1)
)
tmnxMcPathV6v0Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcPathV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcPath7x50V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 2)
)
tmnxMcPath7x50V6v1Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalExtV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxMcPath7x50V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMcPath7710V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 3)
)
tmnxMcPath7710V6v1Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcPath7710V6v1Compliance.setStatus(
        "current"
    )

tmnxMcPath7x50V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 4)
)
tmnxMcPath7x50V7v0Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathTunnelIfV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalExtV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxMcPath7x50V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcPathV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 5)
)
tmnxMcPathV8v0Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathTunnelIfV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalExtV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV8v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcPathV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcPathV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 6)
)
tmnxMcPathV9v0Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathSwPlaneGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathTunnelIfV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalExtV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV8v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV9v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV9v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcPathV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcPathV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 54, 1, 7)
)
tmnxMcPathV10v0Compliance.setObjects(
      *(("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathBdlChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathChlSrcV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathOperChlV6v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathSwPlaneGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathNotificationGroup"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathPlcyV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathTunnelIfV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV7v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalExtV6v1Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV8v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathVdoV9v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV9v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathRprtDestV9v0Group"),
        ("TIMETRA-MCAST-PATH-MGMT-MIB", "tmnxMcPathGlobalV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcPathV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MCAST-PATH-MGMT-MIB",
    **{"TmnxMcPathChlSfPathTypeTc": TmnxMcPathChlSfPathTypeTc,
       "TmnxMcPathBwActivityTc": TmnxMcPathBwActivityTc,
       "TmnxMcPathRtrType": TmnxMcPathRtrType,
       "TmnxMcPathVdoChlType": TmnxMcPathVdoChlType,
       "TmnxMcPathVdoChlTypeOrInherit": TmnxMcPathVdoChlTypeOrInherit,
       "TmnxMcPathVdoPayloadType": TmnxMcPathVdoPayloadType,
       "TmnxMcPathVdoBufferSize": TmnxMcPathVdoBufferSize,
       "TmnxMcPathVdoBwLimit": TmnxMcPathVdoBwLimit,
       "TmnxMcPathVdoReorderAudio": TmnxMcPathVdoReorderAudio,
       "TmnxMcPathVdoFccMinDuration": TmnxMcPathVdoFccMinDuration,
       "TmnxMcPathVdoFccMinDurationOrZero": TmnxMcPathVdoFccMinDurationOrZero,
       "TmnxMcPathKeepAliveOverrideTimer": TmnxMcPathKeepAliveOverrideTimer,
       "timetraMcastPathMgmtMIBModule": timetraMcastPathMgmtMIBModule,
       "tmnxMcPathConformance": tmnxMcPathConformance,
       "tmnxMcPathCompliances": tmnxMcPathCompliances,
       "tmnxMcPathV6v0Compliance": tmnxMcPathV6v0Compliance,
       "tmnxMcPath7x50V6v1Compliance": tmnxMcPath7x50V6v1Compliance,
       "tmnxMcPath7710V6v1Compliance": tmnxMcPath7710V6v1Compliance,
       "tmnxMcPath7x50V7v0Compliance": tmnxMcPath7x50V7v0Compliance,
       "tmnxMcPathV8v0Compliance": tmnxMcPathV8v0Compliance,
       "tmnxMcPathV9v0Compliance": tmnxMcPathV9v0Compliance,
       "tmnxMcPathV10v0Compliance": tmnxMcPathV10v0Compliance,
       "tmnxMcPathGroups": tmnxMcPathGroups,
       "tmnxMcPathGlobalGroup": tmnxMcPathGlobalGroup,
       "tmnxMcPathPlcyV6v0Group": tmnxMcPathPlcyV6v0Group,
       "tmnxMcPathBdlV6v0Group": tmnxMcPathBdlV6v0Group,
       "tmnxMcPathBdlChlV6v0Group": tmnxMcPathBdlChlV6v0Group,
       "tmnxMcPathChlSrcV6v0Group": tmnxMcPathChlSrcV6v0Group,
       "tmnxMcPathOperChlV6v0Group": tmnxMcPathOperChlV6v0Group,
       "tmnxMcPathNotificationGroup": tmnxMcPathNotificationGroup,
       "tmnxMcPathNotifyObjsGroup": tmnxMcPathNotifyObjsGroup,
       "tmnxMcPathGlobalV6v1Group": tmnxMcPathGlobalV6v1Group,
       "tmnxMcPathPlcyV6v1Group": tmnxMcPathPlcyV6v1Group,
       "tmnxMcPathVdoV7v0Group": tmnxMcPathVdoV7v0Group,
       "tmnxMcPathTunnelIfV7v0Group": tmnxMcPathTunnelIfV7v0Group,
       "tmnxMcPathGlobalV7v0Group": tmnxMcPathGlobalV7v0Group,
       "tmnxMcPathObsoleteV7v0Group": tmnxMcPathObsoleteV7v0Group,
       "tmnxMcPathGlobalV8v0Group": tmnxMcPathGlobalV8v0Group,
       "tmnxMcPathVdoV8v0Group": tmnxMcPathVdoV8v0Group,
       "tmnxMcPathGlobalExtV6v1Group": tmnxMcPathGlobalExtV6v1Group,
       "tmnxMcPathGlobalV9v0Group": tmnxMcPathGlobalV9v0Group,
       "tmnxMcPathRprtDestV9v0Group": tmnxMcPathRprtDestV9v0Group,
       "tmnxMcPathVdoV9v0Group": tmnxMcPathVdoV9v0Group,
       "tmnxMcPathVdoObsoletedV9v0Group": tmnxMcPathVdoObsoletedV9v0Group,
       "tmnxMcPathSwPlaneGroup": tmnxMcPathSwPlaneGroup,
       "tmnxMcPathGlobalV10v0Group": tmnxMcPathGlobalV10v0Group,
       "tmnxMcPathObjs": tmnxMcPathObjs,
       "tmnxMcPathGlobalObjs": tmnxMcPathGlobalObjs,
       "tmnxMcPathBwPlcyTableLastChanged": tmnxMcPathBwPlcyTableLastChanged,
       "tmnxMcPathPlcyTableLastChanged": tmnxMcPathPlcyTableLastChanged,
       "tmnxMcPathBdlTableLastChanged": tmnxMcPathBdlTableLastChanged,
       "tmnxMcPathBdlChlTblLastChanged": tmnxMcPathBdlChlTblLastChanged,
       "tmnxMcPathChlSrcTableLastChanged": tmnxMcPathChlSrcTableLastChanged,
       "tmnxMcPathChassisLevelInfo": tmnxMcPathChassisLevelInfo,
       "tmnxMcPathChassisPlaneLimit": tmnxMcPathChassisPlaneLimit,
       "tmnxMcPathChassisSecPlaneLimit": tmnxMcPathChassisSecPlaneLimit,
       "tmnxMcPathChassisDualPlaneLimit": tmnxMcPathChassisDualPlaneLimit,
       "tmnxMcPathChassisDualSecPlaneLmt": tmnxMcPathChassisDualSecPlaneLmt,
       "tmnxMcPathChassisMmrpAdminMode": tmnxMcPathChassisMmrpAdminMode,
       "tmnxMcPathChassisMmrpOperMode": tmnxMcPathChassisMmrpOperMode,
       "tmnxMcPathChassisRRInactiveRec": tmnxMcPathChassisRRInactiveRec,
       "tmnxMcPathChassisPlnLimTotal": tmnxMcPathChassisPlnLimTotal,
       "tmnxMcPathChassisPlnLimDynTotal": tmnxMcPathChassisPlnLimDynTotal,
       "tmnxMcPathChassisPlnLimPriCap": tmnxMcPathChassisPlnLimPriCap,
       "tmnxMcPathChassisPlnLimSecCap": tmnxMcPathChassisPlnLimSecCap,
       "tmnxMcPathChassisPlnLimPriCapRed": tmnxMcPathChassisPlnLimPriCapRed,
       "tmnxMcPathChassisPlnLimSecCapRed": tmnxMcPathChassisPlnLimSecCapRed,
       "tmnxMcPathVdoPlcyTblLastChanged": tmnxMcPathVdoPlcyTblLastChanged,
       "tmnxMcPathBdlExtTableLastChgd": tmnxMcPathBdlExtTableLastChgd,
       "tmnxMcPathBdlChlExtTableLastChgd": tmnxMcPathBdlChlExtTableLastChgd,
       "tmnxMcPathChlSrcExtTableLastChgd": tmnxMcPathChlSrcExtTableLastChgd,
       "tmnxMcPathRprtDestTblLastChanged": tmnxMcPathRprtDestTblLastChanged,
       "tmnxMcPathNotifyObjs": tmnxMcPathNotifyObjs,
       "tmnxMcPathChlGrpAddrType": tmnxMcPathChlGrpAddrType,
       "tmnxMcPathChlGrpAddr": tmnxMcPathChlGrpAddr,
       "tmnxMcPathChlSrcAddrType": tmnxMcPathChlSrcAddrType,
       "tmnxMcPathChlSrcAddr": tmnxMcPathChlSrcAddr,
       "tmnxMcPathChlPathType": tmnxMcPathChlPathType,
       "tmnxMcPathChassisIndex": tmnxMcPathChassisIndex,
       "tmnxMcPathCardSlotNum": tmnxMcPathCardSlotNum,
       "tmnxMcPathMDASlotNum": tmnxMcPathMDASlotNum,
       "tmnxMcPathChlRtrType": tmnxMcPathChlRtrType,
       "tmnxMcPathBwPlcyTable": tmnxMcPathBwPlcyTable,
       "tmnxMcPathBwPlcyEntry": tmnxMcPathBwPlcyEntry,
       "tmnxMcPathBwPlcyName": tmnxMcPathBwPlcyName,
       "tmnxMcPathBwPlcyRowStatus": tmnxMcPathBwPlcyRowStatus,
       "tmnxMcPathBwPlcyLastChanged": tmnxMcPathBwPlcyLastChanged,
       "tmnxMcPathBwPlcyDescription": tmnxMcPathBwPlcyDescription,
       "tmnxMcPathBwPlcyFallPercentReset": tmnxMcPathBwPlcyFallPercentReset,
       "tmnxMcPathBwPlcyAdminBwThd": tmnxMcPathBwPlcyAdminBwThd,
       "tmnxMcPathBwPlcyMcPoolPercentTot": tmnxMcPathBwPlcyMcPoolPercentTot,
       "tmnxMcPathBwPlcyMcPoolResvCbs": tmnxMcPathBwPlcyMcPoolResvCbs,
       "tmnxMcPathBwPlcyMcPoolSlopePlcy": tmnxMcPathBwPlcyMcPoolSlopePlcy,
       "tmnxMcPathBwPlcyPathTable": tmnxMcPathBwPlcyPathTable,
       "tmnxMcPathBwPlcyPathEntry": tmnxMcPathBwPlcyPathEntry,
       "tmnxMcPathBwPlcyPathType": tmnxMcPathBwPlcyPathType,
       "tmnxMcPathBwPlcyPathLimit": tmnxMcPathBwPlcyPathLimit,
       "tmnxMcPathBwPlcyPathCbs": tmnxMcPathBwPlcyPathCbs,
       "tmnxMcPathBwPlcyPathMbs": tmnxMcPathBwPlcyPathMbs,
       "tmnxMcPathBwPlcyPathHighPrio": tmnxMcPathBwPlcyPathHighPrio,
       "tmnxMcPathPlcyTable": tmnxMcPathPlcyTable,
       "tmnxMcPathPlcyEntry": tmnxMcPathPlcyEntry,
       "tmnxMcPathPlcyName": tmnxMcPathPlcyName,
       "tmnxMcPathPlcyRowStatus": tmnxMcPathPlcyRowStatus,
       "tmnxMcPathPlcyLastChanged": tmnxMcPathPlcyLastChanged,
       "tmnxMcPathPlcyDescription": tmnxMcPathPlcyDescription,
       "tmnxMcPathBdlTable": tmnxMcPathBdlTable,
       "tmnxMcPathBdlEntry": tmnxMcPathBdlEntry,
       "tmnxMcPathBdlName": tmnxMcPathBdlName,
       "tmnxMcPathBdlStatus": tmnxMcPathBdlStatus,
       "tmnxMcPathBdlLastChanged": tmnxMcPathBdlLastChanged,
       "tmnxMcPathBdlDescription": tmnxMcPathBdlDescription,
       "tmnxMcPathBdlCongPriorityThd": tmnxMcPathBdlCongPriorityThd,
       "tmnxMcPathBdlEcmpOptThd": tmnxMcPathBdlEcmpOptThd,
       "tmnxMcPathBdlDefChlAdminBw": tmnxMcPathBdlDefChlAdminBw,
       "tmnxMcPathBdlDefChlPref": tmnxMcPathBdlDefChlPref,
       "tmnxMcPathBdlDefChlBwActivity": tmnxMcPathBdlDefChlBwActivity,
       "tmnxMcPathBdlDefChlBwFallDelay": tmnxMcPathBdlDefChlBwFallDelay,
       "tmnxMcPathBdlDefChlBwBlackHoleRt": tmnxMcPathBdlDefChlBwBlackHoleRt,
       "tmnxMcPathBdlDefChlExSfPath": tmnxMcPathBdlDefChlExSfPath,
       "tmnxMcPathBdlVdoFCCState": tmnxMcPathBdlVdoFCCState,
       "tmnxMcPathBdlVdoRTState": tmnxMcPathBdlVdoRTState,
       "tmnxMcPathBdlVdoChlType": tmnxMcPathBdlVdoChlType,
       "tmnxMcPathBdlVdoRTAddrType": tmnxMcPathBdlVdoRTAddrType,
       "tmnxMcPathBdlVdoRTAddress": tmnxMcPathBdlVdoRTAddress,
       "tmnxMcPathBdlVdoRTPort": tmnxMcPathBdlVdoRTPort,
       "tmnxMcPathBdlVdoRTBufferSize": tmnxMcPathBdlVdoRTBufferSize,
       "tmnxMcPathBdlVdoLocalRTPort": tmnxMcPathBdlVdoLocalRTPort,
       "tmnxMcPathBdlVdoLocalFccPort": tmnxMcPathBdlVdoLocalFccPort,
       "tmnxMcPathBdlVdoGroupId": tmnxMcPathBdlVdoGroupId,
       "tmnxMcPathBdlTunnelIfLspName": tmnxMcPathBdlTunnelIfLspName,
       "tmnxMcPathBdlTunIfSdAddrType": tmnxMcPathBdlTunIfSdAddrType,
       "tmnxMcPathBdlTunIfSdAddr": tmnxMcPathBdlTunIfSdAddr,
       "tmnxMcPathBdlVdoSourcePort": tmnxMcPathBdlVdoSourcePort,
       "tmnxMcPathBdlVdoLocalRTState": tmnxMcPathBdlVdoLocalRTState,
       "tmnxMcPathBdlVdoReorderAudio": tmnxMcPathBdlVdoReorderAudio,
       "tmnxMcPathBdlVdoFccMinDuration": tmnxMcPathBdlVdoFccMinDuration,
       "tmnxMcPathBdlKAOverrideTimer": tmnxMcPathBdlKAOverrideTimer,
       "tmnxMcPathBdlP2MPId": tmnxMcPathBdlP2MPId,
       "tmnxMcPathBdlVdoAnalyzer": tmnxMcPathBdlVdoAnalyzer,
       "tmnxMcPathBdlVdoAnalyzerDesc": tmnxMcPathBdlVdoAnalyzerDesc,
       "tmnxMcPathBdlVdoStrSelSrc1Type": tmnxMcPathBdlVdoStrSelSrc1Type,
       "tmnxMcPathBdlVdoStrSelSrc1": tmnxMcPathBdlVdoStrSelSrc1,
       "tmnxMcPathBdlVdoStrSelIntf1": tmnxMcPathBdlVdoStrSelIntf1,
       "tmnxMcPathBdlVdoStrSelSrc2Type": tmnxMcPathBdlVdoStrSelSrc2Type,
       "tmnxMcPathBdlVdoStrSelSrc2": tmnxMcPathBdlVdoStrSelSrc2,
       "tmnxMcPathBdlVdoStrSelIntf2": tmnxMcPathBdlVdoStrSelIntf2,
       "tmnxMcPathBdlChlTable": tmnxMcPathBdlChlTable,
       "tmnxMcPathBdlChlEntry": tmnxMcPathBdlChlEntry,
       "tmnxMcPathBdlChlStartAddrType": tmnxMcPathBdlChlStartAddrType,
       "tmnxMcPathBdlChlStartAddr": tmnxMcPathBdlChlStartAddr,
       "tmnxMcPathBdlChlEndAddrType": tmnxMcPathBdlChlEndAddrType,
       "tmnxMcPathBdlChlEndAddr": tmnxMcPathBdlChlEndAddr,
       "tmnxMcPathBdlChlRowStatus": tmnxMcPathBdlChlRowStatus,
       "tmnxMcPathBdlChlLastChanged": tmnxMcPathBdlChlLastChanged,
       "tmnxMcPathBdlChlAdminBw": tmnxMcPathBdlChlAdminBw,
       "tmnxMcPathBdlChlPref": tmnxMcPathBdlChlPref,
       "tmnxMcPathBdlChlBwActivity": tmnxMcPathBdlChlBwActivity,
       "tmnxMcPathBdlChlBwFallDelay": tmnxMcPathBdlChlBwFallDelay,
       "tmnxMcPathBdlChlBwBlackHoleRt": tmnxMcPathBdlChlBwBlackHoleRt,
       "tmnxMcPathBdlChlExSfPath": tmnxMcPathBdlChlExSfPath,
       "tmnxMcPathBdlChlVdoFCCState": tmnxMcPathBdlChlVdoFCCState,
       "tmnxMcPathBdlChlVdoRTState": tmnxMcPathBdlChlVdoRTState,
       "tmnxMcPathBdlChlVdoChlType": tmnxMcPathBdlChlVdoChlType,
       "tmnxMcPathBdlChlVdoRTAddrType": tmnxMcPathBdlChlVdoRTAddrType,
       "tmnxMcPathBdlChlVdoRTAddress": tmnxMcPathBdlChlVdoRTAddress,
       "tmnxMcPathBdlChlVdoRTPort": tmnxMcPathBdlChlVdoRTPort,
       "tmnxMcPathBdlChlVdoRTBufferSize": tmnxMcPathBdlChlVdoRTBufferSize,
       "tmnxMcPathBdlChlVdoLocalRTPort": tmnxMcPathBdlChlVdoLocalRTPort,
       "tmnxMcPathBdlChlVdoLocalFccPort": tmnxMcPathBdlChlVdoLocalFccPort,
       "tmnxMcPathBdlChlVdoGroupId": tmnxMcPathBdlChlVdoGroupId,
       "tmnxMcPathBdlChlTunnelIfLspName": tmnxMcPathBdlChlTunnelIfLspName,
       "tmnxMcPathBdlChlTunIfSdAddrType": tmnxMcPathBdlChlTunIfSdAddrType,
       "tmnxMcPathBdlChlTunIfSdAddr": tmnxMcPathBdlChlTunIfSdAddr,
       "tmnxMcPathBdlChlVdoLocalRTState": tmnxMcPathBdlChlVdoLocalRTState,
       "tmnxMcPathBdlChlVdoReorderAudio": tmnxMcPathBdlChlVdoReorderAudio,
       "tmnxMcPathBdlChlVdoFccMinDuratn": tmnxMcPathBdlChlVdoFccMinDuratn,
       "tmnxMcPathBdlChlKAOverrideTimer": tmnxMcPathBdlChlKAOverrideTimer,
       "tmnxMcPathBdlChlP2MPId": tmnxMcPathBdlChlP2MPId,
       "tmnxMcPathBdlChlVdoAnalyzer": tmnxMcPathBdlChlVdoAnalyzer,
       "tmnxMcPathBdlChlVdoAnalyzerDesc": tmnxMcPathBdlChlVdoAnalyzerDesc,
       "tmnxMcPathBdlChlVdoStrSelSrc1Typ": tmnxMcPathBdlChlVdoStrSelSrc1Typ,
       "tmnxMcPathBdlChlVdoStrSelSrc1": tmnxMcPathBdlChlVdoStrSelSrc1,
       "tmnxMcPathBdlChlVdoStrSelIntf1": tmnxMcPathBdlChlVdoStrSelIntf1,
       "tmnxMcPathBdlChlVdoStrSelSrc2Typ": tmnxMcPathBdlChlVdoStrSelSrc2Typ,
       "tmnxMcPathBdlChlVdoStrSelSrc2": tmnxMcPathBdlChlVdoStrSelSrc2,
       "tmnxMcPathBdlChlVdoStrSelIntf2": tmnxMcPathBdlChlVdoStrSelIntf2,
       "tmnxMcPathChlSrcTable": tmnxMcPathChlSrcTable,
       "tmnxMcPathChlSrcEntry": tmnxMcPathChlSrcEntry,
       "tmnxMcPathChlSrcSourceAddrType": tmnxMcPathChlSrcSourceAddrType,
       "tmnxMcPathChlSrcSourceAddr": tmnxMcPathChlSrcSourceAddr,
       "tmnxMcPathChlSrcRowStatus": tmnxMcPathChlSrcRowStatus,
       "tmnxMcPathChlSrcLastChanged": tmnxMcPathChlSrcLastChanged,
       "tmnxMcPathChlSrcAdminBw": tmnxMcPathChlSrcAdminBw,
       "tmnxMcPathChlSrcPref": tmnxMcPathChlSrcPref,
       "tmnxMcPathChlSrcBwActivity": tmnxMcPathChlSrcBwActivity,
       "tmnxMcPathChlSrcBwFallDelay": tmnxMcPathChlSrcBwFallDelay,
       "tmnxMcPathChlSrcBwBlackHoleRt": tmnxMcPathChlSrcBwBlackHoleRt,
       "tmnxMcPathChlSrcExSfPath": tmnxMcPathChlSrcExSfPath,
       "tmnxMcPathChlSrcVdoFCCState": tmnxMcPathChlSrcVdoFCCState,
       "tmnxMcPathChlSrcVdoRTState": tmnxMcPathChlSrcVdoRTState,
       "tmnxMcPathChlSrcVdoChlType": tmnxMcPathChlSrcVdoChlType,
       "tmnxMcPathChlSrcVdoRTAddrType": tmnxMcPathChlSrcVdoRTAddrType,
       "tmnxMcPathChlSrcVdoRTAddress": tmnxMcPathChlSrcVdoRTAddress,
       "tmnxMcPathChlSrcVdoRTPort": tmnxMcPathChlSrcVdoRTPort,
       "tmnxMcPathChlSrcVdoRTBufferSize": tmnxMcPathChlSrcVdoRTBufferSize,
       "tmnxMcPathChlSrcVdoLocalRTPort": tmnxMcPathChlSrcVdoLocalRTPort,
       "tmnxMcPathChlSrcVdoLocalFccPort": tmnxMcPathChlSrcVdoLocalFccPort,
       "tmnxMcPathChlSrcVdoGroupId": tmnxMcPathChlSrcVdoGroupId,
       "tmnxMcPathChlSrcTunnelIfLspName": tmnxMcPathChlSrcTunnelIfLspName,
       "tmnxMcPathChlSrcTunIfSdAddrType": tmnxMcPathChlSrcTunIfSdAddrType,
       "tmnxMcPathChlSrcTunIfSdAddr": tmnxMcPathChlSrcTunIfSdAddr,
       "tmnxMcPathChlSrcVdoLocalRTState": tmnxMcPathChlSrcVdoLocalRTState,
       "tmnxMcPathChlSrcVdoReorderAudio": tmnxMcPathChlSrcVdoReorderAudio,
       "tmnxMcPathChlSrcVdoFccMinDuratn": tmnxMcPathChlSrcVdoFccMinDuratn,
       "tmnxMcPathChlSrcKAOverrideTimer": tmnxMcPathChlSrcKAOverrideTimer,
       "tmnxMcPathChlSrcP2MPId": tmnxMcPathChlSrcP2MPId,
       "tmnxMcPathChlSrcVdoAnalyzer": tmnxMcPathChlSrcVdoAnalyzer,
       "tmnxMcPathChlSrcVdoAnalyzerDesc": tmnxMcPathChlSrcVdoAnalyzerDesc,
       "tmnxMcPathChlSrcVdoStSeSrc1Type": tmnxMcPathChlSrcVdoStSeSrc1Type,
       "tmnxMcPathChlSrcVdoStSeSrc1": tmnxMcPathChlSrcVdoStSeSrc1,
       "tmnxMcPathChlSrcVdoStSeIntf1": tmnxMcPathChlSrcVdoStSeIntf1,
       "tmnxMcPathChlSrcVdoStSeSrc2Type": tmnxMcPathChlSrcVdoStSeSrc2Type,
       "tmnxMcPathChlSrcVdoStSeSrc2": tmnxMcPathChlSrcVdoStSeSrc2,
       "tmnxMcPathChlSrcVdoStSeIntf2": tmnxMcPathChlSrcVdoStSeIntf2,
       "tmnxMcPathOperChlTable": tmnxMcPathOperChlTable,
       "tmnxMcPathOperChlEntry": tmnxMcPathOperChlEntry,
       "tmnxMcPathOperChlRtrType": tmnxMcPathOperChlRtrType,
       "tmnxMcPathOperChlGrpAddrType": tmnxMcPathOperChlGrpAddrType,
       "tmnxMcPathOperChlGrpAddr": tmnxMcPathOperChlGrpAddr,
       "tmnxMcPathOperChlSrcAddrType": tmnxMcPathOperChlSrcAddrType,
       "tmnxMcPathOperChlSrcAddr": tmnxMcPathOperChlSrcAddr,
       "tmnxMcPathOperChlBandwidth": tmnxMcPathOperChlBandwidth,
       "tmnxMcPathOperChlCurrentPath": tmnxMcPathOperChlCurrentPath,
       "tmnxMcPathOperChlExplicit": tmnxMcPathOperChlExplicit,
       "tmnxMcPathOperChlAdminBw": tmnxMcPathOperChlAdminBw,
       "tmnxMcPathOperChlPref": tmnxMcPathOperChlPref,
       "tmnxMcPathOperChlBwBlackHole": tmnxMcPathOperChlBwBlackHole,
       "tmnxMcPathOperChlBwBlackHoleRt": tmnxMcPathOperChlBwBlackHoleRt,
       "tmnxMcPathOperChlIngLastHighest": tmnxMcPathOperChlIngLastHighest,
       "tmnxMcPathOperChlIngSecHighest": tmnxMcPathOperChlIngSecHighest,
       "tmnxMcPathOperChlTimeRemaining": tmnxMcPathOperChlTimeRemaining,
       "tmnxMcPathOperChlCurrentPlane": tmnxMcPathOperChlCurrentPlane,
       "tmnxMcPathMdaOperChlTable": tmnxMcPathMdaOperChlTable,
       "tmnxMcPathMdaOperChlEntry": tmnxMcPathMdaOperChlEntry,
       "tmnxMcPathMdaOperChlRtrType": tmnxMcPathMdaOperChlRtrType,
       "tmnxMcPathMdaOperChlGrpAddrType": tmnxMcPathMdaOperChlGrpAddrType,
       "tmnxMcPathMdaOperChlGrpAddr": tmnxMcPathMdaOperChlGrpAddr,
       "tmnxMcPathMdaOperChlSrcAddrType": tmnxMcPathMdaOperChlSrcAddrType,
       "tmnxMcPathMdaOperChlSrcAddr": tmnxMcPathMdaOperChlSrcAddr,
       "tmnxMcPathMdaOperChlBandwidth": tmnxMcPathMdaOperChlBandwidth,
       "tmnxMcPathMdaOperChlCurrentPath": tmnxMcPathMdaOperChlCurrentPath,
       "tmnxMcPathMdaOperChlExplicit": tmnxMcPathMdaOperChlExplicit,
       "tmnxMcPathMdaOperChlAdminBw": tmnxMcPathMdaOperChlAdminBw,
       "tmnxMcPathMdaOperChlPref": tmnxMcPathMdaOperChlPref,
       "tmnxMcPathMdaOperChlBwBlackHole": tmnxMcPathMdaOperChlBwBlackHole,
       "tmnxMcPathMdaOperChlBwBlackHoleRt": tmnxMcPathMdaOperChlBwBlackHoleRt,
       "tmnxMcPathMdaOperChlIngLastHigh": tmnxMcPathMdaOperChlIngLastHigh,
       "tmnxMcPathMdaOperChlIngSecHigh": tmnxMcPathMdaOperChlIngSecHigh,
       "tmnxMcPathMdaOperChlTimeRemain": tmnxMcPathMdaOperChlTimeRemain,
       "tmnxMcPathMdaOperChlCurrentPlane": tmnxMcPathMdaOperChlCurrentPlane,
       "tmnxMcPathBwPlcyT2PathTable": tmnxMcPathBwPlcyT2PathTable,
       "tmnxMcPathBwPlcyT2PathEntry": tmnxMcPathBwPlcyT2PathEntry,
       "tmnxMcPathBwPlcyT2PathType": tmnxMcPathBwPlcyT2PathType,
       "tmnxMcPathBwPlcyT2PathCbs": tmnxMcPathBwPlcyT2PathCbs,
       "tmnxMcPathBwPlcyT2PathMbs": tmnxMcPathBwPlcyT2PathMbs,
       "tmnxMcPathBwPlcyT2PathHighPrio": tmnxMcPathBwPlcyT2PathHighPrio,
       "tmnxMcPathBwPlcyT2PathPaths": tmnxMcPathBwPlcyT2PathPaths,
       "tmnxMcPathBwPlcyT2PathDualPaths": tmnxMcPathBwPlcyT2PathDualPaths,
       "tmnxMcPathBwPlcyT2PathLastChanged": tmnxMcPathBwPlcyT2PathLastChanged,
       "tmnxMcPathVdoPlcyTable": tmnxMcPathVdoPlcyTable,
       "tmnxMcPathVdoPlcyEntry": tmnxMcPathVdoPlcyEntry,
       "tmnxMcPathVdoPlcyIfAddrType": tmnxMcPathVdoPlcyIfAddrType,
       "tmnxMcPathVdoPlcyIfAddress": tmnxMcPathVdoPlcyIfAddress,
       "tmnxMcPathVdoPlcyChlType": tmnxMcPathVdoPlcyChlType,
       "tmnxMcPathVdoPlcyRowStatus": tmnxMcPathVdoPlcyRowStatus,
       "tmnxMcPathVdoPlcyLastChanged": tmnxMcPathVdoPlcyLastChanged,
       "tmnxMcPathVdoPlcyLclRTSvrState": tmnxMcPathVdoPlcyLclRTSvrState,
       "tmnxMcPathVdoPlcyRTRate": tmnxMcPathVdoPlcyRTRate,
       "tmnxMcPathVdoPlcySubBwLimit": tmnxMcPathVdoPlcySubBwLimit,
       "tmnxMcPathVdoPlcyFCCSvrMode": tmnxMcPathVdoPlcyFCCSvrMode,
       "tmnxMcPathVdoPlcyFCCBurst": tmnxMcPathVdoPlcyFCCBurst,
       "tmnxMcPathVdoPlcyFCCMcHandover": tmnxMcPathVdoPlcyFCCMcHandover,
       "tmnxMcPathVdoPlcyFCCDentThd": tmnxMcPathVdoPlcyFCCDentThd,
       "tmnxMcPathVdoPlcyRTPayloadType": tmnxMcPathVdoPlcyRTPayloadType,
       "tmnxMcPathVdoPlcyMaxClntSessions": tmnxMcPathVdoPlcyMaxClntSessions,
       "tmnxMcPathVdoPlcyMaxIgmpLatency": tmnxMcPathVdoPlcyMaxIgmpLatency,
       "tmnxMcPathBdlExtTable": tmnxMcPathBdlExtTable,
       "tmnxMcPathBdlExtEntry": tmnxMcPathBdlExtEntry,
       "tmnxMcPathBdlVdoLastChanged": tmnxMcPathBdlVdoLastChanged,
       "tmnxMcPathBdlVdoCcError": tmnxMcPathBdlVdoCcError,
       "tmnxMcPathBdlVdoPatRepError": tmnxMcPathBdlVdoPatRepError,
       "tmnxMcPathBdlVdoTncPatRep": tmnxMcPathBdlVdoTncPatRep,
       "tmnxMcPathBdlVdoQosPatRep": tmnxMcPathBdlVdoQosPatRep,
       "tmnxMcPathBdlVdoPoaPatRep": tmnxMcPathBdlVdoPoaPatRep,
       "tmnxMcPathBdlVdoPatSyntax": tmnxMcPathBdlVdoPatSyntax,
       "tmnxMcPathBdlVdoPcrRepError": tmnxMcPathBdlVdoPcrRepError,
       "tmnxMcPathBdlVdoTncPcrRep": tmnxMcPathBdlVdoTncPcrRep,
       "tmnxMcPathBdlVdoQosPcrRep": tmnxMcPathBdlVdoQosPcrRep,
       "tmnxMcPathBdlVdoPoaPcrRep": tmnxMcPathBdlVdoPoaPcrRep,
       "tmnxMcPathBdlVdoVidPIDAbsent": tmnxMcPathBdlVdoVidPIDAbsent,
       "tmnxMcPathBdlVdoPIDPmtUnref": tmnxMcPathBdlVdoPIDPmtUnref,
       "tmnxMcPathBdlVdoPmtRepError": tmnxMcPathBdlVdoPmtRepError,
       "tmnxMcPathBdlVdoTncPmtRep": tmnxMcPathBdlVdoTncPmtRep,
       "tmnxMcPathBdlVdoQosPmtRep": tmnxMcPathBdlVdoQosPmtRep,
       "tmnxMcPathBdlVdoPoaPmtRep": tmnxMcPathBdlVdoPoaPmtRep,
       "tmnxMcPathBdlVdoPmtSyntax": tmnxMcPathBdlVdoPmtSyntax,
       "tmnxMcPathBdlVdoScte35Error": tmnxMcPathBdlVdoScte35Error,
       "tmnxMcPathBdlVdoTeiError": tmnxMcPathBdlVdoTeiError,
       "tmnxMcPathBdlVdoTsSyncLoss": tmnxMcPathBdlVdoTsSyncLoss,
       "tmnxMcPathBdlVdoNonVidPIDAbsent": tmnxMcPathBdlVdoNonVidPIDAbsent,
       "tmnxMcPathBdlVdoReportAlarm": tmnxMcPathBdlVdoReportAlarm,
       "tmnxMcPathBdlChlExtTable": tmnxMcPathBdlChlExtTable,
       "tmnxMcPathBdlChlExtEntry": tmnxMcPathBdlChlExtEntry,
       "tmnxMcPathBdlChlVdoLastChanged": tmnxMcPathBdlChlVdoLastChanged,
       "tmnxMcPathBdlChlVdoCcError": tmnxMcPathBdlChlVdoCcError,
       "tmnxMcPathBdlChlVdoPatRepError": tmnxMcPathBdlChlVdoPatRepError,
       "tmnxMcPathBdlChlVdoTncPatRep": tmnxMcPathBdlChlVdoTncPatRep,
       "tmnxMcPathBdlChlVdoQosPatRep": tmnxMcPathBdlChlVdoQosPatRep,
       "tmnxMcPathBdlChlVdoPoaPatRep": tmnxMcPathBdlChlVdoPoaPatRep,
       "tmnxMcPathBdlChlVdoPatSyntax": tmnxMcPathBdlChlVdoPatSyntax,
       "tmnxMcPathBdlChlVdoPcrRepError": tmnxMcPathBdlChlVdoPcrRepError,
       "tmnxMcPathBdlChlVdoTncPcrRep": tmnxMcPathBdlChlVdoTncPcrRep,
       "tmnxMcPathBdlChlVdoQosPcrRep": tmnxMcPathBdlChlVdoQosPcrRep,
       "tmnxMcPathBdlChlVdoPoaPcrRep": tmnxMcPathBdlChlVdoPoaPcrRep,
       "tmnxMcPathBdlChlVdoVidPIDAbs": tmnxMcPathBdlChlVdoVidPIDAbs,
       "tmnxMcPathBdlChlVdoPIDPmtUnref": tmnxMcPathBdlChlVdoPIDPmtUnref,
       "tmnxMcPathBdlChlVdoPmtRepError": tmnxMcPathBdlChlVdoPmtRepError,
       "tmnxMcPathBdlChlVdoTncPmtRep": tmnxMcPathBdlChlVdoTncPmtRep,
       "tmnxMcPathBdlChlVdoQosPmtRep": tmnxMcPathBdlChlVdoQosPmtRep,
       "tmnxMcPathBdlChlVdoPoaPmtRep": tmnxMcPathBdlChlVdoPoaPmtRep,
       "tmnxMcPathBdlChlVdoPmtSyntax": tmnxMcPathBdlChlVdoPmtSyntax,
       "tmnxMcPathBdlChlVdoScte35Error": tmnxMcPathBdlChlVdoScte35Error,
       "tmnxMcPathBdlChlVdoTeiError": tmnxMcPathBdlChlVdoTeiError,
       "tmnxMcPathBdlChlVdoTsSyncLoss": tmnxMcPathBdlChlVdoTsSyncLoss,
       "tmnxMcPathBdlChlVdoNonVidPIDAbs": tmnxMcPathBdlChlVdoNonVidPIDAbs,
       "tmnxMcPathBdlChlVdoReportAlarm": tmnxMcPathBdlChlVdoReportAlarm,
       "tmnxMcPathChlSrcExtTable": tmnxMcPathChlSrcExtTable,
       "tmnxMcPathChlSrcExtEntry": tmnxMcPathChlSrcExtEntry,
       "tmnxMcPathChlSrcVdoLastChanged": tmnxMcPathChlSrcVdoLastChanged,
       "tmnxMcPathChlSrcVdoCcError": tmnxMcPathChlSrcVdoCcError,
       "tmnxMcPathChlSrcVdoPatRepError": tmnxMcPathChlSrcVdoPatRepError,
       "tmnxMcPathChlSrcVdoTncPatRep": tmnxMcPathChlSrcVdoTncPatRep,
       "tmnxMcPathChlSrcVdoQosPatRep": tmnxMcPathChlSrcVdoQosPatRep,
       "tmnxMcPathChlSrcVdoPoaPatRep": tmnxMcPathChlSrcVdoPoaPatRep,
       "tmnxMcPathChlSrcVdoPatSyntax": tmnxMcPathChlSrcVdoPatSyntax,
       "tmnxMcPathChlSrcVdoPcrRepError": tmnxMcPathChlSrcVdoPcrRepError,
       "tmnxMcPathChlSrcVdoTncPcrRep": tmnxMcPathChlSrcVdoTncPcrRep,
       "tmnxMcPathChlSrcVdoQosPcrRep": tmnxMcPathChlSrcVdoQosPcrRep,
       "tmnxMcPathChlSrcVdoPoaPcrRep": tmnxMcPathChlSrcVdoPoaPcrRep,
       "tmnxMcPathChlSrcVdoVidPIDAbs": tmnxMcPathChlSrcVdoVidPIDAbs,
       "tmnxMcPathChlSrcVdoPIDPmtUnref": tmnxMcPathChlSrcVdoPIDPmtUnref,
       "tmnxMcPathChlSrcVdoPmtRepError": tmnxMcPathChlSrcVdoPmtRepError,
       "tmnxMcPathChlSrcVdoTncPmtRep": tmnxMcPathChlSrcVdoTncPmtRep,
       "tmnxMcPathChlSrcVdoQosPmtRep": tmnxMcPathChlSrcVdoQosPmtRep,
       "tmnxMcPathChlSrcVdoPoaPmtRep": tmnxMcPathChlSrcVdoPoaPmtRep,
       "tmnxMcPathChlSrcVdoPmtSyntax": tmnxMcPathChlSrcVdoPmtSyntax,
       "tmnxMcPathChlSrcVdoScte35Error": tmnxMcPathChlSrcVdoScte35Error,
       "tmnxMcPathChlSrcVdoTeiError": tmnxMcPathChlSrcVdoTeiError,
       "tmnxMcPathChlSrcVdoTsSyncLoss": tmnxMcPathChlSrcVdoTsSyncLoss,
       "tmnxMcPathChlSrcVdoNonVidPIDAbs": tmnxMcPathChlSrcVdoNonVidPIDAbs,
       "tmnxMcPathChlSrcVdoReportAlarm": tmnxMcPathChlSrcVdoReportAlarm,
       "tmnxMcPathRprtDestTable": tmnxMcPathRprtDestTable,
       "tmnxMcPathRprtDestEntry": tmnxMcPathRprtDestEntry,
       "tmnxMcPathRprtDestName": tmnxMcPathRprtDestName,
       "tmnxMcPathRprtDestRowStatus": tmnxMcPathRprtDestRowStatus,
       "tmnxMcPathRprtDestLastChanged": tmnxMcPathRprtDestLastChanged,
       "tmnxMcPathRprtDestDescription": tmnxMcPathRprtDestDescription,
       "tmnxMcPathRprtDestAddrType": tmnxMcPathRprtDestAddrType,
       "tmnxMcPathRprtDestAddress": tmnxMcPathRprtDestAddress,
       "tmnxMcPathRprtDestUdpDstPort": tmnxMcPathRprtDestUdpDstPort,
       "tmnxMcPathRprtDestMaxTxDelay": tmnxMcPathRprtDestMaxTxDelay,
       "tmnxMcPathRprtDestAdminState": tmnxMcPathRprtDestAdminState,
       "tmnxMcPathRprtDestFrmsSent": tmnxMcPathRprtDestFrmsSent,
       "tmnxMcPathRprtDestFrmsLost": tmnxMcPathRprtDestFrmsLost,
       "tmnxMcPathRprtDestRecsSent": tmnxMcPathRprtDestRecsSent,
       "tmnxMcPathRprtDestRecsLost": tmnxMcPathRprtDestRecsLost,
       "tmnxMcPathNotifyPrefix": tmnxMcPathNotifyPrefix,
       "tmnxMcPathNotifications": tmnxMcPathNotifications,
       "tmnxMcPathSrcGrpBlkHole": tmnxMcPathSrcGrpBlkHole,
       "tmnxMcPathSrcGrpBlkHoleClear": tmnxMcPathSrcGrpBlkHoleClear,
       "tmnxMcPathAvailBwLimitReached": tmnxMcPathAvailBwLimitReached,
       "tmnxMcPathAvailBwValWithinRange": tmnxMcPathAvailBwValWithinRange}
)
