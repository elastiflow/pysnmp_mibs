# SNMP MIB module (VZW-NLS72-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/VZW-NLS72-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:24:52 2025
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
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("mandatory")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysServices_Type(Integer32):
    """Custom type sysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SysServices_Type.__name__ = "Integer32"
_SysServices_Object = MibScalar
sysServices = _SysServices_Object(
    (1, 3, 6, 1, 2, 1, 1, 7),
    _SysServices_Type()
)
sysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysServices.setStatus("mandatory")
_Nsn_ObjectIdentity = ObjectIdentity
nsn = _Nsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458)
)
_NsnProducts_ObjectIdentity = ObjectIdentity
nsnProducts = _NsnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1)
)
_Lbs_ObjectIdentity = ObjectIdentity
lbs = _Lbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1)
)
_AppAlarmTable_Object = MibTable
appAlarmTable = _AppAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1)
)
if mibBuilder.loadTexts:
    appAlarmTable.setStatus("current")
_AppAlarmEntry_Object = MibTableRow
appAlarmEntry = _AppAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1)
)
appAlarmEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appAlarmRowIndex"),
)
if mibBuilder.loadTexts:
    appAlarmEntry.setStatus("current")
_AppAlarmSystemName_Type = DisplayString
_AppAlarmSystemName_Object = MibTableColumn
appAlarmSystemName = _AppAlarmSystemName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 1),
    _AppAlarmSystemName_Type()
)
appAlarmSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmSystemName.setStatus("current")


class _AppAlarmOriId_Type(Integer32):
    """Custom type appAlarmOriId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_AppAlarmOriId_Type.__name__ = "Integer32"
_AppAlarmOriId_Object = MibTableColumn
appAlarmOriId = _AppAlarmOriId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 2),
    _AppAlarmOriId_Type()
)
appAlarmOriId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmOriId.setStatus("current")
_AppAlarmNeType_Type = DisplayString
_AppAlarmNeType_Object = MibTableColumn
appAlarmNeType = _AppAlarmNeType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 3),
    _AppAlarmNeType_Type()
)
appAlarmNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmNeType.setStatus("current")
_AppAlarmNeName_Type = DisplayString
_AppAlarmNeName_Object = MibTableColumn
appAlarmNeName = _AppAlarmNeName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 4),
    _AppAlarmNeName_Type()
)
appAlarmNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmNeName.setStatus("current")
_AppAlarmTitle_Type = DisplayString
_AppAlarmTitle_Object = MibTableColumn
appAlarmTitle = _AppAlarmTitle_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 5),
    _AppAlarmTitle_Type()
)
appAlarmTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmTitle.setStatus("current")
_AppAlarmTypeID_Type = Integer32
_AppAlarmTypeID_Object = MibTableColumn
appAlarmTypeID = _AppAlarmTypeID_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 6),
    _AppAlarmTypeID_Type()
)
appAlarmTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmTypeID.setStatus("current")
_AppAlarmSeverity_Type = Integer32
_AppAlarmSeverity_Object = MibTableColumn
appAlarmSeverity = _AppAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 7),
    _AppAlarmSeverity_Type()
)
appAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmSeverity.setStatus("current")
_AppAlarmDetail_Type = DisplayString
_AppAlarmDetail_Object = MibTableColumn
appAlarmDetail = _AppAlarmDetail_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 8),
    _AppAlarmDetail_Type()
)
appAlarmDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmDetail.setStatus("current")
_AppAlarmCounts_Type = Integer32
_AppAlarmCounts_Object = MibTableColumn
appAlarmCounts = _AppAlarmCounts_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 9),
    _AppAlarmCounts_Type()
)
appAlarmCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmCounts.setStatus("current")
_AppAlarmCreatetime_Type = DisplayString
_AppAlarmCreatetime_Object = MibTableColumn
appAlarmCreatetime = _AppAlarmCreatetime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 10),
    _AppAlarmCreatetime_Type()
)
appAlarmCreatetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmCreatetime.setStatus("current")
_AppAlarmRowIndex_Type = Integer32
_AppAlarmRowIndex_Object = MibTableColumn
appAlarmRowIndex = _AppAlarmRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 1, 1, 1, 11),
    _AppAlarmRowIndex_Type()
)
appAlarmRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appAlarmRowIndex.setStatus("current")
_App_ObjectIdentity = ObjectIdentity
app = _App_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3)
)
_AppPM_ObjectIdentity = ObjectIdentity
appPM = _AppPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2)
)
_AppLocIFTable_Object = MibTable
appLocIFTable = _AppLocIFTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2)
)
if mibBuilder.loadTexts:
    appLocIFTable.setStatus("current")
_AppLocIFEntry_Object = MibTableRow
appLocIFEntry = _AppLocIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1)
)
appLocIFEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocIFRowIndex"),
)
if mibBuilder.loadTexts:
    appLocIFEntry.setStatus("current")
_AppLocIFReq_Type = Integer32
_AppLocIFReq_Object = MibTableColumn
appLocIFReq = _AppLocIFReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 1),
    _AppLocIFReq_Type()
)
appLocIFReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFReq.setStatus("current")
_AppLocIFValidReq_Type = Integer32
_AppLocIFValidReq_Object = MibTableColumn
appLocIFValidReq = _AppLocIFValidReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 2),
    _AppLocIFValidReq_Type()
)
appLocIFValidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFValidReq.setStatus("current")
_AppLocIFSuccRes_Type = Integer32
_AppLocIFSuccRes_Object = MibTableColumn
appLocIFSuccRes = _AppLocIFSuccRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 3),
    _AppLocIFSuccRes_Type()
)
appLocIFSuccRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFSuccRes.setStatus("current")
_AppLocIFSuccResRate_Type = Integer32
_AppLocIFSuccResRate_Object = MibTableColumn
appLocIFSuccResRate = _AppLocIFSuccResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 4),
    _AppLocIFSuccResRate_Type()
)
appLocIFSuccResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFSuccResRate.setStatus("current")
_AppLocIFGrossSuccResRate_Type = Integer32
_AppLocIFGrossSuccResRate_Object = MibTableColumn
appLocIFGrossSuccResRate = _AppLocIFGrossSuccResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 5),
    _AppLocIFGrossSuccResRate_Type()
)
appLocIFGrossSuccResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFGrossSuccResRate.setStatus("current")
_AppLocIFStartTime_Type = DateAndTime
_AppLocIFStartTime_Object = MibTableColumn
appLocIFStartTime = _AppLocIFStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 6),
    _AppLocIFStartTime_Type()
)
appLocIFStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFStartTime.setStatus("current")
_AppLocIFEndTime_Type = DateAndTime
_AppLocIFEndTime_Object = MibTableColumn
appLocIFEndTime = _AppLocIFEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 7),
    _AppLocIFEndTime_Type()
)
appLocIFEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFEndTime.setStatus("current")
_AppLocIFRowIndex_Type = Integer32
_AppLocIFRowIndex_Object = MibTableColumn
appLocIFRowIndex = _AppLocIFRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 2, 1, 8),
    _AppLocIFRowIndex_Type()
)
appLocIFRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocIFRowIndex.setStatus("current")
_AppLocLeIFTable_Object = MibTable
appLocLeIFTable = _AppLocLeIFTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3)
)
if mibBuilder.loadTexts:
    appLocLeIFTable.setStatus("current")
_AppLocLeIFEntry_Object = MibTableRow
appLocLeIFEntry = _AppLocLeIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1)
)
appLocLeIFEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocLeIFRowIndex"),
)
if mibBuilder.loadTexts:
    appLocLeIFEntry.setStatus("current")
