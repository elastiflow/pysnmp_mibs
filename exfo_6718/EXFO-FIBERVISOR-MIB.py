# SNMP MIB module (EXFO-FIBERVISOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-FIBERVISOR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(alarmEntry,
 alarmIndex) = mibBuilder.importSymbols(
    "EXFO-ALARM-MIB",
    "alarmEntry",
    "alarmIndex")

(exfoModules,
 exfoProductMib) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoModules",
    "exfoProductMib")

(ExfoRealValue,) = mibBuilder.importSymbols(
    "EXFO-TC",
    "ExfoRealValue")

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
 ObjectName,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

exfoFiberVisorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FvAlarmType(TextualConvention, Integer32):
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
        *(("generic", 0),
          ("endOfAnalysis", 1),
          ("launchLevel", 2),
          ("newEventLoss", 3),
          ("reflectance", 4),
          ("nonReflectDeterLoss", 5),
          ("reflectDeterLoss", 6),
          ("sectionAttenuation", 7),
          ("totalLoss", 8),
          ("processingError", 9),
          ("rtuRsLink", 10),
          ("driftFrequency", 11),
          ("emptyChannel", 12),
          ("signalLoss", 13),
          ("minPower", 14),
          ("maxPower", 15),
          ("snr", 16))
    )



class FvAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("acknowledged", 2),
          ("archived", 3))
    )



class AlarmThresholdLevel(TextualConvention, Integer32):
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
        *(("notSpecify", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class FvWdmChannelSide(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("right", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FiberVisor_ObjectIdentity = ObjectIdentity
fiberVisor = _FiberVisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1)
)
if mibBuilder.loadTexts:
    fiberVisor.setStatus("current")
_FiberVisorConf_ObjectIdentity = ObjectIdentity
fiberVisorConf = _FiberVisorConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fiberVisorConf.setStatus("current")
_FiberVisorGroups_ObjectIdentity = ObjectIdentity
fiberVisorGroups = _FiberVisorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fiberVisorGroups.setStatus("current")
_FiberVisorCompls_ObjectIdentity = ObjectIdentity
fiberVisorCompls = _FiberVisorCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fiberVisorCompls.setStatus("current")
_FiberVisorObjs_ObjectIdentity = ObjectIdentity
fiberVisorObjs = _FiberVisorObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fiberVisorObjs.setStatus("current")
_FvFiberConfigurationObjs_ObjectIdentity = ObjectIdentity
fvFiberConfigurationObjs = _FvFiberConfigurationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fvFiberConfigurationObjs.setStatus("current")
_OpticalPathNumber_Type = Unsigned32
_OpticalPathNumber_Object = MibScalar
opticalPathNumber = _OpticalPathNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 1),
    _OpticalPathNumber_Type()
)
opticalPathNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPathNumber.setStatus("current")
_OpticalPathTable_Object = MibTable
opticalPathTable = _OpticalPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    opticalPathTable.setStatus("current")
_OpticalPathEntry_Object = MibTableRow
opticalPathEntry = _OpticalPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 2, 1)
)
opticalPathEntry.setIndexNames(
    (0, "EXFO-FIBERVISOR-MIB", "opticalPathIndex"),
)
if mibBuilder.loadTexts:
    opticalPathEntry.setStatus("current")
_OpticalPathIndex_Type = Unsigned32
_OpticalPathIndex_Object = MibTableColumn
opticalPathIndex = _OpticalPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 2, 1, 1),
    _OpticalPathIndex_Type()
)
opticalPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opticalPathIndex.setStatus("current")


class _OpticalPathName_Type(DisplayString):
    """Custom type opticalPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OpticalPathName_Type.__name__ = "DisplayString"
_OpticalPathName_Object = MibTableColumn
opticalPathName = _OpticalPathName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 2, 1, 2),
    _OpticalPathName_Type()
)
opticalPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPathName.setStatus("current")
_MeasurementPointNumber_Type = Unsigned32
_MeasurementPointNumber_Object = MibScalar
measurementPointNumber = _MeasurementPointNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 3),
    _MeasurementPointNumber_Type()
)
measurementPointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementPointNumber.setStatus("current")
_MeasurementPointTable_Object = MibTable
measurementPointTable = _MeasurementPointTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    measurementPointTable.setStatus("current")
_MeasurementPointEntry_Object = MibTableRow
measurementPointEntry = _MeasurementPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 4, 1)
)
measurementPointEntry.setIndexNames(
    (0, "EXFO-FIBERVISOR-MIB", "measurementPointIndex"),
)
if mibBuilder.loadTexts:
    measurementPointEntry.setStatus("current")
_MeasurementPointIndex_Type = Unsigned32
_MeasurementPointIndex_Object = MibTableColumn
measurementPointIndex = _MeasurementPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 4, 1, 1),
    _MeasurementPointIndex_Type()
)
measurementPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementPointIndex.setStatus("current")


class _MeasurementPointName_Type(DisplayString):
    """Custom type measurementPointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MeasurementPointName_Type.__name__ = "DisplayString"
_MeasurementPointName_Object = MibTableColumn
measurementPointName = _MeasurementPointName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 1, 4, 1, 2),
    _MeasurementPointName_Type()
)
measurementPointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementPointName.setStatus("current")
_FvDeviceObjs_ObjectIdentity = ObjectIdentity
fvDeviceObjs = _FvDeviceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fvDeviceObjs.setStatus("current")
_TscNumber_Type = Unsigned32
_TscNumber_Object = MibScalar
tscNumber = _TscNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 1),
    _TscNumber_Type()
)
tscNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscNumber.setStatus("current")
_TscTable_Object = MibTable
tscTable = _TscTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tscTable.setStatus("current")
_TscEntry_Object = MibTableRow
tscEntry = _TscEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 2, 1)
)
tscEntry.setIndexNames(
    (0, "EXFO-FIBERVISOR-MIB", "tscIndex"),
)
if mibBuilder.loadTexts:
    tscEntry.setStatus("current")
_TscIndex_Type = Unsigned32
_TscIndex_Object = MibTableColumn
tscIndex = _TscIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 2, 1, 1),
    _TscIndex_Type()
)
tscIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tscIndex.setStatus("current")


class _TscName_Type(DisplayString):
    """Custom type tscName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TscName_Type.__name__ = "DisplayString"
_TscName_Object = MibTableColumn
tscName = _TscName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 2, 1, 2),
    _TscName_Type()
)
tscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tscName.setStatus("current")
_RtuNumber_Type = Unsigned32
_RtuNumber_Object = MibScalar
rtuNumber = _RtuNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 3),
    _RtuNumber_Type()
)
rtuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtuNumber.setStatus("current")
_RtuTable_Object = MibTable
rtuTable = _RtuTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rtuTable.setStatus("current")
_RtuEntry_Object = MibTableRow
rtuEntry = _RtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 4, 1)
)
rtuEntry.setIndexNames(
    (0, "EXFO-FIBERVISOR-MIB", "rtuIndex"),
)
if mibBuilder.loadTexts:
    rtuEntry.setStatus("current")
_RtuIndex_Type = Unsigned32
_RtuIndex_Object = MibTableColumn
rtuIndex = _RtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 4, 1, 1),
    _RtuIndex_Type()
)
rtuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtuIndex.setStatus("current")


class _RtuName_Type(DisplayString):
    """Custom type rtuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RtuName_Type.__name__ = "DisplayString"
_RtuName_Object = MibTableColumn
rtuName = _RtuName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 4, 1, 2),
    _RtuName_Type()
)
rtuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtuName.setStatus("current")
_RsNumber_Type = Unsigned32
_RsNumber_Object = MibScalar
rsNumber = _RsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 5),
    _RsNumber_Type()
)
rsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNumber.setStatus("current")
_RsTable_Object = MibTable
rsTable = _RsTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    rsTable.setStatus("current")
_RsEntry_Object = MibTableRow
rsEntry = _RsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 6, 1)
)
rsEntry.setIndexNames(
    (0, "EXFO-FIBERVISOR-MIB", "rsIndex"),
)
if mibBuilder.loadTexts:
    rsEntry.setStatus("current")
_RsIndex_Type = Unsigned32
_RsIndex_Object = MibTableColumn
rsIndex = _RsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 6, 1, 1),
    _RsIndex_Type()
)
rsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIndex.setStatus("current")


