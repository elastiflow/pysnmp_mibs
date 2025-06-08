# SNMP MIB module (TN-PMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-PMON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:44 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(TSapIngQueueId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "TSapIngQueueId")

(TItemDescription,
 TQueueId,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TQueueId",
    "TmnxEncapVal",
    "TmnxPortID")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnPmonMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 99)
)
if mibBuilder.loadTexts:
    tnPmonMIBModule.setRevisions(
        ("2013-07-29 00:00",
         "2013-05-20 00:00",
         "2013-03-26 00:00",
         "2012-11-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmPmonPolicyType(TextualConvention, Integer32):
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
        *(("port", 1),
          ("sap", 2),
          ("eth-cfm-two-way-slm", 3),
          ("eth-cfm-two-way-dm", 4),
          ("eth-cfm-two-way-lm", 5))
    )



class AluWdmStatsIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2),
    )



class AluWdmStatsBinNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )



class AluWdmStatsBinStatus(TextualConvention, Integer32):
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
        *(("valid", 1),
          ("rxValid", 2),
          ("txValid", 3),
          ("invalid", 4),
          ("dataNotAvailable", 5),
          ("partial", 6),
          ("adjusted", 7),
          ("dataLong", 8),
          ("dataComplete", 9))
    )



class AluWdmPmonStatsClearType(TextualConvention, Integer32):
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
        *(("port", 1),
          ("sap", 2),
          ("eth-cfm-oam-test", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnPmonObjs_ObjectIdentity = ObjectIdentity
tnPmonObjs = _TnPmonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99)
)
_TnPmonPolicyAttributeTotal_Type = Integer32
_TnPmonPolicyAttributeTotal_Object = MibScalar
tnPmonPolicyAttributeTotal = _TnPmonPolicyAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 1),
    _TnPmonPolicyAttributeTotal_Type()
)
tnPmonPolicyAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonPolicyAttributeTotal.setStatus("current")
_TnPmonPolicyTable_Object = MibTable
tnPmonPolicyTable = _TnPmonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2)
)
if mibBuilder.loadTexts:
    tnPmonPolicyTable.setStatus("current")
_TnPmonPolicyEntry_Object = MibTableRow
tnPmonPolicyEntry = _TnPmonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1)
)
tnPmonPolicyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonPolicyType"),
    (0, "TN-PMON-MIB", "tnPmonPolicyId"),
)
if mibBuilder.loadTexts:
    tnPmonPolicyEntry.setStatus("current")
_TnPmonPolicyType_Type = AluWdmPmonPolicyType
_TnPmonPolicyType_Object = MibTableColumn
tnPmonPolicyType = _TnPmonPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 1),
    _TnPmonPolicyType_Type()
)
tnPmonPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonPolicyType.setStatus("current")


class _TnPmonPolicyId_Type(Integer32):
    """Custom type tnPmonPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnPmonPolicyId_Type.__name__ = "Integer32"
_TnPmonPolicyId_Object = MibTableColumn
tnPmonPolicyId = _TnPmonPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 2),
    _TnPmonPolicyId_Type()
)
tnPmonPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonPolicyId.setStatus("current")
_TnPmonPolicyRowStatus_Type = RowStatus
_TnPmonPolicyRowStatus_Object = MibTableColumn
tnPmonPolicyRowStatus = _TnPmonPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 3),
    _TnPmonPolicyRowStatus_Type()
)
tnPmonPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyRowStatus.setStatus("current")


class _TnPmonPolicyDescription_Type(TItemDescription):
    """Custom type tnPmonPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TnPmonPolicyDescription_Type.__name__ = "TItemDescription"
_TnPmonPolicyDescription_Object = MibTableColumn
tnPmonPolicyDescription = _TnPmonPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 4),
    _TnPmonPolicyDescription_Type()
)
tnPmonPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyDescription.setStatus("current")


class _TnPmonPolicyNumOfBins15Min_Type(Integer32):
    """Custom type tnPmonPolicyNumOfBins15Min based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_TnPmonPolicyNumOfBins15Min_Type.__name__ = "Integer32"
_TnPmonPolicyNumOfBins15Min_Object = MibTableColumn
tnPmonPolicyNumOfBins15Min = _TnPmonPolicyNumOfBins15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 5),
    _TnPmonPolicyNumOfBins15Min_Type()
)
tnPmonPolicyNumOfBins15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyNumOfBins15Min.setStatus("current")


class _TnPmonPolicyNumOfBins1Day_Type(Integer32):
    """Custom type tnPmonPolicyNumOfBins1Day based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnPmonPolicyNumOfBins1Day_Type.__name__ = "Integer32"
_TnPmonPolicyNumOfBins1Day_Object = MibTableColumn
tnPmonPolicyNumOfBins1Day = _TnPmonPolicyNumOfBins1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 6),
    _TnPmonPolicyNumOfBins1Day_Type()
)
tnPmonPolicyNumOfBins1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyNumOfBins1Day.setStatus("current")


class _TnPmonPolicyFlrInterval15Min_Type(Integer32):
    """Custom type tnPmonPolicyFlrInterval15Min based on Integer32"""
    defaultValue = 1


_TnPmonPolicyFlrInterval15Min_Type.__name__ = "Integer32"
_TnPmonPolicyFlrInterval15Min_Object = MibTableColumn
tnPmonPolicyFlrInterval15Min = _TnPmonPolicyFlrInterval15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 7),
    _TnPmonPolicyFlrInterval15Min_Type()
)
tnPmonPolicyFlrInterval15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrInterval15Min.setStatus("current")


class _TnPmonPolicyFlrInterval1Day_Type(Integer32):
    """Custom type tnPmonPolicyFlrInterval1Day based on Integer32"""
    defaultValue = 60


_TnPmonPolicyFlrInterval1Day_Type.__name__ = "Integer32"
_TnPmonPolicyFlrInterval1Day_Object = MibTableColumn
tnPmonPolicyFlrInterval1Day = _TnPmonPolicyFlrInterval1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 8),
    _TnPmonPolicyFlrInterval1Day_Type()
)
tnPmonPolicyFlrInterval1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrInterval1Day.setStatus("current")


class _TnPmonPolicyFlrAvailabilityInterval15Min_Type(Integer32):
    """Custom type tnPmonPolicyFlrAvailabilityInterval15Min based on Integer32"""
    defaultValue = 10


_TnPmonPolicyFlrAvailabilityInterval15Min_Type.__name__ = "Integer32"
_TnPmonPolicyFlrAvailabilityInterval15Min_Object = MibTableColumn
tnPmonPolicyFlrAvailabilityInterval15Min = _TnPmonPolicyFlrAvailabilityInterval15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 9),
    _TnPmonPolicyFlrAvailabilityInterval15Min_Type()
)
tnPmonPolicyFlrAvailabilityInterval15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrAvailabilityInterval15Min.setStatus("current")


class _TnPmonPolicyFlrAvailabilityInterval1Day_Type(Integer32):
    """Custom type tnPmonPolicyFlrAvailabilityInterval1Day based on Integer32"""
    defaultValue = 10


_TnPmonPolicyFlrAvailabilityInterval1Day_Type.__name__ = "Integer32"
_TnPmonPolicyFlrAvailabilityInterval1Day_Object = MibTableColumn
tnPmonPolicyFlrAvailabilityInterval1Day = _TnPmonPolicyFlrAvailabilityInterval1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 2, 1, 10),
    _TnPmonPolicyFlrAvailabilityInterval1Day_Type()
)
tnPmonPolicyFlrAvailabilityInterval1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonPolicyFlrAvailabilityInterval1Day.setStatus("current")
_TnPmonClearAttributeTotal_Type = Integer32
_TnPmonClearAttributeTotal_Object = MibScalar
tnPmonClearAttributeTotal = _TnPmonClearAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 3),
    _TnPmonClearAttributeTotal_Type()
)
tnPmonClearAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonClearAttributeTotal.setStatus("current")
_TnPmonClearTable_Object = MibTable
tnPmonClearTable = _TnPmonClearTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4)
)
if mibBuilder.loadTexts:
    tnPmonClearTable.setStatus("current")
_TnPmonClearEntry_Object = MibTableRow
tnPmonClearEntry = _TnPmonClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1)
)
tnPmonClearEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonClearType"),
)
if mibBuilder.loadTexts:
    tnPmonClearEntry.setStatus("current")
_TnPmonClearType_Type = AluWdmPmonStatsClearType
_TnPmonClearType_Object = MibTableColumn
tnPmonClearType = _TnPmonClearType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 1),
    _TnPmonClearType_Type()
)
tnPmonClearType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonClearType.setStatus("current")
_TnPmonClearPortId_Type = TmnxPortID
_TnPmonClearPortId_Object = MibTableColumn
tnPmonClearPortId = _TnPmonClearPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 2),
    _TnPmonClearPortId_Type()
)
tnPmonClearPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearPortId.setStatus("current")
_TnPmonClearEncapValue_Type = TmnxEncapVal
_TnPmonClearEncapValue_Object = MibTableColumn
tnPmonClearEncapValue = _TnPmonClearEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 3),
    _TnPmonClearEncapValue_Type()
)
tnPmonClearEncapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearEncapValue.setStatus("current")
_TnPmonClearTestName_Type = SnmpAdminString
_TnPmonClearTestName_Object = MibTableColumn
tnPmonClearTestName = _TnPmonClearTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 4),
    _TnPmonClearTestName_Type()
)
tnPmonClearTestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearTestName.setStatus("current")