_AppLocLeIFReq_Type = Integer32
_AppLocLeIFReq_Object = MibTableColumn
appLocLeIFReq = _AppLocLeIFReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 1),
    _AppLocLeIFReq_Type()
)
appLocLeIFReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocLeIFReq.setStatus("current")
_AppValidLeReq_Type = Integer32
_AppValidLeReq_Object = MibTableColumn
appValidLeReq = _AppValidLeReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 2),
    _AppValidLeReq_Type()
)
appValidLeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appValidLeReq.setStatus("current")
_AppSuccLeRes_Type = Integer32
_AppSuccLeRes_Object = MibTableColumn
appSuccLeRes = _AppSuccLeRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 3),
    _AppSuccLeRes_Type()
)
appSuccLeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccLeRes.setStatus("current")
_AppSuccLeResRate_Type = Integer32
_AppSuccLeResRate_Object = MibTableColumn
appSuccLeResRate = _AppSuccLeResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 4),
    _AppSuccLeResRate_Type()
)
appSuccLeResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccLeResRate.setStatus("current")
_AppGrossSuccLeResRate_Type = Integer32
_AppGrossSuccLeResRate_Object = MibTableColumn
appGrossSuccLeResRate = _AppGrossSuccLeResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 5),
    _AppGrossSuccLeResRate_Type()
)
appGrossSuccLeResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appGrossSuccLeResRate.setStatus("current")
_AppSuccLeQopRes_Type = Integer32
_AppSuccLeQopRes_Object = MibTableColumn
appSuccLeQopRes = _AppSuccLeQopRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 6),
    _AppSuccLeQopRes_Type()
)
appSuccLeQopRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccLeQopRes.setStatus("current")
_AppSuccLeQopResRate_Type = Integer32
_AppSuccLeQopResRate_Object = MibTableColumn
appSuccLeQopResRate = _AppSuccLeQopResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 7),
    _AppSuccLeQopResRate_Type()
)
appSuccLeQopResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccLeQopResRate.setStatus("current")
_AppLoc50LeRes_Type = Integer32
_AppLoc50LeRes_Object = MibTableColumn
appLoc50LeRes = _AppLoc50LeRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 28),
    _AppLoc50LeRes_Type()
)
appLoc50LeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLoc50LeRes.setStatus("current")
_AppLoc150LeRes_Type = Integer32
_AppLoc150LeRes_Object = MibTableColumn
appLoc150LeRes = _AppLoc150LeRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 29),
    _AppLoc150LeRes_Type()
)
appLoc150LeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLoc150LeRes.setStatus("current")
_AppSucc50LeResRate_Type = Integer32
_AppSucc50LeResRate_Object = MibTableColumn
appSucc50LeResRate = _AppSucc50LeResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 30),
    _AppSucc50LeResRate_Type()
)
appSucc50LeResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSucc50LeResRate.setStatus("current")
_AppSucc150LeResRate_Type = Integer32
_AppSucc150LeResRate_Object = MibTableColumn
appSucc150LeResRate = _AppSucc150LeResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 31),
    _AppSucc150LeResRate_Type()
)
appSucc150LeResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSucc150LeResRate.setStatus("current")
_AppLocLeIFStartTime_Type = DateAndTime
_AppLocLeIFStartTime_Object = MibTableColumn
appLocLeIFStartTime = _AppLocLeIFStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 32),
    _AppLocLeIFStartTime_Type()
)
appLocLeIFStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocLeIFStartTime.setStatus("current")
_AppLocLeIFEndTime_Type = DateAndTime
_AppLocLeIFEndTime_Object = MibTableColumn
appLocLeIFEndTime = _AppLocLeIFEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 33),
    _AppLocLeIFEndTime_Type()
)
appLocLeIFEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocLeIFEndTime.setStatus("current")
_AppLocLeIFRowIndex_Type = Integer32
_AppLocLeIFRowIndex_Object = MibTableColumn
appLocLeIFRowIndex = _AppLocLeIFRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 3, 1, 34),
    _AppLocLeIFRowIndex_Type()
)
appLocLeIFRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocLeIFRowIndex.setStatus("current")
_AppLocFailIFTable_Object = MibTable
appLocFailIFTable = _AppLocFailIFTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4)
)
if mibBuilder.loadTexts:
    appLocFailIFTable.setStatus("current")
_AppLocFailIFEntry_Object = MibTableRow
appLocFailIFEntry = _AppLocFailIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1)
)
appLocFailIFEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocFailIFRowIndex"),
)
if mibBuilder.loadTexts:
    appLocFailIFEntry.setStatus("current")
_AppInvalidLeReq_Type = Integer32
_AppInvalidLeReq_Object = MibTableColumn
appInvalidLeReq = _AppInvalidLeReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 1),
    _AppInvalidLeReq_Type()
)
appInvalidLeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appInvalidLeReq.setStatus("current")
_AppFailRes_Type = Integer32
_AppFailRes_Object = MibTableColumn
appFailRes = _AppFailRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 3),
    _AppFailRes_Type()
)
appFailRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailRes.setStatus("current")
_AppFailLeRes_Type = Integer32
_AppFailLeRes_Object = MibTableColumn
appFailLeRes = _AppFailLeRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 4),
    _AppFailLeRes_Type()
)
appFailLeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailLeRes.setStatus("current")
_AppLocFailIFStartTime_Type = DateAndTime
_AppLocFailIFStartTime_Object = MibTableColumn
appLocFailIFStartTime = _AppLocFailIFStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 6),
    _AppLocFailIFStartTime_Type()
)
appLocFailIFStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocFailIFStartTime.setStatus("current")
_AppLocFailIFEndTime_Type = DateAndTime
_AppLocFailIFEndTime_Object = MibTableColumn
appLocFailIFEndTime = _AppLocFailIFEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 7),
    _AppLocFailIFEndTime_Type()
)
appLocFailIFEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocFailIFEndTime.setStatus("current")
_AppLocFailIFRowIndex_Type = Integer32
_AppLocFailIFRowIndex_Object = MibTableColumn
appLocFailIFRowIndex = _AppLocFailIFRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 4, 1, 8),
    _AppLocFailIFRowIndex_Type()
)
appLocFailIFRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocFailIFRowIndex.setStatus("current")
_ApplocFailTable_Object = MibTable
applocFailTable = _ApplocFailTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5)
)
if mibBuilder.loadTexts:
    applocFailTable.setStatus("current")
_ApplocFailEntry_Object = MibTableRow
applocFailEntry = _ApplocFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1)
)
applocFailEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "applocfailRowIndex"),
)
if mibBuilder.loadTexts:
    applocFailEntry.setStatus("current")
_ApplocfailbyAuthenticationError_Type = Integer32
_ApplocfailbyAuthenticationError_Object = MibTableColumn
applocfailbyAuthenticationError = _ApplocfailbyAuthenticationError_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 3),
    _ApplocfailbyAuthenticationError_Type()
)
applocfailbyAuthenticationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailbyAuthenticationError.setStatus("current")
_ApplocfailbyBlackList_Type = Integer32
_ApplocfailbyBlackList_Object = MibTableColumn
applocfailbyBlackList = _ApplocfailbyBlackList_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 4),
    _ApplocfailbyBlackList_Type()
)
applocfailbyBlackList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailbyBlackList.setStatus("current")
_ApplocfailbyInvalidMobileNumber_Type = Integer32
_ApplocfailbyInvalidMobileNumber_Object = MibTableColumn
applocfailbyInvalidMobileNumber = _ApplocfailbyInvalidMobileNumber_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 5),
    _ApplocfailbyInvalidMobileNumber_Type()
)
applocfailbyInvalidMobileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailbyInvalidMobileNumber.setStatus("current")
_Applocfailstarttime_Type = DateAndTime
_Applocfailstarttime_Object = MibTableColumn
applocfailstarttime = _Applocfailstarttime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 6),
    _Applocfailstarttime_Type()
)
applocfailstarttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailstarttime.setStatus("current")
_Applocfailendtime_Type = DateAndTime
_Applocfailendtime_Object = MibTableColumn
applocfailendtime = _Applocfailendtime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 7),
    _Applocfailendtime_Type()
)
applocfailendtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailendtime.setStatus("current")
_ApplocfailRowIndex_Type = Integer32
_ApplocfailRowIndex_Object = MibTableColumn
applocfailRowIndex = _ApplocfailRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 5, 1, 8),
    _ApplocfailRowIndex_Type()
)
applocfailRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applocfailRowIndex.setStatus("current")
_AppFailLeResErrorCodeTable_Object = MibTable
appFailLeResErrorCodeTable = _AppFailLeResErrorCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7)
)
if mibBuilder.loadTexts:
    appFailLeResErrorCodeTable.setStatus("current")
_AppFailLeResErrorCodeEntry_Object = MibTableRow
appFailLeResErrorCodeEntry = _AppFailLeResErrorCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1)
)
appFailLeResErrorCodeEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "failLeResErrorCodeRowIndex"),
)
if mibBuilder.loadTexts:
    appFailLeResErrorCodeEntry.setStatus("current")