class _RsName_Type(DisplayString):
    """Custom type rsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RsName_Type.__name__ = "DisplayString"
_RsName_Object = MibTableColumn
rsName = _RsName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 2, 6, 1, 2),
    _RsName_Type()
)
rsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsName.setStatus("current")
_FvTestObjs_ObjectIdentity = ObjectIdentity
fvTestObjs = _FvTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fvTestObjs.setStatus("current")
_FvAlarmObjs_ObjectIdentity = ObjectIdentity
fvAlarmObjs = _FvAlarmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fvAlarmObjs.setStatus("current")
_FvAlarmTable_Object = MibTable
fvAlarmTable = _FvAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fvAlarmTable.setStatus("current")
_FvAlarmEntry_Object = MibTableRow
fvAlarmEntry = _FvAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fvAlarmEntry.setStatus("current")
_FvAlarmStatus_Type = FvAlarmStatus
_FvAlarmStatus_Object = MibTableColumn
fvAlarmStatus = _FvAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 1, 1, 1),
    _FvAlarmStatus_Type()
)
fvAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fvAlarmStatus.setStatus("current")
_FvAlarmType_Type = FvAlarmType
_FvAlarmType_Object = MibTableColumn
fvAlarmType = _FvAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 1, 1, 2),
    _FvAlarmType_Type()
)
fvAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvAlarmType.setStatus("current")
_FvAlarmComments_Type = DisplayString
_FvAlarmComments_Object = MibTableColumn
fvAlarmComments = _FvAlarmComments_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 1, 1, 3),
    _FvAlarmComments_Type()
)
fvAlarmComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvAlarmComments.setStatus("current")
_FvEndOfAnalysisAlarmTable_Object = MibTable
fvEndOfAnalysisAlarmTable = _FvEndOfAnalysisAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmTable.setStatus("current")
_FvEndOfAnalysisAlarmEntry_Object = MibTableRow
fvEndOfAnalysisAlarmEntry = _FvEndOfAnalysisAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1)
)
fvEndOfAnalysisAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmEntry.setStatus("current")
_FvEndOfAnalysisAlarmOptPathReference_Type = RowPointer
_FvEndOfAnalysisAlarmOptPathReference_Object = MibTableColumn
fvEndOfAnalysisAlarmOptPathReference = _FvEndOfAnalysisAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1, 1),
    _FvEndOfAnalysisAlarmOptPathReference_Type()
)
fvEndOfAnalysisAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmOptPathReference.setStatus("current")
_FvEndOfAnalysisAlarmOptDist_Type = Unsigned32
_FvEndOfAnalysisAlarmOptDist_Object = MibTableColumn
fvEndOfAnalysisAlarmOptDist = _FvEndOfAnalysisAlarmOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1, 2),
    _FvEndOfAnalysisAlarmOptDist_Type()
)
fvEndOfAnalysisAlarmOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmOptDist.setUnits("Meter")
_FvEndOfAnalysisAlarmGeoDist_Type = Unsigned32
_FvEndOfAnalysisAlarmGeoDist_Object = MibTableColumn
fvEndOfAnalysisAlarmGeoDist = _FvEndOfAnalysisAlarmGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1, 3),
    _FvEndOfAnalysisAlarmGeoDist_Type()
)
fvEndOfAnalysisAlarmGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmGeoDist.setUnits("Meter")
_FvEndOfAnalysisAlarmLongitude_Type = ExfoRealValue
_FvEndOfAnalysisAlarmLongitude_Object = MibTableColumn
fvEndOfAnalysisAlarmLongitude = _FvEndOfAnalysisAlarmLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1, 4),
    _FvEndOfAnalysisAlarmLongitude_Type()
)
fvEndOfAnalysisAlarmLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmLongitude.setStatus("current")
_FvEndOfAnalysisAlarmLatitude_Type = ExfoRealValue
_FvEndOfAnalysisAlarmLatitude_Object = MibTableColumn
fvEndOfAnalysisAlarmLatitude = _FvEndOfAnalysisAlarmLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 2, 1, 5),
    _FvEndOfAnalysisAlarmLatitude_Type()
)
fvEndOfAnalysisAlarmLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmLatitude.setStatus("current")
_FvReflectanceAlarmTable_Object = MibTable
fvReflectanceAlarmTable = _FvReflectanceAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    fvReflectanceAlarmTable.setStatus("current")
_FvReflectanceAlarmEntry_Object = MibTableRow
fvReflectanceAlarmEntry = _FvReflectanceAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1)
)
fvReflectanceAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvReflectanceAlarmEntry.setStatus("current")
_FvReflectanceAlarmOptPathReference_Type = RowPointer
_FvReflectanceAlarmOptPathReference_Object = MibTableColumn
fvReflectanceAlarmOptPathReference = _FvReflectanceAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1, 1),
    _FvReflectanceAlarmOptPathReference_Type()
)
fvReflectanceAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectanceAlarmOptPathReference.setStatus("current")
_FvReflectanceAlarmOptDist_Type = Unsigned32
_FvReflectanceAlarmOptDist_Object = MibTableColumn
fvReflectanceAlarmOptDist = _FvReflectanceAlarmOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1, 2),
    _FvReflectanceAlarmOptDist_Type()
)
fvReflectanceAlarmOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectanceAlarmOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvReflectanceAlarmOptDist.setUnits("Meter")
_FvReflectanceAlarmGeoDist_Type = Unsigned32
_FvReflectanceAlarmGeoDist_Object = MibTableColumn
fvReflectanceAlarmGeoDist = _FvReflectanceAlarmGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1, 3),
    _FvReflectanceAlarmGeoDist_Type()
)
fvReflectanceAlarmGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectanceAlarmGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvReflectanceAlarmGeoDist.setUnits("Meter")
_FvReflectanceAlarmLongitude_Type = ExfoRealValue
_FvReflectanceAlarmLongitude_Object = MibTableColumn
fvReflectanceAlarmLongitude = _FvReflectanceAlarmLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1, 4),
    _FvReflectanceAlarmLongitude_Type()
)
fvReflectanceAlarmLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectanceAlarmLongitude.setStatus("current")
_FvReflectanceAlarmLatitude_Type = ExfoRealValue
_FvReflectanceAlarmLatitude_Object = MibTableColumn
fvReflectanceAlarmLatitude = _FvReflectanceAlarmLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 3, 1, 5),
    _FvReflectanceAlarmLatitude_Type()
)
fvReflectanceAlarmLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectanceAlarmLatitude.setStatus("current")
_FvNewEventLossAlarmTable_Object = MibTable
fvNewEventLossAlarmTable = _FvNewEventLossAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    fvNewEventLossAlarmTable.setStatus("current")
_FvNewEventLossAlarmEntry_Object = MibTableRow
fvNewEventLossAlarmEntry = _FvNewEventLossAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1)
)
fvNewEventLossAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvNewEventLossAlarmEntry.setStatus("current")
_FvNewEventLossAlarmOptPathReference_Type = RowPointer
_FvNewEventLossAlarmOptPathReference_Object = MibTableColumn
fvNewEventLossAlarmOptPathReference = _FvNewEventLossAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1, 1),
    _FvNewEventLossAlarmOptPathReference_Type()
)
fvNewEventLossAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmOptPathReference.setStatus("current")
_FvNewEventLossAlarmOptDist_Type = Unsigned32
_FvNewEventLossAlarmOptDist_Object = MibTableColumn
fvNewEventLossAlarmOptDist = _FvNewEventLossAlarmOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1, 2),
    _FvNewEventLossAlarmOptDist_Type()
)
fvNewEventLossAlarmOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmOptDist.setUnits("Meter")
_FvNewEventLossAlarmGeoDist_Type = Unsigned32
_FvNewEventLossAlarmGeoDist_Object = MibTableColumn
fvNewEventLossAlarmGeoDist = _FvNewEventLossAlarmGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1, 3),
    _FvNewEventLossAlarmGeoDist_Type()
)
fvNewEventLossAlarmGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmGeoDist.setUnits("Meter")
_FvNewEventLossAlarmLongitude_Type = ExfoRealValue
_FvNewEventLossAlarmLongitude_Object = MibTableColumn
fvNewEventLossAlarmLongitude = _FvNewEventLossAlarmLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1, 4),
    _FvNewEventLossAlarmLongitude_Type()
)
fvNewEventLossAlarmLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmLongitude.setStatus("current")
_FvNewEventLossAlarmLatitude_Type = ExfoRealValue
_FvNewEventLossAlarmLatitude_Object = MibTableColumn
fvNewEventLossAlarmLatitude = _FvNewEventLossAlarmLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 4, 1, 5),
    _FvNewEventLossAlarmLatitude_Type()
)
fvNewEventLossAlarmLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNewEventLossAlarmLatitude.setStatus("current")
_FvNonReflectDeterLossAlarmTable_Object = MibTable
fvNonReflectDeterLossAlarmTable = _FvNonReflectDeterLossAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmTable.setStatus("current")
_FvNonReflectDeterLossAlarmEntry_Object = MibTableRow
fvNonReflectDeterLossAlarmEntry = _FvNonReflectDeterLossAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1)
)
fvNonReflectDeterLossAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmEntry.setStatus("current")
_FvNonReflectDeterLossAlarmOptPathReference_Type = RowPointer
_FvNonReflectDeterLossAlarmOptPathReference_Object = MibTableColumn
fvNonReflectDeterLossAlarmOptPathReference = _FvNonReflectDeterLossAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1, 1),
    _FvNonReflectDeterLossAlarmOptPathReference_Type()
)
fvNonReflectDeterLossAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmOptPathReference.setStatus("current")
_FvNonReflectDeterLossAlarmOptDist_Type = Unsigned32
_FvNonReflectDeterLossAlarmOptDist_Object = MibTableColumn
fvNonReflectDeterLossAlarmOptDist = _FvNonReflectDeterLossAlarmOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1, 2),
    _FvNonReflectDeterLossAlarmOptDist_Type()
)
fvNonReflectDeterLossAlarmOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmOptDist.setUnits("Meter")
_FvNonReflectDeterLossAlarmGeoDist_Type = Unsigned32
_FvNonReflectDeterLossAlarmGeoDist_Object = MibTableColumn
fvNonReflectDeterLossAlarmGeoDist = _FvNonReflectDeterLossAlarmGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1, 3),
    _FvNonReflectDeterLossAlarmGeoDist_Type()
)
fvNonReflectDeterLossAlarmGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmGeoDist.setUnits("Meter")
_FvNonReflectDeterLossAlarmLongitude_Type = ExfoRealValue
_FvNonReflectDeterLossAlarmLongitude_Object = MibTableColumn
fvNonReflectDeterLossAlarmLongitude = _FvNonReflectDeterLossAlarmLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1, 4),
    _FvNonReflectDeterLossAlarmLongitude_Type()
)
fvNonReflectDeterLossAlarmLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmLongitude.setStatus("current")
_FvNonReflectDeterLossAlarmLatitude_Type = ExfoRealValue
_FvNonReflectDeterLossAlarmLatitude_Object = MibTableColumn
fvNonReflectDeterLossAlarmLatitude = _FvNonReflectDeterLossAlarmLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 5, 1, 5),
    _FvNonReflectDeterLossAlarmLatitude_Type()
)
fvNonReflectDeterLossAlarmLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmLatitude.setStatus("current")
_FvReflectDeterLossAlarmTable_Object = MibTable
fvReflectDeterLossAlarmTable = _FvReflectDeterLossAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmTable.setStatus("current")
_FvReflectDeterLossAlarmEntry_Object = MibTableRow
fvReflectDeterLossAlarmEntry = _FvReflectDeterLossAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1)
)
fvReflectDeterLossAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmEntry.setStatus("current")
_FvReflectDeterLossAlarmOptPathReference_Type = RowPointer
_FvReflectDeterLossAlarmOptPathReference_Object = MibTableColumn
fvReflectDeterLossAlarmOptPathReference = _FvReflectDeterLossAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1, 1),
    _FvReflectDeterLossAlarmOptPathReference_Type()
)
fvReflectDeterLossAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmOptPathReference.setStatus("current")
_FvReflectDeterLossAlarmOptDist_Type = Unsigned32
_FvReflectDeterLossAlarmOptDist_Object = MibTableColumn
fvReflectDeterLossAlarmOptDist = _FvReflectDeterLossAlarmOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1, 2),
    _FvReflectDeterLossAlarmOptDist_Type()
)
fvReflectDeterLossAlarmOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmOptDist.setUnits("Meter")
_FvReflectDeterLossAlarmGeoDist_Type = Unsigned32
_FvReflectDeterLossAlarmGeoDist_Object = MibTableColumn
fvReflectDeterLossAlarmGeoDist = _FvReflectDeterLossAlarmGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1, 3),
    _FvReflectDeterLossAlarmGeoDist_Type()
)
fvReflectDeterLossAlarmGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmGeoDist.setUnits("Meter")
_FvReflectDeterLossAlarmLongitude_Type = ExfoRealValue
_FvReflectDeterLossAlarmLongitude_Object = MibTableColumn
fvReflectDeterLossAlarmLongitude = _FvReflectDeterLossAlarmLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1, 4),
    _FvReflectDeterLossAlarmLongitude_Type()
)
fvReflectDeterLossAlarmLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmLongitude.setStatus("current")
_FvReflectDeterLossAlarmLatitude_Type = ExfoRealValue
_FvReflectDeterLossAlarmLatitude_Object = MibTableColumn
fvReflectDeterLossAlarmLatitude = _FvReflectDeterLossAlarmLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 6, 1, 5),
    _FvReflectDeterLossAlarmLatitude_Type()
)
fvReflectDeterLossAlarmLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmLatitude.setStatus("current")
_FvSectionAttenuationAlarmTable_Object = MibTable
fvSectionAttenuationAlarmTable = _FvSectionAttenuationAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7)
)
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmTable.setStatus("current")
_FvSectionAttenuationAlarmEntry_Object = MibTableRow
fvSectionAttenuationAlarmEntry = _FvSectionAttenuationAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1)
)
fvSectionAttenuationAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEntry.setStatus("current")
_FvSectionAttenuationAlarmOptPathReference_Type = RowPointer
_FvSectionAttenuationAlarmOptPathReference_Object = MibTableColumn
fvSectionAttenuationAlarmOptPathReference = _FvSectionAttenuationAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 1),
    _FvSectionAttenuationAlarmOptPathReference_Type()
)
fvSectionAttenuationAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmOptPathReference.setStatus("current")
_FvSectionAttenuationAlarmStartOptDist_Type = Unsigned32
_FvSectionAttenuationAlarmStartOptDist_Object = MibTableColumn
fvSectionAttenuationAlarmStartOptDist = _FvSectionAttenuationAlarmStartOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 2),
    _FvSectionAttenuationAlarmStartOptDist_Type()
)
fvSectionAttenuationAlarmStartOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartOptDist.setUnits("Meter")
_FvSectionAttenuationAlarmStartGeoDist_Type = Unsigned32
_FvSectionAttenuationAlarmStartGeoDist_Object = MibTableColumn
fvSectionAttenuationAlarmStartGeoDist = _FvSectionAttenuationAlarmStartGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 3),
    _FvSectionAttenuationAlarmStartGeoDist_Type()
)
fvSectionAttenuationAlarmStartGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartGeoDist.setUnits("Meter")
_FvSectionAttenuationAlarmStartLongitude_Type = ExfoRealValue
_FvSectionAttenuationAlarmStartLongitude_Object = MibTableColumn
fvSectionAttenuationAlarmStartLongitude = _FvSectionAttenuationAlarmStartLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 4),
    _FvSectionAttenuationAlarmStartLongitude_Type()
)
fvSectionAttenuationAlarmStartLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartLongitude.setStatus("current")
_FvSectionAttenuationAlarmStartLatitude_Type = ExfoRealValue
_FvSectionAttenuationAlarmStartLatitude_Object = MibTableColumn
fvSectionAttenuationAlarmStartLatitude = _FvSectionAttenuationAlarmStartLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 5),
    _FvSectionAttenuationAlarmStartLatitude_Type()
)
fvSectionAttenuationAlarmStartLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmStartLatitude.setStatus("current")
_FvSectionAttenuationAlarmEndOptDist_Type = Unsigned32
_FvSectionAttenuationAlarmEndOptDist_Object = MibTableColumn
fvSectionAttenuationAlarmEndOptDist = _FvSectionAttenuationAlarmEndOptDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 6),
    _FvSectionAttenuationAlarmEndOptDist_Type()
)
fvSectionAttenuationAlarmEndOptDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndOptDist.setStatus("current")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndOptDist.setUnits("Meter")
_FvSectionAttenuationAlarmEndGeoDist_Type = Unsigned32
_FvSectionAttenuationAlarmEndGeoDist_Object = MibTableColumn
fvSectionAttenuationAlarmEndGeoDist = _FvSectionAttenuationAlarmEndGeoDist_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 7),
    _FvSectionAttenuationAlarmEndGeoDist_Type()
)
fvSectionAttenuationAlarmEndGeoDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndGeoDist.setStatus("current")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndGeoDist.setUnits("Meter")
_FvSectionAttenuationAlarmEndLongitude_Type = ExfoRealValue
_FvSectionAttenuationAlarmEndLongitude_Object = MibTableColumn
fvSectionAttenuationAlarmEndLongitude = _FvSectionAttenuationAlarmEndLongitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 8),
    _FvSectionAttenuationAlarmEndLongitude_Type()
)
fvSectionAttenuationAlarmEndLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndLongitude.setStatus("current")
_FvSectionAttenuationAlarmEndLatitude_Type = ExfoRealValue
_FvSectionAttenuationAlarmEndLatitude_Object = MibTableColumn
fvSectionAttenuationAlarmEndLatitude = _FvSectionAttenuationAlarmEndLatitude_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 7, 1, 9),
    _FvSectionAttenuationAlarmEndLatitude_Type()
)
fvSectionAttenuationAlarmEndLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmEndLatitude.setStatus("current")
_FvRtuRsLinkAlarmTable_Object = MibTable
fvRtuRsLinkAlarmTable = _FvRtuRsLinkAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 8)
)
if mibBuilder.loadTexts:
    fvRtuRsLinkAlarmTable.setStatus("current")
_FvRtuRsLinkAlarmEntry_Object = MibTableRow
fvRtuRsLinkAlarmEntry = _FvRtuRsLinkAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 8, 1)
)
fvRtuRsLinkAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvRtuRsLinkAlarmEntry.setStatus("current")
_FvRtuRsLinkAlarmRsReference_Type = RowPointer
_FvRtuRsLinkAlarmRsReference_Object = MibTableColumn
fvRtuRsLinkAlarmRsReference = _FvRtuRsLinkAlarmRsReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 8, 1, 1),
    _FvRtuRsLinkAlarmRsReference_Type()
)
fvRtuRsLinkAlarmRsReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvRtuRsLinkAlarmRsReference.setStatus("current")
_FvDriftFreqAlarmTable_Object = MibTable
fvDriftFreqAlarmTable = _FvDriftFreqAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 9)
)
if mibBuilder.loadTexts:
    fvDriftFreqAlarmTable.setStatus("current")
_FvDriftFreqAlarmEntry_Object = MibTableRow
fvDriftFreqAlarmEntry = _FvDriftFreqAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 9, 1)
)
fvDriftFreqAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvDriftFreqAlarmEntry.setStatus("current")
_FvDriftFreqAlarmMeasPointReference_Type = RowPointer
_FvDriftFreqAlarmMeasPointReference_Object = MibTableColumn
fvDriftFreqAlarmMeasPointReference = _FvDriftFreqAlarmMeasPointReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 9, 1, 1),
    _FvDriftFreqAlarmMeasPointReference_Type()
)
fvDriftFreqAlarmMeasPointReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvDriftFreqAlarmMeasPointReference.setStatus("current")


class _FvDriftFreqAlarmChannelName_Type(DisplayString):
    """Custom type fvDriftFreqAlarmChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FvDriftFreqAlarmChannelName_Type.__name__ = "DisplayString"