class _TnPmonClearInterval_Type(AluWdmStatsIntervalType):
    """Custom type tnPmonClearInterval based on AluWdmStatsIntervalType"""
    defaultValue = -1


_TnPmonClearInterval_Type.__name__ = "AluWdmStatsIntervalType"
_TnPmonClearInterval_Object = MibTableColumn
tnPmonClearInterval = _TnPmonClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 5),
    _TnPmonClearInterval_Type()
)
tnPmonClearInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearInterval.setStatus("current")


class _TnPmonClearBin_Type(AluWdmStatsBinNumber):
    """Custom type tnPmonClearBin based on AluWdmStatsBinNumber"""
    defaultValue = -1


_TnPmonClearBin_Type.__name__ = "AluWdmStatsBinNumber"
_TnPmonClearBin_Object = MibTableColumn
tnPmonClearBin = _TnPmonClearBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 4, 1, 6),
    _TnPmonClearBin_Type()
)
tnPmonClearBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPmonClearBin.setStatus("current")
_TnPmonTcaAttributeTotal_Type = Integer32
_TnPmonTcaAttributeTotal_Object = MibScalar
tnPmonTcaAttributeTotal = _TnPmonTcaAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 5),
    _TnPmonTcaAttributeTotal_Type()
)
tnPmonTcaAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonTcaAttributeTotal.setStatus("current")
_TnPmonTcaTable_Object = MibTable
tnPmonTcaTable = _TnPmonTcaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6)
)
if mibBuilder.loadTexts:
    tnPmonTcaTable.setStatus("current")
_TnPmonTcaEntry_Object = MibTableRow
tnPmonTcaEntry = _TnPmonTcaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1)
)
tnPmonTcaEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnPmonPolicyType"),
    (0, "TN-PMON-MIB", "tnPmonPolicyId"),
    (0, "TN-PMON-MIB", "tnPmonTcaInterval"),
    (0, "TN-PMON-MIB", "tnPmonTcaSubgroup"),
    (0, "TN-PMON-MIB", "tnPmonTcaId"),
)
if mibBuilder.loadTexts:
    tnPmonTcaEntry.setStatus("current")
_TnPmonTcaInterval_Type = AluWdmStatsIntervalType
_TnPmonTcaInterval_Object = MibTableColumn
tnPmonTcaInterval = _TnPmonTcaInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 1),
    _TnPmonTcaInterval_Type()
)
tnPmonTcaInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaInterval.setStatus("current")
_TnPmonTcaSubgroup_Type = Integer32
_TnPmonTcaSubgroup_Object = MibTableColumn
tnPmonTcaSubgroup = _TnPmonTcaSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 2),
    _TnPmonTcaSubgroup_Type()
)
tnPmonTcaSubgroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaSubgroup.setStatus("current")
_TnPmonTcaId_Type = Integer32
_TnPmonTcaId_Object = MibTableColumn
tnPmonTcaId = _TnPmonTcaId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 3),
    _TnPmonTcaId_Type()
)
tnPmonTcaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPmonTcaId.setStatus("current")
_TnPmonTcaVariable_Type = ObjectIdentifier
_TnPmonTcaVariable_Object = MibTableColumn
tnPmonTcaVariable = _TnPmonTcaVariable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 4),
    _TnPmonTcaVariable_Type()
)
tnPmonTcaVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPmonTcaVariable.setStatus("current")


class _TnPmonTcaValue_Type(SnmpAdminString):
    """Custom type tnPmonTcaValue based on SnmpAdminString"""
    defaultHexValue = "00"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPmonTcaValue_Type.__name__ = "SnmpAdminString"
_TnPmonTcaValue_Object = MibTableColumn
tnPmonTcaValue = _TnPmonTcaValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 6, 1, 5),
    _TnPmonTcaValue_Type()
)
tnPmonTcaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPmonTcaValue.setStatus("current")
_TnEthPortStatsAttributeTotal_Type = Integer32
_TnEthPortStatsAttributeTotal_Object = MibScalar
tnEthPortStatsAttributeTotal = _TnEthPortStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 7),
    _TnEthPortStatsAttributeTotal_Type()
)
tnEthPortStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsAttributeTotal.setStatus("current")
_TnEthPortStatsTable_Object = MibTable
tnEthPortStatsTable = _TnEthPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8)
)
if mibBuilder.loadTexts:
    tnEthPortStatsTable.setStatus("current")