_FailLeResSystemFailure_Type = Integer32
_FailLeResSystemFailure_Object = MibTableColumn
failLeResSystemFailure = _FailLeResSystemFailure_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 1),
    _FailLeResSystemFailure_Type()
)
failLeResSystemFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResSystemFailure.setStatus("current")
_FailLeResUnspecifiedError_Type = Integer32
_FailLeResUnspecifiedError_Object = MibTableColumn
failLeResUnspecifiedError = _FailLeResUnspecifiedError_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 2),
    _FailLeResUnspecifiedError_Type()
)
failLeResUnspecifiedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResUnspecifiedError.setStatus("current")
_FailLeResUnauthorizedApplication_Type = Integer32
_FailLeResUnauthorizedApplication_Object = MibTableColumn
failLeResUnauthorizedApplication = _FailLeResUnauthorizedApplication_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 3),
    _FailLeResUnauthorizedApplication_Type()
)
failLeResUnauthorizedApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResUnauthorizedApplication.setStatus("current")
_FailLeResUnknownSubscriber_Type = Integer32
_FailLeResUnknownSubscriber_Object = MibTableColumn
failLeResUnknownSubscriber = _FailLeResUnknownSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 4),
    _FailLeResUnknownSubscriber_Type()
)
failLeResUnknownSubscriber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResUnknownSubscriber.setStatus("current")
_FailLeResAbsentSubscriber_Type = Integer32
_FailLeResAbsentSubscriber_Object = MibTableColumn
failLeResAbsentSubscriber = _FailLeResAbsentSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 5),
    _FailLeResAbsentSubscriber_Type()
)
failLeResAbsentSubscriber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResAbsentSubscriber.setStatus("current")
_FailLeResPositionMethodFailure_Type = Integer32
_FailLeResPositionMethodFailure_Object = MibTableColumn
failLeResPositionMethodFailure = _FailLeResPositionMethodFailure_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 6),
    _FailLeResPositionMethodFailure_Type()
)
failLeResPositionMethodFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResPositionMethodFailure.setStatus("current")
_FailLeResTimeout_Type = Integer32
_FailLeResTimeout_Object = MibTableColumn
failLeResTimeout = _FailLeResTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 7),
    _FailLeResTimeout_Type()
)
failLeResTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResTimeout.setStatus("current")
_FailLeResCongestion_Type = Integer32
_FailLeResCongestion_Object = MibTableColumn
failLeResCongestion = _FailLeResCongestion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 8),
    _FailLeResCongestion_Type()
)
failLeResCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResCongestion.setStatus("current")
_FailLeResUnsupportedVersion_Type = Integer32
_FailLeResUnsupportedVersion_Object = MibTableColumn
failLeResUnsupportedVersion = _FailLeResUnsupportedVersion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 9),
    _FailLeResUnsupportedVersion_Type()
)
failLeResUnsupportedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResUnsupportedVersion.setStatus("current")
_FailLeResTooManyPositionItems_Type = Integer32
_FailLeResTooManyPositionItems_Object = MibTableColumn
failLeResTooManyPositionItems = _FailLeResTooManyPositionItems_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 10),
    _FailLeResTooManyPositionItems_Type()
)
failLeResTooManyPositionItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResTooManyPositionItems.setStatus("current")
_FailLeResFormatError_Type = Integer32
_FailLeResFormatError_Object = MibTableColumn
failLeResFormatError = _FailLeResFormatError_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 11),
    _FailLeResFormatError_Type()
)
failLeResFormatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResFormatError.setStatus("current")
_FailLeResSyntaxError_Type = Integer32
_FailLeResSyntaxError_Object = MibTableColumn
failLeResSyntaxError = _FailLeResSyntaxError_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 12),
    _FailLeResSyntaxError_Type()
)
failLeResSyntaxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResSyntaxError.setStatus("current")
_FailLeResElementNotSupported_Type = Integer32
_FailLeResElementNotSupported_Object = MibTableColumn
failLeResElementNotSupported = _FailLeResElementNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 13),
    _FailLeResElementNotSupported_Type()
)
failLeResElementNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResElementNotSupported.setStatus("current")
_FailLeResServiceNotSupported_Type = Integer32
_FailLeResServiceNotSupported_Object = MibTableColumn
failLeResServiceNotSupported = _FailLeResServiceNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 14),
    _FailLeResServiceNotSupported_Type()
)
failLeResServiceNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResServiceNotSupported.setStatus("current")
_FailLeResElementAttributeNotSupported_Type = Integer32
_FailLeResElementAttributeNotSupported_Object = MibTableColumn
failLeResElementAttributeNotSupported = _FailLeResElementAttributeNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 15),
    _FailLeResElementAttributeNotSupported_Type()
)
failLeResElementAttributeNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResElementAttributeNotSupported.setStatus("current")
_FailLeResInvalidElementValue_Type = Integer32
_FailLeResInvalidElementValue_Object = MibTableColumn
failLeResInvalidElementValue = _FailLeResInvalidElementValue_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 16),
    _FailLeResInvalidElementValue_Type()
)
failLeResInvalidElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResInvalidElementValue.setStatus("current")
_FailLeResInvalidElementAttributeValue_Type = Integer32
_FailLeResInvalidElementAttributeValue_Object = MibTableColumn
failLeResInvalidElementAttributeValue = _FailLeResInvalidElementAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 17),
    _FailLeResInvalidElementAttributeValue_Type()
)
failLeResInvalidElementAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResInvalidElementAttributeValue.setStatus("current")
_FailLeResElementValueNotSupported_Type = Integer32
_FailLeResElementValueNotSupported_Object = MibTableColumn
failLeResElementValueNotSupported = _FailLeResElementValueNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 18),
    _FailLeResElementValueNotSupported_Type()
)
failLeResElementValueNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResElementValueNotSupported.setStatus("current")
_FailLeResElementAttributeValueNotSupported_Type = Integer32
_FailLeResElementAttributeValueNotSupported_Object = MibTableColumn
failLeResElementAttributeValueNotSupported = _FailLeResElementAttributeValueNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 19),
    _FailLeResElementAttributeValueNotSupported_Type()
)
failLeResElementAttributeValueNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResElementAttributeValueNotSupported.setStatus("current")
_FailLeResQoPNotAttainable_Type = Integer32
_FailLeResQoPNotAttainable_Object = MibTableColumn
failLeResQoPNotAttainable = _FailLeResQoPNotAttainable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 21),
    _FailLeResQoPNotAttainable_Type()
)
failLeResQoPNotAttainable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResQoPNotAttainable.setStatus("current")
_FailLeResPositioningNotAllowed_Type = Integer32
_FailLeResPositioningNotAllowed_Object = MibTableColumn
failLeResPositioningNotAllowed = _FailLeResPositioningNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 22),
    _FailLeResPositioningNotAllowed_Type()
)
failLeResPositioningNotAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResPositioningNotAllowed.setStatus("current")
_FailLeResCongestioninMobileNetwork_Type = Integer32
_FailLeResCongestioninMobileNetwork_Object = MibTableColumn
failLeResCongestioninMobileNetwork = _FailLeResCongestioninMobileNetwork_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 23),
    _FailLeResCongestioninMobileNetwork_Type()
)
failLeResCongestioninMobileNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResCongestioninMobileNetwork.setStatus("current")
_FailLeResDisallowedByLocalRegulations_Type = Integer32
_FailLeResDisallowedByLocalRegulations_Object = MibTableColumn
failLeResDisallowedByLocalRegulations = _FailLeResDisallowedByLocalRegulations_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 24),
    _FailLeResDisallowedByLocalRegulations_Type()
)
failLeResDisallowedByLocalRegulations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResDisallowedByLocalRegulations.setStatus("current")
_FailLeResMisconfigurationOfLocationServer_Type = Integer32
_FailLeResMisconfigurationOfLocationServer_Object = MibTableColumn
failLeResMisconfigurationOfLocationServer = _FailLeResMisconfigurationOfLocationServer_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 25),
    _FailLeResMisconfigurationOfLocationServer_Type()
)
failLeResMisconfigurationOfLocationServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResMisconfigurationOfLocationServer.setStatus("current")
_FailLeResErrorCodeStartTime_Type = DateAndTime
_FailLeResErrorCodeStartTime_Object = MibTableColumn
failLeResErrorCodeStartTime = _FailLeResErrorCodeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 45),
    _FailLeResErrorCodeStartTime_Type()
)
failLeResErrorCodeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResErrorCodeStartTime.setStatus("current")
_FailLeResErrorCodeEndTime_Type = DateAndTime
_FailLeResErrorCodeEndTime_Object = MibTableColumn
failLeResErrorCodeEndTime = _FailLeResErrorCodeEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 46),
    _FailLeResErrorCodeEndTime_Type()
)
failLeResErrorCodeEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResErrorCodeEndTime.setStatus("current")
_FailLeResErrorCodeRowIndex_Type = Integer32
_FailLeResErrorCodeRowIndex_Object = MibTableColumn
failLeResErrorCodeRowIndex = _FailLeResErrorCodeRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 7, 1, 47),
    _FailLeResErrorCodeRowIndex_Type()
)
failLeResErrorCodeRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLeResErrorCodeRowIndex.setStatus("current")
_AppLocStatsTable_Object = MibTable
appLocStatsTable = _AppLocStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8)
)
if mibBuilder.loadTexts:
    appLocStatsTable.setStatus("current")
_AppLocStatsEntry_Object = MibTableRow
appLocStatsEntry = _AppLocStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1)
)
appLocStatsEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocStatsRowIndex"),
)
if mibBuilder.loadTexts:
    appLocStatsEntry.setStatus("current")