_FvDriftFreqAlarmChannelName_Object = MibTableColumn
fvDriftFreqAlarmChannelName = _FvDriftFreqAlarmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 9, 1, 2),
    _FvDriftFreqAlarmChannelName_Type()
)
fvDriftFreqAlarmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvDriftFreqAlarmChannelName.setStatus("current")
_FvDriftFreqAlarmChannelCenter_Type = ExfoRealValue
_FvDriftFreqAlarmChannelCenter_Object = MibTableColumn
fvDriftFreqAlarmChannelCenter = _FvDriftFreqAlarmChannelCenter_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 9, 1, 3),
    _FvDriftFreqAlarmChannelCenter_Type()
)
fvDriftFreqAlarmChannelCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvDriftFreqAlarmChannelCenter.setStatus("current")
if mibBuilder.loadTexts:
    fvDriftFreqAlarmChannelCenter.setUnits("THz")
_FvEmptyChannelAlarmTable_Object = MibTable
fvEmptyChannelAlarmTable = _FvEmptyChannelAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 10)
)
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmTable.setStatus("current")
_FvEmptyChannelAlarmEntry_Object = MibTableRow
fvEmptyChannelAlarmEntry = _FvEmptyChannelAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 10, 1)
)
fvEmptyChannelAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmEntry.setStatus("current")
_FvEmptyChannelAlarmMeasPointReference_Type = RowPointer
_FvEmptyChannelAlarmMeasPointReference_Object = MibTableColumn
fvEmptyChannelAlarmMeasPointReference = _FvEmptyChannelAlarmMeasPointReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 10, 1, 1),
    _FvEmptyChannelAlarmMeasPointReference_Type()
)
fvEmptyChannelAlarmMeasPointReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmMeasPointReference.setStatus("current")