_TnEthPortStatsEntry_Object = MibTableRow
tnEthPortStatsEntry = _TnEthPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1)
)
tnEthPortStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnEthPortStatsPortId"),
    (0, "TN-PMON-MIB", "tnEthPortStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthPortStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthPortStatsEntry.setStatus("current")
_TnEthPortStatsPortId_Type = TmnxPortID
_TnEthPortStatsPortId_Object = MibTableColumn
tnEthPortStatsPortId = _TnEthPortStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 1),
    _TnEthPortStatsPortId_Type()
)
tnEthPortStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsPortId.setStatus("current")
_TnEthPortStatsInterval_Type = AluWdmStatsIntervalType
_TnEthPortStatsInterval_Object = MibTableColumn
tnEthPortStatsInterval = _TnEthPortStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 2),
    _TnEthPortStatsInterval_Type()
)
tnEthPortStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsInterval.setStatus("current")
_TnEthPortStatsBin_Type = AluWdmStatsBinNumber
_TnEthPortStatsBin_Object = MibTableColumn
tnEthPortStatsBin = _TnEthPortStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 3),
    _TnEthPortStatsBin_Type()
)
tnEthPortStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsBin.setStatus("current")
_TnEthPortStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthPortStatsBinStatus_Object = MibTableColumn
tnEthPortStatsBinStatus = _TnEthPortStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 4),
    _TnEthPortStatsBinStatus_Type()
)
tnEthPortStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsBinStatus.setStatus("current")
_TnEthPortStatsStartTime_Type = DateAndTime
_TnEthPortStatsStartTime_Object = MibTableColumn
tnEthPortStatsStartTime = _TnEthPortStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 5),
    _TnEthPortStatsStartTime_Type()
)
tnEthPortStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsStartTime.setStatus("current")
_TnEthPortStatsTotalMembers_Type = Integer32
_TnEthPortStatsTotalMembers_Object = MibTableColumn
tnEthPortStatsTotalMembers = _TnEthPortStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 6),
    _TnEthPortStatsTotalMembers_Type()
)
tnEthPortStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsTotalMembers.setStatus("current")
_TnEthPortStatsIfInOctets_Type = Counter64
_TnEthPortStatsIfInOctets_Object = MibTableColumn
tnEthPortStatsIfInOctets = _TnEthPortStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 7),
    _TnEthPortStatsIfInOctets_Type()
)
tnEthPortStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInOctets.setStatus("current")
_TnEthPortStatsIfInUcastPkts_Type = Counter64
_TnEthPortStatsIfInUcastPkts_Object = MibTableColumn
tnEthPortStatsIfInUcastPkts = _TnEthPortStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 8),
    _TnEthPortStatsIfInUcastPkts_Type()
)
tnEthPortStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInUcastPkts.setStatus("current")
_TnEthPortStatsIfInDiscards_Type = Counter64
_TnEthPortStatsIfInDiscards_Object = MibTableColumn
tnEthPortStatsIfInDiscards = _TnEthPortStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 9),
    _TnEthPortStatsIfInDiscards_Type()
)
tnEthPortStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInDiscards.setStatus("current")
_TnEthPortStatsIfInErrors_Type = Counter64
_TnEthPortStatsIfInErrors_Object = MibTableColumn
tnEthPortStatsIfInErrors = _TnEthPortStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 10),
    _TnEthPortStatsIfInErrors_Type()
)
tnEthPortStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInErrors.setStatus("current")
_TnEthPortStatsIfInUnknownProtos_Type = Counter64
_TnEthPortStatsIfInUnknownProtos_Object = MibTableColumn
tnEthPortStatsIfInUnknownProtos = _TnEthPortStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 11),
    _TnEthPortStatsIfInUnknownProtos_Type()
)
tnEthPortStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInUnknownProtos.setStatus("current")
_TnEthPortStatsIfInMulticastPkts_Type = Counter64
_TnEthPortStatsIfInMulticastPkts_Object = MibTableColumn
tnEthPortStatsIfInMulticastPkts = _TnEthPortStatsIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 12),
    _TnEthPortStatsIfInMulticastPkts_Type()
)
tnEthPortStatsIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInMulticastPkts.setStatus("current")
_TnEthPortStatsIfInBroadcastPkts_Type = Counter64
_TnEthPortStatsIfInBroadcastPkts_Object = MibTableColumn
tnEthPortStatsIfInBroadcastPkts = _TnEthPortStatsIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 13),
    _TnEthPortStatsIfInBroadcastPkts_Type()
)
tnEthPortStatsIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInBroadcastPkts.setStatus("current")
_TnEthPortStatsIfOutOctets_Type = Counter64
_TnEthPortStatsIfOutOctets_Object = MibTableColumn
tnEthPortStatsIfOutOctets = _TnEthPortStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 14),
    _TnEthPortStatsIfOutOctets_Type()
)
tnEthPortStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutOctets.setStatus("current")
_TnEthPortStatsIfOutUcastPkts_Type = Counter64
_TnEthPortStatsIfOutUcastPkts_Object = MibTableColumn
tnEthPortStatsIfOutUcastPkts = _TnEthPortStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 15),
    _TnEthPortStatsIfOutUcastPkts_Type()
)
tnEthPortStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutUcastPkts.setStatus("current")
_TnEthPortStatsIfOutDiscards_Type = Counter64
_TnEthPortStatsIfOutDiscards_Object = MibTableColumn
tnEthPortStatsIfOutDiscards = _TnEthPortStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 16),
    _TnEthPortStatsIfOutDiscards_Type()
)
tnEthPortStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutDiscards.setStatus("current")
_TnEthPortStatsIfOutErrors_Type = Counter64
_TnEthPortStatsIfOutErrors_Object = MibTableColumn
tnEthPortStatsIfOutErrors = _TnEthPortStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 17),
    _TnEthPortStatsIfOutErrors_Type()
)
tnEthPortStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutErrors.setStatus("current")
_TnEthPortStatsIfOutMulticastPkts_Type = Counter64
_TnEthPortStatsIfOutMulticastPkts_Object = MibTableColumn
tnEthPortStatsIfOutMulticastPkts = _TnEthPortStatsIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 18),
    _TnEthPortStatsIfOutMulticastPkts_Type()
)
tnEthPortStatsIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutMulticastPkts.setStatus("current")
_TnEthPortStatsIfOutBroadcastPkts_Type = Counter64
_TnEthPortStatsIfOutBroadcastPkts_Object = MibTableColumn
tnEthPortStatsIfOutBroadcastPkts = _TnEthPortStatsIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 19),
    _TnEthPortStatsIfOutBroadcastPkts_Type()
)
tnEthPortStatsIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutBroadcastPkts.setStatus("current")
_TnEthPortStatsIfInPkts_Type = Counter64
_TnEthPortStatsIfInPkts_Object = MibTableColumn
tnEthPortStatsIfInPkts = _TnEthPortStatsIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 20),
    _TnEthPortStatsIfInPkts_Type()
)
tnEthPortStatsIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfInPkts.setStatus("current")
_TnEthPortStatsIfOutPkts_Type = Counter64
_TnEthPortStatsIfOutPkts_Object = MibTableColumn
tnEthPortStatsIfOutPkts = _TnEthPortStatsIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 21),
    _TnEthPortStatsIfOutPkts_Type()
)
tnEthPortStatsIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortStatsIfOutPkts.setStatus("current")
_TnEthPortEtherStatsDropEvents_Type = Counter64
_TnEthPortEtherStatsDropEvents_Object = MibTableColumn
tnEthPortEtherStatsDropEvents = _TnEthPortEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 22),
    _TnEthPortEtherStatsDropEvents_Type()
)
tnEthPortEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsDropEvents.setStatus("current")
_TnEthPortEtherStatsBroadcastPkts_Type = Counter64
_TnEthPortEtherStatsBroadcastPkts_Object = MibTableColumn
tnEthPortEtherStatsBroadcastPkts = _TnEthPortEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 23),
    _TnEthPortEtherStatsBroadcastPkts_Type()
)
tnEthPortEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsBroadcastPkts.setStatus("current")
_TnEthPortEtherStatsMulticastPkts_Type = Counter64
_TnEthPortEtherStatsMulticastPkts_Object = MibTableColumn
tnEthPortEtherStatsMulticastPkts = _TnEthPortEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 24),
    _TnEthPortEtherStatsMulticastPkts_Type()
)
tnEthPortEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsMulticastPkts.setStatus("current")
_TnEthPortEtherStatsCRCAlignErrors_Type = Counter64
_TnEthPortEtherStatsCRCAlignErrors_Object = MibTableColumn
tnEthPortEtherStatsCRCAlignErrors = _TnEthPortEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 25),
    _TnEthPortEtherStatsCRCAlignErrors_Type()
)
tnEthPortEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsCRCAlignErrors.setStatus("current")
_TnEthPortEtherStatsUndersizePkts_Type = Counter64
_TnEthPortEtherStatsUndersizePkts_Object = MibTableColumn
tnEthPortEtherStatsUndersizePkts = _TnEthPortEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 26),
    _TnEthPortEtherStatsUndersizePkts_Type()
)
tnEthPortEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsUndersizePkts.setStatus("current")
_TnEthPortEtherStatsOversizePkts_Type = Counter64
_TnEthPortEtherStatsOversizePkts_Object = MibTableColumn
tnEthPortEtherStatsOversizePkts = _TnEthPortEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 27),
    _TnEthPortEtherStatsOversizePkts_Type()
)
tnEthPortEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsOversizePkts.setStatus("current")
_TnEthPortEtherStatsFragments_Type = Counter64
_TnEthPortEtherStatsFragments_Object = MibTableColumn
tnEthPortEtherStatsFragments = _TnEthPortEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 28),
    _TnEthPortEtherStatsFragments_Type()
)
tnEthPortEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsFragments.setStatus("current")
_TnEthPortEtherStatsJabbers_Type = Counter64
_TnEthPortEtherStatsJabbers_Object = MibTableColumn
tnEthPortEtherStatsJabbers = _TnEthPortEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 29),
    _TnEthPortEtherStatsJabbers_Type()
)
tnEthPortEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsJabbers.setStatus("current")
_TnEthPortEtherStatsCollisions_Type = Counter64
_TnEthPortEtherStatsCollisions_Object = MibTableColumn
tnEthPortEtherStatsCollisions = _TnEthPortEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 30),
    _TnEthPortEtherStatsCollisions_Type()
)
tnEthPortEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsCollisions.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts = _TnEthPortEtherStatsHighCapacityPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 31),
    _TnEthPortEtherStatsHighCapacityPkts_Type()
)
tnEthPortEtherStatsHighCapacityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts.setStatus("current")
_TnEthPortEtherStatsHighCapacityOctets_Type = Counter64
_TnEthPortEtherStatsHighCapacityOctets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityOctets = _TnEthPortEtherStatsHighCapacityOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 32),
    _TnEthPortEtherStatsHighCapacityOctets_Type()
)
tnEthPortEtherStatsHighCapacityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityOctets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts64Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts64Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts64Octets = _TnEthPortEtherStatsHighCapacityPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 33),
    _TnEthPortEtherStatsHighCapacityPkts64Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts64Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts65to127Octets = _TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 34),
    _TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts65to127Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts128to255Octets = _TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 35),
    _TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts128to255Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts256to511Octets = _TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 36),
    _TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts256to511Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts512to1023Octets = _TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 37),
    _TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets = _TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 38),
    _TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type()
)
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setStatus("current")
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type = Counter64
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object = MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets = _TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 39),
    _TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type()
)
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setStatus("current")
_TnEthPortDot3StatsAlignmentErrors_Type = Counter64
_TnEthPortDot3StatsAlignmentErrors_Object = MibTableColumn
tnEthPortDot3StatsAlignmentErrors = _TnEthPortDot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 40),
    _TnEthPortDot3StatsAlignmentErrors_Type()
)
tnEthPortDot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsAlignmentErrors.setStatus("current")
_TnEthPortDot3StatsFCSErrors_Type = Counter64
_TnEthPortDot3StatsFCSErrors_Object = MibTableColumn
tnEthPortDot3StatsFCSErrors = _TnEthPortDot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 41),
    _TnEthPortDot3StatsFCSErrors_Type()
)
tnEthPortDot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsFCSErrors.setStatus("current")
_TnEthPortDot3StatsSingleCollisionFrames_Type = Counter64
_TnEthPortDot3StatsSingleCollisionFrames_Object = MibTableColumn
tnEthPortDot3StatsSingleCollisionFrames = _TnEthPortDot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 42),
    _TnEthPortDot3StatsSingleCollisionFrames_Type()
)
tnEthPortDot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsSingleCollisionFrames.setStatus("current")
_TnEthPortDot3StatsMultipleCollisionFrames_Type = Counter64
_TnEthPortDot3StatsMultipleCollisionFrames_Object = MibTableColumn
tnEthPortDot3StatsMultipleCollisionFrames = _TnEthPortDot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 43),
    _TnEthPortDot3StatsMultipleCollisionFrames_Type()
)
tnEthPortDot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsMultipleCollisionFrames.setStatus("current")
_TnEthPortDot3StatsSQETestErrors_Type = Counter64
_TnEthPortDot3StatsSQETestErrors_Object = MibTableColumn
tnEthPortDot3StatsSQETestErrors = _TnEthPortDot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 44),
    _TnEthPortDot3StatsSQETestErrors_Type()
)
tnEthPortDot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsSQETestErrors.setStatus("current")
_TnEthPortDot3StatsDeferredTransmissions_Type = Counter64
_TnEthPortDot3StatsDeferredTransmissions_Object = MibTableColumn
tnEthPortDot3StatsDeferredTransmissions = _TnEthPortDot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 45),
    _TnEthPortDot3StatsDeferredTransmissions_Type()
)
tnEthPortDot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsDeferredTransmissions.setStatus("current")
_TnEthPortDot3StatsLateCollisions_Type = Counter64
_TnEthPortDot3StatsLateCollisions_Object = MibTableColumn
tnEthPortDot3StatsLateCollisions = _TnEthPortDot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 46),
    _TnEthPortDot3StatsLateCollisions_Type()
)
tnEthPortDot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsLateCollisions.setStatus("current")
_TnEthPortDot3StatsExcessiveCollisions_Type = Counter64
_TnEthPortDot3StatsExcessiveCollisions_Object = MibTableColumn
tnEthPortDot3StatsExcessiveCollisions = _TnEthPortDot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 47),
    _TnEthPortDot3StatsExcessiveCollisions_Type()
)
tnEthPortDot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsExcessiveCollisions.setStatus("current")
_TnEthPortDot3StatsInternalMacTransmitErrors_Type = Counter64
_TnEthPortDot3StatsInternalMacTransmitErrors_Object = MibTableColumn
tnEthPortDot3StatsInternalMacTransmitErrors = _TnEthPortDot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 48),
    _TnEthPortDot3StatsInternalMacTransmitErrors_Type()
)
tnEthPortDot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsInternalMacTransmitErrors.setStatus("current")
_TnEthPortDot3StatsCarrierSenseErrors_Type = Counter64
_TnEthPortDot3StatsCarrierSenseErrors_Object = MibTableColumn
tnEthPortDot3StatsCarrierSenseErrors = _TnEthPortDot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 49),
    _TnEthPortDot3StatsCarrierSenseErrors_Type()
)
tnEthPortDot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsCarrierSenseErrors.setStatus("current")
_TnEthPortDot3StatsFrameTooLongs_Type = Counter64
_TnEthPortDot3StatsFrameTooLongs_Object = MibTableColumn
tnEthPortDot3StatsFrameTooLongs = _TnEthPortDot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 50),
    _TnEthPortDot3StatsFrameTooLongs_Type()
)
tnEthPortDot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsFrameTooLongs.setStatus("current")
_TnEthPortDot3StatsInternalMacReceiveErrors_Type = Counter64
_TnEthPortDot3StatsInternalMacReceiveErrors_Object = MibTableColumn
tnEthPortDot3StatsInternalMacReceiveErrors = _TnEthPortDot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 51),
    _TnEthPortDot3StatsInternalMacReceiveErrors_Type()
)
tnEthPortDot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsInternalMacReceiveErrors.setStatus("current")
_TnEthPortDot3StatsSymbolErrors_Type = Counter64
_TnEthPortDot3StatsSymbolErrors_Object = MibTableColumn
tnEthPortDot3StatsSymbolErrors = _TnEthPortDot3StatsSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 8, 1, 52),
    _TnEthPortDot3StatsSymbolErrors_Type()
)
tnEthPortDot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortDot3StatsSymbolErrors.setStatus("current")
_TnEthPortEgrQueueStatsAttributeTotal_Type = Integer32
_TnEthPortEgrQueueStatsAttributeTotal_Object = MibScalar
tnEthPortEgrQueueStatsAttributeTotal = _TnEthPortEgrQueueStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 9),
    _TnEthPortEgrQueueStatsAttributeTotal_Type()
)
tnEthPortEgrQueueStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsAttributeTotal.setStatus("current")
_TnEthPortEgrQueueStatsTable_Object = MibTable
tnEthPortEgrQueueStatsTable = _TnEthPortEgrQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10)
)
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsTable.setStatus("current")
_TnEthPortEgrQueueStatsEntry_Object = MibTableRow
tnEthPortEgrQueueStatsEntry = _TnEthPortEgrQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1)
)
tnEthPortEgrQueueStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnEthPortStatsPortId"),
    (0, "TN-PMON-MIB", "tnEthPortStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthPortStatsBin"),
    (0, "TN-PMON-MIB", "tnEthPortStatsQueueId"),
)
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsEntry.setStatus("current")