_MlpClientAuthCount_Type = Integer32
_MlpClientAuthCount_Object = MibTableColumn
mlpClientAuthCount = _MlpClientAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 1),
    _MlpClientAuthCount_Type()
)
mlpClientAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpClientAuthCount.setStatus("current")
_MlpClientAuthFailCount_Type = Integer32
_MlpClientAuthFailCount_Object = MibTableColumn
mlpClientAuthFailCount = _MlpClientAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 2),
    _MlpClientAuthFailCount_Type()
)
mlpClientAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpClientAuthFailCount.setStatus("current")
_MlpClientAuthFailRate_Type = Integer32
_MlpClientAuthFailRate_Object = MibTableColumn
mlpClientAuthFailRate = _MlpClientAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 3),
    _MlpClientAuthFailRate_Type()
)
mlpClientAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlpClientAuthFailRate.setStatus("current")
_DeviceCertAuthCount_Type = Integer32
_DeviceCertAuthCount_Object = MibTableColumn
deviceCertAuthCount = _DeviceCertAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 4),
    _DeviceCertAuthCount_Type()
)
deviceCertAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCertAuthCount.setStatus("current")
_DeviceCertAuthFailCount_Type = Integer32
_DeviceCertAuthFailCount_Object = MibTableColumn
deviceCertAuthFailCount = _DeviceCertAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 5),
    _DeviceCertAuthFailCount_Type()
)
deviceCertAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCertAuthFailCount.setStatus("current")
_DeviceCertAuthFailRate_Type = Integer32
_DeviceCertAuthFailRate_Object = MibTableColumn
deviceCertAuthFailRate = _DeviceCertAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 6),
    _DeviceCertAuthFailRate_Type()
)
deviceCertAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCertAuthFailRate.setStatus("current")
_DeviceACACount_Type = Integer32
_DeviceACACount_Object = MibTableColumn
deviceACACount = _DeviceACACount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 7),
    _DeviceACACount_Type()
)
deviceACACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceACACount.setStatus("current")
_DeviceACAFailCount_Type = Integer32
_DeviceACAFailCount_Object = MibTableColumn
deviceACAFailCount = _DeviceACAFailCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 8),
    _DeviceACAFailCount_Type()
)
deviceACAFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceACAFailCount.setStatus("current")
_DeviceACAFailRate_Type = Integer32
_DeviceACAFailRate_Object = MibTableColumn
deviceACAFailRate = _DeviceACAFailRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 9),
    _DeviceACAFailRate_Type()
)
deviceACAFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceACAFailRate.setStatus("current")
_SuplInitAuthCount_Type = Integer32
_SuplInitAuthCount_Object = MibTableColumn
suplInitAuthCount = _SuplInitAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 10),
    _SuplInitAuthCount_Type()
)
suplInitAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suplInitAuthCount.setStatus("current")
_SuplInitAuthFailCount_Type = Integer32
_SuplInitAuthFailCount_Object = MibTableColumn
suplInitAuthFailCount = _SuplInitAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 11),
    _SuplInitAuthFailCount_Type()
)
suplInitAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suplInitAuthFailCount.setStatus("current")
_SuplInitAuthFailRate_Type = Integer32
_SuplInitAuthFailRate_Object = MibTableColumn
suplInitAuthFailRate = _SuplInitAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 12),
    _SuplInitAuthFailRate_Type()
)
suplInitAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suplInitAuthFailRate.setStatus("current")
_DeviceAuthCount_Type = Integer32
_DeviceAuthCount_Object = MibTableColumn
deviceAuthCount = _DeviceAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 13),
    _DeviceAuthCount_Type()
)
deviceAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAuthCount.setStatus("current")
_DeviceAuthFailCount_Type = Integer32
_DeviceAuthFailCount_Object = MibTableColumn
deviceAuthFailCount = _DeviceAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 14),
    _DeviceAuthFailCount_Type()
)
deviceAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAuthFailCount.setStatus("current")
_DeviceAuthFailRate_Type = Integer32
_DeviceAuthFailRate_Object = MibTableColumn
deviceAuthFailRate = _DeviceAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 15),
    _DeviceAuthFailRate_Type()
)
deviceAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAuthFailRate.setStatus("current")
_SuplUERespTimeout_Type = Integer32
_SuplUERespTimeout_Object = MibTableColumn
suplUERespTimeout = _SuplUERespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 16),
    _SuplUERespTimeout_Type()
)
suplUERespTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suplUERespTimeout.setStatus("current")
_SuplUEConnError_Type = Integer32
_SuplUEConnError_Object = MibTableColumn
suplUEConnError = _SuplUEConnError_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 17),
    _SuplUEConnError_Type()
)
suplUEConnError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suplUEConnError.setStatus("current")
_AppLocStatsStartTime_Type = DateAndTime
_AppLocStatsStartTime_Object = MibTableColumn
appLocStatsStartTime = _AppLocStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 18),
    _AppLocStatsStartTime_Type()
)
appLocStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocStatsStartTime.setStatus("current")
_AppLocStatsEndTime_Type = DateAndTime
_AppLocStatsEndTime_Object = MibTableColumn
appLocStatsEndTime = _AppLocStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 19),
    _AppLocStatsEndTime_Type()
)
appLocStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocStatsEndTime.setStatus("current")
_AppLocStatsRowIndex_Type = Integer32
_AppLocStatsRowIndex_Object = MibTableColumn
appLocStatsRowIndex = _AppLocStatsRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 8, 1, 20),
    _AppLocStatsRowIndex_Type()
)
appLocStatsRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocStatsRowIndex.setStatus("current")
_AppLocBSAStatsTable_Object = MibTable
appLocBSAStatsTable = _AppLocBSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9)
)
if mibBuilder.loadTexts:
    appLocBSAStatsTable.setStatus("current")
_AppLocBSAStatsEntry_Object = MibTableRow
appLocBSAStatsEntry = _AppLocBSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1)
)
appLocBSAStatsEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocBSAStatsRowIndex"),
)
if mibBuilder.loadTexts:
    appLocBSAStatsEntry.setStatus("current")
_BsaNumBySOAP_Type = Integer32
_BsaNumBySOAP_Object = MibTableColumn
bsaNumBySOAP = _BsaNumBySOAP_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 1),
    _BsaNumBySOAP_Type()
)
bsaNumBySOAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumBySOAP.setStatus("current")
_BsaNumRejectBySOAP_Type = Integer32
_BsaNumRejectBySOAP_Object = MibTableColumn
bsaNumRejectBySOAP = _BsaNumRejectBySOAP_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 2),
    _BsaNumRejectBySOAP_Type()
)
bsaNumRejectBySOAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumRejectBySOAP.setStatus("current")
_BsaErrorNumBySOAP_Type = Integer32
_BsaErrorNumBySOAP_Object = MibTableColumn
bsaErrorNumBySOAP = _BsaErrorNumBySOAP_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 3),
    _BsaErrorNumBySOAP_Type()
)
bsaErrorNumBySOAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaErrorNumBySOAP.setStatus("current")
_BsaNumByBULK_Type = Integer32
_BsaNumByBULK_Object = MibTableColumn
bsaNumByBULK = _BsaNumByBULK_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 4),
    _BsaNumByBULK_Type()
)
bsaNumByBULK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumByBULK.setStatus("current")
_BsaNumRejectByBULK_Type = Integer32
_BsaNumRejectByBULK_Object = MibTableColumn
bsaNumRejectByBULK = _BsaNumRejectByBULK_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 5),
    _BsaNumRejectByBULK_Type()
)
bsaNumRejectByBULK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumRejectByBULK.setStatus("current")
_BsaErrorNumByBULK_Type = Integer32
_BsaErrorNumByBULK_Object = MibTableColumn
bsaErrorNumByBULK = _BsaErrorNumByBULK_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 6),
    _BsaErrorNumByBULK_Type()
)
bsaErrorNumByBULK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaErrorNumByBULK.setStatus("current")
_BsaNumByPDM_Type = Integer32
_BsaNumByPDM_Object = MibTableColumn
bsaNumByPDM = _BsaNumByPDM_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 7),
    _BsaNumByPDM_Type()
)
bsaNumByPDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumByPDM.setStatus("current")
_BsaNumRejectByPDM_Type = Integer32
_BsaNumRejectByPDM_Object = MibTableColumn
bsaNumRejectByPDM = _BsaNumRejectByPDM_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 8),
    _BsaNumRejectByPDM_Type()
)
bsaNumRejectByPDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsaNumRejectByPDM.setStatus("current")
_UnknownCellErrorNum_Type = Integer32
_UnknownCellErrorNum_Object = MibTableColumn
unknownCellErrorNum = _UnknownCellErrorNum_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 9),
    _UnknownCellErrorNum_Type()
)
unknownCellErrorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownCellErrorNum.setStatus("current")
_AppLocBSAStatsStartTime_Type = DateAndTime
_AppLocBSAStatsStartTime_Object = MibTableColumn
appLocBSAStatsStartTime = _AppLocBSAStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 10),
    _AppLocBSAStatsStartTime_Type()
)
appLocBSAStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocBSAStatsStartTime.setStatus("current")
_AppLocBSAStatsEndTime_Type = DateAndTime
_AppLocBSAStatsEndTime_Object = MibTableColumn
appLocBSAStatsEndTime = _AppLocBSAStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 11),
    _AppLocBSAStatsEndTime_Type()
)
appLocBSAStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocBSAStatsEndTime.setStatus("current")
_AppLocBSAStatsRowIndex_Type = Integer32
_AppLocBSAStatsRowIndex_Object = MibTableColumn
appLocBSAStatsRowIndex = _AppLocBSAStatsRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 9, 1, 12),
    _AppLocBSAStatsRowIndex_Type()
)
appLocBSAStatsRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocBSAStatsRowIndex.setStatus("current")
_AppLocSystemInfoTable_Object = MibTable
appLocSystemInfoTable = _AppLocSystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10)
)
if mibBuilder.loadTexts:
    appLocSystemInfoTable.setStatus("current")
_AppLocSystemInfoEntry_Object = MibTableRow
appLocSystemInfoEntry = _AppLocSystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1)
)
appLocSystemInfoEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocSystemInfoRowIndex"),
)
if mibBuilder.loadTexts:
    appLocSystemInfoEntry.setStatus("current")
_AsmDataDiskUsage_Type = Integer32
_AsmDataDiskUsage_Object = MibTableColumn
asmDataDiskUsage = _AsmDataDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 1),
    _AsmDataDiskUsage_Type()
)
asmDataDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmDataDiskUsage.setStatus("current")
_AsmFraDiskUsage_Type = Integer32
_AsmFraDiskUsage_Object = MibTableColumn
asmFraDiskUsage = _AsmFraDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 2),
    _AsmFraDiskUsage_Type()
)
asmFraDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmFraDiskUsage.setStatus("current")
_TlrDiskUsage_Type = Integer32
_TlrDiskUsage_Object = MibTableColumn
tlrDiskUsage = _TlrDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 3),
    _TlrDiskUsage_Type()
)
tlrDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlrDiskUsage.setStatus("current")
_BillDiskUsage_Type = Integer32
_BillDiskUsage_Object = MibTableColumn
billDiskUsage = _BillDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 4),
    _BillDiskUsage_Type()
)
billDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billDiskUsage.setStatus("current")
_LogDiskUsage_Type = Integer32
_LogDiskUsage_Object = MibTableColumn
logDiskUsage = _LogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 5),
    _LogDiskUsage_Type()
)
logDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDiskUsage.setStatus("current")
_AppLocSystemInfoStartTime_Type = DateAndTime
_AppLocSystemInfoStartTime_Object = MibTableColumn
appLocSystemInfoStartTime = _AppLocSystemInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 6),
    _AppLocSystemInfoStartTime_Type()
)
appLocSystemInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSystemInfoStartTime.setStatus("current")
_AppLocSystemInfoEndTime_Type = DateAndTime
_AppLocSystemInfoEndTime_Object = MibTableColumn
appLocSystemInfoEndTime = _AppLocSystemInfoEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 7),
    _AppLocSystemInfoEndTime_Type()
)
appLocSystemInfoEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSystemInfoEndTime.setStatus("current")
_AppLocSystemInfoRowIndex_Type = Integer32
_AppLocSystemInfoRowIndex_Object = MibTableColumn
appLocSystemInfoRowIndex = _AppLocSystemInfoRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 10, 1, 8),
    _AppLocSystemInfoRowIndex_Type()
)
appLocSystemInfoRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSystemInfoRowIndex.setStatus("current")
_AppLocHostInfoTable_Object = MibTable
appLocHostInfoTable = _AppLocHostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11)
)
if mibBuilder.loadTexts:
    appLocHostInfoTable.setStatus("current")