class _FvEmptyChannelAlarmChannelName_Type(DisplayString):
    """Custom type fvEmptyChannelAlarmChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FvEmptyChannelAlarmChannelName_Type.__name__ = "DisplayString"
_FvEmptyChannelAlarmChannelName_Object = MibTableColumn
fvEmptyChannelAlarmChannelName = _FvEmptyChannelAlarmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 10, 1, 2),
    _FvEmptyChannelAlarmChannelName_Type()
)
fvEmptyChannelAlarmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmChannelName.setStatus("current")
_FvEmptyChannelAlarmChannelCenter_Type = ExfoRealValue
_FvEmptyChannelAlarmChannelCenter_Object = MibTableColumn
fvEmptyChannelAlarmChannelCenter = _FvEmptyChannelAlarmChannelCenter_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 10, 1, 3),
    _FvEmptyChannelAlarmChannelCenter_Type()
)
fvEmptyChannelAlarmChannelCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmChannelCenter.setStatus("current")
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmChannelCenter.setUnits("THz")
_FvSignalLossAlarmTable_Object = MibTable
fvSignalLossAlarmTable = _FvSignalLossAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 11)
)
if mibBuilder.loadTexts:
    fvSignalLossAlarmTable.setStatus("current")
_FvSignalLossAlarmEntry_Object = MibTableRow
fvSignalLossAlarmEntry = _FvSignalLossAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 11, 1)
)
fvSignalLossAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvSignalLossAlarmEntry.setStatus("current")
_FvSignalLossAlarmMeasPointReference_Type = RowPointer
_FvSignalLossAlarmMeasPointReference_Object = MibTableColumn
fvSignalLossAlarmMeasPointReference = _FvSignalLossAlarmMeasPointReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 11, 1, 1),
    _FvSignalLossAlarmMeasPointReference_Type()
)
fvSignalLossAlarmMeasPointReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSignalLossAlarmMeasPointReference.setStatus("current")
_FvPowerAlarmTable_Object = MibTable
fvPowerAlarmTable = _FvPowerAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 12)
)
if mibBuilder.loadTexts:
    fvPowerAlarmTable.setStatus("current")
_FvPowerAlarmEntry_Object = MibTableRow
fvPowerAlarmEntry = _FvPowerAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 12, 1)
)
fvPowerAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvPowerAlarmEntry.setStatus("current")
_FvPowerAlarmMeasPointReference_Type = RowPointer
_FvPowerAlarmMeasPointReference_Object = MibTableColumn
fvPowerAlarmMeasPointReference = _FvPowerAlarmMeasPointReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 12, 1, 1),
    _FvPowerAlarmMeasPointReference_Type()
)
fvPowerAlarmMeasPointReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvPowerAlarmMeasPointReference.setStatus("current")


class _FvPowerAlarmChannelName_Type(DisplayString):
    """Custom type fvPowerAlarmChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FvPowerAlarmChannelName_Type.__name__ = "DisplayString"