class _TnEthPortStatsQueueId_Type(TQueueId):
    """Custom type tnEthPortStatsQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnEthPortStatsQueueId_Type.__name__ = "TQueueId"
_TnEthPortStatsQueueId_Object = MibTableColumn
tnEthPortStatsQueueId = _TnEthPortStatsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 1),
    _TnEthPortStatsQueueId_Type()
)
tnEthPortStatsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthPortStatsQueueId.setStatus("current")
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsForwarded = _TnEthPortEgrQueueStatsInProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 2),
    _TnEthPortEgrQueueStatsInProfilePktsForwarded_Type()
)
tnEthPortEgrQueueStatsInProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfilePktsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded = _TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 3),
    _TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type()
)
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsForwarded = _TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 4),
    _TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type()
)
tnEthPortEgrQueueStatsInProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfileOctetsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded = _TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 5),
    _TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type()
)
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setStatus("current")
_TnEthPortEgrQueueStatsInProfilePktsDropped_Type = Counter64
_TnEthPortEgrQueueStatsInProfilePktsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsDropped = _TnEthPortEgrQueueStatsInProfilePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 6),
    _TnEthPortEgrQueueStatsInProfilePktsDropped_Type()
)
tnEthPortEgrQueueStatsInProfilePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfilePktsDropped.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsDropped = _TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 7),
    _TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type()
)
tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setStatus("current")
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Type = Counter64
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsDropped = _TnEthPortEgrQueueStatsInProfileOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 8),
    _TnEthPortEgrQueueStatsInProfileOctetsDropped_Type()
)
tnEthPortEgrQueueStatsInProfileOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsInProfileOctetsDropped.setStatus("current")
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type = Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object = MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped = _TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 10, 1, 9),
    _TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type()
)
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setStatus("current")
_TnSapStatsAttributeTotal_Type = Integer32
_TnSapStatsAttributeTotal_Object = MibScalar
tnSapStatsAttributeTotal = _TnSapStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 11),
    _TnSapStatsAttributeTotal_Type()
)
tnSapStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsAttributeTotal.setStatus("current")
_TnSapStatsTable_Object = MibTable
tnSapStatsTable = _TnSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12)
)
if mibBuilder.loadTexts:
    tnSapStatsTable.setStatus("current")
_TnSapStatsEntry_Object = MibTableRow
tnSapStatsEntry = _TnSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1)
)
tnSapStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnSapStatsPortId"),
    (0, "TN-PMON-MIB", "tnSapStatsEncapVal"),
    (0, "TN-PMON-MIB", "tnSapStatsInterval"),
    (0, "TN-PMON-MIB", "tnSapStatsBin"),
)
if mibBuilder.loadTexts:
    tnSapStatsEntry.setStatus("current")
_TnSapStatsPortId_Type = TmnxPortID
_TnSapStatsPortId_Object = MibTableColumn
tnSapStatsPortId = _TnSapStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 1),
    _TnSapStatsPortId_Type()
)
tnSapStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsPortId.setStatus("current")
_TnSapStatsEncapVal_Type = TmnxEncapVal
_TnSapStatsEncapVal_Object = MibTableColumn
tnSapStatsEncapVal = _TnSapStatsEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 2),
    _TnSapStatsEncapVal_Type()
)
tnSapStatsEncapVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsEncapVal.setStatus("current")
_TnSapStatsInterval_Type = AluWdmStatsIntervalType
_TnSapStatsInterval_Object = MibTableColumn
tnSapStatsInterval = _TnSapStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 3),
    _TnSapStatsInterval_Type()
)
tnSapStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsInterval.setStatus("current")
_TnSapStatsBin_Type = AluWdmStatsBinNumber
_TnSapStatsBin_Object = MibTableColumn
tnSapStatsBin = _TnSapStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 4),
    _TnSapStatsBin_Type()
)
tnSapStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsBin.setStatus("current")
_TnSapStatsBinStatus_Type = AluWdmStatsBinStatus
_TnSapStatsBinStatus_Object = MibTableColumn
tnSapStatsBinStatus = _TnSapStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 5),
    _TnSapStatsBinStatus_Type()
)
tnSapStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsBinStatus.setStatus("current")
_TnSapStatsStartTime_Type = DateAndTime
_TnSapStatsStartTime_Object = MibTableColumn
tnSapStatsStartTime = _TnSapStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 6),
    _TnSapStatsStartTime_Type()
)
tnSapStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsStartTime.setStatus("current")
_TnSapStatsTotalMembers_Type = Integer32
_TnSapStatsTotalMembers_Object = MibTableColumn
tnSapStatsTotalMembers = _TnSapStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 7),
    _TnSapStatsTotalMembers_Type()
)
tnSapStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsTotalMembers.setStatus("current")
_TnSapStatsIngressPktsForwarded_Type = Counter64
_TnSapStatsIngressPktsForwarded_Object = MibTableColumn
tnSapStatsIngressPktsForwarded = _TnSapStatsIngressPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 8),
    _TnSapStatsIngressPktsForwarded_Type()
)
tnSapStatsIngressPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressPktsForwarded.setStatus("current")
_TnSapStatsIngressOctetsForwarded_Type = Counter64
_TnSapStatsIngressOctetsForwarded_Object = MibTableColumn
tnSapStatsIngressOctetsForwarded = _TnSapStatsIngressOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 9),
    _TnSapStatsIngressOctetsForwarded_Type()
)
tnSapStatsIngressOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressOctetsForwarded.setStatus("current")
_TnSapStatsEgressPktsForwarded_Type = Counter64
_TnSapStatsEgressPktsForwarded_Object = MibTableColumn
tnSapStatsEgressPktsForwarded = _TnSapStatsEgressPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 10),
    _TnSapStatsEgressPktsForwarded_Type()
)
tnSapStatsEgressPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsEgressPktsForwarded.setStatus("current")
_TnSapStatsEgressOctetsForwarded_Type = Counter64
_TnSapStatsEgressOctetsForwarded_Object = MibTableColumn
tnSapStatsEgressOctetsForwarded = _TnSapStatsEgressOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 11),
    _TnSapStatsEgressOctetsForwarded_Type()
)
tnSapStatsEgressOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsEgressOctetsForwarded.setStatus("current")
_TnSapStatsIngressPktsDropped_Type = Counter64
_TnSapStatsIngressPktsDropped_Object = MibTableColumn
tnSapStatsIngressPktsDropped = _TnSapStatsIngressPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 12),
    _TnSapStatsIngressPktsDropped_Type()
)
tnSapStatsIngressPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressPktsDropped.setStatus("current")
_TnSapStatsIngressOctetsDropped_Type = Counter64
_TnSapStatsIngressOctetsDropped_Object = MibTableColumn
tnSapStatsIngressOctetsDropped = _TnSapStatsIngressOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 13),
    _TnSapStatsIngressOctetsDropped_Type()
)
tnSapStatsIngressOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressOctetsDropped.setStatus("current")
_TnSapStatsIngressExtraTagPktsDropped_Type = Counter64
_TnSapStatsIngressExtraTagPktsDropped_Object = MibTableColumn
tnSapStatsIngressExtraTagPktsDropped = _TnSapStatsIngressExtraTagPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 14),
    _TnSapStatsIngressExtraTagPktsDropped_Type()
)
tnSapStatsIngressExtraTagPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressExtraTagPktsDropped.setStatus("current")
_TnSapStatsIngressExtraTagOctetsDropped_Type = Counter64
_TnSapStatsIngressExtraTagOctetsDropped_Object = MibTableColumn
tnSapStatsIngressExtraTagOctetsDropped = _TnSapStatsIngressExtraTagOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 12, 1, 15),
    _TnSapStatsIngressExtraTagOctetsDropped_Type()
)
tnSapStatsIngressExtraTagOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapStatsIngressExtraTagOctetsDropped.setStatus("current")
_TnSapMeterStatsAttributeTotal_Type = Integer32
_TnSapMeterStatsAttributeTotal_Object = MibScalar
tnSapMeterStatsAttributeTotal = _TnSapMeterStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 13),
    _TnSapMeterStatsAttributeTotal_Type()
)
tnSapMeterStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsAttributeTotal.setStatus("current")
_TnSapMeterStatsTable_Object = MibTable
tnSapMeterStatsTable = _TnSapMeterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14)
)
if mibBuilder.loadTexts:
    tnSapMeterStatsTable.setStatus("current")
_TnSapMeterStatsEntry_Object = MibTableRow
tnSapMeterStatsEntry = _TnSapMeterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1)
)
tnSapMeterStatsEntry.setIndexNames(
    (0, "TN-PMON-MIB", "tnSapStatsPortId"),
    (0, "TN-PMON-MIB", "tnSapStatsEncapVal"),
    (0, "TN-PMON-MIB", "tnSapStatsInterval"),
    (0, "TN-PMON-MIB", "tnSapStatsBin"),
    (0, "TN-PMON-MIB", "tnSapStatsMeterId"),
)
if mibBuilder.loadTexts:
    tnSapMeterStatsEntry.setStatus("current")
_TnSapStatsMeterId_Type = TSapIngQueueId
_TnSapStatsMeterId_Object = MibTableColumn
tnSapStatsMeterId = _TnSapStatsMeterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 1),
    _TnSapStatsMeterId_Type()
)
tnSapStatsMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapStatsMeterId.setStatus("current")
_TnSapMeterStatsInProfilePktsForwarded_Type = Counter64
_TnSapMeterStatsInProfilePktsForwarded_Object = MibTableColumn
tnSapMeterStatsInProfilePktsForwarded = _TnSapMeterStatsInProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 2),
    _TnSapMeterStatsInProfilePktsForwarded_Type()
)
tnSapMeterStatsInProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsInProfilePktsForwarded.setStatus("current")
_TnSapMeterStatsOutOfProfilePktsForwarded_Type = Counter64
_TnSapMeterStatsOutOfProfilePktsForwarded_Object = MibTableColumn
tnSapMeterStatsOutOfProfilePktsForwarded = _TnSapMeterStatsOutOfProfilePktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 3),
    _TnSapMeterStatsOutOfProfilePktsForwarded_Type()
)
tnSapMeterStatsOutOfProfilePktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsOutOfProfilePktsForwarded.setStatus("current")
_TnSapMeterStatsInProfileOctetsForwarded_Type = Counter64
_TnSapMeterStatsInProfileOctetsForwarded_Object = MibTableColumn
tnSapMeterStatsInProfileOctetsForwarded = _TnSapMeterStatsInProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 4),
    _TnSapMeterStatsInProfileOctetsForwarded_Type()
)
tnSapMeterStatsInProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsInProfileOctetsForwarded.setStatus("current")
_TnSapMeterStatsOutOfProfileOctetsForwarded_Type = Counter64
_TnSapMeterStatsOutOfProfileOctetsForwarded_Object = MibTableColumn
tnSapMeterStatsOutOfProfileOctetsForwarded = _TnSapMeterStatsOutOfProfileOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 14, 1, 5),
    _TnSapMeterStatsOutOfProfileOctetsForwarded_Type()
)
tnSapMeterStatsOutOfProfileOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapMeterStatsOutOfProfileOctetsForwarded.setStatus("current")
_TnEthCfmTWSlmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWSlmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWSlmStatsAttributeTotal = _TnEthCfmTWSlmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 15),
    _TnEthCfmTWSlmStatsAttributeTotal_Type()
)
tnEthCfmTWSlmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWSlmStatsTable_Object = MibTable
tnEthCfmTWSlmStatsTable = _TnEthCfmTWSlmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16)
)
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTable.setStatus("current")
_TnEthCfmTWSlmStatsEntry_Object = MibTableRow
tnEthCfmTWSlmStatsEntry = _TnEthCfmTWSlmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1)
)
tnEthCfmTWSlmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWSlmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsEntry.setStatus("current")
_TnEthCfmTWSlmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWSlmStatsTestName_Object = MibTableColumn
tnEthCfmTWSlmStatsTestName = _TnEthCfmTWSlmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 1),
    _TnEthCfmTWSlmStatsTestName_Type()
)
tnEthCfmTWSlmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTestName.setStatus("current")
_TnEthCfmTWSlmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWSlmStatsInterval_Object = MibTableColumn
tnEthCfmTWSlmStatsInterval = _TnEthCfmTWSlmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 2),
    _TnEthCfmTWSlmStatsInterval_Type()
)
tnEthCfmTWSlmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsInterval.setStatus("current")
_TnEthCfmTWSlmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWSlmStatsBin_Object = MibTableColumn
tnEthCfmTWSlmStatsBin = _TnEthCfmTWSlmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 3),
    _TnEthCfmTWSlmStatsBin_Type()
)
tnEthCfmTWSlmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsBin.setStatus("current")
_TnEthCfmTWSlmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWSlmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWSlmStatsBinStatus = _TnEthCfmTWSlmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 4),
    _TnEthCfmTWSlmStatsBinStatus_Type()
)
tnEthCfmTWSlmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsBinStatus.setStatus("current")
_TnEthCfmTWSlmStatsStartTime_Type = DateAndTime
_TnEthCfmTWSlmStatsStartTime_Object = MibTableColumn
tnEthCfmTWSlmStatsStartTime = _TnEthCfmTWSlmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 5),
    _TnEthCfmTWSlmStatsStartTime_Type()
)
tnEthCfmTWSlmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsStartTime.setStatus("current")
_TnEthCfmTWSlmStatsTotalMembers_Type = Integer32
_TnEthCfmTWSlmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWSlmStatsTotalMembers = _TnEthCfmTWSlmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 6),
    _TnEthCfmTWSlmStatsTotalMembers_Type()
)
tnEthCfmTWSlmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsTotalMembers.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin = _TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 7),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage = _TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 8),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax = _TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 9),
    _TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type()
)
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin = _TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 10),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage = _TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 11),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax = _TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 12),
    _TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type()
)
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWSlmStatsNearEndHighLoss_Type = Integer32
_TnEthCfmTWSlmStatsNearEndHighLoss_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndHighLoss = _TnEthCfmTWSlmStatsNearEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 13),
    _TnEthCfmTWSlmStatsNearEndHighLoss_Type()
)
tnEthCfmTWSlmStatsNearEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndHighLoss.setStatus("current")
_TnEthCfmTWSlmStatsFarEndHighLoss_Type = Integer32
_TnEthCfmTWSlmStatsFarEndHighLoss_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndHighLoss = _TnEthCfmTWSlmStatsFarEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 14),
    _TnEthCfmTWSlmStatsFarEndHighLoss_Type()
)
tnEthCfmTWSlmStatsFarEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndHighLoss.setStatus("current")
_TnEthCfmTWSlmStatsNearEndUnavailable_Type = Integer32
_TnEthCfmTWSlmStatsNearEndUnavailable_Object = MibTableColumn
tnEthCfmTWSlmStatsNearEndUnavailable = _TnEthCfmTWSlmStatsNearEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 15),
    _TnEthCfmTWSlmStatsNearEndUnavailable_Type()
)
tnEthCfmTWSlmStatsNearEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsNearEndUnavailable.setStatus("current")
_TnEthCfmTWSlmStatsFarEndUnavailable_Type = Integer32
_TnEthCfmTWSlmStatsFarEndUnavailable_Object = MibTableColumn
tnEthCfmTWSlmStatsFarEndUnavailable = _TnEthCfmTWSlmStatsFarEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 16, 1, 16),
    _TnEthCfmTWSlmStatsFarEndUnavailable_Type()
)
tnEthCfmTWSlmStatsFarEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWSlmStatsFarEndUnavailable.setStatus("current")
_TnEthCfmTWDmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWDmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWDmStatsAttributeTotal = _TnEthCfmTWDmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 17),
    _TnEthCfmTWDmStatsAttributeTotal_Type()
)
tnEthCfmTWDmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWDmStatsTable_Object = MibTable
tnEthCfmTWDmStatsTable = _TnEthCfmTWDmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18)
)
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTable.setStatus("current")
_TnEthCfmTWDmStatsEntry_Object = MibTableRow
tnEthCfmTWDmStatsEntry = _TnEthCfmTWDmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1)
)
tnEthCfmTWDmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWDmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsEntry.setStatus("current")
_TnEthCfmTWDmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWDmStatsTestName_Object = MibTableColumn
tnEthCfmTWDmStatsTestName = _TnEthCfmTWDmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 1),
    _TnEthCfmTWDmStatsTestName_Type()
)
tnEthCfmTWDmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTestName.setStatus("current")
_TnEthCfmTWDmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWDmStatsInterval_Object = MibTableColumn
tnEthCfmTWDmStatsInterval = _TnEthCfmTWDmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 2),
    _TnEthCfmTWDmStatsInterval_Type()
)
tnEthCfmTWDmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsInterval.setStatus("current")
_TnEthCfmTWDmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWDmStatsBin_Object = MibTableColumn
tnEthCfmTWDmStatsBin = _TnEthCfmTWDmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 3),
    _TnEthCfmTWDmStatsBin_Type()
)
tnEthCfmTWDmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsBin.setStatus("current")
_TnEthCfmTWDmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWDmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWDmStatsBinStatus = _TnEthCfmTWDmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 4),
    _TnEthCfmTWDmStatsBinStatus_Type()
)
tnEthCfmTWDmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsBinStatus.setStatus("current")
_TnEthCfmTWDmStatsStartTime_Type = DateAndTime
_TnEthCfmTWDmStatsStartTime_Object = MibTableColumn
tnEthCfmTWDmStatsStartTime = _TnEthCfmTWDmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 5),
    _TnEthCfmTWDmStatsStartTime_Type()
)
tnEthCfmTWDmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsStartTime.setStatus("current")
_TnEthCfmTWDmStatsTotalMembers_Type = Integer32
_TnEthCfmTWDmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWDmStatsTotalMembers = _TnEthCfmTWDmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 6),
    _TnEthCfmTWDmStatsTotalMembers_Type()
)
tnEthCfmTWDmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsTotalMembers.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMin = _TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 7),
    _TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayAverage = _TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 8),
    _TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMax = _TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 9),
    _TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type()
)
tnEthCfmTWDmStatsRoundTripFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsRoundTripFrameDelayMax.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin = _TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 10),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage = _TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 11),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax = _TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 12),
    _TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin = _TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 13),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage = _TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 14),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax = _TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 15),
    _TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMin = _TnEthCfmTWDmStatsNearEndFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 16),
    _TnEthCfmTWDmStatsNearEndFrameDelayMin_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayAverage = _TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 17),
    _TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMax = _TnEthCfmTWDmStatsNearEndFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 18),
    _TnEthCfmTWDmStatsNearEndFrameDelayMax_Type()
)
tnEthCfmTWDmStatsNearEndFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsNearEndFrameDelayMax.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMin = _TnEthCfmTWDmStatsFarEndFrameDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 19),
    _TnEthCfmTWDmStatsFarEndFrameDelayMin_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayMin.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayAverage = _TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 20),
    _TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayAverage.setStatus("current")
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Type = Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Object = MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMax = _TnEthCfmTWDmStatsFarEndFrameDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 18, 1, 21),
    _TnEthCfmTWDmStatsFarEndFrameDelayMax_Type()
)
tnEthCfmTWDmStatsFarEndFrameDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWDmStatsFarEndFrameDelayMax.setStatus("current")
_TnEthCfmTWLmStatsAttributeTotal_Type = Integer32
_TnEthCfmTWLmStatsAttributeTotal_Object = MibScalar
tnEthCfmTWLmStatsAttributeTotal = _TnEthCfmTWLmStatsAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 19),
    _TnEthCfmTWLmStatsAttributeTotal_Type()
)
tnEthCfmTWLmStatsAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsAttributeTotal.setStatus("current")
_TnEthCfmTWLmStatsTable_Object = MibTable
tnEthCfmTWLmStatsTable = _TnEthCfmTWLmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20)
)
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTable.setStatus("current")
_TnEthCfmTWLmStatsEntry_Object = MibTableRow
tnEthCfmTWLmStatsEntry = _TnEthCfmTWLmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1)
)
tnEthCfmTWLmStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsTestName"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsInterval"),
    (0, "TN-PMON-MIB", "tnEthCfmTWLmStatsBin"),
)
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsEntry.setStatus("current")
_TnEthCfmTWLmStatsTestName_Type = SnmpAdminString
_TnEthCfmTWLmStatsTestName_Object = MibTableColumn
tnEthCfmTWLmStatsTestName = _TnEthCfmTWLmStatsTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 1),
    _TnEthCfmTWLmStatsTestName_Type()
)
tnEthCfmTWLmStatsTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTestName.setStatus("current")
_TnEthCfmTWLmStatsInterval_Type = AluWdmStatsIntervalType
_TnEthCfmTWLmStatsInterval_Object = MibTableColumn
tnEthCfmTWLmStatsInterval = _TnEthCfmTWLmStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 2),
    _TnEthCfmTWLmStatsInterval_Type()
)
tnEthCfmTWLmStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsInterval.setStatus("current")
_TnEthCfmTWLmStatsBin_Type = AluWdmStatsBinNumber
_TnEthCfmTWLmStatsBin_Object = MibTableColumn
tnEthCfmTWLmStatsBin = _TnEthCfmTWLmStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 3),
    _TnEthCfmTWLmStatsBin_Type()
)
tnEthCfmTWLmStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsBin.setStatus("current")
_TnEthCfmTWLmStatsBinStatus_Type = AluWdmStatsBinStatus
_TnEthCfmTWLmStatsBinStatus_Object = MibTableColumn
tnEthCfmTWLmStatsBinStatus = _TnEthCfmTWLmStatsBinStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 4),
    _TnEthCfmTWLmStatsBinStatus_Type()
)
tnEthCfmTWLmStatsBinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsBinStatus.setStatus("current")
_TnEthCfmTWLmStatsStartTime_Type = DateAndTime
_TnEthCfmTWLmStatsStartTime_Object = MibTableColumn
tnEthCfmTWLmStatsStartTime = _TnEthCfmTWLmStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 5),
    _TnEthCfmTWLmStatsStartTime_Type()
)
tnEthCfmTWLmStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsStartTime.setStatus("current")
_TnEthCfmTWLmStatsTotalMembers_Type = Integer32
_TnEthCfmTWLmStatsTotalMembers_Object = MibTableColumn
tnEthCfmTWLmStatsTotalMembers = _TnEthCfmTWLmStatsTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 6),
    _TnEthCfmTWLmStatsTotalMembers_Type()
)
tnEthCfmTWLmStatsTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsTotalMembers.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMin = _TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 7),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage = _TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 8),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMax = _TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 9),
    _TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type()
)
tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMin = _TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 10),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage = _TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 11),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setStatus("current")
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type = Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMax = _TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 12),
    _TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type()
)
tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setStatus("current")
_TnEthCfmTWLmStatsNearEndHighLoss_Type = Integer32
_TnEthCfmTWLmStatsNearEndHighLoss_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndHighLoss = _TnEthCfmTWLmStatsNearEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 13),
    _TnEthCfmTWLmStatsNearEndHighLoss_Type()
)
tnEthCfmTWLmStatsNearEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndHighLoss.setStatus("current")
_TnEthCfmTWLmStatsFarEndHighLoss_Type = Integer32
_TnEthCfmTWLmStatsFarEndHighLoss_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndHighLoss = _TnEthCfmTWLmStatsFarEndHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 14),
    _TnEthCfmTWLmStatsFarEndHighLoss_Type()
)
tnEthCfmTWLmStatsFarEndHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndHighLoss.setStatus("current")
_TnEthCfmTWLmStatsNearEndUnavailable_Type = Integer32
_TnEthCfmTWLmStatsNearEndUnavailable_Object = MibTableColumn
tnEthCfmTWLmStatsNearEndUnavailable = _TnEthCfmTWLmStatsNearEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 15),
    _TnEthCfmTWLmStatsNearEndUnavailable_Type()
)
tnEthCfmTWLmStatsNearEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsNearEndUnavailable.setStatus("current")
_TnEthCfmTWLmStatsFarEndUnavailable_Type = Integer32
_TnEthCfmTWLmStatsFarEndUnavailable_Object = MibTableColumn
tnEthCfmTWLmStatsFarEndUnavailable = _TnEthCfmTWLmStatsFarEndUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 99, 20, 1, 16),
    _TnEthCfmTWLmStatsFarEndUnavailable_Type()
)
tnEthCfmTWLmStatsFarEndUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthCfmTWLmStatsFarEndUnavailable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PMON-MIB",
    **{"AluWdmPmonPolicyType": AluWdmPmonPolicyType,
       "AluWdmStatsIntervalType": AluWdmStatsIntervalType,
       "AluWdmStatsBinNumber": AluWdmStatsBinNumber,
       "AluWdmStatsBinStatus": AluWdmStatsBinStatus,
       "AluWdmPmonStatsClearType": AluWdmPmonStatsClearType,
       "tnPmonMIBModule": tnPmonMIBModule,
       "tnPmonObjs": tnPmonObjs,
       "tnPmonPolicyAttributeTotal": tnPmonPolicyAttributeTotal,
       "tnPmonPolicyTable": tnPmonPolicyTable,
       "tnPmonPolicyEntry": tnPmonPolicyEntry,
       "tnPmonPolicyType": tnPmonPolicyType,
       "tnPmonPolicyId": tnPmonPolicyId,
       "tnPmonPolicyRowStatus": tnPmonPolicyRowStatus,
       "tnPmonPolicyDescription": tnPmonPolicyDescription,
       "tnPmonPolicyNumOfBins15Min": tnPmonPolicyNumOfBins15Min,
       "tnPmonPolicyNumOfBins1Day": tnPmonPolicyNumOfBins1Day,
       "tnPmonPolicyFlrInterval15Min": tnPmonPolicyFlrInterval15Min,
       "tnPmonPolicyFlrInterval1Day": tnPmonPolicyFlrInterval1Day,
       "tnPmonPolicyFlrAvailabilityInterval15Min": tnPmonPolicyFlrAvailabilityInterval15Min,
       "tnPmonPolicyFlrAvailabilityInterval1Day": tnPmonPolicyFlrAvailabilityInterval1Day,
       "tnPmonClearAttributeTotal": tnPmonClearAttributeTotal,
       "tnPmonClearTable": tnPmonClearTable,
       "tnPmonClearEntry": tnPmonClearEntry,
       "tnPmonClearType": tnPmonClearType,
       "tnPmonClearPortId": tnPmonClearPortId,
       "tnPmonClearEncapValue": tnPmonClearEncapValue,
       "tnPmonClearTestName": tnPmonClearTestName,
       "tnPmonClearInterval": tnPmonClearInterval,
       "tnPmonClearBin": tnPmonClearBin,
       "tnPmonTcaAttributeTotal": tnPmonTcaAttributeTotal,
       "tnPmonTcaTable": tnPmonTcaTable,
       "tnPmonTcaEntry": tnPmonTcaEntry,
       "tnPmonTcaInterval": tnPmonTcaInterval,
       "tnPmonTcaSubgroup": tnPmonTcaSubgroup,
       "tnPmonTcaId": tnPmonTcaId,
       "tnPmonTcaVariable": tnPmonTcaVariable,
       "tnPmonTcaValue": tnPmonTcaValue,
       "tnEthPortStatsAttributeTotal": tnEthPortStatsAttributeTotal,
       "tnEthPortStatsTable": tnEthPortStatsTable,
       "tnEthPortStatsEntry": tnEthPortStatsEntry,
       "tnEthPortStatsPortId": tnEthPortStatsPortId,
       "tnEthPortStatsInterval": tnEthPortStatsInterval,
       "tnEthPortStatsBin": tnEthPortStatsBin,
       "tnEthPortStatsBinStatus": tnEthPortStatsBinStatus,
       "tnEthPortStatsStartTime": tnEthPortStatsStartTime,
       "tnEthPortStatsTotalMembers": tnEthPortStatsTotalMembers,
       "tnEthPortStatsIfInOctets": tnEthPortStatsIfInOctets,
       "tnEthPortStatsIfInUcastPkts": tnEthPortStatsIfInUcastPkts,
       "tnEthPortStatsIfInDiscards": tnEthPortStatsIfInDiscards,
       "tnEthPortStatsIfInErrors": tnEthPortStatsIfInErrors,
       "tnEthPortStatsIfInUnknownProtos": tnEthPortStatsIfInUnknownProtos,
       "tnEthPortStatsIfInMulticastPkts": tnEthPortStatsIfInMulticastPkts,
       "tnEthPortStatsIfInBroadcastPkts": tnEthPortStatsIfInBroadcastPkts,
       "tnEthPortStatsIfOutOctets": tnEthPortStatsIfOutOctets,
       "tnEthPortStatsIfOutUcastPkts": tnEthPortStatsIfOutUcastPkts,
       "tnEthPortStatsIfOutDiscards": tnEthPortStatsIfOutDiscards,
       "tnEthPortStatsIfOutErrors": tnEthPortStatsIfOutErrors,
       "tnEthPortStatsIfOutMulticastPkts": tnEthPortStatsIfOutMulticastPkts,
       "tnEthPortStatsIfOutBroadcastPkts": tnEthPortStatsIfOutBroadcastPkts,
       "tnEthPortStatsIfInPkts": tnEthPortStatsIfInPkts,
       "tnEthPortStatsIfOutPkts": tnEthPortStatsIfOutPkts,
       "tnEthPortEtherStatsDropEvents": tnEthPortEtherStatsDropEvents,
       "tnEthPortEtherStatsBroadcastPkts": tnEthPortEtherStatsBroadcastPkts,
       "tnEthPortEtherStatsMulticastPkts": tnEthPortEtherStatsMulticastPkts,
       "tnEthPortEtherStatsCRCAlignErrors": tnEthPortEtherStatsCRCAlignErrors,
       "tnEthPortEtherStatsUndersizePkts": tnEthPortEtherStatsUndersizePkts,
       "tnEthPortEtherStatsOversizePkts": tnEthPortEtherStatsOversizePkts,
       "tnEthPortEtherStatsFragments": tnEthPortEtherStatsFragments,
       "tnEthPortEtherStatsJabbers": tnEthPortEtherStatsJabbers,
       "tnEthPortEtherStatsCollisions": tnEthPortEtherStatsCollisions,
       "tnEthPortEtherStatsHighCapacityPkts": tnEthPortEtherStatsHighCapacityPkts,
       "tnEthPortEtherStatsHighCapacityOctets": tnEthPortEtherStatsHighCapacityOctets,
       "tnEthPortEtherStatsHighCapacityPkts64Octets": tnEthPortEtherStatsHighCapacityPkts64Octets,
       "tnEthPortEtherStatsHighCapacityPkts65to127Octets": tnEthPortEtherStatsHighCapacityPkts65to127Octets,
       "tnEthPortEtherStatsHighCapacityPkts128to255Octets": tnEthPortEtherStatsHighCapacityPkts128to255Octets,
       "tnEthPortEtherStatsHighCapacityPkts256to511Octets": tnEthPortEtherStatsHighCapacityPkts256to511Octets,
       "tnEthPortEtherStatsHighCapacityPkts512to1023Octets": tnEthPortEtherStatsHighCapacityPkts512to1023Octets,
       "tnEthPortEtherStatsHighCapacityPkts1024to1518Octets": tnEthPortEtherStatsHighCapacityPkts1024to1518Octets,
       "tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets": tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets,
       "tnEthPortDot3StatsAlignmentErrors": tnEthPortDot3StatsAlignmentErrors,
       "tnEthPortDot3StatsFCSErrors": tnEthPortDot3StatsFCSErrors,
       "tnEthPortDot3StatsSingleCollisionFrames": tnEthPortDot3StatsSingleCollisionFrames,
       "tnEthPortDot3StatsMultipleCollisionFrames": tnEthPortDot3StatsMultipleCollisionFrames,
       "tnEthPortDot3StatsSQETestErrors": tnEthPortDot3StatsSQETestErrors,
       "tnEthPortDot3StatsDeferredTransmissions": tnEthPortDot3StatsDeferredTransmissions,
       "tnEthPortDot3StatsLateCollisions": tnEthPortDot3StatsLateCollisions,
       "tnEthPortDot3StatsExcessiveCollisions": tnEthPortDot3StatsExcessiveCollisions,
       "tnEthPortDot3StatsInternalMacTransmitErrors": tnEthPortDot3StatsInternalMacTransmitErrors,
       "tnEthPortDot3StatsCarrierSenseErrors": tnEthPortDot3StatsCarrierSenseErrors,
       "tnEthPortDot3StatsFrameTooLongs": tnEthPortDot3StatsFrameTooLongs,
       "tnEthPortDot3StatsInternalMacReceiveErrors": tnEthPortDot3StatsInternalMacReceiveErrors,
       "tnEthPortDot3StatsSymbolErrors": tnEthPortDot3StatsSymbolErrors,
       "tnEthPortEgrQueueStatsAttributeTotal": tnEthPortEgrQueueStatsAttributeTotal,
       "tnEthPortEgrQueueStatsTable": tnEthPortEgrQueueStatsTable,
       "tnEthPortEgrQueueStatsEntry": tnEthPortEgrQueueStatsEntry,
       "tnEthPortStatsQueueId": tnEthPortStatsQueueId,
       "tnEthPortEgrQueueStatsInProfilePktsForwarded": tnEthPortEgrQueueStatsInProfilePktsForwarded,
       "tnEthPortEgrQueueStatsOutOfProfilePktsForwarded": tnEthPortEgrQueueStatsOutOfProfilePktsForwarded,
       "tnEthPortEgrQueueStatsInProfileOctetsForwarded": tnEthPortEgrQueueStatsInProfileOctetsForwarded,
       "tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded": tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded,
       "tnEthPortEgrQueueStatsInProfilePktsDropped": tnEthPortEgrQueueStatsInProfilePktsDropped,
       "tnEthPortEgrQueueStatsOutOfProfilePktsDropped": tnEthPortEgrQueueStatsOutOfProfilePktsDropped,
       "tnEthPortEgrQueueStatsInProfileOctetsDropped": tnEthPortEgrQueueStatsInProfileOctetsDropped,
       "tnEthPortEgrQueueStatsOutOfProfileOctetsDropped": tnEthPortEgrQueueStatsOutOfProfileOctetsDropped,
       "tnSapStatsAttributeTotal": tnSapStatsAttributeTotal,
       "tnSapStatsTable": tnSapStatsTable,
       "tnSapStatsEntry": tnSapStatsEntry,
       "tnSapStatsPortId": tnSapStatsPortId,
       "tnSapStatsEncapVal": tnSapStatsEncapVal,
       "tnSapStatsInterval": tnSapStatsInterval,
       "tnSapStatsBin": tnSapStatsBin,
       "tnSapStatsBinStatus": tnSapStatsBinStatus,
       "tnSapStatsStartTime": tnSapStatsStartTime,
       "tnSapStatsTotalMembers": tnSapStatsTotalMembers,
       "tnSapStatsIngressPktsForwarded": tnSapStatsIngressPktsForwarded,
       "tnSapStatsIngressOctetsForwarded": tnSapStatsIngressOctetsForwarded,
       "tnSapStatsEgressPktsForwarded": tnSapStatsEgressPktsForwarded,
       "tnSapStatsEgressOctetsForwarded": tnSapStatsEgressOctetsForwarded,
       "tnSapStatsIngressPktsDropped": tnSapStatsIngressPktsDropped,
       "tnSapStatsIngressOctetsDropped": tnSapStatsIngressOctetsDropped,
       "tnSapStatsIngressExtraTagPktsDropped": tnSapStatsIngressExtraTagPktsDropped,
       "tnSapStatsIngressExtraTagOctetsDropped": tnSapStatsIngressExtraTagOctetsDropped,
       "tnSapMeterStatsAttributeTotal": tnSapMeterStatsAttributeTotal,
       "tnSapMeterStatsTable": tnSapMeterStatsTable,
       "tnSapMeterStatsEntry": tnSapMeterStatsEntry,
       "tnSapStatsMeterId": tnSapStatsMeterId,
       "tnSapMeterStatsInProfilePktsForwarded": tnSapMeterStatsInProfilePktsForwarded,
       "tnSapMeterStatsOutOfProfilePktsForwarded": tnSapMeterStatsOutOfProfilePktsForwarded,
       "tnSapMeterStatsInProfileOctetsForwarded": tnSapMeterStatsInProfileOctetsForwarded,
       "tnSapMeterStatsOutOfProfileOctetsForwarded": tnSapMeterStatsOutOfProfileOctetsForwarded,
       "tnEthCfmTWSlmStatsAttributeTotal": tnEthCfmTWSlmStatsAttributeTotal,
       "tnEthCfmTWSlmStatsTable": tnEthCfmTWSlmStatsTable,
       "tnEthCfmTWSlmStatsEntry": tnEthCfmTWSlmStatsEntry,
       "tnEthCfmTWSlmStatsTestName": tnEthCfmTWSlmStatsTestName,
       "tnEthCfmTWSlmStatsInterval": tnEthCfmTWSlmStatsInterval,
       "tnEthCfmTWSlmStatsBin": tnEthCfmTWSlmStatsBin,
       "tnEthCfmTWSlmStatsBinStatus": tnEthCfmTWSlmStatsBinStatus,
       "tnEthCfmTWSlmStatsStartTime": tnEthCfmTWSlmStatsStartTime,
       "tnEthCfmTWSlmStatsTotalMembers": tnEthCfmTWSlmStatsTotalMembers,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioMin": tnEthCfmTWSlmStatsNearEndFrameLossRatioMin,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage": tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage,
       "tnEthCfmTWSlmStatsNearEndFrameLossRatioMax": tnEthCfmTWSlmStatsNearEndFrameLossRatioMax,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioMin": tnEthCfmTWSlmStatsFarEndFrameLossRatioMin,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage": tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage,
       "tnEthCfmTWSlmStatsFarEndFrameLossRatioMax": tnEthCfmTWSlmStatsFarEndFrameLossRatioMax,
       "tnEthCfmTWSlmStatsNearEndHighLoss": tnEthCfmTWSlmStatsNearEndHighLoss,
       "tnEthCfmTWSlmStatsFarEndHighLoss": tnEthCfmTWSlmStatsFarEndHighLoss,
       "tnEthCfmTWSlmStatsNearEndUnavailable": tnEthCfmTWSlmStatsNearEndUnavailable,
       "tnEthCfmTWSlmStatsFarEndUnavailable": tnEthCfmTWSlmStatsFarEndUnavailable,
       "tnEthCfmTWDmStatsAttributeTotal": tnEthCfmTWDmStatsAttributeTotal,
       "tnEthCfmTWDmStatsTable": tnEthCfmTWDmStatsTable,
       "tnEthCfmTWDmStatsEntry": tnEthCfmTWDmStatsEntry,
       "tnEthCfmTWDmStatsTestName": tnEthCfmTWDmStatsTestName,
       "tnEthCfmTWDmStatsInterval": tnEthCfmTWDmStatsInterval,
       "tnEthCfmTWDmStatsBin": tnEthCfmTWDmStatsBin,
       "tnEthCfmTWDmStatsBinStatus": tnEthCfmTWDmStatsBinStatus,
       "tnEthCfmTWDmStatsStartTime": tnEthCfmTWDmStatsStartTime,
       "tnEthCfmTWDmStatsTotalMembers": tnEthCfmTWDmStatsTotalMembers,
       "tnEthCfmTWDmStatsRoundTripFrameDelayMin": tnEthCfmTWDmStatsRoundTripFrameDelayMin,
       "tnEthCfmTWDmStatsRoundTripFrameDelayAverage": tnEthCfmTWDmStatsRoundTripFrameDelayAverage,
       "tnEthCfmTWDmStatsRoundTripFrameDelayMax": tnEthCfmTWDmStatsRoundTripFrameDelayMax,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationMin": tnEthCfmTWDmStatsNearEndFrameDelayVariationMin,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage": tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage,
       "tnEthCfmTWDmStatsNearEndFrameDelayVariationMax": tnEthCfmTWDmStatsNearEndFrameDelayVariationMax,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationMin": tnEthCfmTWDmStatsFarEndFrameDelayVariationMin,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage": tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage,
       "tnEthCfmTWDmStatsFarEndFrameDelayVariationMax": tnEthCfmTWDmStatsFarEndFrameDelayVariationMax,
       "tnEthCfmTWDmStatsNearEndFrameDelayMin": tnEthCfmTWDmStatsNearEndFrameDelayMin,
       "tnEthCfmTWDmStatsNearEndFrameDelayAverage": tnEthCfmTWDmStatsNearEndFrameDelayAverage,
       "tnEthCfmTWDmStatsNearEndFrameDelayMax": tnEthCfmTWDmStatsNearEndFrameDelayMax,
       "tnEthCfmTWDmStatsFarEndFrameDelayMin": tnEthCfmTWDmStatsFarEndFrameDelayMin,
       "tnEthCfmTWDmStatsFarEndFrameDelayAverage": tnEthCfmTWDmStatsFarEndFrameDelayAverage,
       "tnEthCfmTWDmStatsFarEndFrameDelayMax": tnEthCfmTWDmStatsFarEndFrameDelayMax,
       "tnEthCfmTWLmStatsAttributeTotal": tnEthCfmTWLmStatsAttributeTotal,
       "tnEthCfmTWLmStatsTable": tnEthCfmTWLmStatsTable,
       "tnEthCfmTWLmStatsEntry": tnEthCfmTWLmStatsEntry,
       "tnEthCfmTWLmStatsTestName": tnEthCfmTWLmStatsTestName,
       "tnEthCfmTWLmStatsInterval": tnEthCfmTWLmStatsInterval,
       "tnEthCfmTWLmStatsBin": tnEthCfmTWLmStatsBin,
       "tnEthCfmTWLmStatsBinStatus": tnEthCfmTWLmStatsBinStatus,
       "tnEthCfmTWLmStatsStartTime": tnEthCfmTWLmStatsStartTime,
       "tnEthCfmTWLmStatsTotalMembers": tnEthCfmTWLmStatsTotalMembers,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioMin": tnEthCfmTWLmStatsNearEndFrameLossRatioMin,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioAverage": tnEthCfmTWLmStatsNearEndFrameLossRatioAverage,
       "tnEthCfmTWLmStatsNearEndFrameLossRatioMax": tnEthCfmTWLmStatsNearEndFrameLossRatioMax,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioMin": tnEthCfmTWLmStatsFarEndFrameLossRatioMin,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioAverage": tnEthCfmTWLmStatsFarEndFrameLossRatioAverage,
       "tnEthCfmTWLmStatsFarEndFrameLossRatioMax": tnEthCfmTWLmStatsFarEndFrameLossRatioMax,
       "tnEthCfmTWLmStatsNearEndHighLoss": tnEthCfmTWLmStatsNearEndHighLoss,
       "tnEthCfmTWLmStatsFarEndHighLoss": tnEthCfmTWLmStatsFarEndHighLoss,
       "tnEthCfmTWLmStatsNearEndUnavailable": tnEthCfmTWLmStatsNearEndUnavailable,
       "tnEthCfmTWLmStatsFarEndUnavailable": tnEthCfmTWLmStatsFarEndUnavailable}
)