_AppLocHostInfoEntry_Object = MibTableRow
appLocHostInfoEntry = _AppLocHostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1)
)
appLocHostInfoEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocHostInfoRowIndex"),
)
if mibBuilder.loadTexts:
    appLocHostInfoEntry.setStatus("current")
_BladeID_Type = Integer32
_BladeID_Object = MibTableColumn
bladeID = _BladeID_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 1),
    _BladeID_Type()
)
bladeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeID.setStatus("current")
_AverCpuUsage_Type = Integer32
_AverCpuUsage_Object = MibTableColumn
averCpuUsage = _AverCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 2),
    _AverCpuUsage_Type()
)
averCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averCpuUsage.setStatus("current")
_AverMemUsage_Type = Integer32
_AverMemUsage_Object = MibTableColumn
averMemUsage = _AverMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 3),
    _AverMemUsage_Type()
)
averMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averMemUsage.setStatus("current")
_AverSwapUsage_Type = Integer32
_AverSwapUsage_Object = MibTableColumn
averSwapUsage = _AverSwapUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 4),
    _AverSwapUsage_Type()
)
averSwapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averSwapUsage.setStatus("current")
_AverDiskUsage_Type = Integer32
_AverDiskUsage_Object = MibTableColumn
averDiskUsage = _AverDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 5),
    _AverDiskUsage_Type()
)
averDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averDiskUsage.setStatus("current")
_AppLocHostInfoStartTime_Type = DateAndTime
_AppLocHostInfoStartTime_Object = MibTableColumn
appLocHostInfoStartTime = _AppLocHostInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 6),
    _AppLocHostInfoStartTime_Type()
)
appLocHostInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocHostInfoStartTime.setStatus("current")
_AppLocHostInfoEndTime_Type = DateAndTime
_AppLocHostInfoEndTime_Object = MibTableColumn
appLocHostInfoEndTime = _AppLocHostInfoEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 7),
    _AppLocHostInfoEndTime_Type()
)
appLocHostInfoEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocHostInfoEndTime.setStatus("current")
_AppLocHostInfoRowIndex_Type = Integer32
_AppLocHostInfoRowIndex_Object = MibTableColumn
appLocHostInfoRowIndex = _AppLocHostInfoRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 11, 1, 8),
    _AppLocHostInfoRowIndex_Type()
)
appLocHostInfoRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocHostInfoRowIndex.setStatus("current")
_AppFailPerSidTable_Object = MibTable
appFailPerSidTable = _AppFailPerSidTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12)
)
if mibBuilder.loadTexts:
    appFailPerSidTable.setStatus("current")
_AppFailPerSidEntry_Object = MibTableRow
appFailPerSidEntry = _AppFailPerSidEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1)
)
appFailPerSidEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appFailPerSidRowIndex"),
)
if mibBuilder.loadTexts:
    appFailPerSidEntry.setStatus("current")
_SidNid_Type = OctetString
_SidNid_Object = MibTableColumn
sidNid = _SidNid_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1, 1),
    _SidNid_Type()
)
sidNid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sidNid.setStatus("current")
_FailNumPerSidNid_Type = Integer32
_FailNumPerSidNid_Object = MibTableColumn
failNumPerSidNid = _FailNumPerSidNid_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1, 2),
    _FailNumPerSidNid_Type()
)
failNumPerSidNid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failNumPerSidNid.setStatus("current")
_AppFailPerSidStartTime_Type = DateAndTime
_AppFailPerSidStartTime_Object = MibTableColumn
appFailPerSidStartTime = _AppFailPerSidStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1, 3),
    _AppFailPerSidStartTime_Type()
)
appFailPerSidStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerSidStartTime.setStatus("current")
_AppFailPerSidEndTime_Type = DateAndTime
_AppFailPerSidEndTime_Object = MibTableColumn
appFailPerSidEndTime = _AppFailPerSidEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1, 4),
    _AppFailPerSidEndTime_Type()
)
appFailPerSidEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerSidEndTime.setStatus("current")
_AppFailPerSidRowIndex_Type = Integer32
_AppFailPerSidRowIndex_Object = MibTableColumn
appFailPerSidRowIndex = _AppFailPerSidRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 12, 1, 5),
    _AppFailPerSidRowIndex_Type()
)
appFailPerSidRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerSidRowIndex.setStatus("current")
_AppFailPerMccTable_Object = MibTable
appFailPerMccTable = _AppFailPerMccTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13)
)
if mibBuilder.loadTexts:
    appFailPerMccTable.setStatus("current")
_AppFailPerMccEntry_Object = MibTableRow
appFailPerMccEntry = _AppFailPerMccEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1)
)
appFailPerMccEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appFailPerMccRowIndex"),
)
if mibBuilder.loadTexts:
    appFailPerMccEntry.setStatus("current")
_MccMncTac_Type = OctetString
_MccMncTac_Object = MibTableColumn
mccMncTac = _MccMncTac_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1, 1),
    _MccMncTac_Type()
)
mccMncTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccMncTac.setStatus("current")
_FailNumPerMccMncTac_Type = Integer32
_FailNumPerMccMncTac_Object = MibTableColumn
failNumPerMccMncTac = _FailNumPerMccMncTac_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1, 2),
    _FailNumPerMccMncTac_Type()
)
failNumPerMccMncTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failNumPerMccMncTac.setStatus("current")
_AppFailPerMccStartTime_Type = DateAndTime
_AppFailPerMccStartTime_Object = MibTableColumn
appFailPerMccStartTime = _AppFailPerMccStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1, 3),
    _AppFailPerMccStartTime_Type()
)
appFailPerMccStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerMccStartTime.setStatus("current")
_AppFailPerMccEndTime_Type = DateAndTime
_AppFailPerMccEndTime_Object = MibTableColumn
appFailPerMccEndTime = _AppFailPerMccEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1, 4),
    _AppFailPerMccEndTime_Type()
)
appFailPerMccEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerMccEndTime.setStatus("current")
_AppFailPerMccRowIndex_Type = Integer32
_AppFailPerMccRowIndex_Object = MibTableColumn
appFailPerMccRowIndex = _AppFailPerMccRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 13, 1, 5),
    _AppFailPerMccRowIndex_Type()
)
appFailPerMccRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appFailPerMccRowIndex.setStatus("current")
_AppLocMethodTable_Object = MibTable
appLocMethodTable = _AppLocMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14)
)
if mibBuilder.loadTexts:
    appLocMethodTable.setStatus("current")
_AppLocMethodEntry_Object = MibTableRow
appLocMethodEntry = _AppLocMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1)
)
appLocMethodEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocMethodRowIndex"),
)
if mibBuilder.loadTexts:
    appLocMethodEntry.setStatus("current")