_FvPowerAlarmChannelName_Object = MibTableColumn
fvPowerAlarmChannelName = _FvPowerAlarmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 12, 1, 2),
    _FvPowerAlarmChannelName_Type()
)
fvPowerAlarmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvPowerAlarmChannelName.setStatus("current")
_FvPowerAlarmChannelCenter_Type = ExfoRealValue
_FvPowerAlarmChannelCenter_Object = MibTableColumn
fvPowerAlarmChannelCenter = _FvPowerAlarmChannelCenter_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 12, 1, 3),
    _FvPowerAlarmChannelCenter_Type()
)
fvPowerAlarmChannelCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvPowerAlarmChannelCenter.setStatus("current")
if mibBuilder.loadTexts:
    fvPowerAlarmChannelCenter.setUnits("THz")
_FvSnrAlarmTable_Object = MibTable
fvSnrAlarmTable = _FvSnrAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13)
)
if mibBuilder.loadTexts:
    fvSnrAlarmTable.setStatus("current")
_FvSnrAlarmEntry_Object = MibTableRow
fvSnrAlarmEntry = _FvSnrAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13, 1)
)
fvSnrAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvSnrAlarmEntry.setStatus("current")
_FvSnrAlarmMeasPointReference_Type = RowPointer
_FvSnrAlarmMeasPointReference_Object = MibTableColumn
fvSnrAlarmMeasPointReference = _FvSnrAlarmMeasPointReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13, 1, 1),
    _FvSnrAlarmMeasPointReference_Type()
)
fvSnrAlarmMeasPointReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSnrAlarmMeasPointReference.setStatus("current")