_AppMethodMSBIS801AGPS_Type = Integer32
_AppMethodMSBIS801AGPS_Object = MibTableColumn
appMethodMSBIS801AGPS = _AppMethodMSBIS801AGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 1),
    _AppMethodMSBIS801AGPS_Type()
)
appMethodMSBIS801AGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSBIS801AGPS.setStatus("current")
_AppMethodMSBRRLPAGPS_Type = Integer32
_AppMethodMSBRRLPAGPS_Object = MibTableColumn
appMethodMSBRRLPAGPS = _AppMethodMSBRRLPAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 2),
    _AppMethodMSBRRLPAGPS_Type()
)
appMethodMSBRRLPAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSBRRLPAGPS.setStatus("current")
_AppMethodMSBLPPAGPS_Type = Integer32
_AppMethodMSBLPPAGPS_Object = MibTableColumn
appMethodMSBLPPAGPS = _AppMethodMSBLPPAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 3),
    _AppMethodMSBLPPAGPS_Type()
)
appMethodMSBLPPAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSBLPPAGPS.setStatus("current")
_AppMethodMSAIS801AGPS_Type = Integer32
_AppMethodMSAIS801AGPS_Object = MibTableColumn
appMethodMSAIS801AGPS = _AppMethodMSAIS801AGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 4),
    _AppMethodMSAIS801AGPS_Type()
)
appMethodMSAIS801AGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAIS801AGPS.setStatus("current")
_AppMethodMSAIS801HYBRIDAGPS_Type = Integer32
_AppMethodMSAIS801HYBRIDAGPS_Object = MibTableColumn
appMethodMSAIS801HYBRIDAGPS = _AppMethodMSAIS801HYBRIDAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 5),
    _AppMethodMSAIS801HYBRIDAGPS_Type()
)
appMethodMSAIS801HYBRIDAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAIS801HYBRIDAGPS.setStatus("current")
_AppMethodMSAIS801HYBRIDECI_Type = Integer32
_AppMethodMSAIS801HYBRIDECI_Object = MibTableColumn
appMethodMSAIS801HYBRIDECI = _AppMethodMSAIS801HYBRIDECI_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 6),
    _AppMethodMSAIS801HYBRIDECI_Type()
)
appMethodMSAIS801HYBRIDECI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAIS801HYBRIDECI.setStatus("current")
_AppMethodMSAIS801HYBRIDAFLT_Type = Integer32
_AppMethodMSAIS801HYBRIDAFLT_Object = MibTableColumn
appMethodMSAIS801HYBRIDAFLT = _AppMethodMSAIS801HYBRIDAFLT_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 7),
    _AppMethodMSAIS801HYBRIDAFLT_Type()
)
appMethodMSAIS801HYBRIDAFLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAIS801HYBRIDAFLT.setStatus("current")
_AppMethodMSAIS801AFLT_Type = Integer32
_AppMethodMSAIS801AFLT_Object = MibTableColumn
appMethodMSAIS801AFLT = _AppMethodMSAIS801AFLT_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 8),
    _AppMethodMSAIS801AFLT_Type()
)
appMethodMSAIS801AFLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAIS801AFLT.setStatus("current")
_AppMethodMSARRLPAGPS_Type = Integer32
_AppMethodMSARRLPAGPS_Object = MibTableColumn
appMethodMSARRLPAGPS = _AppMethodMSARRLPAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 9),
    _AppMethodMSARRLPAGPS_Type()
)
appMethodMSARRLPAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSARRLPAGPS.setStatus("current")
_AppMethodMSALPPAGPS_Type = Integer32
_AppMethodMSALPPAGPS_Object = MibTableColumn
appMethodMSALPPAGPS = _AppMethodMSALPPAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 10),
    _AppMethodMSALPPAGPS_Type()
)
appMethodMSALPPAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPAGPS.setStatus("current")
_AppMethodMSALPPOTDOA_Type = Integer32
_AppMethodMSALPPOTDOA_Object = MibTableColumn
appMethodMSALPPOTDOA = _AppMethodMSALPPOTDOA_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 11),
    _AppMethodMSALPPOTDOA_Type()
)
appMethodMSALPPOTDOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPOTDOA.setStatus("current")
_AppMethodMSALPPHYBRIDAGPS_Type = Integer32
_AppMethodMSALPPHYBRIDAGPS_Object = MibTableColumn
appMethodMSALPPHYBRIDAGPS = _AppMethodMSALPPHYBRIDAGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 12),
    _AppMethodMSALPPHYBRIDAGPS_Type()
)
appMethodMSALPPHYBRIDAGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPHYBRIDAGPS.setStatus("current")
_AppMethodMSALPPHYBRIDECI_Type = Integer32
_AppMethodMSALPPHYBRIDECI_Object = MibTableColumn
appMethodMSALPPHYBRIDECI = _AppMethodMSALPPHYBRIDECI_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 13),
    _AppMethodMSALPPHYBRIDECI_Type()
)
appMethodMSALPPHYBRIDECI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPHYBRIDECI.setStatus("current")
_AppMethodMSALPPHYBRIDOTDOA_Type = Integer32
_AppMethodMSALPPHYBRIDOTDOA_Object = MibTableColumn
appMethodMSALPPHYBRIDOTDOA = _AppMethodMSALPPHYBRIDOTDOA_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 14),
    _AppMethodMSALPPHYBRIDOTDOA_Type()
)
appMethodMSALPPHYBRIDOTDOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPHYBRIDOTDOA.setStatus("current")
_AppMethodMSALPPHYBRIDHYBRID_Type = Integer32
_AppMethodMSALPPHYBRIDHYBRID_Object = MibTableColumn
appMethodMSALPPHYBRIDHYBRID = _AppMethodMSALPPHYBRIDHYBRID_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 15),
    _AppMethodMSALPPHYBRIDHYBRID_Type()
)
appMethodMSALPPHYBRIDHYBRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPHYBRIDHYBRID.setStatus("current")
_AppMethodMSAECI_Type = Integer32
_AppMethodMSAECI_Object = MibTableColumn
appMethodMSAECI = _AppMethodMSAECI_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 16),
    _AppMethodMSAECI_Type()
)
appMethodMSAECI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSAECI.setStatus("current")
_AppMethodIS801HYBRIDHYBRID_Type = Integer32
_AppMethodIS801HYBRIDHYBRID_Object = MibTableColumn
appMethodIS801HYBRIDHYBRID = _AppMethodIS801HYBRIDHYBRID_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 17),
    _AppMethodIS801HYBRIDHYBRID_Type()
)
appMethodIS801HYBRIDHYBRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodIS801HYBRIDHYBRID.setStatus("current")
_AppMethodULPLPPAUTOGPS_Type = Integer32
_AppMethodULPLPPAUTOGPS_Object = MibTableColumn
appMethodULPLPPAUTOGPS = _AppMethodULPLPPAUTOGPS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 18),
    _AppMethodULPLPPAUTOGPS_Type()
)
appMethodULPLPPAUTOGPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodULPLPPAUTOGPS.setStatus("current")
_AppMethodMSBRRLPAGNSS_Type = Integer32
_AppMethodMSBRRLPAGNSS_Object = MibTableColumn
appMethodMSBRRLPAGNSS = _AppMethodMSBRRLPAGNSS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 19),
    _AppMethodMSBRRLPAGNSS_Type()
)
appMethodMSBRRLPAGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSBRRLPAGNSS.setStatus("current")
_AppMethodMSBLPPAGNSS_Type = Integer32
_AppMethodMSBLPPAGNSS_Object = MibTableColumn
appMethodMSBLPPAGNSS = _AppMethodMSBLPPAGNSS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 20),
    _AppMethodMSBLPPAGNSS_Type()
)
appMethodMSBLPPAGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSBLPPAGNSS.setStatus("current")
_AppMethodMSARRLPAGNSS_Type = Integer32
_AppMethodMSARRLPAGNSS_Object = MibTableColumn
appMethodMSARRLPAGNSS = _AppMethodMSARRLPAGNSS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 21),
    _AppMethodMSARRLPAGNSS_Type()
)
appMethodMSARRLPAGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSARRLPAGNSS.setStatus("current")
_AppMethodMSALPPAGNSS_Type = Integer32
_AppMethodMSALPPAGNSS_Object = MibTableColumn
appMethodMSALPPAGNSS = _AppMethodMSALPPAGNSS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 22),
    _AppMethodMSALPPAGNSS_Type()
)
appMethodMSALPPAGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPAGNSS.setStatus("current")
_AppMethodMSALPPHYBRIDAGNSS_Type = Integer32
_AppMethodMSALPPHYBRIDAGNSS_Object = MibTableColumn
appMethodMSALPPHYBRIDAGNSS = _AppMethodMSALPPHYBRIDAGNSS_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 23),
    _AppMethodMSALPPHYBRIDAGNSS_Type()
)
appMethodMSALPPHYBRIDAGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appMethodMSALPPHYBRIDAGNSS.setStatus("current")
_AppLocMethodStartTime_Type = DateAndTime
_AppLocMethodStartTime_Object = MibTableColumn
appLocMethodStartTime = _AppLocMethodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 24),
    _AppLocMethodStartTime_Type()
)
appLocMethodStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocMethodStartTime.setStatus("current")
_AppLocMethodEndTime_Type = DateAndTime
_AppLocMethodEndTime_Object = MibTableColumn
appLocMethodEndTime = _AppLocMethodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 25),
    _AppLocMethodEndTime_Type()
)
appLocMethodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocMethodEndTime.setStatus("current")
_AppLocMethodRowIndex_Type = Integer32
_AppLocMethodRowIndex_Object = MibTableColumn
appLocMethodRowIndex = _AppLocMethodRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 14, 1, 26),
    _AppLocMethodRowIndex_Type()
)
appLocMethodRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocMethodRowIndex.setStatus("current")
_AppLocSlsIFTable_Object = MibTable
appLocSlsIFTable = _AppLocSlsIFTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15)
)
if mibBuilder.loadTexts:
    appLocSlsIFTable.setStatus("current")
_AppLocSlsIFEntry_Object = MibTableRow
appLocSlsIFEntry = _AppLocSlsIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1)
)
appLocSlsIFEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocSlsIFRowIndex"),
)
if mibBuilder.loadTexts:
    appLocSlsIFEntry.setStatus("current")
_AppLocSlsIFReq_Type = Integer32
_AppLocSlsIFReq_Object = MibTableColumn
appLocSlsIFReq = _AppLocSlsIFReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 1),
    _AppLocSlsIFReq_Type()
)
appLocSlsIFReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlsIFReq.setStatus("current")
_AppValidSlsReq_Type = Integer32
_AppValidSlsReq_Object = MibTableColumn
appValidSlsReq = _AppValidSlsReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 2),
    _AppValidSlsReq_Type()
)
appValidSlsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appValidSlsReq.setStatus("current")
_AppSuccSlsRes_Type = Integer32
_AppSuccSlsRes_Object = MibTableColumn
appSuccSlsRes = _AppSuccSlsRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 3),
    _AppSuccSlsRes_Type()
)
appSuccSlsRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccSlsRes.setStatus("current")
_AppSuccSlsResRate_Type = Integer32
_AppSuccSlsResRate_Object = MibTableColumn
appSuccSlsResRate = _AppSuccSlsResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 4),
    _AppSuccSlsResRate_Type()
)
appSuccSlsResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccSlsResRate.setStatus("current")
_AppLocSlsIFStartTime_Type = DateAndTime
_AppLocSlsIFStartTime_Object = MibTableColumn
appLocSlsIFStartTime = _AppLocSlsIFStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 5),
    _AppLocSlsIFStartTime_Type()
)
appLocSlsIFStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlsIFStartTime.setStatus("current")
_AppLocSlsIFEndTime_Type = DateAndTime
_AppLocSlsIFEndTime_Object = MibTableColumn
appLocSlsIFEndTime = _AppLocSlsIFEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 6),
    _AppLocSlsIFEndTime_Type()
)
appLocSlsIFEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlsIFEndTime.setStatus("current")
_AppLocSlsIFRowIndex_Type = Integer32
_AppLocSlsIFRowIndex_Object = MibTableColumn
appLocSlsIFRowIndex = _AppLocSlsIFRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 15, 1, 7),
    _AppLocSlsIFRowIndex_Type()
)
appLocSlsIFRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlsIFRowIndex.setStatus("current")
_AppLocSlgIFTable_Object = MibTable
appLocSlgIFTable = _AppLocSlgIFTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16)
)
if mibBuilder.loadTexts:
    appLocSlgIFTable.setStatus("current")