class _FvSnrAlarmChannelName_Type(DisplayString):
    """Custom type fvSnrAlarmChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FvSnrAlarmChannelName_Type.__name__ = "DisplayString"
_FvSnrAlarmChannelName_Object = MibTableColumn
fvSnrAlarmChannelName = _FvSnrAlarmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13, 1, 2),
    _FvSnrAlarmChannelName_Type()
)
fvSnrAlarmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSnrAlarmChannelName.setStatus("current")
_FvSnrAlarmChannelCenter_Type = ExfoRealValue
_FvSnrAlarmChannelCenter_Object = MibTableColumn
fvSnrAlarmChannelCenter = _FvSnrAlarmChannelCenter_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13, 1, 3),
    _FvSnrAlarmChannelCenter_Type()
)
fvSnrAlarmChannelCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSnrAlarmChannelCenter.setStatus("current")
if mibBuilder.loadTexts:
    fvSnrAlarmChannelCenter.setUnits("THz")
_FvSnrAlarmChannelSide_Type = FvWdmChannelSide
_FvSnrAlarmChannelSide_Object = MibTableColumn
fvSnrAlarmChannelSide = _FvSnrAlarmChannelSide_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 13, 1, 4),
    _FvSnrAlarmChannelSide_Type()
)
fvSnrAlarmChannelSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSnrAlarmChannelSide.setStatus("current")
_FvTotalLossAlarmTable_Object = MibTable
fvTotalLossAlarmTable = _FvTotalLossAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 14)
)
if mibBuilder.loadTexts:
    fvTotalLossAlarmTable.setStatus("current")
_FvTotalLossAlarmEntry_Object = MibTableRow
fvTotalLossAlarmEntry = _FvTotalLossAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 14, 1)
)
fvTotalLossAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvTotalLossAlarmEntry.setStatus("current")
_FvTotalLossAlarmOptPathReference_Type = RowPointer
_FvTotalLossAlarmOptPathReference_Object = MibTableColumn
fvTotalLossAlarmOptPathReference = _FvTotalLossAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 14, 1, 1),
    _FvTotalLossAlarmOptPathReference_Type()
)
fvTotalLossAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvTotalLossAlarmOptPathReference.setStatus("current")
_FvLaunchLevelAlarmTable_Object = MibTable
fvLaunchLevelAlarmTable = _FvLaunchLevelAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 15)
)
if mibBuilder.loadTexts:
    fvLaunchLevelAlarmTable.setStatus("current")
_FvLaunchLevelAlarmEntry_Object = MibTableRow
fvLaunchLevelAlarmEntry = _FvLaunchLevelAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 15, 1)
)
fvLaunchLevelAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvLaunchLevelAlarmEntry.setStatus("current")
_FvLaunchLevelAlarmOptPathReference_Type = RowPointer
_FvLaunchLevelAlarmOptPathReference_Object = MibTableColumn
fvLaunchLevelAlarmOptPathReference = _FvLaunchLevelAlarmOptPathReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 15, 1, 1),
    _FvLaunchLevelAlarmOptPathReference_Type()
)
fvLaunchLevelAlarmOptPathReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvLaunchLevelAlarmOptPathReference.setStatus("current")
_FvProcessingErrorAlarmTable_Object = MibTable
fvProcessingErrorAlarmTable = _FvProcessingErrorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 16)
)
if mibBuilder.loadTexts:
    fvProcessingErrorAlarmTable.setStatus("current")
_FvProcessingErrorAlarmEntry_Object = MibTableRow
fvProcessingErrorAlarmEntry = _FvProcessingErrorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 16, 1)
)
fvProcessingErrorAlarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    fvProcessingErrorAlarmEntry.setStatus("current")
_FvProcessingErrorAlarmSoftwareReference_Type = RowPointer
_FvProcessingErrorAlarmSoftwareReference_Object = MibTableColumn
fvProcessingErrorAlarmSoftwareReference = _FvProcessingErrorAlarmSoftwareReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 2, 4, 16, 1, 1),
    _FvProcessingErrorAlarmSoftwareReference_Type()
)
fvProcessingErrorAlarmSoftwareReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvProcessingErrorAlarmSoftwareReference.setStatus("current")
_FiberVisorEvents_ObjectIdentity = ObjectIdentity
fiberVisorEvents = _FiberVisorEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fiberVisorEvents.setStatus("current")
_FvSoftware_ObjectIdentity = ObjectIdentity
fvSoftware = _FvSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4)
)
if mibBuilder.loadTexts:
    fvSoftware.setStatus("current")
_ExfoRftsSystemSchedulerManager_ObjectIdentity = ObjectIdentity
exfoRftsSystemSchedulerManager = _ExfoRftsSystemSchedulerManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1)
)
_ExfoRftsOtdrMonitoringMonitor_ObjectIdentity = ObjectIdentity
exfoRftsOtdrMonitoringMonitor = _ExfoRftsOtdrMonitoringMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 2)
)
_ExfoRftsSvrClientManagerClientManager_ObjectIdentity = ObjectIdentity
exfoRftsSvrClientManagerClientManager = _ExfoRftsSvrClientManagerClientManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 3)
)
_ExfoRftsRFTSMulti_ObjectIdentity = ObjectIdentity
exfoRftsRFTSMulti = _ExfoRftsRFTSMulti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 4)
)
_ExfoRftsSwitchControllerSwitchController_ObjectIdentity = ObjectIdentity
exfoRftsSwitchControllerSwitchController = _ExfoRftsSwitchControllerSwitchController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 5)
)
_ExfoRftsMwmMonitoringMonitor_ObjectIdentity = ObjectIdentity
exfoRftsMwmMonitoringMonitor = _ExfoRftsMwmMonitoringMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 6)
)
_ExfoRftsBdsync_ObjectIdentity = ObjectIdentity
exfoRftsBdsync = _ExfoRftsBdsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1000)
)
_ExfoRftsRtuParamItfOnTscCRtuConfig_ObjectIdentity = ObjectIdentity
exfoRftsRtuParamItfOnTscCRtuConfig = _ExfoRftsRtuParamItfOnTscCRtuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1001)
)
_ExfoRftsServiceCheckerRTUChecker_ObjectIdentity = ObjectIdentity
exfoRftsServiceCheckerRTUChecker = _ExfoRftsServiceCheckerRTUChecker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1002)
)
_ExfoRftsServiceCheckerDriveSpaceChecker_ObjectIdentity = ObjectIdentity
exfoRftsServiceCheckerDriveSpaceChecker = _ExfoRftsServiceCheckerDriveSpaceChecker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1003)
)
_ExfoRftsServiceCheckerAckChecker_ObjectIdentity = ObjectIdentity
exfoRftsServiceCheckerAckChecker = _ExfoRftsServiceCheckerAckChecker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1004)
)
_ExfoRftsAlarmGenerator_ObjectIdentity = ObjectIdentity
exfoRftsAlarmGenerator = _ExfoRftsAlarmGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1005)
)
_ExfoRftsMsgReceiver_ObjectIdentity = ObjectIdentity
exfoRftsMsgReceiver = _ExfoRftsMsgReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 4, 1006)
)
_FvThreshold_ObjectIdentity = ObjectIdentity
fvThreshold = _FvThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5)
)
if mibBuilder.loadTexts:
    fvThreshold.setStatus("current")
_NewEventLossThreshold_ObjectIdentity = ObjectIdentity
newEventLossThreshold = _NewEventLossThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    newEventLossThreshold.setStatus("current")
_NonReflectiveDeteriorationLossThreshold_ObjectIdentity = ObjectIdentity
nonReflectiveDeteriorationLossThreshold = _NonReflectiveDeteriorationLossThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    nonReflectiveDeteriorationLossThreshold.setStatus("current")
_SectionAttenuationThreshold_ObjectIdentity = ObjectIdentity
sectionAttenuationThreshold = _SectionAttenuationThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    sectionAttenuationThreshold.setStatus("current")
_TotalLossThreshold_ObjectIdentity = ObjectIdentity
totalLossThreshold = _TotalLossThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    totalLossThreshold.setStatus("current")
_ReflectanceThreshold_ObjectIdentity = ObjectIdentity
reflectanceThreshold = _ReflectanceThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 5)
)
if mibBuilder.loadTexts:
    reflectanceThreshold.setStatus("current")
_LaunchLevelThreshold_ObjectIdentity = ObjectIdentity
launchLevelThreshold = _LaunchLevelThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 6)
)
if mibBuilder.loadTexts:
    launchLevelThreshold.setStatus("current")
_ReflectiveDeteriorationLossThreshold_ObjectIdentity = ObjectIdentity
reflectiveDeteriorationLossThreshold = _ReflectiveDeteriorationLossThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 7)
)
if mibBuilder.loadTexts:
    reflectiveDeteriorationLossThreshold.setStatus("current")
_DriftFrequencyThreshold_ObjectIdentity = ObjectIdentity
driftFrequencyThreshold = _DriftFrequencyThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 8)
)
if mibBuilder.loadTexts:
    driftFrequencyThreshold.setStatus("current")
_MinPowerThreshold_ObjectIdentity = ObjectIdentity
minPowerThreshold = _MinPowerThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 9)
)
if mibBuilder.loadTexts:
    minPowerThreshold.setStatus("current")
_MaxPowerThreshold_ObjectIdentity = ObjectIdentity
maxPowerThreshold = _MaxPowerThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 10)
)
if mibBuilder.loadTexts:
    maxPowerThreshold.setStatus("current")
_SnrThreshold_ObjectIdentity = ObjectIdentity
snrThreshold = _SnrThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 5, 11)
)
if mibBuilder.loadTexts:
    snrThreshold.setStatus("current")
_FvTestCategory_ObjectIdentity = ObjectIdentity
fvTestCategory = _FvTestCategory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 6)
)
if mibBuilder.loadTexts:
    fvTestCategory.setStatus("current")
_OpticalPathWithDefaultRefTrace_ObjectIdentity = ObjectIdentity
opticalPathWithDefaultRefTrace = _OpticalPathWithDefaultRefTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    opticalPathWithDefaultRefTrace.setStatus("current")
_MeasurementPointWithDefaultRefTrace_ObjectIdentity = ObjectIdentity
measurementPointWithDefaultRefTrace = _MeasurementPointWithDefaultRefTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    measurementPointWithDefaultRefTrace.setStatus("current")
alarmEntry.registerAugmentions(
    ("EXFO-FIBERVISOR-MIB",
     "fvAlarmEntry")
)
fvAlarmEntry.setIndexNames(*alarmEntry.getIndexNames())

# Managed Objects groups

fvFiberConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 1)
)
fvFiberConfigurationGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "opticalPathNumber"),
        ("EXFO-FIBERVISOR-MIB", "opticalPathName"),
        ("EXFO-FIBERVISOR-MIB", "measurementPointNumber"),
        ("EXFO-FIBERVISOR-MIB", "measurementPointName"))
)
if mibBuilder.loadTexts:
    fvFiberConfigurationGroup.setStatus("current")

fvDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 2)
)
fvDeviceGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "tscNumber"),
        ("EXFO-FIBERVISOR-MIB", "tscName"),
        ("EXFO-FIBERVISOR-MIB", "rtuNumber"),
        ("EXFO-FIBERVISOR-MIB", "rtuName"),
        ("EXFO-FIBERVISOR-MIB", "rsNumber"),
        ("EXFO-FIBERVISOR-MIB", "rsName"))
)
if mibBuilder.loadTexts:
    fvDeviceGroup.setStatus("current")

fvAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 3)
)
fvAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvAlarmStatus"),
        ("EXFO-FIBERVISOR-MIB", "fvAlarmType"),
        ("EXFO-FIBERVISOR-MIB", "fvAlarmComments"))
)
if mibBuilder.loadTexts:
    fvAlarmGroup.setStatus("current")

fvEndOfAnalysisAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 4)
)
fvEndOfAnalysisAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmLatitude"))
)
if mibBuilder.loadTexts:
    fvEndOfAnalysisAlarmGroup.setStatus("current")

fvReflectanceAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 5)
)
fvReflectanceAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmLatitude"))
)
if mibBuilder.loadTexts:
    fvReflectanceAlarmGroup.setStatus("current")

fvNewEventLossAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 6)
)
fvNewEventLossAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmLatitude"))
)
if mibBuilder.loadTexts:
    fvNewEventLossAlarmGroup.setStatus("current")

fvNonReflectDeterLossAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 7)
)
fvNonReflectDeterLossAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmLatitude"))
)
if mibBuilder.loadTexts:
    fvNonReflectDeterLossAlarmGroup.setStatus("current")

fvReflectDeterLossAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 8)
)
fvReflectDeterLossAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmLatitude"))
)
if mibBuilder.loadTexts:
    fvReflectDeterLossAlarmGroup.setStatus("current")

fvSectionAttenuationAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 9)
)
fvSectionAttenuationAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmOptPathReference"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmStartOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmStartGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmStartLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmStartLatitude"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmEndOptDist"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmEndGeoDist"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmEndLongitude"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmEndLatitude"))
)
if mibBuilder.loadTexts:
    fvSectionAttenuationAlarmGroup.setStatus("current")

fvRtuRsLinkAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 10)
)
fvRtuRsLinkAlarmGroup.setObjects(
    ("EXFO-FIBERVISOR-MIB", "fvRtuRsLinkAlarmRsReference")
)
if mibBuilder.loadTexts:
    fvRtuRsLinkAlarmGroup.setStatus("current")

fvDriftFreqAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 11)
)
fvDriftFreqAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvDriftFreqAlarmMeasPointReference"),
        ("EXFO-FIBERVISOR-MIB", "fvDriftFreqAlarmChannelName"),
        ("EXFO-FIBERVISOR-MIB", "fvDriftFreqAlarmChannelCenter"))
)
if mibBuilder.loadTexts:
    fvDriftFreqAlarmGroup.setStatus("current")

fvEmptyChannelAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 12)
)
fvEmptyChannelAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvEmptyChannelAlarmMeasPointReference"),
        ("EXFO-FIBERVISOR-MIB", "fvEmptyChannelAlarmChannelName"),
        ("EXFO-FIBERVISOR-MIB", "fvEmptyChannelAlarmChannelCenter"))
)
if mibBuilder.loadTexts:
    fvEmptyChannelAlarmGroup.setStatus("current")

fvSignalLossAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 13)
)
fvSignalLossAlarmGroup.setObjects(
    ("EXFO-FIBERVISOR-MIB", "fvSignalLossAlarmMeasPointReference")
)
if mibBuilder.loadTexts:
    fvSignalLossAlarmGroup.setStatus("current")

fvPowerAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 14)
)
fvPowerAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvPowerAlarmMeasPointReference"),
        ("EXFO-FIBERVISOR-MIB", "fvPowerAlarmChannelName"),
        ("EXFO-FIBERVISOR-MIB", "fvPowerAlarmChannelCenter"))
)
if mibBuilder.loadTexts:
    fvPowerAlarmGroup.setStatus("current")

fvSnrAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 15)
)
fvSnrAlarmGroup.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvSnrAlarmMeasPointReference"),
        ("EXFO-FIBERVISOR-MIB", "fvSnrAlarmChannelName"),
        ("EXFO-FIBERVISOR-MIB", "fvSnrAlarmChannelCenter"),
        ("EXFO-FIBERVISOR-MIB", "fvSnrAlarmChannelSide"))
)
if mibBuilder.loadTexts:
    fvSnrAlarmGroup.setStatus("current")

fvTotalLossAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 16)
)
fvTotalLossAlarmGroup.setObjects(
    ("EXFO-FIBERVISOR-MIB", "fvTotalLossAlarmOptPathReference")
)
if mibBuilder.loadTexts:
    fvTotalLossAlarmGroup.setStatus("current")

fvLaunchLevelAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 17)
)
fvLaunchLevelAlarmGroup.setObjects(
    ("EXFO-FIBERVISOR-MIB", "fvLaunchLevelAlarmOptPathReference")
)
if mibBuilder.loadTexts:
    fvLaunchLevelAlarmGroup.setStatus("current")

fvProcessingErrorAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 1, 18)
)
fvProcessingErrorAlarmGroup.setObjects(
    ("EXFO-FIBERVISOR-MIB", "fvProcessingErrorAlarmSoftwareReference")
)
if mibBuilder.loadTexts:
    fvProcessingErrorAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fvAdvancedCompls = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6718, 3, 1, 1, 2, 1)
)
fvAdvancedCompls.setObjects(
      *(("EXFO-FIBERVISOR-MIB", "fvFiberConfigurationGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvDeviceGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvEndOfAnalysisAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectanceAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvNewEventLossAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvNonReflectDeterLossAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvReflectDeterLossAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvSectionAttenuationAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvTotalLossAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvLaunchLevelAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvRtuRsLinkAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvDriftFreqAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvEmptyChannelAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvSignalLossAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvPowerAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvSnrAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "fvProcessingErrorAlarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "alarmGroup"),
        ("EXFO-FIBERVISOR-MIB", "alarmNotificationGroup"),
        ("EXFO-FIBERVISOR-MIB", "uncontrolledTestRequestGroup"),
        ("EXFO-FIBERVISOR-MIB", "uncontrolledTestResultGroup"),
        ("EXFO-FIBERVISOR-MIB", "uncontrolledTestNotificationGroup"),
        ("EXFO-FIBERVISOR-MIB", "efdGroup"),
        ("EXFO-FIBERVISOR-MIB", "tmnEventStateNotificationGroup"),
        ("EXFO-FIBERVISOR-MIB", "tmnEventObjectNotificationGroup"))
)
if mibBuilder.loadTexts:
    fvAdvancedCompls.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-FIBERVISOR-MIB",
    **{"FvAlarmType": FvAlarmType,
       "FvAlarmStatus": FvAlarmStatus,
       "AlarmThresholdLevel": AlarmThresholdLevel,
       "FvWdmChannelSide": FvWdmChannelSide,
       "exfoFiberVisorMib": exfoFiberVisorMib,
       "fiberVisor": fiberVisor,
       "fiberVisorConf": fiberVisorConf,
       "fiberVisorGroups": fiberVisorGroups,
       "fvFiberConfigurationGroup": fvFiberConfigurationGroup,
       "fvDeviceGroup": fvDeviceGroup,
       "fvAlarmGroup": fvAlarmGroup,
       "fvEndOfAnalysisAlarmGroup": fvEndOfAnalysisAlarmGroup,
       "fvReflectanceAlarmGroup": fvReflectanceAlarmGroup,
       "fvNewEventLossAlarmGroup": fvNewEventLossAlarmGroup,
       "fvNonReflectDeterLossAlarmGroup": fvNonReflectDeterLossAlarmGroup,
       "fvReflectDeterLossAlarmGroup": fvReflectDeterLossAlarmGroup,
       "fvSectionAttenuationAlarmGroup": fvSectionAttenuationAlarmGroup,
       "fvRtuRsLinkAlarmGroup": fvRtuRsLinkAlarmGroup,
       "fvDriftFreqAlarmGroup": fvDriftFreqAlarmGroup,
       "fvEmptyChannelAlarmGroup": fvEmptyChannelAlarmGroup,
       "fvSignalLossAlarmGroup": fvSignalLossAlarmGroup,
       "fvPowerAlarmGroup": fvPowerAlarmGroup,
       "fvSnrAlarmGroup": fvSnrAlarmGroup,
       "fvTotalLossAlarmGroup": fvTotalLossAlarmGroup,
       "fvLaunchLevelAlarmGroup": fvLaunchLevelAlarmGroup,
       "fvProcessingErrorAlarmGroup": fvProcessingErrorAlarmGroup,
       "fiberVisorCompls": fiberVisorCompls,
       "fvAdvancedCompls": fvAdvancedCompls,
       "fiberVisorObjs": fiberVisorObjs,
       "fvFiberConfigurationObjs": fvFiberConfigurationObjs,
       "opticalPathNumber": opticalPathNumber,
       "opticalPathTable": opticalPathTable,
       "opticalPathEntry": opticalPathEntry,
       "opticalPathIndex": opticalPathIndex,
       "opticalPathName": opticalPathName,
       "measurementPointNumber": measurementPointNumber,
       "measurementPointTable": measurementPointTable,
       "measurementPointEntry": measurementPointEntry,
       "measurementPointIndex": measurementPointIndex,
       "measurementPointName": measurementPointName,
       "fvDeviceObjs": fvDeviceObjs,
       "tscNumber": tscNumber,
       "tscTable": tscTable,
       "tscEntry": tscEntry,
       "tscIndex": tscIndex,
       "tscName": tscName,
       "rtuNumber": rtuNumber,
       "rtuTable": rtuTable,
       "rtuEntry": rtuEntry,
       "rtuIndex": rtuIndex,
       "rtuName": rtuName,
       "rsNumber": rsNumber,
       "rsTable": rsTable,
       "rsEntry": rsEntry,
       "rsIndex": rsIndex,
       "rsName": rsName,
       "fvTestObjs": fvTestObjs,
       "fvAlarmObjs": fvAlarmObjs,
       "fvAlarmTable": fvAlarmTable,
       "fvAlarmEntry": fvAlarmEntry,
       "fvAlarmStatus": fvAlarmStatus,
       "fvAlarmType": fvAlarmType,
       "fvAlarmComments": fvAlarmComments,
       "fvEndOfAnalysisAlarmTable": fvEndOfAnalysisAlarmTable,
       "fvEndOfAnalysisAlarmEntry": fvEndOfAnalysisAlarmEntry,
       "fvEndOfAnalysisAlarmOptPathReference": fvEndOfAnalysisAlarmOptPathReference,
       "fvEndOfAnalysisAlarmOptDist": fvEndOfAnalysisAlarmOptDist,
       "fvEndOfAnalysisAlarmGeoDist": fvEndOfAnalysisAlarmGeoDist,
       "fvEndOfAnalysisAlarmLongitude": fvEndOfAnalysisAlarmLongitude,
       "fvEndOfAnalysisAlarmLatitude": fvEndOfAnalysisAlarmLatitude,
       "fvReflectanceAlarmTable": fvReflectanceAlarmTable,
       "fvReflectanceAlarmEntry": fvReflectanceAlarmEntry,
       "fvReflectanceAlarmOptPathReference": fvReflectanceAlarmOptPathReference,
       "fvReflectanceAlarmOptDist": fvReflectanceAlarmOptDist,
       "fvReflectanceAlarmGeoDist": fvReflectanceAlarmGeoDist,
       "fvReflectanceAlarmLongitude": fvReflectanceAlarmLongitude,
       "fvReflectanceAlarmLatitude": fvReflectanceAlarmLatitude,
       "fvNewEventLossAlarmTable": fvNewEventLossAlarmTable,
       "fvNewEventLossAlarmEntry": fvNewEventLossAlarmEntry,
       "fvNewEventLossAlarmOptPathReference": fvNewEventLossAlarmOptPathReference,
       "fvNewEventLossAlarmOptDist": fvNewEventLossAlarmOptDist,
       "fvNewEventLossAlarmGeoDist": fvNewEventLossAlarmGeoDist,
       "fvNewEventLossAlarmLongitude": fvNewEventLossAlarmLongitude,
       "fvNewEventLossAlarmLatitude": fvNewEventLossAlarmLatitude,
       "fvNonReflectDeterLossAlarmTable": fvNonReflectDeterLossAlarmTable,
       "fvNonReflectDeterLossAlarmEntry": fvNonReflectDeterLossAlarmEntry,
       "fvNonReflectDeterLossAlarmOptPathReference": fvNonReflectDeterLossAlarmOptPathReference,
       "fvNonReflectDeterLossAlarmOptDist": fvNonReflectDeterLossAlarmOptDist,
       "fvNonReflectDeterLossAlarmGeoDist": fvNonReflectDeterLossAlarmGeoDist,
       "fvNonReflectDeterLossAlarmLongitude": fvNonReflectDeterLossAlarmLongitude,
       "fvNonReflectDeterLossAlarmLatitude": fvNonReflectDeterLossAlarmLatitude,
       "fvReflectDeterLossAlarmTable": fvReflectDeterLossAlarmTable,
       "fvReflectDeterLossAlarmEntry": fvReflectDeterLossAlarmEntry,
       "fvReflectDeterLossAlarmOptPathReference": fvReflectDeterLossAlarmOptPathReference,
       "fvReflectDeterLossAlarmOptDist": fvReflectDeterLossAlarmOptDist,
       "fvReflectDeterLossAlarmGeoDist": fvReflectDeterLossAlarmGeoDist,
       "fvReflectDeterLossAlarmLongitude": fvReflectDeterLossAlarmLongitude,
       "fvReflectDeterLossAlarmLatitude": fvReflectDeterLossAlarmLatitude,
       "fvSectionAttenuationAlarmTable": fvSectionAttenuationAlarmTable,
       "fvSectionAttenuationAlarmEntry": fvSectionAttenuationAlarmEntry,
       "fvSectionAttenuationAlarmOptPathReference": fvSectionAttenuationAlarmOptPathReference,
       "fvSectionAttenuationAlarmStartOptDist": fvSectionAttenuationAlarmStartOptDist,
       "fvSectionAttenuationAlarmStartGeoDist": fvSectionAttenuationAlarmStartGeoDist,
       "fvSectionAttenuationAlarmStartLongitude": fvSectionAttenuationAlarmStartLongitude,
       "fvSectionAttenuationAlarmStartLatitude": fvSectionAttenuationAlarmStartLatitude,
       "fvSectionAttenuationAlarmEndOptDist": fvSectionAttenuationAlarmEndOptDist,
       "fvSectionAttenuationAlarmEndGeoDist": fvSectionAttenuationAlarmEndGeoDist,
       "fvSectionAttenuationAlarmEndLongitude": fvSectionAttenuationAlarmEndLongitude,
       "fvSectionAttenuationAlarmEndLatitude": fvSectionAttenuationAlarmEndLatitude,
       "fvRtuRsLinkAlarmTable": fvRtuRsLinkAlarmTable,
       "fvRtuRsLinkAlarmEntry": fvRtuRsLinkAlarmEntry,
       "fvRtuRsLinkAlarmRsReference": fvRtuRsLinkAlarmRsReference,
       "fvDriftFreqAlarmTable": fvDriftFreqAlarmTable,
       "fvDriftFreqAlarmEntry": fvDriftFreqAlarmEntry,
       "fvDriftFreqAlarmMeasPointReference": fvDriftFreqAlarmMeasPointReference,
       "fvDriftFreqAlarmChannelName": fvDriftFreqAlarmChannelName,
       "fvDriftFreqAlarmChannelCenter": fvDriftFreqAlarmChannelCenter,
       "fvEmptyChannelAlarmTable": fvEmptyChannelAlarmTable,
       "fvEmptyChannelAlarmEntry": fvEmptyChannelAlarmEntry,
       "fvEmptyChannelAlarmMeasPointReference": fvEmptyChannelAlarmMeasPointReference,
       "fvEmptyChannelAlarmChannelName": fvEmptyChannelAlarmChannelName,
       "fvEmptyChannelAlarmChannelCenter": fvEmptyChannelAlarmChannelCenter,
       "fvSignalLossAlarmTable": fvSignalLossAlarmTable,
       "fvSignalLossAlarmEntry": fvSignalLossAlarmEntry,
       "fvSignalLossAlarmMeasPointReference": fvSignalLossAlarmMeasPointReference,
       "fvPowerAlarmTable": fvPowerAlarmTable,
       "fvPowerAlarmEntry": fvPowerAlarmEntry,
       "fvPowerAlarmMeasPointReference": fvPowerAlarmMeasPointReference,
       "fvPowerAlarmChannelName": fvPowerAlarmChannelName,
       "fvPowerAlarmChannelCenter": fvPowerAlarmChannelCenter,
       "fvSnrAlarmTable": fvSnrAlarmTable,
       "fvSnrAlarmEntry": fvSnrAlarmEntry,
       "fvSnrAlarmMeasPointReference": fvSnrAlarmMeasPointReference,
       "fvSnrAlarmChannelName": fvSnrAlarmChannelName,
       "fvSnrAlarmChannelCenter": fvSnrAlarmChannelCenter,
       "fvSnrAlarmChannelSide": fvSnrAlarmChannelSide,
       "fvTotalLossAlarmTable": fvTotalLossAlarmTable,
       "fvTotalLossAlarmEntry": fvTotalLossAlarmEntry,
       "fvTotalLossAlarmOptPathReference": fvTotalLossAlarmOptPathReference,
       "fvLaunchLevelAlarmTable": fvLaunchLevelAlarmTable,
       "fvLaunchLevelAlarmEntry": fvLaunchLevelAlarmEntry,
       "fvLaunchLevelAlarmOptPathReference": fvLaunchLevelAlarmOptPathReference,
       "fvProcessingErrorAlarmTable": fvProcessingErrorAlarmTable,
       "fvProcessingErrorAlarmEntry": fvProcessingErrorAlarmEntry,
       "fvProcessingErrorAlarmSoftwareReference": fvProcessingErrorAlarmSoftwareReference,
       "fiberVisorEvents": fiberVisorEvents,
       "fvSoftware": fvSoftware,
       "exfoRftsSystemSchedulerManager": exfoRftsSystemSchedulerManager,
       "exfoRftsOtdrMonitoringMonitor": exfoRftsOtdrMonitoringMonitor,
       "exfoRftsSvrClientManagerClientManager": exfoRftsSvrClientManagerClientManager,
       "exfoRftsRFTSMulti": exfoRftsRFTSMulti,
       "exfoRftsSwitchControllerSwitchController": exfoRftsSwitchControllerSwitchController,
       "exfoRftsMwmMonitoringMonitor": exfoRftsMwmMonitoringMonitor,
       "exfoRftsBdsync": exfoRftsBdsync,
       "exfoRftsRtuParamItfOnTscCRtuConfig": exfoRftsRtuParamItfOnTscCRtuConfig,
       "exfoRftsServiceCheckerRTUChecker": exfoRftsServiceCheckerRTUChecker,
       "exfoRftsServiceCheckerDriveSpaceChecker": exfoRftsServiceCheckerDriveSpaceChecker,
       "exfoRftsServiceCheckerAckChecker": exfoRftsServiceCheckerAckChecker,
       "exfoRftsAlarmGenerator": exfoRftsAlarmGenerator,
       "exfoRftsMsgReceiver": exfoRftsMsgReceiver,
       "fvThreshold": fvThreshold,
       "newEventLossThreshold": newEventLossThreshold,
       "nonReflectiveDeteriorationLossThreshold": nonReflectiveDeteriorationLossThreshold,
       "sectionAttenuationThreshold": sectionAttenuationThreshold,
       "totalLossThreshold": totalLossThreshold,
       "reflectanceThreshold": reflectanceThreshold,
       "launchLevelThreshold": launchLevelThreshold,
       "reflectiveDeteriorationLossThreshold": reflectiveDeteriorationLossThreshold,
       "driftFrequencyThreshold": driftFrequencyThreshold,
       "minPowerThreshold": minPowerThreshold,
       "maxPowerThreshold": maxPowerThreshold,
       "snrThreshold": snrThreshold,
       "fvTestCategory": fvTestCategory,
       "opticalPathWithDefaultRefTrace": opticalPathWithDefaultRefTrace,
       "measurementPointWithDefaultRefTrace": measurementPointWithDefaultRefTrace}
)