_AppLocSlgIFEntry_Object = MibTableRow
appLocSlgIFEntry = _AppLocSlgIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1)
)
appLocSlgIFEntry.setIndexNames(
    (0, "VZW-NLS72-MIB", "appLocSlgIFRowIndex"),
)
if mibBuilder.loadTexts:
    appLocSlgIFEntry.setStatus("current")
_AppLocSlgIFReq_Type = Integer32
_AppLocSlgIFReq_Object = MibTableColumn
appLocSlgIFReq = _AppLocSlgIFReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 1),
    _AppLocSlgIFReq_Type()
)
appLocSlgIFReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlgIFReq.setStatus("current")
_AppValidSlgReq_Type = Integer32
_AppValidSlgReq_Object = MibTableColumn
appValidSlgReq = _AppValidSlgReq_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 2),
    _AppValidSlgReq_Type()
)
appValidSlgReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appValidSlgReq.setStatus("current")
_AppSuccSlgRes_Type = Integer32
_AppSuccSlgRes_Object = MibTableColumn
appSuccSlgRes = _AppSuccSlgRes_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 3),
    _AppSuccSlgRes_Type()
)
appSuccSlgRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccSlgRes.setStatus("current")
_AppSuccSlgResRate_Type = Integer32
_AppSuccSlgResRate_Object = MibTableColumn
appSuccSlgResRate = _AppSuccSlgResRate_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 4),
    _AppSuccSlgResRate_Type()
)
appSuccSlgResRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSuccSlgResRate.setStatus("current")
_AppLocSlgIFStartTime_Type = DateAndTime
_AppLocSlgIFStartTime_Object = MibTableColumn
appLocSlgIFStartTime = _AppLocSlgIFStartTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 5),
    _AppLocSlgIFStartTime_Type()
)
appLocSlgIFStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlgIFStartTime.setStatus("current")
_AppLocSlgIFEndTime_Type = DateAndTime
_AppLocSlgIFEndTime_Object = MibTableColumn
appLocSlgIFEndTime = _AppLocSlgIFEndTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 6),
    _AppLocSlgIFEndTime_Type()
)
appLocSlgIFEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlgIFEndTime.setStatus("current")
_AppLocSlgIFRowIndex_Type = Integer32
_AppLocSlgIFRowIndex_Object = MibTableColumn
appLocSlgIFRowIndex = _AppLocSlgIFRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 2, 16, 1, 7),
    _AppLocSlgIFRowIndex_Type()
)
appLocSlgIFRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLocSlgIFRowIndex.setStatus("current")
_AppFM_ObjectIdentity = ObjectIdentity
appFM = _AppFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3)
)

# Managed Objects groups


# Notification objects

lbsCommonAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 1)
)
lbsCommonAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    lbsCommonAlarm.setStatus(
        "current"
    )

omc2ProcessCommunicationErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 2)
)
omc2ProcessCommunicationErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    omc2ProcessCommunicationErrorAlarm.setStatus(
        "current"
    )

process2ProcessCommunicationErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 3)
)
process2ProcessCommunicationErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    process2ProcessCommunicationErrorAlarm.setStatus(
        "current"
    )

processInternalErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 4)
)
processInternalErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    processInternalErrorAlarm.setStatus(
        "current"
    )

process2ExternalInterfaceCommunicationErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 5)
)
process2ExternalInterfaceCommunicationErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    process2ExternalInterfaceCommunicationErrorAlarm.setStatus(
        "current"
    )

systemEnviromentErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 6)
)
systemEnviromentErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    systemEnviromentErrorAlarm.setStatus(
        "current"
    )

pdmErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 40, 3, 3, 7)
)
pdmErrorAlarm.setObjects(
      *(("VZW-NLS72-MIB", "appAlarmSystemName"),
        ("VZW-NLS72-MIB", "appAlarmOriId"),
        ("VZW-NLS72-MIB", "appAlarmNeType"),
        ("VZW-NLS72-MIB", "appAlarmNeName"),
        ("VZW-NLS72-MIB", "appAlarmTitle"),
        ("VZW-NLS72-MIB", "appAlarmTypeID"),
        ("VZW-NLS72-MIB", "appAlarmSeverity"),
        ("VZW-NLS72-MIB", "appAlarmDetail"),
        ("VZW-NLS72-MIB", "appAlarmCounts"),
        ("VZW-NLS72-MIB", "appAlarmCreatetime"))
)
if mibBuilder.loadTexts:
    pdmErrorAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VZW-NLS72-MIB",
    **{"mib-2": mib_2,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysServices": sysServices,
       "nsn": nsn,
       "nsnProducts": nsnProducts,
       "lbs": lbs,
       "common": common,
       "appAlarmTable": appAlarmTable,
       "appAlarmEntry": appAlarmEntry,
       "appAlarmSystemName": appAlarmSystemName,
       "appAlarmOriId": appAlarmOriId,
       "appAlarmNeType": appAlarmNeType,
       "appAlarmNeName": appAlarmNeName,
       "appAlarmTitle": appAlarmTitle,
       "appAlarmTypeID": appAlarmTypeID,
       "appAlarmSeverity": appAlarmSeverity,
       "appAlarmDetail": appAlarmDetail,
       "appAlarmCounts": appAlarmCounts,
       "appAlarmCreatetime": appAlarmCreatetime,
       "appAlarmRowIndex": appAlarmRowIndex,
       "app": app,
       "appPM": appPM,
       "appLocIFTable": appLocIFTable,
       "appLocIFEntry": appLocIFEntry,
       "appLocIFReq": appLocIFReq,
       "appLocIFValidReq": appLocIFValidReq,
       "appLocIFSuccRes": appLocIFSuccRes,
       "appLocIFSuccResRate": appLocIFSuccResRate,
       "appLocIFGrossSuccResRate": appLocIFGrossSuccResRate,
       "appLocIFStartTime": appLocIFStartTime,
       "appLocIFEndTime": appLocIFEndTime,
       "appLocIFRowIndex": appLocIFRowIndex,
       "appLocLeIFTable": appLocLeIFTable,
       "appLocLeIFEntry": appLocLeIFEntry,
       "appLocLeIFReq": appLocLeIFReq,
       "appValidLeReq": appValidLeReq,
       "appSuccLeRes": appSuccLeRes,
       "appSuccLeResRate": appSuccLeResRate,
       "appGrossSuccLeResRate": appGrossSuccLeResRate,
       "appSuccLeQopRes": appSuccLeQopRes,
       "appSuccLeQopResRate": appSuccLeQopResRate,
       "appLoc50LeRes": appLoc50LeRes,
       "appLoc150LeRes": appLoc150LeRes,
       "appSucc50LeResRate": appSucc50LeResRate,
       "appSucc150LeResRate": appSucc150LeResRate,
       "appLocLeIFStartTime": appLocLeIFStartTime,
       "appLocLeIFEndTime": appLocLeIFEndTime,
       "appLocLeIFRowIndex": appLocLeIFRowIndex,
       "appLocFailIFTable": appLocFailIFTable,
       "appLocFailIFEntry": appLocFailIFEntry,
       "appInvalidLeReq": appInvalidLeReq,
       "appFailRes": appFailRes,
       "appFailLeRes": appFailLeRes,
       "appLocFailIFStartTime": appLocFailIFStartTime,
       "appLocFailIFEndTime": appLocFailIFEndTime,
       "appLocFailIFRowIndex": appLocFailIFRowIndex,
       "applocFailTable": applocFailTable,
       "applocFailEntry": applocFailEntry,
       "applocfailbyAuthenticationError": applocfailbyAuthenticationError,
       "applocfailbyBlackList": applocfailbyBlackList,
       "applocfailbyInvalidMobileNumber": applocfailbyInvalidMobileNumber,
       "applocfailstarttime": applocfailstarttime,
       "applocfailendtime": applocfailendtime,
       "applocfailRowIndex": applocfailRowIndex,
       "appFailLeResErrorCodeTable": appFailLeResErrorCodeTable,
       "appFailLeResErrorCodeEntry": appFailLeResErrorCodeEntry,
       "failLeResSystemFailure": failLeResSystemFailure,
       "failLeResUnspecifiedError": failLeResUnspecifiedError,
       "failLeResUnauthorizedApplication": failLeResUnauthorizedApplication,
       "failLeResUnknownSubscriber": failLeResUnknownSubscriber,
       "failLeResAbsentSubscriber": failLeResAbsentSubscriber,
       "failLeResPositionMethodFailure": failLeResPositionMethodFailure,
       "failLeResTimeout": failLeResTimeout,
       "failLeResCongestion": failLeResCongestion,
       "failLeResUnsupportedVersion": failLeResUnsupportedVersion,
       "failLeResTooManyPositionItems": failLeResTooManyPositionItems,
       "failLeResFormatError": failLeResFormatError,
       "failLeResSyntaxError": failLeResSyntaxError,
       "failLeResElementNotSupported": failLeResElementNotSupported,
       "failLeResServiceNotSupported": failLeResServiceNotSupported,
       "failLeResElementAttributeNotSupported": failLeResElementAttributeNotSupported,
       "failLeResInvalidElementValue": failLeResInvalidElementValue,
       "failLeResInvalidElementAttributeValue": failLeResInvalidElementAttributeValue,
       "failLeResElementValueNotSupported": failLeResElementValueNotSupported,
       "failLeResElementAttributeValueNotSupported": failLeResElementAttributeValueNotSupported,
       "failLeResQoPNotAttainable": failLeResQoPNotAttainable,
       "failLeResPositioningNotAllowed": failLeResPositioningNotAllowed,
       "failLeResCongestioninMobileNetwork": failLeResCongestioninMobileNetwork,
       "failLeResDisallowedByLocalRegulations": failLeResDisallowedByLocalRegulations,
       "failLeResMisconfigurationOfLocationServer": failLeResMisconfigurationOfLocationServer,
       "failLeResErrorCodeStartTime": failLeResErrorCodeStartTime,
       "failLeResErrorCodeEndTime": failLeResErrorCodeEndTime,
       "failLeResErrorCodeRowIndex": failLeResErrorCodeRowIndex,
       "appLocStatsTable": appLocStatsTable,
       "appLocStatsEntry": appLocStatsEntry,
       "mlpClientAuthCount": mlpClientAuthCount,
       "mlpClientAuthFailCount": mlpClientAuthFailCount,
       "mlpClientAuthFailRate": mlpClientAuthFailRate,
       "deviceCertAuthCount": deviceCertAuthCount,
       "deviceCertAuthFailCount": deviceCertAuthFailCount,
       "deviceCertAuthFailRate": deviceCertAuthFailRate,
       "deviceACACount": deviceACACount,
       "deviceACAFailCount": deviceACAFailCount,
       "deviceACAFailRate": deviceACAFailRate,
       "suplInitAuthCount": suplInitAuthCount,
       "suplInitAuthFailCount": suplInitAuthFailCount,
       "suplInitAuthFailRate": suplInitAuthFailRate,
       "deviceAuthCount": deviceAuthCount,
       "deviceAuthFailCount": deviceAuthFailCount,
       "deviceAuthFailRate": deviceAuthFailRate,
       "suplUERespTimeout": suplUERespTimeout,
       "suplUEConnError": suplUEConnError,
       "appLocStatsStartTime": appLocStatsStartTime,
       "appLocStatsEndTime": appLocStatsEndTime,
       "appLocStatsRowIndex": appLocStatsRowIndex,
       "appLocBSAStatsTable": appLocBSAStatsTable,
       "appLocBSAStatsEntry": appLocBSAStatsEntry,
       "bsaNumBySOAP": bsaNumBySOAP,
       "bsaNumRejectBySOAP": bsaNumRejectBySOAP,
       "bsaErrorNumBySOAP": bsaErrorNumBySOAP,
       "bsaNumByBULK": bsaNumByBULK,
       "bsaNumRejectByBULK": bsaNumRejectByBULK,
       "bsaErrorNumByBULK": bsaErrorNumByBULK,
       "bsaNumByPDM": bsaNumByPDM,
       "bsaNumRejectByPDM": bsaNumRejectByPDM,
       "unknownCellErrorNum": unknownCellErrorNum,
       "appLocBSAStatsStartTime": appLocBSAStatsStartTime,
       "appLocBSAStatsEndTime": appLocBSAStatsEndTime,
       "appLocBSAStatsRowIndex": appLocBSAStatsRowIndex,
       "appLocSystemInfoTable": appLocSystemInfoTable,
       "appLocSystemInfoEntry": appLocSystemInfoEntry,
       "asmDataDiskUsage": asmDataDiskUsage,
       "asmFraDiskUsage": asmFraDiskUsage,
       "tlrDiskUsage": tlrDiskUsage,
       "billDiskUsage": billDiskUsage,
       "logDiskUsage": logDiskUsage,
       "appLocSystemInfoStartTime": appLocSystemInfoStartTime,
       "appLocSystemInfoEndTime": appLocSystemInfoEndTime,
       "appLocSystemInfoRowIndex": appLocSystemInfoRowIndex,
       "appLocHostInfoTable": appLocHostInfoTable,
       "appLocHostInfoEntry": appLocHostInfoEntry,
       "bladeID": bladeID,
       "averCpuUsage": averCpuUsage,
       "averMemUsage": averMemUsage,
       "averSwapUsage": averSwapUsage,
       "averDiskUsage": averDiskUsage,
       "appLocHostInfoStartTime": appLocHostInfoStartTime,
       "appLocHostInfoEndTime": appLocHostInfoEndTime,
       "appLocHostInfoRowIndex": appLocHostInfoRowIndex,
       "appFailPerSidTable": appFailPerSidTable,
       "appFailPerSidEntry": appFailPerSidEntry,
       "sidNid": sidNid,
       "failNumPerSidNid": failNumPerSidNid,
       "appFailPerSidStartTime": appFailPerSidStartTime,
       "appFailPerSidEndTime": appFailPerSidEndTime,
       "appFailPerSidRowIndex": appFailPerSidRowIndex,
       "appFailPerMccTable": appFailPerMccTable,
       "appFailPerMccEntry": appFailPerMccEntry,
       "mccMncTac": mccMncTac,
       "failNumPerMccMncTac": failNumPerMccMncTac,
       "appFailPerMccStartTime": appFailPerMccStartTime,
       "appFailPerMccEndTime": appFailPerMccEndTime,
       "appFailPerMccRowIndex": appFailPerMccRowIndex,
       "appLocMethodTable": appLocMethodTable,
       "appLocMethodEntry": appLocMethodEntry,
       "appMethodMSBIS801AGPS": appMethodMSBIS801AGPS,
       "appMethodMSBRRLPAGPS": appMethodMSBRRLPAGPS,
       "appMethodMSBLPPAGPS": appMethodMSBLPPAGPS,
       "appMethodMSAIS801AGPS": appMethodMSAIS801AGPS,
       "appMethodMSAIS801HYBRIDAGPS": appMethodMSAIS801HYBRIDAGPS,
       "appMethodMSAIS801HYBRIDECI": appMethodMSAIS801HYBRIDECI,
       "appMethodMSAIS801HYBRIDAFLT": appMethodMSAIS801HYBRIDAFLT,
       "appMethodMSAIS801AFLT": appMethodMSAIS801AFLT,
       "appMethodMSARRLPAGPS": appMethodMSARRLPAGPS,
       "appMethodMSALPPAGPS": appMethodMSALPPAGPS,
       "appMethodMSALPPOTDOA": appMethodMSALPPOTDOA,
       "appMethodMSALPPHYBRIDAGPS": appMethodMSALPPHYBRIDAGPS,
       "appMethodMSALPPHYBRIDECI": appMethodMSALPPHYBRIDECI,
       "appMethodMSALPPHYBRIDOTDOA": appMethodMSALPPHYBRIDOTDOA,
       "appMethodMSALPPHYBRIDHYBRID": appMethodMSALPPHYBRIDHYBRID,
       "appMethodMSAECI": appMethodMSAECI,
       "appMethodIS801HYBRIDHYBRID": appMethodIS801HYBRIDHYBRID,
       "appMethodULPLPPAUTOGPS": appMethodULPLPPAUTOGPS,
       "appMethodMSBRRLPAGNSS": appMethodMSBRRLPAGNSS,
       "appMethodMSBLPPAGNSS": appMethodMSBLPPAGNSS,
       "appMethodMSARRLPAGNSS": appMethodMSARRLPAGNSS,
       "appMethodMSALPPAGNSS": appMethodMSALPPAGNSS,
       "appMethodMSALPPHYBRIDAGNSS": appMethodMSALPPHYBRIDAGNSS,
       "appLocMethodStartTime": appLocMethodStartTime,
       "appLocMethodEndTime": appLocMethodEndTime,
       "appLocMethodRowIndex": appLocMethodRowIndex,
       "appLocSlsIFTable": appLocSlsIFTable,
       "appLocSlsIFEntry": appLocSlsIFEntry,
       "appLocSlsIFReq": appLocSlsIFReq,
       "appValidSlsReq": appValidSlsReq,
       "appSuccSlsRes": appSuccSlsRes,
       "appSuccSlsResRate": appSuccSlsResRate,
       "appLocSlsIFStartTime": appLocSlsIFStartTime,
       "appLocSlsIFEndTime": appLocSlsIFEndTime,
       "appLocSlsIFRowIndex": appLocSlsIFRowIndex,
       "appLocSlgIFTable": appLocSlgIFTable,
       "appLocSlgIFEntry": appLocSlgIFEntry,
       "appLocSlgIFReq": appLocSlgIFReq,
       "appValidSlgReq": appValidSlgReq,
       "appSuccSlgRes": appSuccSlgRes,
       "appSuccSlgResRate": appSuccSlgResRate,
       "appLocSlgIFStartTime": appLocSlgIFStartTime,
       "appLocSlgIFEndTime": appLocSlgIFEndTime,
       "appLocSlgIFRowIndex": appLocSlgIFRowIndex,
       "appFM": appFM,
       "lbsCommonAlarm": lbsCommonAlarm,
       "omc2ProcessCommunicationErrorAlarm": omc2ProcessCommunicationErrorAlarm,
       "process2ProcessCommunicationErrorAlarm": process2ProcessCommunicationErrorAlarm,
       "processInternalErrorAlarm": processInternalErrorAlarm,
       "process2ExternalInterfaceCommunicationErrorAlarm": process2ExternalInterfaceCommunicationErrorAlarm,
       "systemEnviromentErrorAlarm": systemEnviromentErrorAlarm,
       "pdmErrorAlarm": pdmErrorAlarm}
)
