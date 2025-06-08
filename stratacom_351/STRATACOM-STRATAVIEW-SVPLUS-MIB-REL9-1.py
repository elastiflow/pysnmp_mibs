# SNMP MIB module (STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ErrCode(Integer32):
    """Custom type ErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              10,
              20,
              21,
              22,
              23,
              24,
              25,
              30,
              31,
              40,
              41,
              50,
              90,
              91,
              92,
              93,
              95,
              99,
              100,
              101,
              102,
              103,
              105,
              106,
              107,
              108,
              110,
              111,
              120,
              121,
              122,
              125,
              126,
              127,
              130,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("invalid-node", 2),
          ("invalid-shelf", 3),
          ("invalid-release", 4),
          ("bad-value", 10),
          ("insd-timeout", 20),
          ("insd-died", 21),
          ("insd-unavailable", 22),
          ("insd-error", 23),
          ("insd-connect-error", 24),
          ("insd-node-not-found", 25),
          ("sv-db-error", 30),
          ("ins-db-error", 31),
          ("malloc-error", 40),
          ("interna-error", 41),
          ("delete-conns-first", 50),
          ("anitype-missing", 90),
          ("trmendpt-missing", 91),
          ("asscendpt-missing", 92),
          ("trmend-mismatch", 93),
          ("invalid-dlci", 95),
          ("multiple-instances", 99),
          ("rowstatus-missing", 100),
          ("ani-exists", 101),
          ("ani-not-found", 102),
          ("invalid-ani", 103),
          ("multiple-anis", 105),
          ("invalid-format", 106),
          ("na-frsm", 107),
          ("na-frp", 108),
          ("invalid-set", 110),
          ("illegal-set", 111),
          ("trmend-exists", 120),
          ("conn-exists", 121),
          ("conn-not-found", 122),
          ("multiple-conns", 125),
          ("no-more-conns", 126),
          ("port-not-found", 127),
          ("assc-endpt-not-found", 130),
          ("no-error-entry", 500),
          ("not-applicable", 501),
          ("invalid-flushall", 502))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_Svplus_ObjectIdentity = ObjectIdentity
svplus = _Svplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1)
)
_ServiceGroup_ObjectIdentity = ObjectIdentity
serviceGroup = _ServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 101)
)
_ConnGroup_ObjectIdentity = ObjectIdentity
connGroup = _ConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1)
)
_SvConnMibUpTime_Type = TimeTicks
_SvConnMibUpTime_Object = MibScalar
svConnMibUpTime = _SvConnMibUpTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 1),
    _SvConnMibUpTime_Type()
)
svConnMibUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnMibUpTime.setStatus("mandatory")
_SvConnTable_Object = MibTable
svConnTable = _SvConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3)
)
if mibBuilder.loadTexts:
    svConnTable.setStatus("mandatory")
_SvConnEntry_Object = MibTableRow
svConnEntry = _SvConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1)
)
svConnEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnIndex"),
)
if mibBuilder.loadTexts:
    svConnEntry.setStatus("mandatory")


class _SvConnIndex_Type(Integer32):
    """Custom type svConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SvConnIndex_Type.__name__ = "Integer32"
_SvConnIndex_Object = MibTableColumn
svConnIndex = _SvConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 1),
    _SvConnIndex_Type()
)
svConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnIndex.setStatus("mandatory")
_SvConnLocalEndPt_Type = ObjectIdentifier
_SvConnLocalEndPt_Object = MibTableColumn
svConnLocalEndPt = _SvConnLocalEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 2),
    _SvConnLocalEndPt_Type()
)
svConnLocalEndPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnLocalEndPt.setStatus("mandatory")
_SvConnRemoteEndPt_Type = ObjectIdentifier
_SvConnRemoteEndPt_Object = MibTableColumn
svConnRemoteEndPt = _SvConnRemoteEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 3),
    _SvConnRemoteEndPt_Type()
)
svConnRemoteEndPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnRemoteEndPt.setStatus("mandatory")


class _SvConnAdminStatus_Type(Integer32):
    """Custom type svConnAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("testing", 3))
    )


_SvConnAdminStatus_Type.__name__ = "Integer32"
_SvConnAdminStatus_Object = MibTableColumn
svConnAdminStatus = _SvConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 4),
    _SvConnAdminStatus_Type()
)
svConnAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnAdminStatus.setStatus("mandatory")


class _SvConnOpStatus_Type(Integer32):
    """Custom type svConnOpStatus based on Integer32"""
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
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("incomplete", 5))
    )


_SvConnOpStatus_Type.__name__ = "Integer32"
_SvConnOpStatus_Object = MibTableColumn
svConnOpStatus = _SvConnOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 5),
    _SvConnOpStatus_Type()
)
svConnOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnOpStatus.setStatus("mandatory")


class _SvConnRowStatus_Type(Integer32):
    """Custom type svConnRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_SvConnRowStatus_Type.__name__ = "Integer32"
_SvConnRowStatus_Object = MibTableColumn
svConnRowStatus = _SvConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 6),
    _SvConnRowStatus_Type()
)
svConnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnRowStatus.setStatus("mandatory")


class _SvConnTrkAvoidType_Type(Integer32):
    """Custom type svConnTrkAvoidType based on Integer32"""
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
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_SvConnTrkAvoidType_Type.__name__ = "Integer32"
_SvConnTrkAvoidType_Object = MibTableColumn
svConnTrkAvoidType = _SvConnTrkAvoidType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 7),
    _SvConnTrkAvoidType_Type()
)
svConnTrkAvoidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnTrkAvoidType.setStatus("mandatory")


class _SvConnTrkAvoidZCS_Type(Integer32):
    """Custom type svConnTrkAvoidZCS based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvConnTrkAvoidZCS_Type.__name__ = "Integer32"
_SvConnTrkAvoidZCS_Object = MibTableColumn
svConnTrkAvoidZCS = _SvConnTrkAvoidZCS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 8),
    _SvConnTrkAvoidZCS_Type()
)
svConnTrkAvoidZCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnTrkAvoidZCS.setStatus("mandatory")


class _SvConnForesight_Type(Integer32):
    """Custom type svConnForesight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvConnForesight_Type.__name__ = "Integer32"
_SvConnForesight_Object = MibTableColumn
svConnForesight = _SvConnForesight_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 9),
    _SvConnForesight_Type()
)
svConnForesight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnForesight.setStatus("deprecated")


class _SvConnClassOfService_Type(Integer32):
    """Custom type svConnClassOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SvConnClassOfService_Type.__name__ = "Integer32"
_SvConnClassOfService_Object = MibTableColumn
svConnClassOfService = _SvConnClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 10),
    _SvConnClassOfService_Type()
)
svConnClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnClassOfService.setStatus("mandatory")


class _SvConnCurrRouteDesc_Type(DisplayString):
    """Custom type svConnCurrRouteDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvConnCurrRouteDesc_Type.__name__ = "DisplayString"
_SvConnCurrRouteDesc_Object = MibTableColumn
svConnCurrRouteDesc = _SvConnCurrRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 11),
    _SvConnCurrRouteDesc_Type()
)
svConnCurrRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnCurrRouteDesc.setStatus("mandatory")


class _SvConnPrefRouteDesc_Type(DisplayString):
    """Custom type svConnPrefRouteDesc based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvConnPrefRouteDesc_Type.__name__ = "DisplayString"
_SvConnPrefRouteDesc_Object = MibTableColumn
svConnPrefRouteDesc = _SvConnPrefRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 12),
    _SvConnPrefRouteDesc_Type()
)
svConnPrefRouteDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnPrefRouteDesc.setStatus("mandatory")


class _SvConnRouteMaster_Type(DisplayString):
    """Custom type svConnRouteMaster based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvConnRouteMaster_Type.__name__ = "DisplayString"
_SvConnRouteMaster_Object = MibTableColumn
svConnRouteMaster = _SvConnRouteMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 13),
    _SvConnRouteMaster_Type()
)
svConnRouteMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRouteMaster.setStatus("mandatory")


class _SvConnLocOSpacePkts_Type(Integer32):
    """Custom type svConnLocOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SvConnLocOSpacePkts_Type.__name__ = "Integer32"
_SvConnLocOSpacePkts_Object = MibTableColumn
svConnLocOSpacePkts = _SvConnLocOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 14),
    _SvConnLocOSpacePkts_Type()
)
svConnLocOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnLocOSpacePkts.setStatus("mandatory")


class _SvConnLocOSpaceBdaCmax_Type(Integer32):
    """Custom type svConnLocOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_SvConnLocOSpaceBdaCmax_Type.__name__ = "Integer32"
_SvConnLocOSpaceBdaCmax_Object = MibTableColumn
svConnLocOSpaceBdaCmax = _SvConnLocOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 15),
    _SvConnLocOSpaceBdaCmax_Type()
)
svConnLocOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnLocOSpaceBdaCmax.setStatus("mandatory")


class _SvConnLocOSpaceBdbCmax_Type(Integer32):
    """Custom type svConnLocOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_SvConnLocOSpaceBdbCmax_Type.__name__ = "Integer32"
_SvConnLocOSpaceBdbCmax_Object = MibTableColumn
svConnLocOSpaceBdbCmax = _SvConnLocOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 16),
    _SvConnLocOSpaceBdbCmax_Type()
)
svConnLocOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnLocOSpaceBdbCmax.setStatus("mandatory")


class _SvConnRemOSpacePkts_Type(Integer32):
    """Custom type svConnRemOSpacePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SvConnRemOSpacePkts_Type.__name__ = "Integer32"
_SvConnRemOSpacePkts_Object = MibTableColumn
svConnRemOSpacePkts = _SvConnRemOSpacePkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 17),
    _SvConnRemOSpacePkts_Type()
)
svConnRemOSpacePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRemOSpacePkts.setStatus("mandatory")


class _SvConnRemOSpaceBdaCmax_Type(Integer32):
    """Custom type svConnRemOSpaceBdaCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_SvConnRemOSpaceBdaCmax_Type.__name__ = "Integer32"
_SvConnRemOSpaceBdaCmax_Object = MibTableColumn
svConnRemOSpaceBdaCmax = _SvConnRemOSpaceBdaCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 18),
    _SvConnRemOSpaceBdaCmax_Type()
)
svConnRemOSpaceBdaCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRemOSpaceBdaCmax.setStatus("mandatory")


class _SvConnRemOSpaceBdbCmax_Type(Integer32):
    """Custom type svConnRemOSpaceBdbCmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_SvConnRemOSpaceBdbCmax_Type.__name__ = "Integer32"
_SvConnRemOSpaceBdbCmax_Object = MibTableColumn
svConnRemOSpaceBdbCmax = _SvConnRemOSpaceBdbCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 19),
    _SvConnRemOSpaceBdbCmax_Type()
)
svConnRemOSpaceBdbCmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRemOSpaceBdbCmax.setStatus("mandatory")


class _SvConnTestType_Type(Integer32):
    """Custom type svConnTestType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("continuity", 1),
          ("delay", 2),
          ("none", 255))
    )


_SvConnTestType_Type.__name__ = "Integer32"
_SvConnTestType_Object = MibTableColumn
svConnTestType = _SvConnTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 20),
    _SvConnTestType_Type()
)
svConnTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnTestType.setStatus("mandatory")
_SvConnTestResult_Type = Integer32
_SvConnTestResult_Object = MibTableColumn
svConnTestResult = _SvConnTestResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 21),
    _SvConnTestResult_Type()
)
svConnTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnTestResult.setStatus("mandatory")


class _SvConnAbitStatus_Type(Integer32):
    """Custom type svConnAbitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("fail", 2))
    )


_SvConnAbitStatus_Type.__name__ = "Integer32"
_SvConnAbitStatus_Object = MibTableColumn
svConnAbitStatus = _SvConnAbitStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 22),
    _SvConnAbitStatus_Type()
)
svConnAbitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAbitStatus.setStatus("mandatory")


class _SvConnType_Type(Integer32):
    """Custom type svConnType based on Integer32"""
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
              200)
        )
    )
    namedValues = NamedValues(
        *(("fr-fr", 1),
          ("atm-atm", 2),
          ("atm-fr", 3),
          ("ce-ce", 4),
          ("voice-voice", 5),
          ("data-data", 6),
          ("atm-ce", 7),
          ("unknown", 200))
    )


_SvConnType_Type.__name__ = "Integer32"
_SvConnType_Object = MibTableColumn
svConnType = _SvConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 23),
    _SvConnType_Type()
)
svConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnType.setStatus("mandatory")
_SvConnLocalStr_Type = DisplayString
_SvConnLocalStr_Object = MibTableColumn
svConnLocalStr = _SvConnLocalStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 24),
    _SvConnLocalStr_Type()
)
svConnLocalStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnLocalStr.setStatus("mandatory")
_SvConnRemoteStr_Type = DisplayString
_SvConnRemoteStr_Object = MibTableColumn
svConnRemoteStr = _SvConnRemoteStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 25),
    _SvConnRemoteStr_Type()
)
svConnRemoteStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRemoteStr.setStatus("mandatory")


class _SvConnSubType_Type(Integer32):
    """Custom type svConnSubType based on Integer32"""
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
              31,
              32,
              33,
              200)
        )
    )
    namedValues = NamedValues(
        *(("cbr1", 1),
          ("vbr1", 2),
          ("vbr2", 3),
          ("vbr3", 4),
          ("abr-fs", 5),
          ("fr-fs", 6),
          ("fr", 7),
          ("ubr-1", 8),
          ("ubr-2", 9),
          ("abr-1", 10),
          ("atfst", 31),
          ("atftfst", 32),
          ("atfxfst", 33),
          ("unknown", 200))
    )


_SvConnSubType_Type.__name__ = "Integer32"
_SvConnSubType_Object = MibTableColumn
svConnSubType = _SvConnSubType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 26),
    _SvConnSubType_Type()
)
svConnSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnSubType.setStatus("mandatory")
_SvConnMiddlEndPt_Type = ObjectIdentifier
_SvConnMiddlEndPt_Object = MibTableColumn
svConnMiddlEndPt = _SvConnMiddlEndPt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 27),
    _SvConnMiddlEndPt_Type()
)
svConnMiddlEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnMiddlEndPt.setStatus("mandatory")
_SvConnMiddleStr_Type = DisplayString
_SvConnMiddleStr_Object = MibTableColumn
svConnMiddleStr = _SvConnMiddleStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 28),
    _SvConnMiddleStr_Type()
)
svConnMiddleStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnMiddleStr.setStatus("mandatory")
_SvConnNumSegments_Type = Integer32
_SvConnNumSegments_Object = MibTableColumn
svConnNumSegments = _SvConnNumSegments_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 29),
    _SvConnNumSegments_Type()
)
svConnNumSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnNumSegments.setStatus("mandatory")
_SvConnSegment1_Type = DisplayString
_SvConnSegment1_Object = MibTableColumn
svConnSegment1 = _SvConnSegment1_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 30),
    _SvConnSegment1_Type()
)
svConnSegment1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnSegment1.setStatus("mandatory")
_SvConnSegment2_Type = DisplayString
_SvConnSegment2_Object = MibTableColumn
svConnSegment2 = _SvConnSegment2_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 31),
    _SvConnSegment2_Type()
)
svConnSegment2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnSegment2.setStatus("mandatory")
_SvConnSegment3_Type = DisplayString
_SvConnSegment3_Object = MibTableColumn
svConnSegment3 = _SvConnSegment3_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 32),
    _SvConnSegment3_Type()
)
svConnSegment3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnSegment3.setStatus("mandatory")


class _SvConnOvrSubOvrRide_Type(Integer32):
    """Custom type svConnOvrSubOvrRide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SvConnOvrSubOvrRide_Type.__name__ = "Integer32"
_SvConnOvrSubOvrRide_Object = MibTableColumn
svConnOvrSubOvrRide = _SvConnOvrSubOvrRide_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 33),
    _SvConnOvrSubOvrRide_Type()
)
svConnOvrSubOvrRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnOvrSubOvrRide.setStatus("mandatory")


class _SvConnLocOSpaceCells_Type(Integer32):
    """Custom type svConnLocOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SvConnLocOSpaceCells_Type.__name__ = "Integer32"
_SvConnLocOSpaceCells_Object = MibTableColumn
svConnLocOSpaceCells = _SvConnLocOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 34),
    _SvConnLocOSpaceCells_Type()
)
svConnLocOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnLocOSpaceCells.setStatus("mandatory")


class _SvConnRemOSpaceCells_Type(Integer32):
    """Custom type svConnRemOSpaceCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SvConnRemOSpaceCells_Type.__name__ = "Integer32"
_SvConnRemOSpaceCells_Object = MibTableColumn
svConnRemOSpaceCells = _SvConnRemOSpaceCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 35),
    _SvConnRemOSpaceCells_Type()
)
svConnRemOSpaceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnRemOSpaceCells.setStatus("mandatory")


class _SvConnCellRouting_Type(Integer32):
    """Custom type svConnCellRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvConnCellRouting_Type.__name__ = "Integer32"
_SvConnCellRouting_Object = MibTableColumn
svConnCellRouting = _SvConnCellRouting_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 3, 1, 36),
    _SvConnCellRouting_Type()
)
svConnCellRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svConnCellRouting.setStatus("mandatory")
_SvCmpaErrorLastIndex_Type = Integer32
_SvCmpaErrorLastIndex_Object = MibScalar
svCmpaErrorLastIndex = _SvCmpaErrorLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 8),
    _SvCmpaErrorLastIndex_Type()
)
svCmpaErrorLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorLastIndex.setStatus("mandatory")


class _SvCmpaErrorFlushAll_Type(Integer32):
    """Custom type svCmpaErrorFlushAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("flush", 2))
    )


_SvCmpaErrorFlushAll_Type.__name__ = "Integer32"
_SvCmpaErrorFlushAll_Object = MibScalar
svCmpaErrorFlushAll = _SvCmpaErrorFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 9),
    _SvCmpaErrorFlushAll_Type()
)
svCmpaErrorFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCmpaErrorFlushAll.setStatus("mandatory")
_SvCmpaErrorTable_Object = MibTable
svCmpaErrorTable = _SvCmpaErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 10)
)
if mibBuilder.loadTexts:
    svCmpaErrorTable.setStatus("mandatory")
_SvCmpaErrorEntry_Object = MibTableRow
svCmpaErrorEntry = _SvCmpaErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 10, 1)
)
svCmpaErrorEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCmpaErrorReqId"),
)
if mibBuilder.loadTexts:
    svCmpaErrorEntry.setStatus("mandatory")
_SvCmpaErrorReqId_Type = Integer32
_SvCmpaErrorReqId_Object = MibTableColumn
svCmpaErrorReqId = _SvCmpaErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 10, 1, 1),
    _SvCmpaErrorReqId_Type()
)
svCmpaErrorReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorReqId.setStatus("mandatory")


class _SvCmpaErrorDesc_Type(DisplayString):
    """Custom type svCmpaErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SvCmpaErrorDesc_Type.__name__ = "DisplayString"
_SvCmpaErrorDesc_Object = MibTableColumn
svCmpaErrorDesc = _SvCmpaErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 10, 1, 2),
    _SvCmpaErrorDesc_Type()
)
svCmpaErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorDesc.setStatus("mandatory")


class _SvCmpaErrorEcode_Type(Integer32):
    """Custom type svCmpaErrorEcode based on Integer32"""
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
              20,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-shelf", 3),
          ("invalid-release", 4),
          ("node-timeout", 5),
          ("node-busy", 6),
          ("no-snmpcomm", 7),
          ("snmpcomm-error", 8),
          ("node-error", 9),
          ("bad-value", 10),
          ("port-not-found", 11),
          ("slot-is-full", 12),
          ("slot-not-found", 20),
          ("conn-not-found", 100),
          ("endpt-exists", 101),
          ("lendpt-exists", 102),
          ("rendpt-exists", 103),
          ("lendpt-missing", 104),
          ("rendpt-missing", 105),
          ("db-lendpt-not-found", 106),
          ("db-rendpt-not-found", 107),
          ("lendpt-not-found", 108),
          ("rendpt-not-found", 109),
          ("dangling-endpt", 110),
          ("endpt-rowstatus-missing", 111),
          ("conn-rowstatus-missing", 112),
          ("invalid-endpt-rowstatus", 113),
          ("invalid-conn-rowstatus", 114),
          ("invalid-connindex", 115),
          ("testtype-missing", 116),
          ("partial-add", 117),
          ("partial-mod", 118),
          ("invalid-bw", 119),
          ("not-active", 120),
          ("invalid-adminstatus", 121),
          ("not-clear", 122),
          ("invalid-endpt-comb", 123),
          ("invalid-chantype", 124),
          ("cmgrd-timeout", 125),
          ("no-cmgrd", 126),
          ("ronly-for-frp", 127),
          ("invalid-chanFECNconfig", 128),
          ("invalid-chanCLPtoDEmap", 129),
          ("ibs-less-bc", 130),
          ("invalid-NRM", 131),
          ("invalid-TBE", 132),
          ("foresight-disabled", 133),
          ("invalid-FRTT", 134),
          ("invalid-VSVD", 135),
          ("invalid-Policing", 136),
          ("invalid-PCRZeroPlus1", 137),
          ("invalid-CDVTZeroPlus1", 138),
          ("invalid-MCR", 139),
          ("invalid-PercUtil", 140),
          ("invalid-SCRZeroPlus1", 141),
          ("invalid-MBS", 142),
          ("invalid-FGCRA", 143),
          ("invalid-BCM", 144),
          ("invalid-ICR", 145),
          ("invalid-RateUp", 146),
          ("invalid-RateDown", 147),
          ("invalid-ICRTO", 149),
          ("invalid-MinAdjustPeriod", 150),
          ("invalid-connectionOvrSubOvrRide", 151),
          ("policing-not-settable-on-axis", 152),
          ("rateup-not-settable-on-axis", 153),
          ("ratedown-not-settable-on-axis", 154),
          ("frtt-not-settable-on-axis", 155),
          ("tbe-not-settable-on-axis", 156),
          ("vsvd-not-settable-on-axis", 157),
          ("icrto-not-settable-on-axis", 158),
          ("minadj-not-settable-on-axis", 159),
          ("nrm-not-settable-on-axis", 160),
          ("bcm-not-settable-on-axis", 161),
          ("connSubType-not-settable-for-MODIFY", 162),
          ("connSubType-conflicts-with-endPoints", 163),
          ("invalid-value-atmEndPointHiCLP", 164),
          ("invalid-value-atmEndPointLoCLP", 165),
          ("invalid-value-atmEndPointVcQSize", 166),
          ("invalid-value-atmEndPointEfciQSize", 167),
          ("invalid-value-atmEndPointIBS", 168),
          ("not-testable", 169),
          ("subType-na-for-axis", 200),
          ("portSpeed-mismatch", 201),
          ("lineType-mismatch", 202),
          ("portType-mismatch", 203),
          ("create-only", 204),
          ("na-cesm4", 205),
          ("na-cesm-unstruct", 206),
          ("no-error-entry", 500),
          ("not-applicable", 501),
          ("invalid-flushall", 502))
    )


_SvCmpaErrorEcode_Type.__name__ = "Integer32"
_SvCmpaErrorEcode_Object = MibTableColumn
svCmpaErrorEcode = _SvCmpaErrorEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 10, 1, 3),
    _SvCmpaErrorEcode_Type()
)
svCmpaErrorEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorEcode.setStatus("mandatory")


class _SvCmpaErrorLastDesc_Type(DisplayString):
    """Custom type svCmpaErrorLastDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvCmpaErrorLastDesc_Type.__name__ = "DisplayString"
_SvCmpaErrorLastDesc_Object = MibScalar
svCmpaErrorLastDesc = _SvCmpaErrorLastDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 11),
    _SvCmpaErrorLastDesc_Type()
)
svCmpaErrorLastDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorLastDesc.setStatus("mandatory")


class _SvCmpaErrorLastEcode_Type(Integer32):
    """Custom type svCmpaErrorLastEcode based on Integer32"""
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
              20,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-shelf", 3),
          ("invalid-release", 4),
          ("node-timeout", 5),
          ("node-busy", 6),
          ("no-snmpcomm", 7),
          ("snmpcomm-error", 8),
          ("node-error", 9),
          ("bad-value", 10),
          ("port-not-found", 11),
          ("slot-is-full", 12),
          ("slot-not-found", 20),
          ("conn-not-found", 100),
          ("endpt-exists", 101),
          ("lendpt-exists", 102),
          ("rendpt-exists", 103),
          ("lendpt-missing", 104),
          ("rendpt-missing", 105),
          ("db-lendpt-not-found", 106),
          ("db-rendpt-not-found", 107),
          ("lendpt-not-found", 108),
          ("rendpt-not-found", 109),
          ("dangling-endpt", 110),
          ("endpt-rowstatus-missing", 111),
          ("conn-rowstatus-missing", 112),
          ("invalid-endpt-rowstatus", 113),
          ("invalid-conn-rowstatus", 114),
          ("invalid-connindex", 115),
          ("testtype-missing", 116),
          ("partial-add", 117),
          ("partial-mod", 118),
          ("invalid-bw", 119),
          ("not-active", 120),
          ("invalid-adminstatus", 121),
          ("not-clear", 122),
          ("invalid-endpt-comb", 123),
          ("invalid-chantype", 124),
          ("cmgrd-timeout", 125),
          ("no-cmgrd", 126),
          ("ronly-for-frp", 127),
          ("invalid-chanFECNconfig", 128),
          ("invalid-chanCLPtoDEmap", 129),
          ("ibs-less-bc", 130),
          ("invalid-NRM", 131),
          ("invalid-TBE", 132),
          ("foresight-disabled", 133),
          ("invalid-FRTT", 134),
          ("invalid-VSVD", 135),
          ("invalid-Policing", 136),
          ("invalid-PCRZeroPlus1", 137),
          ("invalid-atmEndPointCDVTZeroPlus1", 138),
          ("invalid-MCR", 139),
          ("invalid-PercUtil", 140),
          ("invalid-SCRZeroPlus1", 141),
          ("invalid-MBS", 142),
          ("invalid-FGCRA", 143),
          ("invalid-BCM", 144),
          ("invalid-ICR", 145),
          ("invalid-RateUp", 146),
          ("invalid-RateDown", 147),
          ("invalid-ICRTO", 149),
          ("invalid-MinAdjustPeriod", 150),
          ("invalid-connectionOvrSubOvrRide", 151),
          ("policing-not-settable-on-axis", 152),
          ("rateup-not-settable-on-axis", 153),
          ("ratedown-not-settable-on-axis", 154),
          ("frtt-not-settable-on-axis", 155),
          ("tbe-not-settable-on-axis", 156),
          ("vsvd-not-settable-on-axis", 157),
          ("icrto-not-settable-on-axis", 158),
          ("minadj-not-settable-on-axis", 159),
          ("nrm-not-settable-on-axis", 160),
          ("bcm-not-settable-on-axis", 161),
          ("connSubType-not-settable-for-MODIFY", 162),
          ("connSubType-conflicts-with-endPoints", 163),
          ("invalid-value-atmEndPointHiCLP", 164),
          ("invalid-value-atmEndPointLoCLP", 165),
          ("invalid-value-atmEndPointVcQSize", 166),
          ("invalid-value-atmEndPointEfciQSize", 167),
          ("invalid-value-atmEndPointIBS", 168),
          ("not-testable", 169),
          ("subType-na-for-axis", 200),
          ("portSpeed-mismatch", 201),
          ("lineType-mismatch", 202),
          ("portType-mismatch", 203),
          ("create-only", 204),
          ("na-cesm4", 205),
          ("na-cesm-unstruct", 206),
          ("no-error-entry", 500),
          ("not-applicable", 501),
          ("invalid-flushall", 502))
    )


_SvCmpaErrorLastEcode_Type.__name__ = "Integer32"
_SvCmpaErrorLastEcode_Object = MibScalar
svCmpaErrorLastEcode = _SvCmpaErrorLastEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 12),
    _SvCmpaErrorLastEcode_Type()
)
svCmpaErrorLastEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCmpaErrorLastEcode.setStatus("mandatory")
_AtmEndPointTable_Object = MibTable
atmEndPointTable = _AtmEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15)
)
if mibBuilder.loadTexts:
    atmEndPointTable.setStatus("mandatory")
_AtmEndPointEntry_Object = MibTableRow
atmEndPointEntry = _AtmEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1)
)
atmEndPointEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointNodeName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointIfShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointVpi"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "atmEndPointVci"),
)
if mibBuilder.loadTexts:
    atmEndPointEntry.setStatus("mandatory")


class _AtmEndPointNodeName_Type(DisplayString):
    """Custom type atmEndPointNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AtmEndPointNodeName_Type.__name__ = "DisplayString"
_AtmEndPointNodeName_Object = MibTableColumn
atmEndPointNodeName = _AtmEndPointNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 1),
    _AtmEndPointNodeName_Type()
)
atmEndPointNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointNodeName.setStatus("mandatory")


class _AtmEndPointIfShelf_Type(DisplayString):
    """Custom type atmEndPointIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtmEndPointIfShelf_Type.__name__ = "DisplayString"
_AtmEndPointIfShelf_Object = MibTableColumn
atmEndPointIfShelf = _AtmEndPointIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 2),
    _AtmEndPointIfShelf_Type()
)
atmEndPointIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointIfShelf.setStatus("mandatory")


class _AtmEndPointSlot_Type(Integer32):
    """Custom type atmEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmEndPointSlot_Type.__name__ = "Integer32"
_AtmEndPointSlot_Object = MibTableColumn
atmEndPointSlot = _AtmEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 3),
    _AtmEndPointSlot_Type()
)
atmEndPointSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointSlot.setStatus("mandatory")


class _AtmEndPointPort_Type(Integer32):
    """Custom type atmEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AtmEndPointPort_Type.__name__ = "Integer32"
_AtmEndPointPort_Object = MibTableColumn
atmEndPointPort = _AtmEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 4),
    _AtmEndPointPort_Type()
)
atmEndPointPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointPort.setStatus("mandatory")


class _AtmEndPointVpi_Type(Integer32):
    """Custom type atmEndPointVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmEndPointVpi_Type.__name__ = "Integer32"
_AtmEndPointVpi_Object = MibTableColumn
atmEndPointVpi = _AtmEndPointVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 5),
    _AtmEndPointVpi_Type()
)
atmEndPointVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointVpi.setStatus("mandatory")


class _AtmEndPointVci_Type(Integer32):
    """Custom type atmEndPointVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmEndPointVci_Type.__name__ = "Integer32"
_AtmEndPointVci_Object = MibTableColumn
atmEndPointVci = _AtmEndPointVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 6),
    _AtmEndPointVci_Type()
)
atmEndPointVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointVci.setStatus("mandatory")


class _AtmEndPointConnIndx_Type(Integer32):
    """Custom type atmEndPointConnIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmEndPointConnIndx_Type.__name__ = "Integer32"
_AtmEndPointConnIndx_Object = MibTableColumn
atmEndPointConnIndx = _AtmEndPointConnIndx_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 7),
    _AtmEndPointConnIndx_Type()
)
atmEndPointConnIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointConnIndx.setStatus("mandatory")


class _AtmEndPointOpStatus_Type(Integer32):
    """Custom type atmEndPointOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              200)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("unknown", 200))
    )


_AtmEndPointOpStatus_Type.__name__ = "Integer32"
_AtmEndPointOpStatus_Object = MibTableColumn
atmEndPointOpStatus = _AtmEndPointOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 8),
    _AtmEndPointOpStatus_Type()
)
atmEndPointOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointOpStatus.setStatus("mandatory")


class _AtmEndPointRowStatus_Type(Integer32):
    """Custom type atmEndPointRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_AtmEndPointRowStatus_Type.__name__ = "Integer32"
_AtmEndPointRowStatus_Object = MibTableColumn
atmEndPointRowStatus = _AtmEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 9),
    _AtmEndPointRowStatus_Type()
)
atmEndPointRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointRowStatus.setStatus("mandatory")


class _AtmEndPointType_Type(Integer32):
    """Custom type atmEndPointType based on Integer32"""
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
              200)
        )
    )
    namedValues = NamedValues(
        *(("asi-Atm", 1),
          ("ausm-Atm", 2),
          ("bni-Atm", 3),
          ("ausm-8-Atm", 4),
          ("ausm-8-Aim", 5),
          ("bxm-Atm", 6),
          ("uxm-Atm", 7),
          ("bme-Atm", 8),
          ("unknown", 200))
    )


_AtmEndPointType_Type.__name__ = "Integer32"
_AtmEndPointType_Object = MibTableColumn
atmEndPointType = _AtmEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 10),
    _AtmEndPointType_Type()
)
atmEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEndPointType.setStatus("mandatory")


class _AtmEndPointPCRZeroPlus1_Type(Integer32):
    """Custom type atmEndPointPCRZeroPlus1 based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1412832),
    )


_AtmEndPointPCRZeroPlus1_Type.__name__ = "Integer32"
_AtmEndPointPCRZeroPlus1_Object = MibTableColumn
atmEndPointPCRZeroPlus1 = _AtmEndPointPCRZeroPlus1_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 11),
    _AtmEndPointPCRZeroPlus1_Type()
)
atmEndPointPCRZeroPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointPCRZeroPlus1.setStatus("mandatory")


class _AtmEndPointCDVTZeroPlus1_Type(Integer32):
    """Custom type atmEndPointCDVTZeroPlus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_AtmEndPointCDVTZeroPlus1_Type.__name__ = "Integer32"
_AtmEndPointCDVTZeroPlus1_Object = MibTableColumn
atmEndPointCDVTZeroPlus1 = _AtmEndPointCDVTZeroPlus1_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 12),
    _AtmEndPointCDVTZeroPlus1_Type()
)
atmEndPointCDVTZeroPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointCDVTZeroPlus1.setStatus("mandatory")


class _AtmEndPointMCR_Type(Integer32):
    """Custom type atmEndPointMCR based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndPointMCR_Type.__name__ = "Integer32"
_AtmEndPointMCR_Object = MibTableColumn
atmEndPointMCR = _AtmEndPointMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 13),
    _AtmEndPointMCR_Type()
)
atmEndPointMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointMCR.setStatus("mandatory")


class _AtmEndPointPercUtil_Type(Integer32):
    """Custom type atmEndPointPercUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndPointPercUtil_Type.__name__ = "Integer32"
_AtmEndPointPercUtil_Object = MibTableColumn
atmEndPointPercUtil = _AtmEndPointPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 14),
    _AtmEndPointPercUtil_Type()
)
atmEndPointPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointPercUtil.setStatus("mandatory")


class _AtmEndPointSCRZeroPlus1_Type(Integer32):
    """Custom type atmEndPointSCRZeroPlus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 1412832),
    )


_AtmEndPointSCRZeroPlus1_Type.__name__ = "Integer32"
_AtmEndPointSCRZeroPlus1_Object = MibTableColumn
atmEndPointSCRZeroPlus1 = _AtmEndPointSCRZeroPlus1_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 15),
    _AtmEndPointSCRZeroPlus1_Type()
)
atmEndPointSCRZeroPlus1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointSCRZeroPlus1.setStatus("mandatory")


class _AtmEndPointMBS_Type(Integer32):
    """Custom type atmEndPointMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_AtmEndPointMBS_Type.__name__ = "Integer32"
_AtmEndPointMBS_Object = MibTableColumn
atmEndPointMBS = _AtmEndPointMBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 16),
    _AtmEndPointMBS_Type()
)
atmEndPointMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointMBS.setStatus("mandatory")


class _AtmEndPointFGCRA_Type(Integer32):
    """Custom type atmEndPointFGCRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndPointFGCRA_Type.__name__ = "Integer32"
_AtmEndPointFGCRA_Object = MibTableColumn
atmEndPointFGCRA = _AtmEndPointFGCRA_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 17),
    _AtmEndPointFGCRA_Type()
)
atmEndPointFGCRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointFGCRA.setStatus("mandatory")


class _AtmEndPointBCM_Type(Integer32):
    """Custom type atmEndPointBCM based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndPointBCM_Type.__name__ = "Integer32"
_AtmEndPointBCM_Object = MibTableColumn
atmEndPointBCM = _AtmEndPointBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 18),
    _AtmEndPointBCM_Type()
)
atmEndPointBCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointBCM.setStatus("mandatory")


class _AtmEndPointICR_Type(Integer32):
    """Custom type atmEndPointICR based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndPointICR_Type.__name__ = "Integer32"
_AtmEndPointICR_Object = MibTableColumn
atmEndPointICR = _AtmEndPointICR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 19),
    _AtmEndPointICR_Type()
)
atmEndPointICR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointICR.setStatus("mandatory")


class _AtmEndPointRateUp_Type(Integer32):
    """Custom type atmEndPointRateUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1412832),
    )


_AtmEndPointRateUp_Type.__name__ = "Integer32"
_AtmEndPointRateUp_Object = MibTableColumn
atmEndPointRateUp = _AtmEndPointRateUp_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 20),
    _AtmEndPointRateUp_Type()
)
atmEndPointRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointRateUp.setStatus("mandatory")


class _AtmEndPointRateDown_Type(Integer32):
    """Custom type atmEndPointRateDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_AtmEndPointRateDown_Type.__name__ = "Integer32"
_AtmEndPointRateDown_Object = MibTableColumn
atmEndPointRateDown = _AtmEndPointRateDown_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 21),
    _AtmEndPointRateDown_Type()
)
atmEndPointRateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointRateDown.setStatus("mandatory")


class _AtmEndPointICRTO_Type(Integer32):
    """Custom type atmEndPointICRTO based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(62, 255000),
    )


_AtmEndPointICRTO_Type.__name__ = "Integer32"
_AtmEndPointICRTO_Object = MibTableColumn
atmEndPointICRTO = _AtmEndPointICRTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 23),
    _AtmEndPointICRTO_Type()
)
atmEndPointICRTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointICRTO.setStatus("mandatory")


class _AtmEndPointMinAdjustPeriod_Type(Integer32):
    """Custom type atmEndPointMinAdjustPeriod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmEndPointMinAdjustPeriod_Type.__name__ = "Integer32"
_AtmEndPointMinAdjustPeriod_Object = MibTableColumn
atmEndPointMinAdjustPeriod = _AtmEndPointMinAdjustPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 24),
    _AtmEndPointMinAdjustPeriod_Type()
)
atmEndPointMinAdjustPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointMinAdjustPeriod.setStatus("mandatory")


class _AtmEndPointNRM_Type(Integer32):
    """Custom type atmEndPointNRM based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_AtmEndPointNRM_Type.__name__ = "Integer32"
_AtmEndPointNRM_Object = MibTableColumn
atmEndPointNRM = _AtmEndPointNRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 25),
    _AtmEndPointNRM_Type()
)
atmEndPointNRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointNRM.setStatus("mandatory")


class _AtmEndPointTBE_Type(Integer32):
    """Custom type atmEndPointTBE based on Integer32"""
    defaultValue = 1048320

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048320),
    )


_AtmEndPointTBE_Type.__name__ = "Integer32"
_AtmEndPointTBE_Object = MibTableColumn
atmEndPointTBE = _AtmEndPointTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 26),
    _AtmEndPointTBE_Type()
)
atmEndPointTBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointTBE.setStatus("mandatory")


class _AtmEndPointFRTT_Type(Integer32):
    """Custom type atmEndPointFRTT based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16700),
    )


_AtmEndPointFRTT_Type.__name__ = "Integer32"
_AtmEndPointFRTT_Object = MibTableColumn
atmEndPointFRTT = _AtmEndPointFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 27),
    _AtmEndPointFRTT_Type()
)
atmEndPointFRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointFRTT.setStatus("mandatory")


class _AtmEndPointVSVD_Type(Integer32):
    """Custom type atmEndPointVSVD based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AtmEndPointVSVD_Type.__name__ = "Integer32"
_AtmEndPointVSVD_Object = MibTableColumn
atmEndPointVSVD = _AtmEndPointVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 28),
    _AtmEndPointVSVD_Type()
)
atmEndPointVSVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointVSVD.setStatus("mandatory")


class _AtmEndPointPolicing_Type(Integer32):
    """Custom type atmEndPointPolicing based on Integer32"""
    defaultValue = 4

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
        *(("policingVbr1", 1),
          ("policingVbr2", 2),
          ("policingVbr3", 3),
          ("policingPcrplc", 4),
          ("none", 5))
    )


_AtmEndPointPolicing_Type.__name__ = "Integer32"
_AtmEndPointPolicing_Object = MibTableColumn
atmEndPointPolicing = _AtmEndPointPolicing_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 29),
    _AtmEndPointPolicing_Type()
)
atmEndPointPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointPolicing.setStatus("mandatory")


class _AtmEndPointHiCLP_Type(Integer32):
    """Custom type atmEndPointHiCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndPointHiCLP_Type.__name__ = "Integer32"
_AtmEndPointHiCLP_Object = MibTableColumn
atmEndPointHiCLP = _AtmEndPointHiCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 30),
    _AtmEndPointHiCLP_Type()
)
atmEndPointHiCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointHiCLP.setStatus("mandatory")


class _AtmEndPointLoCLP_Type(Integer32):
    """Custom type atmEndPointLoCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndPointLoCLP_Type.__name__ = "Integer32"
_AtmEndPointLoCLP_Object = MibTableColumn
atmEndPointLoCLP = _AtmEndPointLoCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 31),
    _AtmEndPointLoCLP_Type()
)
atmEndPointLoCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointLoCLP.setStatus("mandatory")


class _AtmEndPointVcQSize_Type(Integer32):
    """Custom type atmEndPointVcQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_AtmEndPointVcQSize_Type.__name__ = "Integer32"
_AtmEndPointVcQSize_Object = MibTableColumn
atmEndPointVcQSize = _AtmEndPointVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 32),
    _AtmEndPointVcQSize_Type()
)
atmEndPointVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointVcQSize.setStatus("mandatory")


class _AtmEndPointEfciQSize_Type(Integer32):
    """Custom type atmEndPointEfciQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AtmEndPointEfciQSize_Type.__name__ = "Integer32"
_AtmEndPointEfciQSize_Object = MibTableColumn
atmEndPointEfciQSize = _AtmEndPointEfciQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 33),
    _AtmEndPointEfciQSize_Type()
)
atmEndPointEfciQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointEfciQSize.setStatus("mandatory")


class _AtmEndPointIBS_Type(Integer32):
    """Custom type atmEndPointIBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24000),
    )


_AtmEndPointIBS_Type.__name__ = "Integer32"
_AtmEndPointIBS_Object = MibTableColumn
atmEndPointIBS = _AtmEndPointIBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 15, 1, 34),
    _AtmEndPointIBS_Type()
)
atmEndPointIBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEndPointIBS.setStatus("mandatory")
_FrEndPointTable_Object = MibTable
frEndPointTable = _FrEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16)
)
if mibBuilder.loadTexts:
    frEndPointTable.setStatus("mandatory")
_FrEndPointEntry_Object = MibTableRow
frEndPointEntry = _FrEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1)
)
frEndPointEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointNodeName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointIfShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "frEndPointDlci"),
)
if mibBuilder.loadTexts:
    frEndPointEntry.setStatus("mandatory")


class _FrEndPointNodeName_Type(DisplayString):
    """Custom type frEndPointNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrEndPointNodeName_Type.__name__ = "DisplayString"
_FrEndPointNodeName_Object = MibTableColumn
frEndPointNodeName = _FrEndPointNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 1),
    _FrEndPointNodeName_Type()
)
frEndPointNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointNodeName.setStatus("mandatory")


class _FrEndPointIfShelf_Type(DisplayString):
    """Custom type frEndPointIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FrEndPointIfShelf_Type.__name__ = "DisplayString"
_FrEndPointIfShelf_Object = MibTableColumn
frEndPointIfShelf = _FrEndPointIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 2),
    _FrEndPointIfShelf_Type()
)
frEndPointIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointIfShelf.setStatus("mandatory")


class _FrEndPointSlot_Type(Integer32):
    """Custom type frEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrEndPointSlot_Type.__name__ = "Integer32"
_FrEndPointSlot_Object = MibTableColumn
frEndPointSlot = _FrEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 3),
    _FrEndPointSlot_Type()
)
frEndPointSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointSlot.setStatus("mandatory")


class _FrEndPointPort_Type(Integer32):
    """Custom type frEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FrEndPointPort_Type.__name__ = "Integer32"
_FrEndPointPort_Object = MibTableColumn
frEndPointPort = _FrEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 4),
    _FrEndPointPort_Type()
)
frEndPointPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointPort.setStatus("mandatory")


class _FrEndPointDlci_Type(Integer32):
    """Custom type frEndPointDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_FrEndPointDlci_Type.__name__ = "Integer32"
_FrEndPointDlci_Object = MibTableColumn
frEndPointDlci = _FrEndPointDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 5),
    _FrEndPointDlci_Type()
)
frEndPointDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointDlci.setStatus("mandatory")


class _FrEndPointConnIndex_Type(Integer32):
    """Custom type frEndPointConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrEndPointConnIndex_Type.__name__ = "Integer32"
_FrEndPointConnIndex_Object = MibTableColumn
frEndPointConnIndex = _FrEndPointConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 6),
    _FrEndPointConnIndex_Type()
)
frEndPointConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointConnIndex.setStatus("mandatory")


class _FrEndPointOpStatus_Type(Integer32):
    """Custom type frEndPointOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("alarm", 16))
    )


_FrEndPointOpStatus_Type.__name__ = "Integer32"
_FrEndPointOpStatus_Object = MibTableColumn
frEndPointOpStatus = _FrEndPointOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 7),
    _FrEndPointOpStatus_Type()
)
frEndPointOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointOpStatus.setStatus("mandatory")


class _FrEndPointRowStatus_Type(Integer32):
    """Custom type frEndPointRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_FrEndPointRowStatus_Type.__name__ = "Integer32"
_FrEndPointRowStatus_Object = MibTableColumn
frEndPointRowStatus = _FrEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 8),
    _FrEndPointRowStatus_Type()
)
frEndPointRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointRowStatus.setStatus("mandatory")


class _FrEndPointMIR_Type(Integer32):
    """Custom type frEndPointMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 53248000),
    )


_FrEndPointMIR_Type.__name__ = "Integer32"
_FrEndPointMIR_Object = MibTableColumn
frEndPointMIR = _FrEndPointMIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 9),
    _FrEndPointMIR_Type()
)
frEndPointMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointMIR.setStatus("mandatory")


class _FrEndPointCIR_Type(Integer32):
    """Custom type frEndPointCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 53248000),
    )


_FrEndPointCIR_Type.__name__ = "Integer32"
_FrEndPointCIR_Object = MibTableColumn
frEndPointCIR = _FrEndPointCIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 10),
    _FrEndPointCIR_Type()
)
frEndPointCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointCIR.setStatus("mandatory")


class _FrEndPointBc_Type(Integer32):
    """Custom type frEndPointBc based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointBc_Type.__name__ = "Integer32"
_FrEndPointBc_Object = MibTableColumn
frEndPointBc = _FrEndPointBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 11),
    _FrEndPointBc_Type()
)
frEndPointBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointBc.setStatus("mandatory")


class _FrEndPointBe_Type(Integer32):
    """Custom type frEndPointBe based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointBe_Type.__name__ = "Integer32"
_FrEndPointBe_Object = MibTableColumn
frEndPointBe = _FrEndPointBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 12),
    _FrEndPointBe_Type()
)
frEndPointBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointBe.setStatus("mandatory")


class _FrEndPointVcQSize_Type(Integer32):
    """Custom type frEndPointVcQSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointVcQSize_Type.__name__ = "Integer32"
_FrEndPointVcQSize_Object = MibTableColumn
frEndPointVcQSize = _FrEndPointVcQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 13),
    _FrEndPointVcQSize_Type()
)
frEndPointVcQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointVcQSize.setStatus("mandatory")


class _FrEndPointPIR_Type(Integer32):
    """Custom type frEndPointPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 53248000),
    )


_FrEndPointPIR_Type.__name__ = "Integer32"
_FrEndPointPIR_Object = MibTableColumn
frEndPointPIR = _FrEndPointPIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 14),
    _FrEndPointPIR_Type()
)
frEndPointPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointPIR.setStatus("mandatory")


class _FrEndPointCMAX_Type(Integer32):
    """Custom type frEndPointCMAX based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrEndPointCMAX_Type.__name__ = "Integer32"
_FrEndPointCMAX_Object = MibTableColumn
frEndPointCMAX = _FrEndPointCMAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 15),
    _FrEndPointCMAX_Type()
)
frEndPointCMAX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointCMAX.setStatus("mandatory")


class _FrEndPointEcnQSize_Type(Integer32):
    """Custom type frEndPointEcnQSize based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointEcnQSize_Type.__name__ = "Integer32"
_FrEndPointEcnQSize_Object = MibTableColumn
frEndPointEcnQSize = _FrEndPointEcnQSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 16),
    _FrEndPointEcnQSize_Type()
)
frEndPointEcnQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointEcnQSize.setStatus("mandatory")


class _FrEndPointQIR_Type(Integer32):
    """Custom type frEndPointQIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 53248000),
    )


_FrEndPointQIR_Type.__name__ = "Integer32"
_FrEndPointQIR_Object = MibTableColumn
frEndPointQIR = _FrEndPointQIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 17),
    _FrEndPointQIR_Type()
)
frEndPointQIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointQIR.setStatus("mandatory")


class _FrEndPointPercUtil_Type(Integer32):
    """Custom type frEndPointPercUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrEndPointPercUtil_Type.__name__ = "Integer32"
_FrEndPointPercUtil_Object = MibTableColumn
frEndPointPercUtil = _FrEndPointPercUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 18),
    _FrEndPointPercUtil_Type()
)
frEndPointPercUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointPercUtil.setStatus("mandatory")


class _FrEndPointPriority_Type(Integer32):
    """Custom type frEndPointPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FrEndPointPriority_Type.__name__ = "Integer32"
_FrEndPointPriority_Object = MibTableColumn
frEndPointPriority = _FrEndPointPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 19),
    _FrEndPointPriority_Type()
)
frEndPointPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointPriority.setStatus("mandatory")


class _FrEndPointInitialBurstSize_Type(Integer32):
    """Custom type frEndPointInitialBurstSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointInitialBurstSize_Type.__name__ = "Integer32"
_FrEndPointInitialBurstSize_Object = MibTableColumn
frEndPointInitialBurstSize = _FrEndPointInitialBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 20),
    _FrEndPointInitialBurstSize_Type()
)
frEndPointInitialBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointInitialBurstSize.setStatus("mandatory")


class _FrEndPointDeTagging_Type(Integer32):
    """Custom type frEndPointDeTagging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrEndPointDeTagging_Type.__name__ = "Integer32"
_FrEndPointDeTagging_Object = MibTableColumn
frEndPointDeTagging = _FrEndPointDeTagging_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 21),
    _FrEndPointDeTagging_Type()
)
frEndPointDeTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointDeTagging.setStatus("mandatory")


class _FrEndPointIngressDeThreshold_Type(Integer32):
    """Custom type frEndPointIngressDeThreshold based on Integer32"""
    defaultValue = 32767

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointIngressDeThreshold_Type.__name__ = "Integer32"
_FrEndPointIngressDeThreshold_Object = MibTableColumn
frEndPointIngressDeThreshold = _FrEndPointIngressDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 22),
    _FrEndPointIngressDeThreshold_Type()
)
frEndPointIngressDeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointIngressDeThreshold.setStatus("mandatory")


class _FrEndPointEgressQDepth_Type(Integer32):
    """Custom type frEndPointEgressQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointEgressQDepth_Type.__name__ = "Integer32"
_FrEndPointEgressQDepth_Object = MibTableColumn
frEndPointEgressQDepth = _FrEndPointEgressQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 23),
    _FrEndPointEgressQDepth_Type()
)
frEndPointEgressQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointEgressQDepth.setStatus("mandatory")


class _FrEndPointEgressDeThreshold_Type(Integer32):
    """Custom type frEndPointEgressDeThreshold based on Integer32"""
    defaultValue = 32767

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointEgressDeThreshold_Type.__name__ = "Integer32"
_FrEndPointEgressDeThreshold_Object = MibTableColumn
frEndPointEgressDeThreshold = _FrEndPointEgressDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 24),
    _FrEndPointEgressDeThreshold_Type()
)
frEndPointEgressDeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointEgressDeThreshold.setStatus("mandatory")


class _FrEndPointEgressEcnThreshold_Type(Integer32):
    """Custom type frEndPointEgressEcnThreshold based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointEgressEcnThreshold_Type.__name__ = "Integer32"
_FrEndPointEgressEcnThreshold_Object = MibTableColumn
frEndPointEgressEcnThreshold = _FrEndPointEgressEcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 25),
    _FrEndPointEgressEcnThreshold_Type()
)
frEndPointEgressEcnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointEgressEcnThreshold.setStatus("mandatory")


class _FrEndPointEgressQSelect_Type(Integer32):
    """Custom type frEndPointEgressQSelect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_FrEndPointEgressQSelect_Type.__name__ = "Integer32"
_FrEndPointEgressQSelect_Object = MibTableColumn
frEndPointEgressQSelect = _FrEndPointEgressQSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 26),
    _FrEndPointEgressQSelect_Type()
)
frEndPointEgressQSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointEgressQSelect.setStatus("mandatory")


class _FrEndPointLpbkState_Type(Integer32):
    """Custom type frEndPointLpbkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrEndPointLpbkState_Type.__name__ = "Integer32"
_FrEndPointLpbkState_Object = MibTableColumn
frEndPointLpbkState = _FrEndPointLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 27),
    _FrEndPointLpbkState_Type()
)
frEndPointLpbkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointLpbkState.setStatus("mandatory")


class _FrEndPointType_Type(Integer32):
    """Custom type frEndPointType based on Integer32"""
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
              200)
        )
    )
    namedValues = NamedValues(
        *(("frp-fr", 1),
          ("ait-fr", 2),
          ("frsm-fr", 3),
          ("frsm-FUNI", 4),
          ("frsm-FF", 5),
          ("frp-FF", 6),
          ("frasm-stun", 7),
          ("frasm-bstun", 8),
          ("frasm-fras", 9),
          ("unknown", 200))
    )


_FrEndPointType_Type.__name__ = "Integer32"
_FrEndPointType_Object = MibTableColumn
frEndPointType = _FrEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 28),
    _FrEndPointType_Type()
)
frEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointType.setStatus("mandatory")


class _FrEndPointchanType_Type(Integer32):
    """Custom type frEndPointchanType based on Integer32"""
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
        *(("frNIW", 1),
          ("frSIW-transparent", 2),
          ("frSIW-translate", 3),
          ("frFUNI", 4),
          ("frForward", 5))
    )


_FrEndPointchanType_Type.__name__ = "Integer32"
_FrEndPointchanType_Object = MibTableColumn
frEndPointchanType = _FrEndPointchanType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 29),
    _FrEndPointchanType_Type()
)
frEndPointchanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointchanType.setStatus("mandatory")


class _FrEndPointchanFECNconfig_Type(Integer32):
    """Custom type frEndPointchanFECNconfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapEFCI", 1),
          ("setEFCIzero", 2))
    )


_FrEndPointchanFECNconfig_Type.__name__ = "Integer32"
_FrEndPointchanFECNconfig_Object = MibTableColumn
frEndPointchanFECNconfig = _FrEndPointchanFECNconfig_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 30),
    _FrEndPointchanFECNconfig_Type()
)
frEndPointchanFECNconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointchanFECNconfig.setStatus("mandatory")


class _FrEndPointchanDEtoCLPmap_Type(Integer32):
    """Custom type frEndPointchanDEtoCLPmap based on Integer32"""
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
        *(("mapCLP", 1),
          ("setCLPzero", 2),
          ("setCLPone", 3))
    )


_FrEndPointchanDEtoCLPmap_Type.__name__ = "Integer32"
_FrEndPointchanDEtoCLPmap_Object = MibTableColumn
frEndPointchanDEtoCLPmap = _FrEndPointchanDEtoCLPmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 31),
    _FrEndPointchanDEtoCLPmap_Type()
)
frEndPointchanDEtoCLPmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointchanDEtoCLPmap.setStatus("mandatory")


class _FrEndPointchanCLPtoDEmap_Type(Integer32):
    """Custom type frEndPointchanCLPtoDEmap based on Integer32"""
    defaultValue = 1

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
        *(("mapDE", 1),
          ("setDEzero", 2),
          ("setDEone", 3),
          ("ignoreCLP", 4))
    )


_FrEndPointchanCLPtoDEmap_Type.__name__ = "Integer32"
_FrEndPointchanCLPtoDEmap_Object = MibTableColumn
frEndPointchanCLPtoDEmap = _FrEndPointchanCLPtoDEmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 32),
    _FrEndPointchanCLPtoDEmap_Type()
)
frEndPointchanCLPtoDEmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEndPointchanCLPtoDEmap.setStatus("mandatory")


class _FrEndPointLine_Type(Integer32):
    """Custom type frEndPointLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FrEndPointLine_Type.__name__ = "Integer32"
_FrEndPointLine_Object = MibTableColumn
frEndPointLine = _FrEndPointLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 16, 1, 33),
    _FrEndPointLine_Type()
)
frEndPointLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frEndPointLine.setStatus("mandatory")
_SvConnAlarmTable_Object = MibTable
svConnAlarmTable = _SvConnAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17)
)
if mibBuilder.loadTexts:
    svConnAlarmTable.setStatus("mandatory")
_SvConnAlarmEntry_Object = MibTableRow
svConnAlarmEntry = _SvConnAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1)
)
svConnAlarmEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmVpiOrDlci"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmVci"),
)
if mibBuilder.loadTexts:
    svConnAlarmEntry.setStatus("mandatory")


class _SvConnAlarmNode_Type(DisplayString):
    """Custom type svConnAlarmNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvConnAlarmNode_Type.__name__ = "DisplayString"
_SvConnAlarmNode_Object = MibTableColumn
svConnAlarmNode = _SvConnAlarmNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 1),
    _SvConnAlarmNode_Type()
)
svConnAlarmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmNode.setStatus("mandatory")


class _SvConnAlarmShelf_Type(DisplayString):
    """Custom type svConnAlarmShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvConnAlarmShelf_Type.__name__ = "DisplayString"
_SvConnAlarmShelf_Object = MibTableColumn
svConnAlarmShelf = _SvConnAlarmShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 2),
    _SvConnAlarmShelf_Type()
)
svConnAlarmShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmShelf.setStatus("mandatory")


class _SvConnAlarmSlot_Type(Integer32):
    """Custom type svConnAlarmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvConnAlarmSlot_Type.__name__ = "Integer32"
_SvConnAlarmSlot_Object = MibTableColumn
svConnAlarmSlot = _SvConnAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 3),
    _SvConnAlarmSlot_Type()
)
svConnAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmSlot.setStatus("mandatory")


class _SvConnAlarmLine_Type(Integer32):
    """Custom type svConnAlarmLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvConnAlarmLine_Type.__name__ = "Integer32"
_SvConnAlarmLine_Object = MibTableColumn
svConnAlarmLine = _SvConnAlarmLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 4),
    _SvConnAlarmLine_Type()
)
svConnAlarmLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmLine.setStatus("mandatory")


class _SvConnAlarmPort_Type(Integer32):
    """Custom type svConnAlarmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvConnAlarmPort_Type.__name__ = "Integer32"
_SvConnAlarmPort_Object = MibTableColumn
svConnAlarmPort = _SvConnAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 5),
    _SvConnAlarmPort_Type()
)
svConnAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmPort.setStatus("mandatory")


class _SvConnAlarmVpiOrDlci_Type(Integer32):
    """Custom type svConnAlarmVpiOrDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SvConnAlarmVpiOrDlci_Type.__name__ = "Integer32"
_SvConnAlarmVpiOrDlci_Object = MibTableColumn
svConnAlarmVpiOrDlci = _SvConnAlarmVpiOrDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 6),
    _SvConnAlarmVpiOrDlci_Type()
)
svConnAlarmVpiOrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmVpiOrDlci.setStatus("mandatory")


class _SvConnAlarmVci_Type(Integer32):
    """Custom type svConnAlarmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvConnAlarmVci_Type.__name__ = "Integer32"
_SvConnAlarmVci_Object = MibTableColumn
svConnAlarmVci = _SvConnAlarmVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 7),
    _SvConnAlarmVci_Type()
)
svConnAlarmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmVci.setStatus("mandatory")
_SvConnAlarmRemoteEnd_Type = ObjectIdentifier
_SvConnAlarmRemoteEnd_Object = MibTableColumn
svConnAlarmRemoteEnd = _SvConnAlarmRemoteEnd_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 8),
    _SvConnAlarmRemoteEnd_Type()
)
svConnAlarmRemoteEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmRemoteEnd.setStatus("mandatory")


class _SvConnAlarmConnType_Type(Integer32):
    """Custom type svConnAlarmConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fr", 1),
          ("atm", 2),
          ("atm-fr", 3))
    )


_SvConnAlarmConnType_Type.__name__ = "Integer32"
_SvConnAlarmConnType_Object = MibTableColumn
svConnAlarmConnType = _SvConnAlarmConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 9),
    _SvConnAlarmConnType_Type()
)
svConnAlarmConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmConnType.setStatus("mandatory")


class _SvConnAlarmLocalEndNNI_Type(Integer32):
    """Custom type svConnAlarmLocalEndNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_SvConnAlarmLocalEndNNI_Type.__name__ = "Integer32"
_SvConnAlarmLocalEndNNI_Object = MibTableColumn
svConnAlarmLocalEndNNI = _SvConnAlarmLocalEndNNI_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 10),
    _SvConnAlarmLocalEndNNI_Type()
)
svConnAlarmLocalEndNNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmLocalEndNNI.setStatus("mandatory")


class _SvConnAlarmRemoteEndNNI_Type(Integer32):
    """Custom type svConnAlarmRemoteEndNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_SvConnAlarmRemoteEndNNI_Type.__name__ = "Integer32"
_SvConnAlarmRemoteEndNNI_Object = MibTableColumn
svConnAlarmRemoteEndNNI = _SvConnAlarmRemoteEndNNI_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 17, 1, 11),
    _SvConnAlarmRemoteEndNNI_Type()
)
svConnAlarmRemoteEndNNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svConnAlarmRemoteEndNNI.setStatus("mandatory")
_VoiceEndPointTable_Object = MibTable
voiceEndPointTable = _VoiceEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18)
)
if mibBuilder.loadTexts:
    voiceEndPointTable.setStatus("mandatory")
_VoiceEndPointEntry_Object = MibTableRow
voiceEndPointEntry = _VoiceEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1)
)
voiceEndPointEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointNodeName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointIfShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "voiceEndPointDlci"),
)
if mibBuilder.loadTexts:
    voiceEndPointEntry.setStatus("mandatory")


class _VoiceEndPointNodeName_Type(DisplayString):
    """Custom type voiceEndPointNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_VoiceEndPointNodeName_Type.__name__ = "DisplayString"
_VoiceEndPointNodeName_Object = MibTableColumn
voiceEndPointNodeName = _VoiceEndPointNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 1),
    _VoiceEndPointNodeName_Type()
)
voiceEndPointNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndPointNodeName.setStatus("mandatory")


class _VoiceEndPointIfShelf_Type(DisplayString):
    """Custom type voiceEndPointIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VoiceEndPointIfShelf_Type.__name__ = "DisplayString"
_VoiceEndPointIfShelf_Object = MibTableColumn
voiceEndPointIfShelf = _VoiceEndPointIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 2),
    _VoiceEndPointIfShelf_Type()
)
voiceEndPointIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceEndPointIfShelf.setStatus("mandatory")


class _VoiceEndPointSlot_Type(Integer32):
    """Custom type voiceEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VoiceEndPointSlot_Type.__name__ = "Integer32"
_VoiceEndPointSlot_Object = MibTableColumn
voiceEndPointSlot = _VoiceEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 3),
    _VoiceEndPointSlot_Type()
)
voiceEndPointSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointSlot.setStatus("mandatory")


class _VoiceEndPointPort_Type(Integer32):
    """Custom type voiceEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VoiceEndPointPort_Type.__name__ = "Integer32"
_VoiceEndPointPort_Object = MibTableColumn
voiceEndPointPort = _VoiceEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 4),
    _VoiceEndPointPort_Type()
)
voiceEndPointPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointPort.setStatus("mandatory")


class _VoiceEndPointDlci_Type(Integer32):
    """Custom type voiceEndPointDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_VoiceEndPointDlci_Type.__name__ = "Integer32"
_VoiceEndPointDlci_Object = MibTableColumn
voiceEndPointDlci = _VoiceEndPointDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 5),
    _VoiceEndPointDlci_Type()
)
voiceEndPointDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointDlci.setStatus("mandatory")


class _VoiceEndPointConnIndex_Type(Integer32):
    """Custom type voiceEndPointConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VoiceEndPointConnIndex_Type.__name__ = "Integer32"
_VoiceEndPointConnIndex_Object = MibTableColumn
voiceEndPointConnIndex = _VoiceEndPointConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 6),
    _VoiceEndPointConnIndex_Type()
)
voiceEndPointConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointConnIndex.setStatus("mandatory")


class _VoiceEndPointLine_Type(Integer32):
    """Custom type voiceEndPointLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VoiceEndPointLine_Type.__name__ = "Integer32"
_VoiceEndPointLine_Object = MibTableColumn
voiceEndPointLine = _VoiceEndPointLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 18, 1, 7),
    _VoiceEndPointLine_Type()
)
voiceEndPointLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceEndPointLine.setStatus("mandatory")
_DataEndPointTable_Object = MibTable
dataEndPointTable = _DataEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19)
)
if mibBuilder.loadTexts:
    dataEndPointTable.setStatus("mandatory")
_DataEndPointEntry_Object = MibTableRow
dataEndPointEntry = _DataEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1)
)
dataEndPointEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointNodeName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointIfShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dataEndPointDlci"),
)
if mibBuilder.loadTexts:
    dataEndPointEntry.setStatus("mandatory")


class _DataEndPointNodeName_Type(DisplayString):
    """Custom type dataEndPointNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_DataEndPointNodeName_Type.__name__ = "DisplayString"
_DataEndPointNodeName_Object = MibTableColumn
dataEndPointNodeName = _DataEndPointNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 1),
    _DataEndPointNodeName_Type()
)
dataEndPointNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndPointNodeName.setStatus("mandatory")


class _DataEndPointIfShelf_Type(DisplayString):
    """Custom type dataEndPointIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DataEndPointIfShelf_Type.__name__ = "DisplayString"
_DataEndPointIfShelf_Object = MibTableColumn
dataEndPointIfShelf = _DataEndPointIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 2),
    _DataEndPointIfShelf_Type()
)
dataEndPointIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataEndPointIfShelf.setStatus("mandatory")


class _DataEndPointSlot_Type(Integer32):
    """Custom type dataEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DataEndPointSlot_Type.__name__ = "Integer32"
_DataEndPointSlot_Object = MibTableColumn
dataEndPointSlot = _DataEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 3),
    _DataEndPointSlot_Type()
)
dataEndPointSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPointSlot.setStatus("mandatory")


class _DataEndPointPort_Type(Integer32):
    """Custom type dataEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DataEndPointPort_Type.__name__ = "Integer32"
_DataEndPointPort_Object = MibTableColumn
dataEndPointPort = _DataEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 4),
    _DataEndPointPort_Type()
)
dataEndPointPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPointPort.setStatus("mandatory")


class _DataEndPointDlci_Type(Integer32):
    """Custom type dataEndPointDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DataEndPointDlci_Type.__name__ = "Integer32"
_DataEndPointDlci_Object = MibTableColumn
dataEndPointDlci = _DataEndPointDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 5),
    _DataEndPointDlci_Type()
)
dataEndPointDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPointDlci.setStatus("mandatory")


class _DataEndPointConnIndex_Type(Integer32):
    """Custom type dataEndPointConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DataEndPointConnIndex_Type.__name__ = "Integer32"
_DataEndPointConnIndex_Object = MibTableColumn
dataEndPointConnIndex = _DataEndPointConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 6),
    _DataEndPointConnIndex_Type()
)
dataEndPointConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPointConnIndex.setStatus("mandatory")


class _DataEndPointLine_Type(Integer32):
    """Custom type dataEndPointLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DataEndPointLine_Type.__name__ = "Integer32"
_DataEndPointLine_Object = MibTableColumn
dataEndPointLine = _DataEndPointLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 19, 1, 7),
    _DataEndPointLine_Type()
)
dataEndPointLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataEndPointLine.setStatus("mandatory")
_SvCeEndPointTable_Object = MibTable
svCeEndPointTable = _SvCeEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21)
)
if mibBuilder.loadTexts:
    svCeEndPointTable.setStatus("mandatory")
_SvCeEndPointEntry_Object = MibTableRow
svCeEndPointEntry = _SvCeEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1)
)
svCeEndPointEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCeEndPointNodeName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCeEndPointIfShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCeEndPointSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCeEndPointLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCeEndPointPort"),
)
if mibBuilder.loadTexts:
    svCeEndPointEntry.setStatus("mandatory")


class _SvCeEndPointNodeName_Type(DisplayString):
    """Custom type svCeEndPointNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvCeEndPointNodeName_Type.__name__ = "DisplayString"
_SvCeEndPointNodeName_Object = MibTableColumn
svCeEndPointNodeName = _SvCeEndPointNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 1),
    _SvCeEndPointNodeName_Type()
)
svCeEndPointNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointNodeName.setStatus("mandatory")


class _SvCeEndPointIfShelf_Type(DisplayString):
    """Custom type svCeEndPointIfShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvCeEndPointIfShelf_Type.__name__ = "DisplayString"
_SvCeEndPointIfShelf_Object = MibTableColumn
svCeEndPointIfShelf = _SvCeEndPointIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 2),
    _SvCeEndPointIfShelf_Type()
)
svCeEndPointIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointIfShelf.setStatus("mandatory")


class _SvCeEndPointSlot_Type(Integer32):
    """Custom type svCeEndPointSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvCeEndPointSlot_Type.__name__ = "Integer32"
_SvCeEndPointSlot_Object = MibTableColumn
svCeEndPointSlot = _SvCeEndPointSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 3),
    _SvCeEndPointSlot_Type()
)
svCeEndPointSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointSlot.setStatus("mandatory")


class _SvCeEndPointPort_Type(Integer32):
    """Custom type svCeEndPointPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvCeEndPointPort_Type.__name__ = "Integer32"
_SvCeEndPointPort_Object = MibTableColumn
svCeEndPointPort = _SvCeEndPointPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 4),
    _SvCeEndPointPort_Type()
)
svCeEndPointPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointPort.setStatus("mandatory")


class _SvCeEndPointConnIndex_Type(Integer32):
    """Custom type svCeEndPointConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SvCeEndPointConnIndex_Type.__name__ = "Integer32"
_SvCeEndPointConnIndex_Object = MibTableColumn
svCeEndPointConnIndex = _SvCeEndPointConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 5),
    _SvCeEndPointConnIndex_Type()
)
svCeEndPointConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointConnIndex.setStatus("mandatory")


class _SvCeEndPointOpStatus_Type(Integer32):
    """Custom type svCeEndPointOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              200)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("unknown", 200))
    )


_SvCeEndPointOpStatus_Type.__name__ = "Integer32"
_SvCeEndPointOpStatus_Object = MibTableColumn
svCeEndPointOpStatus = _SvCeEndPointOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 6),
    _SvCeEndPointOpStatus_Type()
)
svCeEndPointOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointOpStatus.setStatus("mandatory")


class _SvCeEndPointRowStatus_Type(Integer32):
    """Custom type svCeEndPointRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_SvCeEndPointRowStatus_Type.__name__ = "Integer32"
_SvCeEndPointRowStatus_Object = MibTableColumn
svCeEndPointRowStatus = _SvCeEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 7),
    _SvCeEndPointRowStatus_Type()
)
svCeEndPointRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointRowStatus.setStatus("mandatory")


class _SvCeEndPointType_Type(Integer32):
    """Custom type svCeEndPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              200)
        )
    )
    namedValues = NamedValues(
        *(("cesm-4", 1),
          ("cesm-8-unstructured", 2),
          ("cesm-8-structured", 3),
          ("unknown", 200))
    )


_SvCeEndPointType_Type.__name__ = "Integer32"
_SvCeEndPointType_Object = MibTableColumn
svCeEndPointType = _SvCeEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 8),
    _SvCeEndPointType_Type()
)
svCeEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointType.setStatus("mandatory")


class _SvCeEndPointBufMaxSize_Type(Integer32):
    """Custom type svCeEndPointBufMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SvCeEndPointBufMaxSize_Type.__name__ = "Integer32"
_SvCeEndPointBufMaxSize_Object = MibTableColumn
svCeEndPointBufMaxSize = _SvCeEndPointBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 9),
    _SvCeEndPointBufMaxSize_Type()
)
svCeEndPointBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointBufMaxSize.setStatus("mandatory")


class _SvCeEndPointCDVRxT_Type(Integer32):
    """Custom type svCeEndPointCDVRxT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 65535),
    )


_SvCeEndPointCDVRxT_Type.__name__ = "Integer32"
_SvCeEndPointCDVRxT_Object = MibTableColumn
svCeEndPointCDVRxT = _SvCeEndPointCDVRxT_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 10),
    _SvCeEndPointCDVRxT_Type()
)
svCeEndPointCDVRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointCDVRxT.setStatus("mandatory")


class _SvCeEndPointCellLossPeriod_Type(Integer32):
    """Custom type svCeEndPointCellLossPeriod based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_SvCeEndPointCellLossPeriod_Type.__name__ = "Integer32"
_SvCeEndPointCellLossPeriod_Object = MibTableColumn
svCeEndPointCellLossPeriod = _SvCeEndPointCellLossPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 11),
    _SvCeEndPointCellLossPeriod_Type()
)
svCeEndPointCellLossPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointCellLossPeriod.setStatus("mandatory")


class _SvCeEndPointLine_Type(Integer32):
    """Custom type svCeEndPointLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvCeEndPointLine_Type.__name__ = "Integer32"
_SvCeEndPointLine_Object = MibTableColumn
svCeEndPointLine = _SvCeEndPointLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 12),
    _SvCeEndPointLine_Type()
)
svCeEndPointLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCeEndPointLine.setStatus("mandatory")


class _SvCeEndPointCBRClockMode_Type(Integer32):
    """Custom type svCeEndPointCBRClockMode based on Integer32"""
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
        *(("synchronous", 1),
          ("srts", 2),
          ("adaptive", 3))
    )


_SvCeEndPointCBRClockMode_Type.__name__ = "Integer32"
_SvCeEndPointCBRClockMode_Object = MibTableColumn
svCeEndPointCBRClockMode = _SvCeEndPointCBRClockMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 13),
    _SvCeEndPointCBRClockMode_Type()
)
svCeEndPointCBRClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointCBRClockMode.setStatus("mandatory")


class _SvCeEndPointCAS_Type(Integer32):
    """Custom type svCeEndPointCAS based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SvCeEndPointCAS_Type.__name__ = "Integer32"
_SvCeEndPointCAS_Object = MibTableColumn
svCeEndPointCAS = _SvCeEndPointCAS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 14),
    _SvCeEndPointCAS_Type()
)
svCeEndPointCAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointCAS.setStatus("mandatory")


class _SvCeEndPointPartialFill_Type(Integer32):
    """Custom type svCeEndPointPartialFill based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 47),
    )


_SvCeEndPointPartialFill_Type.__name__ = "Integer32"
_SvCeEndPointPartialFill_Object = MibTableColumn
svCeEndPointPartialFill = _SvCeEndPointPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 15),
    _SvCeEndPointPartialFill_Type()
)
svCeEndPointPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointPartialFill.setStatus("mandatory")


class _SvCeEndPointIdleDet_Type(Integer32):
    """Custom type svCeEndPointIdleDet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableOnhook", 2))
    )


_SvCeEndPointIdleDet_Type.__name__ = "Integer32"
_SvCeEndPointIdleDet_Object = MibTableColumn
svCeEndPointIdleDet = _SvCeEndPointIdleDet_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 16),
    _SvCeEndPointIdleDet_Type()
)
svCeEndPointIdleDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointIdleDet.setStatus("mandatory")


class _SvCeEndPointOnhookCode_Type(Integer32):
    """Custom type svCeEndPointOnhookCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SvCeEndPointOnhookCode_Type.__name__ = "Integer32"
_SvCeEndPointOnhookCode_Object = MibTableColumn
svCeEndPointOnhookCode = _SvCeEndPointOnhookCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 17),
    _SvCeEndPointOnhookCode_Type()
)
svCeEndPointOnhookCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointOnhookCode.setStatus("mandatory")


class _SvCeEndPointIdleSupp_Type(Integer32):
    """Custom type svCeEndPointIdleSupp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SvCeEndPointIdleSupp_Type.__name__ = "Integer32"
_SvCeEndPointIdleSupp_Object = MibTableColumn
svCeEndPointIdleSupp = _SvCeEndPointIdleSupp_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 18),
    _SvCeEndPointIdleSupp_Type()
)
svCeEndPointIdleSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointIdleSupp.setStatus("mandatory")


class _SvCeEndPointIdleCodeIntgnPeriod_Type(Integer32):
    """Custom type svCeEndPointIdleCodeIntgnPeriod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvCeEndPointIdleCodeIntgnPeriod_Type.__name__ = "Integer32"
_SvCeEndPointIdleCodeIntgnPeriod_Object = MibTableColumn
svCeEndPointIdleCodeIntgnPeriod = _SvCeEndPointIdleCodeIntgnPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 1, 21, 1, 19),
    _SvCeEndPointIdleCodeIntgnPeriod_Type()
)
svCeEndPointIdleCodeIntgnPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCeEndPointIdleCodeIntgnPeriod.setStatus("mandatory")
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2)
)
_SvPortTable_Object = MibTable
svPortTable = _SvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1)
)
if mibBuilder.loadTexts:
    svPortTable.setStatus("mandatory")
_SvPortEntry_Object = MibTableRow
svPortEntry = _SvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1)
)
svPortEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortLineIndex"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortPort"),
)
if mibBuilder.loadTexts:
    svPortEntry.setStatus("mandatory")


class _SvPortNode_Type(DisplayString):
    """Custom type svPortNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvPortNode_Type.__name__ = "DisplayString"
_SvPortNode_Object = MibTableColumn
svPortNode = _SvPortNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 1),
    _SvPortNode_Type()
)
svPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortNode.setStatus("mandatory")


class _SvPortShelf_Type(DisplayString):
    """Custom type svPortShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvPortShelf_Type.__name__ = "DisplayString"
_SvPortShelf_Object = MibTableColumn
svPortShelf = _SvPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 2),
    _SvPortShelf_Type()
)
svPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortShelf.setStatus("mandatory")


class _SvPortSlot_Type(Integer32):
    """Custom type svPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvPortSlot_Type.__name__ = "Integer32"
_SvPortSlot_Object = MibTableColumn
svPortSlot = _SvPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 3),
    _SvPortSlot_Type()
)
svPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortSlot.setStatus("mandatory")


class _SvPortPort_Type(Integer32):
    """Custom type svPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SvPortPort_Type.__name__ = "Integer32"
_SvPortPort_Object = MibTableColumn
svPortPort = _SvPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 4),
    _SvPortPort_Type()
)
svPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortPort.setStatus("mandatory")


class _SvPortCardType_Type(Integer32):
    """Custom type svPortCardType based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("frp", 2),
          ("frsm-4", 3),
          ("cesm-4", 4),
          ("ufm", 5),
          ("ausm-4", 6),
          ("ausm-8", 7),
          ("asi", 8),
          ("bxm", 9),
          ("frsm-8", 10),
          ("frm", 11),
          ("frsm-hs1", 12),
          ("ufmU", 14),
          ("bxm-1", 15),
          ("bxm-2", 16),
          ("bxm-4", 17),
          ("bxm-8", 18),
          ("bxm-12", 19),
          ("frasm-8", 20),
          ("uxm", 21),
          ("cesm-8", 22))
    )


_SvPortCardType_Type.__name__ = "Integer32"
_SvPortCardType_Object = MibTableColumn
svPortCardType = _SvPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 5),
    _SvPortCardType_Type()
)
svPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortCardType.setStatus("mandatory")


class _SvPortIfType_Type(Integer32):
    """Custom type svPortIfType based on Integer32"""
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
              16,
              17,
              18,
              23,
              24,
              25,
              26,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3),
          ("t3", 4),
          ("e3", 5),
          ("oc3-smf", 6),
          ("oc3-mmf", 7),
          ("oc3-stm1", 8),
          ("oc3-utp", 9),
          ("oc3-stp", 10),
          ("oc3-smflr", 11),
          ("oc12-smf", 16),
          ("oc12-mmf", 17),
          ("oc12-smflr", 18),
          ("v35", 23),
          ("x21", 24),
          ("hssi", 25),
          ("lm-bxm", 26),
          ("oc3-snm", 35),
          ("oc12-snm", 36),
          ("oc3-2-smf", 37),
          ("oc3-4-smf", 38),
          ("oc3-4-mmf", 39),
          ("t3-3", 40),
          ("t3-6", 41),
          ("e3-3", 42),
          ("e3-6", 43),
          ("oc3-stm1e", 44),
          ("oc3-xlr", 45),
          ("oc12-xlr", 46))
    )


_SvPortIfType_Type.__name__ = "Integer32"
_SvPortIfType_Object = MibTableColumn
svPortIfType = _SvPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 6),
    _SvPortIfType_Type()
)
svPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortIfType.setStatus("mandatory")


class _SvPortState_Type(Integer32):
    """Custom type svPortState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("remoteLoopback", 5),
          ("lineFailure", 6),
          ("signallingFailure", 7),
          ("outOfCellDelineation", 8),
          ("bandwidthChanged", 9),
          ("failedDueToAcpTimeout", 10),
          ("failedDueToMajorAlmonAimGrp", 11),
          ("failedDueToAimSigFailure", 12),
          ("failedDueToBadDiffDelay", 13),
          ("failedDueToArbConflict", 14),
          ("inBert", 15),
          ("farEndRemoteLoopback", 16),
          ("notConfigured", 17))
    )


_SvPortState_Type.__name__ = "Integer32"
_SvPortState_Object = MibTableColumn
svPortState = _SvPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 7),
    _SvPortState_Type()
)
svPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortState.setStatus("mandatory")


class _SvPortSpeed_Type(Integer32):
    """Custom type svPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(560, 1412830),
    )


_SvPortSpeed_Type.__name__ = "Integer32"
_SvPortSpeed_Object = MibTableColumn
svPortSpeed = _SvPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 8),
    _SvPortSpeed_Type()
)
svPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortSpeed.setStatus("mandatory")
_SvPortLine_Type = Integer32
_SvPortLine_Object = MibTableColumn
svPortLine = _SvPortLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 9),
    _SvPortLine_Type()
)
svPortLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortLine.setStatus("mandatory")
_SvPortLineIndex_Type = Integer32
_SvPortLineIndex_Object = MibTableColumn
svPortLineIndex = _SvPortLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 10),
    _SvPortLineIndex_Type()
)
svPortLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortLineIndex.setStatus("mandatory")


class _SvPortPhysicalPort_Type(Integer32):
    """Custom type svPortPhysicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )


_SvPortPhysicalPort_Type.__name__ = "Integer32"
_SvPortPhysicalPort_Object = MibTableColumn
svPortPhysicalPort = _SvPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 1, 1, 11),
    _SvPortPhysicalPort_Type()
)
svPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortPhysicalPort.setStatus("mandatory")
_SvNextLogicalPortTable_Object = MibTable
svNextLogicalPortTable = _SvNextLogicalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2)
)
if mibBuilder.loadTexts:
    svNextLogicalPortTable.setStatus("mandatory")
_SvNextLogicalPortEntry_Object = MibTableRow
svNextLogicalPortEntry = _SvNextLogicalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2, 1)
)
svNextLogicalPortEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSlot"),
)
if mibBuilder.loadTexts:
    svNextLogicalPortEntry.setStatus("mandatory")


class _SvNode_Type(DisplayString):
    """Custom type svNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvNode_Type.__name__ = "DisplayString"
_SvNode_Object = MibTableColumn
svNode = _SvNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2, 1, 1),
    _SvNode_Type()
)
svNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNode.setStatus("mandatory")


class _SvShelf_Type(DisplayString):
    """Custom type svShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvShelf_Type.__name__ = "DisplayString"
_SvShelf_Object = MibTableColumn
svShelf = _SvShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2, 1, 2),
    _SvShelf_Type()
)
svShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svShelf.setStatus("mandatory")


class _SvSlot_Type(Integer32):
    """Custom type svSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvSlot_Type.__name__ = "Integer32"
_SvSlot_Object = MibTableColumn
svSlot = _SvSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2, 1, 3),
    _SvSlot_Type()
)
svSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSlot.setStatus("mandatory")


class _SvPort_Type(Integer32):
    """Custom type svPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SvPort_Type.__name__ = "Integer32"
_SvPort_Object = MibTableColumn
svPort = _SvPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 2, 1, 4),
    _SvPort_Type()
)
svPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPort.setStatus("mandatory")
_SvPhysicalToLogicalMapTable_Object = MibTable
svPhysicalToLogicalMapTable = _SvPhysicalToLogicalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3)
)
if mibBuilder.loadTexts:
    svPhysicalToLogicalMapTable.setStatus("mandatory")
_SvPhysicalToLogicalMapEntry_Object = MibTableRow
svPhysicalToLogicalMapEntry = _SvPhysicalToLogicalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1)
)
svPhysicalToLogicalMapEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svMapNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svMapShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svMapSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svMapPhysicalInfo"),
)
if mibBuilder.loadTexts:
    svPhysicalToLogicalMapEntry.setStatus("mandatory")


class _SvMapNode_Type(DisplayString):
    """Custom type svMapNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvMapNode_Type.__name__ = "DisplayString"
_SvMapNode_Object = MibTableColumn
svMapNode = _SvMapNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1, 1),
    _SvMapNode_Type()
)
svMapNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svMapNode.setStatus("mandatory")


class _SvMapShelf_Type(DisplayString):
    """Custom type svMapShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvMapShelf_Type.__name__ = "DisplayString"
_SvMapShelf_Object = MibTableColumn
svMapShelf = _SvMapShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1, 2),
    _SvMapShelf_Type()
)
svMapShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svMapShelf.setStatus("mandatory")


class _SvMapSlot_Type(Integer32):
    """Custom type svMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvMapSlot_Type.__name__ = "Integer32"
_SvMapSlot_Object = MibTableColumn
svMapSlot = _SvMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1, 3),
    _SvMapSlot_Type()
)
svMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svMapSlot.setStatus("mandatory")


class _SvMapPhysicalInfo_Type(DisplayString):
    """Custom type svMapPhysicalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SvMapPhysicalInfo_Type.__name__ = "DisplayString"
_SvMapPhysicalInfo_Object = MibTableColumn
svMapPhysicalInfo = _SvMapPhysicalInfo_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1, 4),
    _SvMapPhysicalInfo_Type()
)
svMapPhysicalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svMapPhysicalInfo.setStatus("mandatory")


class _SvMapLogicalPort_Type(Integer32):
    """Custom type svMapLogicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SvMapLogicalPort_Type.__name__ = "Integer32"
_SvMapLogicalPort_Object = MibTableColumn
svMapLogicalPort = _SvMapLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 3, 1, 5),
    _SvMapLogicalPort_Type()
)
svMapLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svMapLogicalPort.setStatus("mandatory")
_SvFrPortTable_Object = MibTable
svFrPortTable = _SvFrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4)
)
if mibBuilder.loadTexts:
    svFrPortTable.setStatus("mandatory")
_SvFrPortEntry_Object = MibTableRow
svFrPortEntry = _SvFrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1)
)
svFrPortEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrPortNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrPortShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrPortSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrPortLineIndex"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrPortPort"),
)
if mibBuilder.loadTexts:
    svFrPortEntry.setStatus("mandatory")


class _SvFrPortNode_Type(DisplayString):
    """Custom type svFrPortNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvFrPortNode_Type.__name__ = "DisplayString"
_SvFrPortNode_Object = MibTableColumn
svFrPortNode = _SvFrPortNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 1),
    _SvFrPortNode_Type()
)
svFrPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortNode.setStatus("mandatory")


class _SvFrPortShelf_Type(DisplayString):
    """Custom type svFrPortShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvFrPortShelf_Type.__name__ = "DisplayString"
_SvFrPortShelf_Object = MibTableColumn
svFrPortShelf = _SvFrPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 2),
    _SvFrPortShelf_Type()
)
svFrPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortShelf.setStatus("mandatory")


class _SvFrPortSlot_Type(Integer32):
    """Custom type svFrPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvFrPortSlot_Type.__name__ = "Integer32"
_SvFrPortSlot_Object = MibTableColumn
svFrPortSlot = _SvFrPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 3),
    _SvFrPortSlot_Type()
)
svFrPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortSlot.setStatus("mandatory")


class _SvFrPortPort_Type(Integer32):
    """Custom type svFrPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SvFrPortPort_Type.__name__ = "Integer32"
_SvFrPortPort_Object = MibTableColumn
svFrPortPort = _SvFrPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 4),
    _SvFrPortPort_Type()
)
svFrPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortPort.setStatus("mandatory")


class _SvFrPortRowStatus_Type(Integer32):
    """Custom type svFrPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4))
    )


_SvFrPortRowStatus_Type.__name__ = "Integer32"
_SvFrPortRowStatus_Object = MibTableColumn
svFrPortRowStatus = _SvFrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 5),
    _SvFrPortRowStatus_Type()
)
svFrPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortRowStatus.setStatus("mandatory")


class _SvFrPortType_Type(Integer32):
    """Custom type svFrPortType based on Integer32"""
    defaultValue = 1

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
        *(("frame-relay", 1),
          ("frFUNI", 2),
          ("frame-forward", 3),
          ("sdlc-stun", 4),
          ("sdlc-fras", 5),
          ("bsc-bstun", 6))
    )


_SvFrPortType_Type.__name__ = "Integer32"
_SvFrPortType_Object = MibTableColumn
svFrPortType = _SvFrPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 6),
    _SvFrPortType_Type()
)
svFrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortType.setStatus("mandatory")


class _SvFrPortCardType_Type(Integer32):
    """Custom type svFrPortCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              10,
              11,
              12,
              14,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("frp", 2),
          ("frsm-4", 3),
          ("ufm", 5),
          ("frsm-8", 10),
          ("frm", 11),
          ("frsm-hs1", 12),
          ("ufmU", 14),
          ("frasm-8", 20))
    )


_SvFrPortCardType_Type.__name__ = "Integer32"
_SvFrPortCardType_Object = MibTableColumn
svFrPortCardType = _SvFrPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 7),
    _SvFrPortCardType_Type()
)
svFrPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortCardType.setStatus("mandatory")


class _SvFrPortIfType_Type(Integer32):
    """Custom type svFrPortIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3),
          ("v35", 23),
          ("x21", 24),
          ("hssi", 25))
    )


_SvFrPortIfType_Type.__name__ = "Integer32"
_SvFrPortIfType_Object = MibTableColumn
svFrPortIfType = _SvFrPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 8),
    _SvFrPortIfType_Type()
)
svFrPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortIfType.setStatus("mandatory")


class _SvFrPortOperState_Type(Integer32):
    """Custom type svFrPortOperState based on Integer32"""
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
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("remoteLoopback", 5),
          ("lineFailure", 6),
          ("signallingFailure", 7),
          ("inBert", 15),
          ("farEndRemoteLoopback", 16),
          ("notConfigured", 17))
    )


_SvFrPortOperState_Type.__name__ = "Integer32"
_SvFrPortOperState_Object = MibTableColumn
svFrPortOperState = _SvFrPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 9),
    _SvFrPortOperState_Type()
)
svFrPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortOperState.setStatus("mandatory")


class _SvFrPortAdminState_Type(Integer32):
    """Custom type svFrPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvFrPortAdminState_Type.__name__ = "Integer32"
_SvFrPortAdminState_Object = MibTableColumn
svFrPortAdminState = _SvFrPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 10),
    _SvFrPortAdminState_Type()
)
svFrPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortAdminState.setStatus("mandatory")


class _SvFrPortLine_Type(Integer32):
    """Custom type svFrPortLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvFrPortLine_Type.__name__ = "Integer32"
_SvFrPortLine_Object = MibTableColumn
svFrPortLine = _SvFrPortLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 11),
    _SvFrPortLine_Type()
)
svFrPortLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortLine.setStatus("mandatory")


class _SvFrPortStartingCh_Type(Integer32):
    """Custom type svFrPortStartingCh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvFrPortStartingCh_Type.__name__ = "Integer32"
_SvFrPortStartingCh_Object = MibTableColumn
svFrPortStartingCh = _SvFrPortStartingCh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 12),
    _SvFrPortStartingCh_Type()
)
svFrPortStartingCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortStartingCh.setStatus("mandatory")
_SvFrPortChCnt_Type = Integer32
_SvFrPortChCnt_Object = MibTableColumn
svFrPortChCnt = _SvFrPortChCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 13),
    _SvFrPortChCnt_Type()
)
svFrPortChCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortChCnt.setStatus("mandatory")


class _SvFrPortSpeed_Type(Integer32):
    """Custom type svFrPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(560, 20480),
    )


_SvFrPortSpeed_Type.__name__ = "Integer32"
_SvFrPortSpeed_Object = MibTableColumn
svFrPortSpeed = _SvFrPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 14),
    _SvFrPortSpeed_Type()
)
svFrPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortSpeed.setStatus("mandatory")


class _SvFrPortDs0ChSpeed_Type(Integer32):
    """Custom type svFrPortDs0ChSpeed based on Integer32"""
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
        *(("s56k", 1),
          ("s64k", 2),
          ("na", 3))
    )


_SvFrPortDs0ChSpeed_Type.__name__ = "Integer32"
_SvFrPortDs0ChSpeed_Object = MibTableColumn
svFrPortDs0ChSpeed = _SvFrPortDs0ChSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 15),
    _SvFrPortDs0ChSpeed_Type()
)
svFrPortDs0ChSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortDs0ChSpeed.setStatus("mandatory")


class _SvFrPortSigProt_Type(Integer32):
    """Custom type svFrPortSigProt based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("lmi-noasyn", 2),
          ("lmi-asyn", 3),
          ("uni-annexA", 4),
          ("uni-annexD", 5),
          ("nni-annexA", 6),
          ("nni-annexD", 7))
    )


_SvFrPortSigProt_Type.__name__ = "Integer32"
_SvFrPortSigProt_Object = MibTableColumn
svFrPortSigProt = _SvFrPortSigProt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 16),
    _SvFrPortSigProt_Type()
)
svFrPortSigProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortSigProt.setStatus("mandatory")


class _SvFrPortNNIStatus_Type(Integer32):
    """Custom type svFrPortNNIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SvFrPortNNIStatus_Type.__name__ = "Integer32"
_SvFrPortNNIStatus_Object = MibTableColumn
svFrPortNNIStatus = _SvFrPortNNIStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 17),
    _SvFrPortNNIStatus_Type()
)
svFrPortNNIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortNNIStatus.setStatus("mandatory")


class _SvFrPortAsyncUpd_Type(Integer32):
    """Custom type svFrPortAsyncUpd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SvFrPortAsyncUpd_Type.__name__ = "Integer32"
_SvFrPortAsyncUpd_Object = MibTableColumn
svFrPortAsyncUpd = _SvFrPortAsyncUpd_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 18),
    _SvFrPortAsyncUpd_Type()
)
svFrPortAsyncUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortAsyncUpd.setStatus("mandatory")


class _SvFrPortPollVerTimer_Type(Integer32):
    """Custom type svFrPortPollVerTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SvFrPortPollVerTimer_Type.__name__ = "Integer32"
_SvFrPortPollVerTimer_Object = MibTableColumn
svFrPortPollVerTimer = _SvFrPortPollVerTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 19),
    _SvFrPortPollVerTimer_Type()
)
svFrPortPollVerTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortPollVerTimer.setStatus("mandatory")


class _SvFrPortErrThresh_Type(Integer32):
    """Custom type svFrPortErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvFrPortErrThresh_Type.__name__ = "Integer32"
_SvFrPortErrThresh_Object = MibTableColumn
svFrPortErrThresh = _SvFrPortErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 20),
    _SvFrPortErrThresh_Type()
)
svFrPortErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortErrThresh.setStatus("mandatory")


class _SvFrPortMonEveCnt_Type(Integer32):
    """Custom type svFrPortMonEveCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvFrPortMonEveCnt_Type.__name__ = "Integer32"
_SvFrPortMonEveCnt_Object = MibTableColumn
svFrPortMonEveCnt = _SvFrPortMonEveCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 21),
    _SvFrPortMonEveCnt_Type()
)
svFrPortMonEveCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortMonEveCnt.setStatus("mandatory")


class _SvFrPortFrmFlags_Type(Integer32):
    """Custom type svFrPortFrmFlags based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvFrPortFrmFlags_Type.__name__ = "Integer32"
_SvFrPortFrmFlags_Object = MibTableColumn
svFrPortFrmFlags = _SvFrPortFrmFlags_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 22),
    _SvFrPortFrmFlags_Type()
)
svFrPortFrmFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortFrmFlags.setStatus("mandatory")


class _SvFrPortLinkTimer_Type(Integer32):
    """Custom type svFrPortLinkTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SvFrPortLinkTimer_Type.__name__ = "Integer32"
_SvFrPortLinkTimer_Object = MibTableColumn
svFrPortLinkTimer = _SvFrPortLinkTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 23),
    _SvFrPortLinkTimer_Type()
)
svFrPortLinkTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortLinkTimer.setStatus("mandatory")


class _SvFrPortPollCycle_Type(Integer32):
    """Custom type svFrPortPollCycle based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvFrPortPollCycle_Type.__name__ = "Integer32"
_SvFrPortPollCycle_Object = MibTableColumn
svFrPortPollCycle = _SvFrPortPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 24),
    _SvFrPortPollCycle_Type()
)
svFrPortPollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortPollCycle.setStatus("mandatory")


class _SvFrPortCLLMEnable_Type(Integer32):
    """Custom type svFrPortCLLMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SvFrPortCLLMEnable_Type.__name__ = "Integer32"
_SvFrPortCLLMEnable_Object = MibTableColumn
svFrPortCLLMEnable = _SvFrPortCLLMEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 25),
    _SvFrPortCLLMEnable_Type()
)
svFrPortCLLMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortCLLMEnable.setStatus("mandatory")


class _SvFrPortCLLMTimer_Type(Integer32):
    """Custom type svFrPortCLLMTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 5000),
    )


_SvFrPortCLLMTimer_Type.__name__ = "Integer32"
_SvFrPortCLLMTimer_Object = MibTableColumn
svFrPortCLLMTimer = _SvFrPortCLLMTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 26),
    _SvFrPortCLLMTimer_Type()
)
svFrPortCLLMTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortCLLMTimer.setStatus("mandatory")


class _SvFrPortVcCount_Type(Integer32):
    """Custom type svFrPortVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SvFrPortVcCount_Type.__name__ = "Integer32"
_SvFrPortVcCount_Object = MibTableColumn
svFrPortVcCount = _SvFrPortVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 27),
    _SvFrPortVcCount_Type()
)
svFrPortVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortVcCount.setStatus("mandatory")
_SvFrPortVcPtr_Type = ObjectIdentifier
_SvFrPortVcPtr_Object = MibTableColumn
svFrPortVcPtr = _SvFrPortVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 28),
    _SvFrPortVcPtr_Type()
)
svFrPortVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortVcPtr.setStatus("mandatory")


class _SvFrAxPortSvcRatio_Type(Integer32):
    """Custom type svFrAxPortSvcRatio based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SvFrAxPortSvcRatio_Type.__name__ = "Integer32"
_SvFrAxPortSvcRatio_Object = MibTableColumn
svFrAxPortSvcRatio = _SvFrAxPortSvcRatio_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 29),
    _SvFrAxPortSvcRatio_Type()
)
svFrAxPortSvcRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrAxPortSvcRatio.setStatus("mandatory")


class _SvFrIxPortMaxTxQDepth_Type(Integer32):
    """Custom type svFrIxPortMaxTxQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvFrIxPortMaxTxQDepth_Type.__name__ = "Integer32"
_SvFrIxPortMaxTxQDepth_Object = MibTableColumn
svFrIxPortMaxTxQDepth = _SvFrIxPortMaxTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 30),
    _SvFrIxPortMaxTxQDepth_Type()
)
svFrIxPortMaxTxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortMaxTxQDepth.setStatus("mandatory")


class _SvFrIxPortECNQThresh_Type(Integer32):
    """Custom type svFrIxPortECNQThresh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvFrIxPortECNQThresh_Type.__name__ = "Integer32"
_SvFrIxPortECNQThresh_Object = MibTableColumn
svFrIxPortECNQThresh = _SvFrIxPortECNQThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 31),
    _SvFrIxPortECNQThresh_Type()
)
svFrIxPortECNQThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortECNQThresh.setStatus("mandatory")


class _SvFrIxPortDEThresh_Type(Integer32):
    """Custom type svFrIxPortDEThresh based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvFrIxPortDEThresh_Type.__name__ = "Integer32"
_SvFrIxPortDEThresh_Object = MibTableColumn
svFrIxPortDEThresh = _SvFrIxPortDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 32),
    _SvFrIxPortDEThresh_Type()
)
svFrIxPortDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortDEThresh.setStatus("mandatory")


class _SvFrIxPortIDEMap_Type(Integer32):
    """Custom type svFrIxPortIDEMap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SvFrIxPortIDEMap_Type.__name__ = "Integer32"
_SvFrIxPortIDEMap_Object = MibTableColumn
svFrIxPortIDEMap = _SvFrIxPortIDEMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 33),
    _SvFrIxPortIDEMap_Type()
)
svFrIxPortIDEMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortIDEMap.setStatus("mandatory")


class _SvFrIxPortCommPri_Type(Integer32):
    """Custom type svFrIxPortCommPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SvFrIxPortCommPri_Type.__name__ = "Integer32"
_SvFrIxPortCommPri_Object = MibTableColumn
svFrIxPortCommPri = _SvFrIxPortCommPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 34),
    _SvFrIxPortCommPri_Type()
)
svFrIxPortCommPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortCommPri.setStatus("mandatory")


class _SvFrIxPortUpRNR_Type(Integer32):
    """Custom type svFrIxPortUpRNR based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SvFrIxPortUpRNR_Type.__name__ = "Integer32"
_SvFrIxPortUpRNR_Object = MibTableColumn
svFrIxPortUpRNR = _SvFrIxPortUpRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 35),
    _SvFrIxPortUpRNR_Type()
)
svFrIxPortUpRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortUpRNR.setStatus("mandatory")


class _SvFrIxPortLowRNR_Type(Integer32):
    """Custom type svFrIxPortLowRNR based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SvFrIxPortLowRNR_Type.__name__ = "Integer32"
_SvFrIxPortLowRNR_Object = MibTableColumn
svFrIxPortLowRNR = _SvFrIxPortLowRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 36),
    _SvFrIxPortLowRNR_Type()
)
svFrIxPortLowRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortLowRNR.setStatus("mandatory")


class _SvFrIxPortOamThresh_Type(Integer32):
    """Custom type svFrIxPortOamThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SvFrIxPortOamThresh_Type.__name__ = "Integer32"
_SvFrIxPortOamThresh_Object = MibTableColumn
svFrIxPortOamThresh = _SvFrIxPortOamThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 37),
    _SvFrIxPortOamThresh_Type()
)
svFrIxPortOamThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortOamThresh.setStatus("mandatory")


class _SvFrIxPortEFCItoBECN_Type(Integer32):
    """Custom type svFrIxPortEFCItoBECN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2),
          ("none", 3))
    )


_SvFrIxPortEFCItoBECN_Type.__name__ = "Integer32"
_SvFrIxPortEFCItoBECN_Object = MibTableColumn
svFrIxPortEFCItoBECN = _SvFrIxPortEFCItoBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 38),
    _SvFrIxPortEFCItoBECN_Type()
)
svFrIxPortEFCItoBECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortEFCItoBECN.setStatus("mandatory")


class _SvFrIxPortClockType_Type(Integer32):
    """Custom type svFrIxPortClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("looped", 2),
          ("none", 3))
    )


_SvFrIxPortClockType_Type.__name__ = "Integer32"
_SvFrIxPortClockType_Object = MibTableColumn
svFrIxPortClockType = _SvFrIxPortClockType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 39),
    _SvFrIxPortClockType_Type()
)
svFrIxPortClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrIxPortClockType.setStatus("mandatory")


class _SvFrIxPortSrRTS_Type(Integer32):
    """Custom type svFrIxPortSrRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("none", 3))
    )


_SvFrIxPortSrRTS_Type.__name__ = "Integer32"
_SvFrIxPortSrRTS_Object = MibTableColumn
svFrIxPortSrRTS = _SvFrIxPortSrRTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 40),
    _SvFrIxPortSrRTS_Type()
)
svFrIxPortSrRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortSrRTS.setStatus("mandatory")


class _SvFrIxPortSrDTR_Type(Integer32):
    """Custom type svFrIxPortSrDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("none", 3))
    )


_SvFrIxPortSrDTR_Type.__name__ = "Integer32"
_SvFrIxPortSrDTR_Object = MibTableColumn
svFrIxPortSrDTR = _SvFrIxPortSrDTR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 41),
    _SvFrIxPortSrDTR_Type()
)
svFrIxPortSrDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortSrDTR.setStatus("mandatory")


class _SvFrIxPortSrDCD_Type(Integer32):
    """Custom type svFrIxPortSrDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("none", 3))
    )


_SvFrIxPortSrDCD_Type.__name__ = "Integer32"
_SvFrIxPortSrDCD_Object = MibTableColumn
svFrIxPortSrDCD = _SvFrIxPortSrDCD_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 42),
    _SvFrIxPortSrDCD_Type()
)
svFrIxPortSrDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortSrDCD.setStatus("mandatory")


class _SvFrIxPortSrCTS_Type(Integer32):
    """Custom type svFrIxPortSrCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("none", 3))
    )


_SvFrIxPortSrCTS_Type.__name__ = "Integer32"
_SvFrIxPortSrCTS_Object = MibTableColumn
svFrIxPortSrCTS = _SvFrIxPortSrCTS_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 43),
    _SvFrIxPortSrCTS_Type()
)
svFrIxPortSrCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortSrCTS.setStatus("mandatory")


class _SvFrIxPortSrDSR_Type(Integer32):
    """Custom type svFrIxPortSrDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("none", 3))
    )


_SvFrIxPortSrDSR_Type.__name__ = "Integer32"
_SvFrIxPortSrDSR_Object = MibTableColumn
svFrIxPortSrDSR = _SvFrIxPortSrDSR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 44),
    _SvFrIxPortSrDSR_Type()
)
svFrIxPortSrDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortSrDSR.setStatus("mandatory")


class _SvFrIxPortLoopBack_Type(Integer32):
    """Custom type svFrIxPortLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2),
          ("remote", 3))
    )


_SvFrIxPortLoopBack_Type.__name__ = "Integer32"
_SvFrIxPortLoopBack_Object = MibTableColumn
svFrIxPortLoopBack = _SvFrIxPortLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 45),
    _SvFrIxPortLoopBack_Type()
)
svFrIxPortLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortLoopBack.setStatus("mandatory")


class _SvFrIxPortExtConFail_Type(Integer32):
    """Custom type svFrIxPortExtConFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvFrIxPortExtConFail_Type.__name__ = "Integer32"
_SvFrIxPortExtConFail_Object = MibTableColumn
svFrIxPortExtConFail = _SvFrIxPortExtConFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 46),
    _SvFrIxPortExtConFail_Type()
)
svFrIxPortExtConFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrIxPortExtConFail.setStatus("mandatory")


class _SvFrPortLineIndex_Type(Integer32):
    """Custom type svFrPortLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvFrPortLineIndex_Type.__name__ = "Integer32"
_SvFrPortLineIndex_Object = MibTableColumn
svFrPortLineIndex = _SvFrPortLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 47),
    _SvFrPortLineIndex_Type()
)
svFrPortLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrPortLineIndex.setStatus("mandatory")


class _SvFrPortEnhancedLmi_Type(Integer32):
    """Custom type svFrPortEnhancedLmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("none", 3))
    )


_SvFrPortEnhancedLmi_Type.__name__ = "Integer32"
_SvFrPortEnhancedLmi_Object = MibTableColumn
svFrPortEnhancedLmi = _SvFrPortEnhancedLmi_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 48),
    _SvFrPortEnhancedLmi_Type()
)
svFrPortEnhancedLmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortEnhancedLmi.setStatus("mandatory")


class _SvFrPortSubRateSpeed_Type(Integer32):
    """Custom type svFrPortSubRateSpeed based on Integer32"""
    defaultValue = 5

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
        *(("speed2400", 1),
          ("speed4800", 2),
          ("speed9600", 3),
          ("speed56000", 4),
          ("speed64000", 5))
    )


_SvFrPortSubRateSpeed_Type.__name__ = "Integer32"
_SvFrPortSubRateSpeed_Object = MibTableColumn
svFrPortSubRateSpeed = _SvFrPortSubRateSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 49),
    _SvFrPortSubRateSpeed_Type()
)
svFrPortSubRateSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortSubRateSpeed.setStatus("mandatory")


class _SvFrPortPhysicalInterface_Type(Integer32):
    """Custom type svFrPortPhysicalInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0", 1),
          ("ds0a", 2))
    )


_SvFrPortPhysicalInterface_Type.__name__ = "Integer32"
_SvFrPortPhysicalInterface_Object = MibTableColumn
svFrPortPhysicalInterface = _SvFrPortPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 50),
    _SvFrPortPhysicalInterface_Type()
)
svFrPortPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortPhysicalInterface.setStatus("mandatory")


class _SvFrPortDataEncoding_Type(Integer32):
    """Custom type svFrPortDataEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_SvFrPortDataEncoding_Type.__name__ = "Integer32"
_SvFrPortDataEncoding_Object = MibTableColumn
svFrPortDataEncoding = _SvFrPortDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 51),
    _SvFrPortDataEncoding_Type()
)
svFrPortDataEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortDataEncoding.setStatus("mandatory")


class _SvFrPortRole_Type(Integer32):
    """Custom type svFrPortRole based on Integer32"""
    defaultValue = 1

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
        *(("primary", 1),
          ("secondary", 2),
          ("negotiable", 3),
          ("xidprimrole", 4),
          ("contention", 5))
    )


_SvFrPortRole_Type.__name__ = "Integer32"
_SvFrPortRole_Object = MibTableColumn
svFrPortRole = _SvFrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 52),
    _SvFrPortRole_Type()
)
svFrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortRole.setStatus("mandatory")


class _SvFrPortMaxFrame_Type(Integer32):
    """Custom type svFrPortMaxFrame based on Integer32"""
    defaultValue = 12000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12000),
    )


_SvFrPortMaxFrame_Type.__name__ = "Integer32"
_SvFrPortMaxFrame_Object = MibTableColumn
svFrPortMaxFrame = _SvFrPortMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 53),
    _SvFrPortMaxFrame_Type()
)
svFrPortMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortMaxFrame.setStatus("mandatory")


class _SvFrPortRetryCnt_Type(Integer32):
    """Custom type svFrPortRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvFrPortRetryCnt_Type.__name__ = "Integer32"
_SvFrPortRetryCnt_Object = MibTableColumn
svFrPortRetryCnt = _SvFrPortRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 54),
    _SvFrPortRetryCnt_Type()
)
svFrPortRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortRetryCnt.setStatus("mandatory")


class _SvFrPortAckWaitTime_Type(Integer32):
    """Custom type svFrPortAckWaitTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_SvFrPortAckWaitTime_Type.__name__ = "Integer32"
_SvFrPortAckWaitTime_Object = MibTableColumn
svFrPortAckWaitTime = _SvFrPortAckWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 55),
    _SvFrPortAckWaitTime_Type()
)
svFrPortAckWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortAckWaitTime.setStatus("mandatory")


class _SvFrPortPollInterval_Type(Integer32):
    """Custom type svFrPortPollInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SvFrPortPollInterval_Type.__name__ = "Integer32"
_SvFrPortPollInterval_Object = MibTableColumn
svFrPortPollInterval = _SvFrPortPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 56),
    _SvFrPortPollInterval_Type()
)
svFrPortPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortPollInterval.setStatus("mandatory")


class _SvFrPortPollTimeout_Type(Integer32):
    """Custom type svFrPortPollTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SvFrPortPollTimeout_Type.__name__ = "Integer32"
_SvFrPortPollTimeout_Object = MibTableColumn
svFrPortPollTimeout = _SvFrPortPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 57),
    _SvFrPortPollTimeout_Type()
)
svFrPortPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortPollTimeout.setStatus("mandatory")


class _SvFrPortProtocolGroup_Type(Integer32):
    """Custom type svFrPortProtocolGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvFrPortProtocolGroup_Type.__name__ = "Integer32"
_SvFrPortProtocolGroup_Object = MibTableColumn
svFrPortProtocolGroup = _SvFrPortProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 4, 1, 58),
    _SvFrPortProtocolGroup_Type()
)
svFrPortProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrPortProtocolGroup.setStatus("mandatory")
_SvAtmPortTable_Object = MibTable
svAtmPortTable = _SvAtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5)
)
if mibBuilder.loadTexts:
    svAtmPortTable.setStatus("mandatory")
_SvAtmPortEntry_Object = MibTableRow
svAtmPortEntry = _SvAtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1)
)
svAtmPortEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svAtmPortNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svAtmPortShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svAtmPortSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svAtmPortPort"),
)
if mibBuilder.loadTexts:
    svAtmPortEntry.setStatus("mandatory")


class _SvAtmPortNode_Type(DisplayString):
    """Custom type svAtmPortNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvAtmPortNode_Type.__name__ = "DisplayString"
_SvAtmPortNode_Object = MibTableColumn
svAtmPortNode = _SvAtmPortNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 1),
    _SvAtmPortNode_Type()
)
svAtmPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortNode.setStatus("mandatory")


class _SvAtmPortShelf_Type(DisplayString):
    """Custom type svAtmPortShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvAtmPortShelf_Type.__name__ = "DisplayString"
_SvAtmPortShelf_Object = MibTableColumn
svAtmPortShelf = _SvAtmPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 2),
    _SvAtmPortShelf_Type()
)
svAtmPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortShelf.setStatus("mandatory")


class _SvAtmPortSlot_Type(Integer32):
    """Custom type svAtmPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvAtmPortSlot_Type.__name__ = "Integer32"
_SvAtmPortSlot_Object = MibTableColumn
svAtmPortSlot = _SvAtmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 3),
    _SvAtmPortSlot_Type()
)
svAtmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortSlot.setStatus("mandatory")


class _SvAtmPortPort_Type(Integer32):
    """Custom type svAtmPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvAtmPortPort_Type.__name__ = "Integer32"
_SvAtmPortPort_Object = MibTableColumn
svAtmPortPort = _SvAtmPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 4),
    _SvAtmPortPort_Type()
)
svAtmPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortPort.setStatus("mandatory")


class _SvAtmPortRowStatus_Type(Integer32):
    """Custom type svAtmPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("addlines", 7),
          ("dellines", 8))
    )


_SvAtmPortRowStatus_Type.__name__ = "Integer32"
_SvAtmPortRowStatus_Object = MibTableColumn
svAtmPortRowStatus = _SvAtmPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 5),
    _SvAtmPortRowStatus_Type()
)
svAtmPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortRowStatus.setStatus("mandatory")


class _SvAtmPortOperState_Type(Integer32):
    """Custom type svAtmPortOperState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4),
          ("remoteLoopback", 5),
          ("lineFailure", 6),
          ("signallingFailure", 7),
          ("outOfCellDelineation", 8),
          ("bandwidthChanged", 9),
          ("failedDueToAcpTimeout", 10),
          ("failedDueToMajorAlmonAimGrp", 11),
          ("failedDueToAimSigFailure", 12),
          ("failedDueToBadDiffDelay", 13),
          ("failedDueToArbConflict", 14))
    )


_SvAtmPortOperState_Type.__name__ = "Integer32"
_SvAtmPortOperState_Object = MibTableColumn
svAtmPortOperState = _SvAtmPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 6),
    _SvAtmPortOperState_Type()
)
svAtmPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortOperState.setStatus("mandatory")


class _SvAtmPortAdminState_Type(Integer32):
    """Custom type svAtmPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmPortAdminState_Type.__name__ = "Integer32"
_SvAtmPortAdminState_Object = MibTableColumn
svAtmPortAdminState = _SvAtmPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 7),
    _SvAtmPortAdminState_Type()
)
svAtmPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortAdminState.setStatus("mandatory")


class _SvAtmPortCardType_Type(Integer32):
    """Custom type svAtmPortCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              15,
              16,
              17,
              18,
              19,
              21)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ausm-4", 6),
          ("ausm-8", 7),
          ("asi", 8),
          ("bxm", 9),
          ("bxm-1", 15),
          ("bxm-2", 16),
          ("bxm-4", 17),
          ("bxm-8", 18),
          ("bxm-12", 19),
          ("uxm", 21))
    )


_SvAtmPortCardType_Type.__name__ = "Integer32"
_SvAtmPortCardType_Object = MibTableColumn
svAtmPortCardType = _SvAtmPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 8),
    _SvAtmPortCardType_Type()
)
svAtmPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortCardType.setStatus("mandatory")


class _SvAtmPortIfType_Type(Integer32):
    """Custom type svAtmPortIfType based on Integer32"""
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
              16,
              17,
              18,
              26,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3),
          ("t3", 4),
          ("e3", 5),
          ("oc3-smf", 6),
          ("oc3-mmf", 7),
          ("oc3-stm1", 8),
          ("oc3-utp", 9),
          ("oc3-stp", 10),
          ("oc3-smflr", 11),
          ("oc12-smf", 16),
          ("oc12-mmf", 17),
          ("oc12-smflr", 18),
          ("lm-bxm", 26),
          ("oc3-snm", 35),
          ("oc12-snm", 36),
          ("oc3-2-smf", 37),
          ("oc3-4-smf", 38),
          ("oc3-4-mmf", 39),
          ("t3-3", 40),
          ("t3-6", 41),
          ("e3-3", 42),
          ("e3-6", 43))
    )


_SvAtmPortIfType_Type.__name__ = "Integer32"
_SvAtmPortIfType_Object = MibTableColumn
svAtmPortIfType = _SvAtmPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 9),
    _SvAtmPortIfType_Type()
)
svAtmPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortIfType.setStatus("mandatory")


class _SvAtmPortSpeed_Type(Integer32):
    """Custom type svAtmPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3622, 1412830),
    )


_SvAtmPortSpeed_Type.__name__ = "Integer32"
_SvAtmPortSpeed_Object = MibTableColumn
svAtmPortSpeed = _SvAtmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 10),
    _SvAtmPortSpeed_Type()
)
svAtmPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortSpeed.setStatus("mandatory")


class _SvAtmPortVcCount_Type(Integer32):
    """Custom type svAtmPortVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SvAtmPortVcCount_Type.__name__ = "Integer32"
_SvAtmPortVcCount_Object = MibTableColumn
svAtmPortVcCount = _SvAtmPortVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 11),
    _SvAtmPortVcCount_Type()
)
svAtmPortVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortVcCount.setStatus("mandatory")
_SvAtmPortVcPtr_Type = ObjectIdentifier
_SvAtmPortVcPtr_Object = MibTableColumn
svAtmPortVcPtr = _SvAtmPortVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 12),
    _SvAtmPortVcPtr_Type()
)
svAtmPortVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortVcPtr.setStatus("mandatory")


class _SvAtmPortType_Type(Integer32):
    """Custom type svAtmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atm-uni", 4),
          ("atm-nni", 5))
    )


_SvAtmPortType_Type.__name__ = "Integer32"
_SvAtmPortType_Object = MibTableColumn
svAtmPortType = _SvAtmPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 13),
    _SvAtmPortType_Type()
)
svAtmPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortType.setStatus("mandatory")


class _SvAtmPortSignallingProtocol_Type(Integer32):
    """Custom type svAtmPortSignallingProtocol based on Integer32"""
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
        *(("none", 1),
          ("lmi", 2),
          ("ilmi", 3))
    )


_SvAtmPortSignallingProtocol_Type.__name__ = "Integer32"
_SvAtmPortSignallingProtocol_Object = MibTableColumn
svAtmPortSignallingProtocol = _SvAtmPortSignallingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 14),
    _SvAtmPortSignallingProtocol_Type()
)
svAtmPortSignallingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortSignallingProtocol.setStatus("mandatory")


class _SvAtmPortIlmiVpi_Type(Integer32):
    """Custom type svAtmPortIlmiVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SvAtmPortIlmiVpi_Type.__name__ = "Integer32"
_SvAtmPortIlmiVpi_Object = MibTableColumn
svAtmPortIlmiVpi = _SvAtmPortIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 15),
    _SvAtmPortIlmiVpi_Type()
)
svAtmPortIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiVpi.setStatus("mandatory")


class _SvAtmPortIlmiVci_Type(Integer32):
    """Custom type svAtmPortIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SvAtmPortIlmiVci_Type.__name__ = "Integer32"
_SvAtmPortIlmiVci_Object = MibTableColumn
svAtmPortIlmiVci = _SvAtmPortIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 16),
    _SvAtmPortIlmiVci_Type()
)
svAtmPortIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiVci.setStatus("mandatory")


class _SvAtmPortIlmiTrapEnable_Type(Integer32):
    """Custom type svAtmPortIlmiTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmPortIlmiTrapEnable_Type.__name__ = "Integer32"
_SvAtmPortIlmiTrapEnable_Object = MibTableColumn
svAtmPortIlmiTrapEnable = _SvAtmPortIlmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 17),
    _SvAtmPortIlmiTrapEnable_Type()
)
svAtmPortIlmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiTrapEnable.setStatus("mandatory")


class _SvAtmPortIlmiMinimumTrapInterval_Type(Integer32):
    """Custom type svAtmPortIlmiMinimumTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvAtmPortIlmiMinimumTrapInterval_Type.__name__ = "Integer32"
_SvAtmPortIlmiMinimumTrapInterval_Object = MibTableColumn
svAtmPortIlmiMinimumTrapInterval = _SvAtmPortIlmiMinimumTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 18),
    _SvAtmPortIlmiMinimumTrapInterval_Type()
)
svAtmPortIlmiMinimumTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiMinimumTrapInterval.setStatus("mandatory")


class _SvAtmPortIlmiAlivePollEnable_Type(Integer32):
    """Custom type svAtmPortIlmiAlivePollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmPortIlmiAlivePollEnable_Type.__name__ = "Integer32"
_SvAtmPortIlmiAlivePollEnable_Object = MibTableColumn
svAtmPortIlmiAlivePollEnable = _SvAtmPortIlmiAlivePollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 19),
    _SvAtmPortIlmiAlivePollEnable_Type()
)
svAtmPortIlmiAlivePollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiAlivePollEnable.setStatus("mandatory")


class _SvAtmPortIlmiAlivePollInterval_Type(Integer32):
    """Custom type svAtmPortIlmiAlivePollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60)
        )
    )
    namedValues = NamedValues(
        *(("v1", 5),
          ("v2", 10),
          ("v3", 15),
          ("v4", 20),
          ("v5", 25),
          ("v6", 30),
          ("v7", 35),
          ("v8", 40),
          ("v9", 45),
          ("v10", 50),
          ("v11", 55),
          ("v12", 60))
    )


_SvAtmPortIlmiAlivePollInterval_Type.__name__ = "Integer32"
_SvAtmPortIlmiAlivePollInterval_Object = MibTableColumn
svAtmPortIlmiAlivePollInterval = _SvAtmPortIlmiAlivePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 20),
    _SvAtmPortIlmiAlivePollInterval_Type()
)
svAtmPortIlmiAlivePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiAlivePollInterval.setStatus("mandatory")


class _SvAtmPortIlmiEventThreshold_Type(Integer32):
    """Custom type svAtmPortIlmiEventThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvAtmPortIlmiEventThreshold_Type.__name__ = "Integer32"
_SvAtmPortIlmiEventThreshold_Object = MibTableColumn
svAtmPortIlmiEventThreshold = _SvAtmPortIlmiEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 21),
    _SvAtmPortIlmiEventThreshold_Type()
)
svAtmPortIlmiEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiEventThreshold.setStatus("mandatory")


class _SvAtmPortIlmiErrorThreshold_Type(Integer32):
    """Custom type svAtmPortIlmiErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvAtmPortIlmiErrorThreshold_Type.__name__ = "Integer32"
_SvAtmPortIlmiErrorThreshold_Object = MibTableColumn
svAtmPortIlmiErrorThreshold = _SvAtmPortIlmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 22),
    _SvAtmPortIlmiErrorThreshold_Type()
)
svAtmPortIlmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiErrorThreshold.setStatus("mandatory")


class _SvAtmPortIlmiEnquiryInterval_Type(Integer32):
    """Custom type svAtmPortIlmiEnquiryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SvAtmPortIlmiEnquiryInterval_Type.__name__ = "Integer32"
_SvAtmPortIlmiEnquiryInterval_Object = MibTableColumn
svAtmPortIlmiEnquiryInterval = _SvAtmPortIlmiEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 23),
    _SvAtmPortIlmiEnquiryInterval_Type()
)
svAtmPortIlmiEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIlmiEnquiryInterval.setStatus("mandatory")


class _SvAtmPortLmiVpi_Type(Integer32):
    """Custom type svAtmPortLmiVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SvAtmPortLmiVpi_Type.__name__ = "Integer32"
_SvAtmPortLmiVpi_Object = MibTableColumn
svAtmPortLmiVpi = _SvAtmPortLmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 24),
    _SvAtmPortLmiVpi_Type()
)
svAtmPortLmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiVpi.setStatus("mandatory")


class _SvAtmPortLmiVci_Type(Integer32):
    """Custom type svAtmPortLmiVci based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvAtmPortLmiVci_Type.__name__ = "Integer32"
_SvAtmPortLmiVci_Object = MibTableColumn
svAtmPortLmiVci = _SvAtmPortLmiVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 25),
    _SvAtmPortLmiVci_Type()
)
svAtmPortLmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiVci.setStatus("mandatory")


class _SvAtmPortLmiPollEnable_Type(Integer32):
    """Custom type svAtmPortLmiPollEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmPortLmiPollEnable_Type.__name__ = "Integer32"
_SvAtmPortLmiPollEnable_Object = MibTableColumn
svAtmPortLmiPollEnable = _SvAtmPortLmiPollEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 26),
    _SvAtmPortLmiPollEnable_Type()
)
svAtmPortLmiPollEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiPollEnable.setStatus("mandatory")


class _SvAtmPortLmiStatEnqTimer_Type(Integer32):
    """Custom type svAtmPortLmiStatEnqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SvAtmPortLmiStatEnqTimer_Type.__name__ = "Integer32"
_SvAtmPortLmiStatEnqTimer_Object = MibTableColumn
svAtmPortLmiStatEnqTimer = _SvAtmPortLmiStatEnqTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 27),
    _SvAtmPortLmiStatEnqTimer_Type()
)
svAtmPortLmiStatEnqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiStatEnqTimer.setStatus("mandatory")


class _SvAtmPortLmiUpdStatTimer_Type(Integer32):
    """Custom type svAtmPortLmiUpdStatTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SvAtmPortLmiUpdStatTimer_Type.__name__ = "Integer32"
_SvAtmPortLmiUpdStatTimer_Object = MibTableColumn
svAtmPortLmiUpdStatTimer = _SvAtmPortLmiUpdStatTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 28),
    _SvAtmPortLmiUpdStatTimer_Type()
)
svAtmPortLmiUpdStatTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiUpdStatTimer.setStatus("mandatory")


class _SvAtmPortLmiStatEnqRetry_Type(Integer32):
    """Custom type svAtmPortLmiStatEnqRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvAtmPortLmiStatEnqRetry_Type.__name__ = "Integer32"
_SvAtmPortLmiStatEnqRetry_Object = MibTableColumn
svAtmPortLmiStatEnqRetry = _SvAtmPortLmiStatEnqRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 29),
    _SvAtmPortLmiStatEnqRetry_Type()
)
svAtmPortLmiStatEnqRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiStatEnqRetry.setStatus("mandatory")


class _SvAtmPortLmiUpdStatRetry_Type(Integer32):
    """Custom type svAtmPortLmiUpdStatRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvAtmPortLmiUpdStatRetry_Type.__name__ = "Integer32"
_SvAtmPortLmiUpdStatRetry_Object = MibTableColumn
svAtmPortLmiUpdStatRetry = _SvAtmPortLmiUpdStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 30),
    _SvAtmPortLmiUpdStatRetry_Type()
)
svAtmPortLmiUpdStatRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiUpdStatRetry.setStatus("mandatory")


class _SvAtmPortLmiPollTimer_Type(Integer32):
    """Custom type svAtmPortLmiPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SvAtmPortLmiPollTimer_Type.__name__ = "Integer32"
_SvAtmPortLmiPollTimer_Object = MibTableColumn
svAtmPortLmiPollTimer = _SvAtmPortLmiPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 31),
    _SvAtmPortLmiPollTimer_Type()
)
svAtmPortLmiPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortLmiPollTimer.setStatus("mandatory")


class _SvAtmBxPortMetro_Type(Integer32):
    """Custom type svAtmBxPortMetro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmBxPortMetro_Type.__name__ = "Integer32"
_SvAtmBxPortMetro_Object = MibTableColumn
svAtmBxPortMetro = _SvAtmBxPortMetro_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 32),
    _SvAtmBxPortMetro_Type()
)
svAtmBxPortMetro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmBxPortMetro.setStatus("mandatory")


class _SvAtmPortNumLines_Type(Integer32):
    """Custom type svAtmPortNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvAtmPortNumLines_Type.__name__ = "Integer32"
_SvAtmPortNumLines_Object = MibTableColumn
svAtmPortNumLines = _SvAtmPortNumLines_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 33),
    _SvAtmPortNumLines_Type()
)
svAtmPortNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortNumLines.setStatus("mandatory")


class _SvAtmPortAssociatedLines_Type(DisplayString):
    """Custom type svAtmPortAssociatedLines based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SvAtmPortAssociatedLines_Type.__name__ = "DisplayString"
_SvAtmPortAssociatedLines_Object = MibTableColumn
svAtmPortAssociatedLines = _SvAtmPortAssociatedLines_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 34),
    _SvAtmPortAssociatedLines_Type()
)
svAtmPortAssociatedLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortAssociatedLines.setStatus("mandatory")


class _SvAtmImaPortMode_Type(Integer32):
    """Custom type svAtmImaPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("ima", 2))
    )


_SvAtmImaPortMode_Type.__name__ = "Integer32"
_SvAtmImaPortMode_Object = MibTableColumn
svAtmImaPortMode = _SvAtmImaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 35),
    _SvAtmImaPortMode_Type()
)
svAtmImaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmImaPortMode.setStatus("mandatory")


class _SvAtmImaPortNumRedundantLines_Type(Integer32):
    """Custom type svAtmImaPortNumRedundantLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvAtmImaPortNumRedundantLines_Type.__name__ = "Integer32"
_SvAtmImaPortNumRedundantLines_Object = MibTableColumn
svAtmImaPortNumRedundantLines = _SvAtmImaPortNumRedundantLines_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 36),
    _SvAtmImaPortNumRedundantLines_Type()
)
svAtmImaPortNumRedundantLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmImaPortNumRedundantLines.setStatus("mandatory")


class _SvAtmImaPortMaxTolerableDiffDelay_Type(Integer32):
    """Custom type svAtmImaPortMaxTolerableDiffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SvAtmImaPortMaxTolerableDiffDelay_Type.__name__ = "Integer32"
_SvAtmImaPortMaxTolerableDiffDelay_Object = MibTableColumn
svAtmImaPortMaxTolerableDiffDelay = _SvAtmImaPortMaxTolerableDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 37),
    _SvAtmImaPortMaxTolerableDiffDelay_Type()
)
svAtmImaPortMaxTolerableDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmImaPortMaxTolerableDiffDelay.setStatus("mandatory")


class _SvAtmPortCACOverride_Type(Integer32):
    """Custom type svAtmPortCACOverride based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvAtmPortCACOverride_Type.__name__ = "Integer32"
_SvAtmPortCACOverride_Object = MibTableColumn
svAtmPortCACOverride = _SvAtmPortCACOverride_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 38),
    _SvAtmPortCACOverride_Type()
)
svAtmPortCACOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortCACOverride.setStatus("mandatory")


class _SvAtmPortlcpCellsPeriodicity_Type(Integer32):
    """Custom type svAtmPortlcpCellsPeriodicity based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 128),
    )


_SvAtmPortlcpCellsPeriodicity_Type.__name__ = "Integer32"
_SvAtmPortlcpCellsPeriodicity_Object = MibTableColumn
svAtmPortlcpCellsPeriodicity = _SvAtmPortlcpCellsPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 39),
    _SvAtmPortlcpCellsPeriodicity_Type()
)
svAtmPortlcpCellsPeriodicity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortlcpCellsPeriodicity.setStatus("mandatory")


class _SvAtmPortTxAvailCellRate_Type(Integer32):
    """Custom type svAtmPortTxAvailCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 38330),
    )


_SvAtmPortTxAvailCellRate_Type.__name__ = "Integer32"
_SvAtmPortTxAvailCellRate_Object = MibTableColumn
svAtmPortTxAvailCellRate = _SvAtmPortTxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 40),
    _SvAtmPortTxAvailCellRate_Type()
)
svAtmPortTxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortTxAvailCellRate.setStatus("mandatory")


class _SvAtmPortSymmetry_Type(Integer32):
    """Custom type svAtmPortSymmetry based on Integer32"""
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
        *(("symmetricOperation", 1),
          ("asymmetricOperation", 2),
          ("asymmetriConfiguration", 3))
    )


_SvAtmPortSymmetry_Type.__name__ = "Integer32"
_SvAtmPortSymmetry_Object = MibTableColumn
svAtmPortSymmetry = _SvAtmPortSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 41),
    _SvAtmPortSymmetry_Type()
)
svAtmPortSymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortSymmetry.setStatus("mandatory")


class _SvAtmPortMinNumRxLinks_Type(Integer32):
    """Custom type svAtmPortMinNumRxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvAtmPortMinNumRxLinks_Type.__name__ = "Integer32"
_SvAtmPortMinNumRxLinks_Object = MibTableColumn
svAtmPortMinNumRxLinks = _SvAtmPortMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 42),
    _SvAtmPortMinNumRxLinks_Type()
)
svAtmPortMinNumRxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortMinNumRxLinks.setStatus("mandatory")


class _SvAtmPortNeTxClkMode_Type(Integer32):
    """Custom type svAtmPortNeTxClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )


_SvAtmPortNeTxClkMode_Type.__name__ = "Integer32"
_SvAtmPortNeTxClkMode_Object = MibTableColumn
svAtmPortNeTxClkMode = _SvAtmPortNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 43),
    _SvAtmPortNeTxClkMode_Type()
)
svAtmPortNeTxClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortNeTxClkMode.setStatus("mandatory")
_SvAtmPortNumRxCfgLnks_Type = Integer32
_SvAtmPortNumRxCfgLnks_Object = MibTableColumn
svAtmPortNumRxCfgLnks = _SvAtmPortNumRxCfgLnks_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 44),
    _SvAtmPortNumRxCfgLnks_Type()
)
svAtmPortNumRxCfgLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortNumRxCfgLnks.setStatus("mandatory")


class _SvAtmPortTestLinkIfIndex_Type(Integer32):
    """Custom type svAtmPortTestLinkIfIndex based on Integer32"""
    defaultValue = -1


_SvAtmPortTestLinkIfIndex_Type.__name__ = "Integer32"
_SvAtmPortTestLinkIfIndex_Object = MibTableColumn
svAtmPortTestLinkIfIndex = _SvAtmPortTestLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 45),
    _SvAtmPortTestLinkIfIndex_Type()
)
svAtmPortTestLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortTestLinkIfIndex.setStatus("mandatory")


class _SvAtmPortTestPattern_Type(Integer32):
    """Custom type svAtmPortTestPattern based on Integer32"""
    defaultValue = -1


_SvAtmPortTestPattern_Type.__name__ = "Integer32"
_SvAtmPortTestPattern_Object = MibTableColumn
svAtmPortTestPattern = _SvAtmPortTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 46),
    _SvAtmPortTestPattern_Type()
)
svAtmPortTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortTestPattern.setStatus("mandatory")


class _SvAtmPortTestProcStatus_Type(Integer32):
    """Custom type svAtmPortTestProcStatus based on Integer32"""
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
        *(("disabled", 1),
          ("operating", 2),
          ("linkfail", 3))
    )


_SvAtmPortTestProcStatus_Type.__name__ = "Integer32"
_SvAtmPortTestProcStatus_Object = MibTableColumn
svAtmPortTestProcStatus = _SvAtmPortTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 47),
    _SvAtmPortTestProcStatus_Type()
)
svAtmPortTestProcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortTestProcStatus.setStatus("mandatory")


class _SvAtmPortIntegrationUpTime_Type(Integer32):
    """Custom type svAtmPortIntegrationUpTime based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_SvAtmPortIntegrationUpTime_Type.__name__ = "Integer32"
_SvAtmPortIntegrationUpTime_Object = MibTableColumn
svAtmPortIntegrationUpTime = _SvAtmPortIntegrationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 48),
    _SvAtmPortIntegrationUpTime_Type()
)
svAtmPortIntegrationUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIntegrationUpTime.setStatus("mandatory")


class _SvAtmPortIntegrationDownTime_Type(Integer32):
    """Custom type svAtmPortIntegrationDownTime based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 400000),
    )


_SvAtmPortIntegrationDownTime_Type.__name__ = "Integer32"
_SvAtmPortIntegrationDownTime_Object = MibTableColumn
svAtmPortIntegrationDownTime = _SvAtmPortIntegrationDownTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 49),
    _SvAtmPortIntegrationDownTime_Type()
)
svAtmPortIntegrationDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortIntegrationDownTime.setStatus("mandatory")


class _SvAtmPortMinNumTxLinks_Type(Integer32):
    """Custom type svAtmPortMinNumTxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvAtmPortMinNumTxLinks_Type.__name__ = "Integer32"
_SvAtmPortMinNumTxLinks_Object = MibTableColumn
svAtmPortMinNumTxLinks = _SvAtmPortMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 50),
    _SvAtmPortMinNumTxLinks_Type()
)
svAtmPortMinNumTxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAtmPortMinNumTxLinks.setStatus("mandatory")


class _SvAtmPortnumLinksPresentInImaGroup_Type(Integer32):
    """Custom type svAtmPortnumLinksPresentInImaGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvAtmPortnumLinksPresentInImaGroup_Type.__name__ = "Integer32"
_SvAtmPortnumLinksPresentInImaGroup_Object = MibTableColumn
svAtmPortnumLinksPresentInImaGroup = _SvAtmPortnumLinksPresentInImaGroup_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 51),
    _SvAtmPortnumLinksPresentInImaGroup_Type()
)
svAtmPortnumLinksPresentInImaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortnumLinksPresentInImaGroup.setStatus("mandatory")


class _SvAtmPortimaArbitrationWinner_Type(Integer32):
    """Custom type svAtmPortimaArbitrationWinner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isUnknown", 1),
          ("isWinner", 2),
          ("isLoser", 3))
    )


_SvAtmPortimaArbitrationWinner_Type.__name__ = "Integer32"
_SvAtmPortimaArbitrationWinner_Object = MibTableColumn
svAtmPortimaArbitrationWinner = _SvAtmPortimaArbitrationWinner_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 52),
    _SvAtmPortimaArbitrationWinner_Type()
)
svAtmPortimaArbitrationWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortimaArbitrationWinner.setStatus("mandatory")


class _SvAtmPortremoteImaId_Type(Integer32):
    """Custom type svAtmPortremoteImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvAtmPortremoteImaId_Type.__name__ = "Integer32"
_SvAtmPortremoteImaId_Object = MibTableColumn
svAtmPortremoteImaId = _SvAtmPortremoteImaId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 53),
    _SvAtmPortremoteImaId_Type()
)
svAtmPortremoteImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortremoteImaId.setStatus("mandatory")


class _SvAtmPortlocImaId_Type(Integer32):
    """Custom type svAtmPortlocImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvAtmPortlocImaId_Type.__name__ = "Integer32"
_SvAtmPortlocImaId_Object = MibTableColumn
svAtmPortlocImaId = _SvAtmPortlocImaId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 54),
    _SvAtmPortlocImaId_Type()
)
svAtmPortlocImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortlocImaId.setStatus("mandatory")
_SvAtmPortimaObsDiffDelay_Type = Integer32
_SvAtmPortimaObsDiffDelay_Object = MibTableColumn
svAtmPortimaObsDiffDelay = _SvAtmPortimaObsDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 55),
    _SvAtmPortimaObsDiffDelay_Type()
)
svAtmPortimaObsDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortimaObsDiffDelay.setStatus("mandatory")


class _SvAtmPortOversubscribed_Type(Integer32):
    """Custom type svAtmPortOversubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvAtmPortOversubscribed_Type.__name__ = "Integer32"
_SvAtmPortOversubscribed_Object = MibTableColumn
svAtmPortOversubscribed = _SvAtmPortOversubscribed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 56),
    _SvAtmPortOversubscribed_Type()
)
svAtmPortOversubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortOversubscribed.setStatus("mandatory")
_SvAtmPortRxAvailCellRate_Type = Integer32
_SvAtmPortRxAvailCellRate_Object = MibTableColumn
svAtmPortRxAvailCellRate = _SvAtmPortRxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 57),
    _SvAtmPortRxAvailCellRate_Type()
)
svAtmPortRxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortRxAvailCellRate.setStatus("mandatory")


class _SvAtmPortFeState_Type(Integer32):
    """Custom type svAtmPortFeState based on Integer32"""
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
        *(("notConfigured", 1),
          ("startUp", 2),
          ("startUpAck", 3),
          ("configAbortUnsupportedM", 4),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("insufficientLinks", 7),
          ("blocked", 8),
          ("operational", 9))
    )


_SvAtmPortFeState_Type.__name__ = "Integer32"
_SvAtmPortFeState_Object = MibTableColumn
svAtmPortFeState = _SvAtmPortFeState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 58),
    _SvAtmPortFeState_Type()
)
svAtmPortFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortFeState.setStatus("mandatory")


class _SvAtmPortFailureStatus_Type(Integer32):
    """Custom type svAtmPortFailureStatus based on Integer32"""
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
        *(("noFailure", 1),
          ("startUpNe", 2),
          ("startUpFe", 3),
          ("invalidMValueNe", 4),
          ("invalidMValueFe", 5),
          ("failedAssymetricNe", 6),
          ("failedAssymetricFe", 7),
          ("insufficientLinksNe", 8),
          ("insufficientLinksFe", 9),
          ("blockedNe", 10),
          ("blockedFe", 11),
          ("otherFailure", 12))
    )


_SvAtmPortFailureStatus_Type.__name__ = "Integer32"
_SvAtmPortFailureStatus_Object = MibTableColumn
svAtmPortFailureStatus = _SvAtmPortFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 59),
    _SvAtmPortFailureStatus_Type()
)
svAtmPortFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortFailureStatus.setStatus("mandatory")


class _SvAtmPortFeTxClkMode_Type(Integer32):
    """Custom type svAtmPortFeTxClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )


_SvAtmPortFeTxClkMode_Type.__name__ = "Integer32"
_SvAtmPortFeTxClkMode_Object = MibTableColumn
svAtmPortFeTxClkMode = _SvAtmPortFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 60),
    _SvAtmPortFeTxClkMode_Type()
)
svAtmPortFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortFeTxClkMode.setStatus("mandatory")
_SvAtmPortTxTimingRefLink_Type = Integer32
_SvAtmPortTxTimingRefLink_Object = MibTableColumn
svAtmPortTxTimingRefLink = _SvAtmPortTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 61),
    _SvAtmPortTxTimingRefLink_Type()
)
svAtmPortTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortTxTimingRefLink.setStatus("mandatory")
_SvAtmPortRxTimingRefLink_Type = Integer32
_SvAtmPortRxTimingRefLink_Object = MibTableColumn
svAtmPortRxTimingRefLink = _SvAtmPortRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 62),
    _SvAtmPortRxTimingRefLink_Type()
)
svAtmPortRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortRxTimingRefLink.setStatus("mandatory")


class _SvAtmPortRxFrameLength_Type(Integer32):
    """Custom type svAtmPortRxFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m32", 32),
          ("m64", 64),
          ("m128", 128),
          ("m256", 256))
    )


_SvAtmPortRxFrameLength_Type.__name__ = "Integer32"
_SvAtmPortRxFrameLength_Object = MibTableColumn
svAtmPortRxFrameLength = _SvAtmPortRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 63),
    _SvAtmPortRxFrameLength_Type()
)
svAtmPortRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortRxFrameLength.setStatus("mandatory")
_SvAtmPortLeastDelayLink_Type = Integer32
_SvAtmPortLeastDelayLink_Object = MibTableColumn
svAtmPortLeastDelayLink = _SvAtmPortLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 64),
    _SvAtmPortLeastDelayLink_Type()
)
svAtmPortLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortLeastDelayLink.setStatus("mandatory")
_SvAtmPortNumRxActLnks_Type = Integer32
_SvAtmPortNumRxActLnks_Object = MibTableColumn
svAtmPortNumRxActLnks = _SvAtmPortNumRxActLnks_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 65),
    _SvAtmPortNumRxActLnks_Type()
)
svAtmPortNumRxActLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortNumRxActLnks.setStatus("mandatory")


class _SvAtmPortNeState_Type(Integer32):
    """Custom type svAtmPortNeState based on Integer32"""
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
        *(("notConfigured", 1),
          ("startUp", 2),
          ("startUpAck", 3),
          ("configAbortUnsupportedM", 4),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("insufficientLinks", 7),
          ("blocked", 8),
          ("operational", 9))
    )


_SvAtmPortNeState_Type.__name__ = "Integer32"
_SvAtmPortNeState_Object = MibTableColumn
svAtmPortNeState = _SvAtmPortNeState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 5, 1, 66),
    _SvAtmPortNeState_Type()
)
svAtmPortNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAtmPortNeState.setStatus("mandatory")
_PsaErrorLastIndex_Type = Integer32
_PsaErrorLastIndex_Object = MibScalar
psaErrorLastIndex = _PsaErrorLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 6),
    _PsaErrorLastIndex_Type()
)
psaErrorLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorLastIndex.setStatus("mandatory")


class _PsaErrorFlushAll_Type(Integer32):
    """Custom type psaErrorFlushAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("flush", 2))
    )


_PsaErrorFlushAll_Type.__name__ = "Integer32"
_PsaErrorFlushAll_Object = MibScalar
psaErrorFlushAll = _PsaErrorFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 7),
    _PsaErrorFlushAll_Type()
)
psaErrorFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psaErrorFlushAll.setStatus("mandatory")
_PsaErrorTable_Object = MibTable
psaErrorTable = _PsaErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 8)
)
if mibBuilder.loadTexts:
    psaErrorTable.setStatus("mandatory")
_PsaErrorEntry_Object = MibTableRow
psaErrorEntry = _PsaErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 8, 1)
)
psaErrorEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "psaErrorReqId"),
)
if mibBuilder.loadTexts:
    psaErrorEntry.setStatus("mandatory")
_PsaErrorReqId_Type = Integer32
_PsaErrorReqId_Object = MibTableColumn
psaErrorReqId = _PsaErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 8, 1, 1),
    _PsaErrorReqId_Type()
)
psaErrorReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorReqId.setStatus("mandatory")


class _PsaErrorDesc_Type(DisplayString):
    """Custom type psaErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PsaErrorDesc_Type.__name__ = "DisplayString"
_PsaErrorDesc_Object = MibTableColumn
psaErrorDesc = _PsaErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 8, 1, 2),
    _PsaErrorDesc_Type()
)
psaErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorDesc.setStatus("mandatory")


class _PsaErrorEcode_Type(Integer32):
    """Custom type psaErrorEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-shelf", 3),
          ("invalid-release", 4),
          ("node-timeout", 5),
          ("node-busy", 6),
          ("no-snmpcomm", 7),
          ("snmpcomm-error", 8),
          ("node-error", 9),
          ("bad-value", 10),
          ("port-not-found", 11),
          ("slot-is-full", 12),
          ("no-emd", 13),
          ("emd-error", 14),
          ("rowstatus-missing", 100),
          ("port-exists", 101),
          ("invalid-slot", 102),
          ("invalid-line", 103),
          ("line-is-full", 104),
          ("multiple-ports", 105),
          ("port-reserved", 106),
          ("na-frsm", 107),
          ("na-frp", 108),
          ("no-up-down-frsm", 109),
          ("invalid-set", 110),
          ("illegal-set", 111),
          ("partial-add", 112),
          ("na-ausm", 113),
          ("na-iam", 114),
          ("na-atm", 115),
          ("na-bxm", 116),
          ("na-hs1", 117),
          ("na-cesm", 118),
          ("invalid-port-index", 119),
          ("unsupported-card", 120),
          ("lmi-var", 121),
          ("na-ufm", 122),
          ("na-frm", 123),
          ("na-asi", 124),
          ("na-card", 125),
          ("missing-mandatory", 127),
          ("na-frsm-hs1", 128),
          ("invalid-line-number", 129),
          ("na-ufmU", 130),
          ("protocol-group-not-found", 131),
          ("na-frasm", 132),
          ("na-uxm", 133),
          ("link-station-not-found", 134),
          ("channel-route-not-found", 135),
          ("channel-not-found", 136),
          ("card-not-found", 137),
          ("invalid-grp-type-index", 138),
          ("invalid-grp-number-index", 139),
          ("invalid-station-addr-index", 140),
          ("db-access-error", 141),
          ("internal-error", 142),
          ("link-station-exists", 143),
          ("max-link-station-count-reached", 144),
          ("na-port-type", 145),
          ("invalid-channel-dlci-index", 146),
          ("channel-route-exists", 147),
          ("max-channel-route-count-reached", 148),
          ("protocol-group-exists", 149),
          ("max-protocol-group-count-reached", 150),
          ("invalid-config-type", 151),
          ("no-error-entry", 500),
          ("not-applicable", 501),
          ("invalid-flushall", 502))
    )


_PsaErrorEcode_Type.__name__ = "Integer32"
_PsaErrorEcode_Object = MibTableColumn
psaErrorEcode = _PsaErrorEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 8, 1, 3),
    _PsaErrorEcode_Type()
)
psaErrorEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorEcode.setStatus("mandatory")


class _PsaErrorLastDesc_Type(DisplayString):
    """Custom type psaErrorLastDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsaErrorLastDesc_Type.__name__ = "DisplayString"
_PsaErrorLastDesc_Object = MibScalar
psaErrorLastDesc = _PsaErrorLastDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 9),
    _PsaErrorLastDesc_Type()
)
psaErrorLastDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorLastDesc.setStatus("mandatory")


class _PsaErrorLastEcode_Type(Integer32):
    """Custom type psaErrorLastEcode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("invalid-network", 1),
          ("invalid-node", 2),
          ("invalid-shelf", 3),
          ("invalid-release", 4),
          ("node-timeout", 5),
          ("node-busy", 6),
          ("no-snmpcomm", 7),
          ("snmpcomm-error", 8),
          ("node-error", 9),
          ("bad-value", 10),
          ("port-not-found", 11),
          ("slot-is-full", 12),
          ("no-emd", 13),
          ("emd-error", 14),
          ("rowstatus-missing", 100),
          ("port-exists", 101),
          ("invalid-slot", 102),
          ("invalid-line", 103),
          ("line-is-full", 104),
          ("multiple-ports", 105),
          ("port-reserved", 106),
          ("na-frsm", 107),
          ("na-frp", 108),
          ("no-up-down-frsm", 109),
          ("invalid-set", 110),
          ("illegal-set", 111),
          ("partial-add", 112),
          ("na-ausm", 113),
          ("na-iam", 114),
          ("na-atm", 115),
          ("na-bxm", 116),
          ("na-hs1", 117),
          ("na-cesm", 118),
          ("invalid-port-index", 119),
          ("unsupported-card", 120),
          ("lmi-var", 121),
          ("na-ufm", 122),
          ("na-frm", 123),
          ("na-asi", 124),
          ("na-card", 125),
          ("missing-mandatory", 127),
          ("na-frsm-hs1", 128),
          ("invalid-line-number", 129),
          ("na-ufmU", 130),
          ("protocol-group-not-found", 131),
          ("na-frasm", 132),
          ("na-uxm", 133),
          ("link-station-not-found", 134),
          ("channel-route-not-found", 135),
          ("channel-not-found", 136),
          ("card-not-found", 137),
          ("invalid-grp-type-index", 138),
          ("invalid-grp-number-index", 139),
          ("invalid-station-addr-index", 140),
          ("db-access-error", 141),
          ("internal-error", 142),
          ("link-station-exists", 143),
          ("max-link-station-count-reached", 144),
          ("na-port-type", 145),
          ("invalid-channel-dlci-index", 146),
          ("channel-route-exists", 147),
          ("max-channel-route-count-reached", 148),
          ("protocol-group-exists", 149),
          ("max-protocol-group-count-reached", 150),
          ("invalid-config-type", 151),
          ("no-error-entry", 500),
          ("not-applicable", 501),
          ("invalid-flushall", 502))
    )


_PsaErrorLastEcode_Type.__name__ = "Integer32"
_PsaErrorLastEcode_Object = MibScalar
psaErrorLastEcode = _PsaErrorLastEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 10),
    _PsaErrorLastEcode_Type()
)
psaErrorLastEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psaErrorLastEcode.setStatus("mandatory")
_SvPortAlarmTable_Object = MibTable
svPortAlarmTable = _SvPortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11)
)
if mibBuilder.loadTexts:
    svPortAlarmTable.setStatus("mandatory")
_SvPortAlarmEntry_Object = MibTableRow
svPortAlarmEntry = _SvPortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1)
)
svPortAlarmEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortAlarmNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortAlarmShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortAlarmSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortAlarmLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortAlarmPort"),
)
if mibBuilder.loadTexts:
    svPortAlarmEntry.setStatus("mandatory")


class _SvPortAlarmNode_Type(DisplayString):
    """Custom type svPortAlarmNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvPortAlarmNode_Type.__name__ = "DisplayString"
_SvPortAlarmNode_Object = MibTableColumn
svPortAlarmNode = _SvPortAlarmNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 1),
    _SvPortAlarmNode_Type()
)
svPortAlarmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmNode.setStatus("mandatory")


class _SvPortAlarmShelf_Type(DisplayString):
    """Custom type svPortAlarmShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvPortAlarmShelf_Type.__name__ = "DisplayString"
_SvPortAlarmShelf_Object = MibTableColumn
svPortAlarmShelf = _SvPortAlarmShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 2),
    _SvPortAlarmShelf_Type()
)
svPortAlarmShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmShelf.setStatus("mandatory")


class _SvPortAlarmSlot_Type(Integer32):
    """Custom type svPortAlarmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SvPortAlarmSlot_Type.__name__ = "Integer32"
_SvPortAlarmSlot_Object = MibTableColumn
svPortAlarmSlot = _SvPortAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 3),
    _SvPortAlarmSlot_Type()
)
svPortAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmSlot.setStatus("mandatory")


class _SvPortAlarmLine_Type(Integer32):
    """Custom type svPortAlarmLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SvPortAlarmLine_Type.__name__ = "Integer32"
_SvPortAlarmLine_Object = MibTableColumn
svPortAlarmLine = _SvPortAlarmLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 4),
    _SvPortAlarmLine_Type()
)
svPortAlarmLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmLine.setStatus("mandatory")


class _SvPortAlarmPort_Type(Integer32):
    """Custom type svPortAlarmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SvPortAlarmPort_Type.__name__ = "Integer32"
_SvPortAlarmPort_Object = MibTableColumn
svPortAlarmPort = _SvPortAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 5),
    _SvPortAlarmPort_Type()
)
svPortAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmPort.setStatus("mandatory")


class _SvPortAlarmPortType_Type(Integer32):
    """Custom type svPortAlarmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fr", 1),
          ("atm", 4),
          ("cesm", 5))
    )


_SvPortAlarmPortType_Type.__name__ = "Integer32"
_SvPortAlarmPortType_Object = MibTableColumn
svPortAlarmPortType = _SvPortAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 11, 1, 6),
    _SvPortAlarmPortType_Type()
)
svPortAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPortAlarmPortType.setStatus("mandatory")
_SvFrasmProtocolGroupTable_Object = MibTable
svFrasmProtocolGroupTable = _SvFrasmProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12)
)
if mibBuilder.loadTexts:
    svFrasmProtocolGroupTable.setStatus("mandatory")
_SvFrasmProtocolGroupEntry_Object = MibTableRow
svFrasmProtocolGroupEntry = _SvFrasmProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1)
)
svFrasmProtocolGroupEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrasmProtocolGroupNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrasmProtocolGroupShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrasmProtocolGroupSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrasmProtocolGroupType"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svFrasmProtocolGroupNumber"),
)
if mibBuilder.loadTexts:
    svFrasmProtocolGroupEntry.setStatus("mandatory")


class _SvFrasmProtocolGroupNode_Type(DisplayString):
    """Custom type svFrasmProtocolGroupNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvFrasmProtocolGroupNode_Type.__name__ = "DisplayString"
_SvFrasmProtocolGroupNode_Object = MibTableColumn
svFrasmProtocolGroupNode = _SvFrasmProtocolGroupNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 1),
    _SvFrasmProtocolGroupNode_Type()
)
svFrasmProtocolGroupNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupNode.setStatus("mandatory")


class _SvFrasmProtocolGroupShelf_Type(DisplayString):
    """Custom type svFrasmProtocolGroupShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvFrasmProtocolGroupShelf_Type.__name__ = "DisplayString"
_SvFrasmProtocolGroupShelf_Object = MibTableColumn
svFrasmProtocolGroupShelf = _SvFrasmProtocolGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 2),
    _SvFrasmProtocolGroupShelf_Type()
)
svFrasmProtocolGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupShelf.setStatus("mandatory")


class _SvFrasmProtocolGroupSlot_Type(Integer32):
    """Custom type svFrasmProtocolGroupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SvFrasmProtocolGroupSlot_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupSlot_Object = MibTableColumn
svFrasmProtocolGroupSlot = _SvFrasmProtocolGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 3),
    _SvFrasmProtocolGroupSlot_Type()
)
svFrasmProtocolGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupSlot.setStatus("mandatory")


class _SvFrasmProtocolGroupType_Type(Integer32):
    """Custom type svFrasmProtocolGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stun", 1),
          ("bstun", 2))
    )


_SvFrasmProtocolGroupType_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupType_Object = MibTableColumn
svFrasmProtocolGroupType = _SvFrasmProtocolGroupType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 4),
    _SvFrasmProtocolGroupType_Type()
)
svFrasmProtocolGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupType.setStatus("mandatory")


class _SvFrasmProtocolGroupNumber_Type(Integer32):
    """Custom type svFrasmProtocolGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvFrasmProtocolGroupNumber_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupNumber_Object = MibTableColumn
svFrasmProtocolGroupNumber = _SvFrasmProtocolGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 5),
    _SvFrasmProtocolGroupNumber_Type()
)
svFrasmProtocolGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupNumber.setStatus("mandatory")


class _SvFrasmProtocolGroupRowStatus_Type(Integer32):
    """Custom type svFrasmProtocolGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4))
    )


_SvFrasmProtocolGroupRowStatus_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupRowStatus_Object = MibTableColumn
svFrasmProtocolGroupRowStatus = _SvFrasmProtocolGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 6),
    _SvFrasmProtocolGroupRowStatus_Type()
)
svFrasmProtocolGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupRowStatus.setStatus("mandatory")


class _SvFrasmProtocolGroupConfigType_Type(Integer32):
    """Custom type svFrasmProtocolGroupConfigType based on Integer32"""
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
        *(("sdlc", 1),
          ("sdlctg", 2),
          ("bsc", 3))
    )


_SvFrasmProtocolGroupConfigType_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupConfigType_Object = MibTableColumn
svFrasmProtocolGroupConfigType = _SvFrasmProtocolGroupConfigType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 7),
    _SvFrasmProtocolGroupConfigType_Type()
)
svFrasmProtocolGroupConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupConfigType.setStatus("mandatory")


class _SvFrasmProtocolGroupLocalAck_Type(Integer32):
    """Custom type svFrasmProtocolGroupLocalAck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SvFrasmProtocolGroupLocalAck_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupLocalAck_Object = MibTableColumn
svFrasmProtocolGroupLocalAck = _SvFrasmProtocolGroupLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 8),
    _SvFrasmProtocolGroupLocalAck_Type()
)
svFrasmProtocolGroupLocalAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupLocalAck.setStatus("mandatory")


class _SvFrasmProtocolGroupOperStatus_Type(Integer32):
    """Custom type svFrasmProtocolGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_SvFrasmProtocolGroupOperStatus_Type.__name__ = "Integer32"
_SvFrasmProtocolGroupOperStatus_Object = MibTableColumn
svFrasmProtocolGroupOperStatus = _SvFrasmProtocolGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 12, 1, 9),
    _SvFrasmProtocolGroupOperStatus_Type()
)
svFrasmProtocolGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svFrasmProtocolGroupOperStatus.setStatus("mandatory")
_SvSdlcLinkStationTable_Object = MibTable
svSdlcLinkStationTable = _SvSdlcLinkStationTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13)
)
if mibBuilder.loadTexts:
    svSdlcLinkStationTable.setStatus("mandatory")
_SvSdlcLinkStationEntry_Object = MibTableRow
svSdlcLinkStationEntry = _SvSdlcLinkStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1)
)
svSdlcLinkStationEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svSdlcLinkStationAddress"),
)
if mibBuilder.loadTexts:
    svSdlcLinkStationEntry.setStatus("mandatory")


class _SvSdlcLinkStationNode_Type(DisplayString):
    """Custom type svSdlcLinkStationNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvSdlcLinkStationNode_Type.__name__ = "DisplayString"
_SvSdlcLinkStationNode_Object = MibTableColumn
svSdlcLinkStationNode = _SvSdlcLinkStationNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 1),
    _SvSdlcLinkStationNode_Type()
)
svSdlcLinkStationNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationNode.setStatus("mandatory")


class _SvSdlcLinkStationShelf_Type(DisplayString):
    """Custom type svSdlcLinkStationShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvSdlcLinkStationShelf_Type.__name__ = "DisplayString"
_SvSdlcLinkStationShelf_Object = MibTableColumn
svSdlcLinkStationShelf = _SvSdlcLinkStationShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 2),
    _SvSdlcLinkStationShelf_Type()
)
svSdlcLinkStationShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationShelf.setStatus("mandatory")


class _SvSdlcLinkStationSlot_Type(Integer32):
    """Custom type svSdlcLinkStationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SvSdlcLinkStationSlot_Type.__name__ = "Integer32"
_SvSdlcLinkStationSlot_Object = MibTableColumn
svSdlcLinkStationSlot = _SvSdlcLinkStationSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 3),
    _SvSdlcLinkStationSlot_Type()
)
svSdlcLinkStationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationSlot.setStatus("mandatory")


class _SvSdlcLinkStationLine_Type(Integer32):
    """Custom type svSdlcLinkStationLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvSdlcLinkStationLine_Type.__name__ = "Integer32"
_SvSdlcLinkStationLine_Object = MibTableColumn
svSdlcLinkStationLine = _SvSdlcLinkStationLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 4),
    _SvSdlcLinkStationLine_Type()
)
svSdlcLinkStationLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationLine.setStatus("mandatory")


class _SvSdlcLinkStationPort_Type(Integer32):
    """Custom type svSdlcLinkStationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvSdlcLinkStationPort_Type.__name__ = "Integer32"
_SvSdlcLinkStationPort_Object = MibTableColumn
svSdlcLinkStationPort = _SvSdlcLinkStationPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 5),
    _SvSdlcLinkStationPort_Type()
)
svSdlcLinkStationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationPort.setStatus("mandatory")


class _SvSdlcLinkStationAddress_Type(Integer32):
    """Custom type svSdlcLinkStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvSdlcLinkStationAddress_Type.__name__ = "Integer32"
_SvSdlcLinkStationAddress_Object = MibTableColumn
svSdlcLinkStationAddress = _SvSdlcLinkStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 6),
    _SvSdlcLinkStationAddress_Type()
)
svSdlcLinkStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationAddress.setStatus("mandatory")


class _SvSdlcLinkStationRowStatus_Type(Integer32):
    """Custom type svSdlcLinkStationRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4))
    )


_SvSdlcLinkStationRowStatus_Type.__name__ = "Integer32"
_SvSdlcLinkStationRowStatus_Object = MibTableColumn
svSdlcLinkStationRowStatus = _SvSdlcLinkStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 7),
    _SvSdlcLinkStationRowStatus_Type()
)
svSdlcLinkStationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svSdlcLinkStationRowStatus.setStatus("mandatory")


class _SvSdlcLinkStationXID_Type(Integer32):
    """Custom type svSdlcLinkStationXID based on Integer32"""
    defaultValue = 0


_SvSdlcLinkStationXID_Type.__name__ = "Integer32"
_SvSdlcLinkStationXID_Object = MibTableColumn
svSdlcLinkStationXID = _SvSdlcLinkStationXID_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 8),
    _SvSdlcLinkStationXID_Type()
)
svSdlcLinkStationXID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svSdlcLinkStationXID.setStatus("mandatory")


class _SvSdlcLinkStationMaxFrame_Type(Integer32):
    """Custom type svSdlcLinkStationMaxFrame based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_SvSdlcLinkStationMaxFrame_Type.__name__ = "Integer32"
_SvSdlcLinkStationMaxFrame_Object = MibTableColumn
svSdlcLinkStationMaxFrame = _SvSdlcLinkStationMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 9),
    _SvSdlcLinkStationMaxFrame_Type()
)
svSdlcLinkStationMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svSdlcLinkStationMaxFrame.setStatus("mandatory")


class _SvSdlcLinkStationOperStatus_Type(Integer32):
    """Custom type svSdlcLinkStationOperStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("discpend", 2),
          ("snrmseen", 3),
          ("error", 4),
          ("xidsent", 5),
          ("xidstop", 6),
          ("snrmsent", 7),
          ("connect", 8),
          ("thembusy", 9),
          ("usbusy", 10),
          ("bothbusy", 11))
    )


_SvSdlcLinkStationOperStatus_Type.__name__ = "Integer32"
_SvSdlcLinkStationOperStatus_Object = MibTableColumn
svSdlcLinkStationOperStatus = _SvSdlcLinkStationOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 13, 1, 10),
    _SvSdlcLinkStationOperStatus_Type()
)
svSdlcLinkStationOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSdlcLinkStationOperStatus.setStatus("mandatory")
_SvChannelRouteTable_Object = MibTable
svChannelRouteTable = _SvChannelRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14)
)
if mibBuilder.loadTexts:
    svChannelRouteTable.setStatus("mandatory")
_SvChannelRouteEntry_Object = MibTableRow
svChannelRouteEntry = _SvChannelRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1)
)
svChannelRouteEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRouteNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRouteShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRouteSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRouteLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRoutePort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svChannelRouteStationAddress"),
)
if mibBuilder.loadTexts:
    svChannelRouteEntry.setStatus("mandatory")


class _SvChannelRouteNode_Type(DisplayString):
    """Custom type svChannelRouteNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvChannelRouteNode_Type.__name__ = "DisplayString"
_SvChannelRouteNode_Object = MibTableColumn
svChannelRouteNode = _SvChannelRouteNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 1),
    _SvChannelRouteNode_Type()
)
svChannelRouteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteNode.setStatus("mandatory")


class _SvChannelRouteShelf_Type(DisplayString):
    """Custom type svChannelRouteShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvChannelRouteShelf_Type.__name__ = "DisplayString"
_SvChannelRouteShelf_Object = MibTableColumn
svChannelRouteShelf = _SvChannelRouteShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 2),
    _SvChannelRouteShelf_Type()
)
svChannelRouteShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteShelf.setStatus("mandatory")


class _SvChannelRouteSlot_Type(Integer32):
    """Custom type svChannelRouteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SvChannelRouteSlot_Type.__name__ = "Integer32"
_SvChannelRouteSlot_Object = MibTableColumn
svChannelRouteSlot = _SvChannelRouteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 3),
    _SvChannelRouteSlot_Type()
)
svChannelRouteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteSlot.setStatus("mandatory")


class _SvChannelRouteLine_Type(Integer32):
    """Custom type svChannelRouteLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvChannelRouteLine_Type.__name__ = "Integer32"
_SvChannelRouteLine_Object = MibTableColumn
svChannelRouteLine = _SvChannelRouteLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 4),
    _SvChannelRouteLine_Type()
)
svChannelRouteLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteLine.setStatus("mandatory")


class _SvChannelRoutePort_Type(Integer32):
    """Custom type svChannelRoutePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvChannelRoutePort_Type.__name__ = "Integer32"
_SvChannelRoutePort_Object = MibTableColumn
svChannelRoutePort = _SvChannelRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 5),
    _SvChannelRoutePort_Type()
)
svChannelRoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRoutePort.setStatus("mandatory")


class _SvChannelRouteStationAddress_Type(Integer32):
    """Custom type svChannelRouteStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvChannelRouteStationAddress_Type.__name__ = "Integer32"
_SvChannelRouteStationAddress_Object = MibTableColumn
svChannelRouteStationAddress = _SvChannelRouteStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 6),
    _SvChannelRouteStationAddress_Type()
)
svChannelRouteStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteStationAddress.setStatus("mandatory")


class _SvChannelRouteRowStatus_Type(Integer32):
    """Custom type svChannelRouteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4))
    )


_SvChannelRouteRowStatus_Type.__name__ = "Integer32"
_SvChannelRouteRowStatus_Object = MibTableColumn
svChannelRouteRowStatus = _SvChannelRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 7),
    _SvChannelRouteRowStatus_Type()
)
svChannelRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteRowStatus.setStatus("mandatory")


class _SvChannelRouteDlci_Type(Integer32):
    """Custom type svChannelRouteDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_SvChannelRouteDlci_Type.__name__ = "Integer32"
_SvChannelRouteDlci_Object = MibTableColumn
svChannelRouteDlci = _SvChannelRouteDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 8),
    _SvChannelRouteDlci_Type()
)
svChannelRouteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteDlci.setStatus("mandatory")


class _SvChannelRouteOperStatus_Type(Integer32):
    """Custom type svChannelRouteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_SvChannelRouteOperStatus_Type.__name__ = "Integer32"
_SvChannelRouteOperStatus_Object = MibTableColumn
svChannelRouteOperStatus = _SvChannelRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 9),
    _SvChannelRouteOperStatus_Type()
)
svChannelRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svChannelRouteOperStatus.setStatus("mandatory")


class _SvChannelRouteLSAP_Type(Integer32):
    """Custom type svChannelRouteLSAP based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SvChannelRouteLSAP_Type.__name__ = "Integer32"
_SvChannelRouteLSAP_Object = MibTableColumn
svChannelRouteLSAP = _SvChannelRouteLSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 10),
    _SvChannelRouteLSAP_Type()
)
svChannelRouteLSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteLSAP.setStatus("mandatory")


class _SvChannelRouteRSAP_Type(Integer32):
    """Custom type svChannelRouteRSAP based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SvChannelRouteRSAP_Type.__name__ = "Integer32"
_SvChannelRouteRSAP_Object = MibTableColumn
svChannelRouteRSAP = _SvChannelRouteRSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 11),
    _SvChannelRouteRSAP_Type()
)
svChannelRouteRSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteRSAP.setStatus("mandatory")


class _SvChannelRouteTHType_Type(Integer32):
    """Custom type svChannelRouteTHType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pfid", 2),
          ("fid4", 4),
          ("afid", 10))
    )


_SvChannelRouteTHType_Type.__name__ = "Integer32"
_SvChannelRouteTHType_Object = MibTableColumn
svChannelRouteTHType = _SvChannelRouteTHType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 12),
    _SvChannelRouteTHType_Type()
)
svChannelRouteTHType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteTHType.setStatus("mandatory")


class _SvChannelRouteChannelType_Type(Integer32):
    """Custom type svChannelRouteChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stun", 1),
          ("bstun", 2),
          ("frasbnn", 3))
    )


_SvChannelRouteChannelType_Type.__name__ = "Integer32"
_SvChannelRouteChannelType_Object = MibTableColumn
svChannelRouteChannelType = _SvChannelRouteChannelType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 14, 1, 13),
    _SvChannelRouteChannelType_Type()
)
svChannelRouteChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svChannelRouteChannelType.setStatus("mandatory")
_SvLlcChannelParamTable_Object = MibTable
svLlcChannelParamTable = _SvLlcChannelParamTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15)
)
if mibBuilder.loadTexts:
    svLlcChannelParamTable.setStatus("mandatory")
_SvLlcChannelParamEntry_Object = MibTableRow
svLlcChannelParamEntry = _SvLlcChannelParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1)
)
svLlcChannelParamEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamPort"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svLlcChannelParamDlci"),
)
if mibBuilder.loadTexts:
    svLlcChannelParamEntry.setStatus("mandatory")


class _SvLlcChannelParamNode_Type(DisplayString):
    """Custom type svLlcChannelParamNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvLlcChannelParamNode_Type.__name__ = "DisplayString"
_SvLlcChannelParamNode_Object = MibTableColumn
svLlcChannelParamNode = _SvLlcChannelParamNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 1),
    _SvLlcChannelParamNode_Type()
)
svLlcChannelParamNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamNode.setStatus("mandatory")


class _SvLlcChannelParamShelf_Type(DisplayString):
    """Custom type svLlcChannelParamShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvLlcChannelParamShelf_Type.__name__ = "DisplayString"
_SvLlcChannelParamShelf_Object = MibTableColumn
svLlcChannelParamShelf = _SvLlcChannelParamShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 2),
    _SvLlcChannelParamShelf_Type()
)
svLlcChannelParamShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamShelf.setStatus("mandatory")


class _SvLlcChannelParamSlot_Type(Integer32):
    """Custom type svLlcChannelParamSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SvLlcChannelParamSlot_Type.__name__ = "Integer32"
_SvLlcChannelParamSlot_Object = MibTableColumn
svLlcChannelParamSlot = _SvLlcChannelParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 3),
    _SvLlcChannelParamSlot_Type()
)
svLlcChannelParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamSlot.setStatus("mandatory")


class _SvLlcChannelParamLine_Type(Integer32):
    """Custom type svLlcChannelParamLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvLlcChannelParamLine_Type.__name__ = "Integer32"
_SvLlcChannelParamLine_Object = MibTableColumn
svLlcChannelParamLine = _SvLlcChannelParamLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 4),
    _SvLlcChannelParamLine_Type()
)
svLlcChannelParamLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamLine.setStatus("mandatory")


class _SvLlcChannelParamPort_Type(Integer32):
    """Custom type svLlcChannelParamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvLlcChannelParamPort_Type.__name__ = "Integer32"
_SvLlcChannelParamPort_Object = MibTableColumn
svLlcChannelParamPort = _SvLlcChannelParamPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 5),
    _SvLlcChannelParamPort_Type()
)
svLlcChannelParamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamPort.setStatus("mandatory")


class _SvLlcChannelParamDlci_Type(Integer32):
    """Custom type svLlcChannelParamDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_SvLlcChannelParamDlci_Type.__name__ = "Integer32"
_SvLlcChannelParamDlci_Object = MibTableColumn
svLlcChannelParamDlci = _SvLlcChannelParamDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 6),
    _SvLlcChannelParamDlci_Type()
)
svLlcChannelParamDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLlcChannelParamDlci.setStatus("mandatory")


class _SvLlcChannelParamRowStatus_Type(Integer32):
    """Custom type svLlcChannelParamRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("modify", 4)
    )


_SvLlcChannelParamRowStatus_Type.__name__ = "Integer32"
_SvLlcChannelParamRowStatus_Object = MibTableColumn
svLlcChannelParamRowStatus = _SvLlcChannelParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 7),
    _SvLlcChannelParamRowStatus_Type()
)
svLlcChannelParamRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svLlcChannelParamRowStatus.setStatus("mandatory")


class _SvLlcChannelParamRetryCnt_Type(Integer32):
    """Custom type svLlcChannelParamRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvLlcChannelParamRetryCnt_Type.__name__ = "Integer32"
_SvLlcChannelParamRetryCnt_Object = MibTableColumn
svLlcChannelParamRetryCnt = _SvLlcChannelParamRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 8),
    _SvLlcChannelParamRetryCnt_Type()
)
svLlcChannelParamRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svLlcChannelParamRetryCnt.setStatus("mandatory")


class _SvLlcChannelParamAckWaitTime_Type(Integer32):
    """Custom type svLlcChannelParamAckWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_SvLlcChannelParamAckWaitTime_Type.__name__ = "Integer32"
_SvLlcChannelParamAckWaitTime_Object = MibTableColumn
svLlcChannelParamAckWaitTime = _SvLlcChannelParamAckWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 15, 1, 9),
    _SvLlcChannelParamAckWaitTime_Type()
)
svLlcChannelParamAckWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svLlcChannelParamAckWaitTime.setStatus("mandatory")
_SvCesmPortTable_Object = MibTable
svCesmPortTable = _SvCesmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16)
)
if mibBuilder.loadTexts:
    svCesmPortTable.setStatus("mandatory")
_SvCesmPortEntry_Object = MibTableRow
svCesmPortEntry = _SvCesmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1)
)
svCesmPortEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCesmPortNode"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCesmPortShelf"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCesmPortSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCesmPortLine"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svCesmPortPort"),
)
if mibBuilder.loadTexts:
    svCesmPortEntry.setStatus("mandatory")


class _SvCesmPortNode_Type(DisplayString):
    """Custom type svCesmPortNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SvCesmPortNode_Type.__name__ = "DisplayString"
_SvCesmPortNode_Object = MibTableColumn
svCesmPortNode = _SvCesmPortNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 1),
    _SvCesmPortNode_Type()
)
svCesmPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortNode.setStatus("mandatory")


class _SvCesmPortShelf_Type(DisplayString):
    """Custom type svCesmPortShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvCesmPortShelf_Type.__name__ = "DisplayString"
_SvCesmPortShelf_Object = MibTableColumn
svCesmPortShelf = _SvCesmPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 2),
    _SvCesmPortShelf_Type()
)
svCesmPortShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortShelf.setStatus("mandatory")


class _SvCesmPortSlot_Type(Integer32):
    """Custom type svCesmPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SvCesmPortSlot_Type.__name__ = "Integer32"
_SvCesmPortSlot_Object = MibTableColumn
svCesmPortSlot = _SvCesmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 3),
    _SvCesmPortSlot_Type()
)
svCesmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortSlot.setStatus("mandatory")


class _SvCesmPortLine_Type(Integer32):
    """Custom type svCesmPortLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SvCesmPortLine_Type.__name__ = "Integer32"
_SvCesmPortLine_Object = MibTableColumn
svCesmPortLine = _SvCesmPortLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 4),
    _SvCesmPortLine_Type()
)
svCesmPortLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortLine.setStatus("mandatory")


class _SvCesmPortPort_Type(Integer32):
    """Custom type svCesmPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvCesmPortPort_Type.__name__ = "Integer32"
_SvCesmPortPort_Object = MibTableColumn
svCesmPortPort = _SvCesmPortPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 5),
    _SvCesmPortPort_Type()
)
svCesmPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortPort.setStatus("mandatory")


class _SvCesmPortRowStatus_Type(Integer32):
    """Custom type svCesmPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4))
    )


_SvCesmPortRowStatus_Type.__name__ = "Integer32"
_SvCesmPortRowStatus_Object = MibTableColumn
svCesmPortRowStatus = _SvCesmPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 6),
    _SvCesmPortRowStatus_Type()
)
svCesmPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCesmPortRowStatus.setStatus("mandatory")


class _SvCesmPortOperState_Type(Integer32):
    """Custom type svCesmPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3))
    )


_SvCesmPortOperState_Type.__name__ = "Integer32"
_SvCesmPortOperState_Object = MibTableColumn
svCesmPortOperState = _SvCesmPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 7),
    _SvCesmPortOperState_Type()
)
svCesmPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortOperState.setStatus("mandatory")


class _SvCesmPortAdminState_Type(Integer32):
    """Custom type svCesmPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SvCesmPortAdminState_Type.__name__ = "Integer32"
_SvCesmPortAdminState_Object = MibTableColumn
svCesmPortAdminState = _SvCesmPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 8),
    _SvCesmPortAdminState_Type()
)
svCesmPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCesmPortAdminState.setStatus("mandatory")


class _SvCesmPortCardType_Type(Integer32):
    """Custom type svCesmPortCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              22)
        )
    )
    namedValues = NamedValues(
        *(("cesm-4", 4),
          ("cesm-8", 22))
    )


_SvCesmPortCardType_Type.__name__ = "Integer32"
_SvCesmPortCardType_Object = MibTableColumn
svCesmPortCardType = _SvCesmPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 9),
    _SvCesmPortCardType_Type()
)
svCesmPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortCardType.setStatus("mandatory")


class _SvCesmPortIfType_Type(Integer32):
    """Custom type svCesmPortIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1", 2),
          ("e1", 3))
    )


_SvCesmPortIfType_Type.__name__ = "Integer32"
_SvCesmPortIfType_Object = MibTableColumn
svCesmPortIfType = _SvCesmPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 10),
    _SvCesmPortIfType_Type()
)
svCesmPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortIfType.setStatus("mandatory")


class _SvCesmPortSpeed_Type(Integer32):
    """Custom type svCesmPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(640, 20480),
    )


_SvCesmPortSpeed_Type.__name__ = "Integer32"
_SvCesmPortSpeed_Object = MibTableColumn
svCesmPortSpeed = _SvCesmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 11),
    _SvCesmPortSpeed_Type()
)
svCesmPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCesmPortSpeed.setStatus("mandatory")


class _SvCesmPortVcCount_Type(Integer32):
    """Custom type svCesmPortVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SvCesmPortVcCount_Type.__name__ = "Integer32"
_SvCesmPortVcCount_Object = MibTableColumn
svCesmPortVcCount = _SvCesmPortVcCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 12),
    _SvCesmPortVcCount_Type()
)
svCesmPortVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortVcCount.setStatus("mandatory")
_SvCesmPortVcPtr_Type = ObjectIdentifier
_SvCesmPortVcPtr_Object = MibTableColumn
svCesmPortVcPtr = _SvCesmPortVcPtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 13),
    _SvCesmPortVcPtr_Type()
)
svCesmPortVcPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortVcPtr.setStatus("mandatory")


class _SvCesmPortType_Type(Integer32):
    """Custom type svCesmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("structured", 1),
          ("unstructured", 2),
          ("framingOnVcDisconnect", 3))
    )


_SvCesmPortType_Type.__name__ = "Integer32"
_SvCesmPortType_Object = MibTableColumn
svCesmPortType = _SvCesmPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 14),
    _SvCesmPortType_Type()
)
svCesmPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svCesmPortType.setStatus("mandatory")


class _SvCesmPortChCnt_Type(Integer32):
    """Custom type svCesmPortChCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SvCesmPortChCnt_Type.__name__ = "Integer32"
_SvCesmPortChCnt_Object = MibTableColumn
svCesmPortChCnt = _SvCesmPortChCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 2, 16, 1, 15),
    _SvCesmPortChCnt_Type()
)
svCesmPortChCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svCesmPortChCnt.setStatus("mandatory")
_InsDas_ObjectIdentity = ObjectIdentity
insDas = _InsDas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3)
)
_DasAniTable_Object = MibTable
dasAniTable = _DasAniTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1)
)
if mibBuilder.loadTexts:
    dasAniTable.setStatus("mandatory")
_DasAniEntry_Object = MibTableRow
dasAniEntry = _DasAniEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1)
)
dasAniEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dasAniAni"),
)
if mibBuilder.loadTexts:
    dasAniEntry.setStatus("mandatory")


class _DasAniAni_Type(DisplayString):
    """Custom type dasAniAni based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DasAniAni_Type.__name__ = "DisplayString"
_DasAniAni_Object = MibTableColumn
dasAniAni = _DasAniAni_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 1),
    _DasAniAni_Type()
)
dasAniAni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasAniAni.setStatus("mandatory")


class _DasAniRowStatus_Type(Integer32):
    """Custom type dasAniRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addAni", 1),
          ("delAni", 2),
          ("modAni", 3))
    )


_DasAniRowStatus_Type.__name__ = "Integer32"
_DasAniRowStatus_Object = MibTableColumn
dasAniRowStatus = _DasAniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 2),
    _DasAniRowStatus_Type()
)
dasAniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniRowStatus.setStatus("mandatory")


class _DasAniAniType_Type(Integer32):
    """Custom type dasAniAniType based on Integer32"""
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
        *(("dialup", 1),
          ("dialbackup", 2),
          ("dasiDialup", 3),
          ("dasiDialbackup", 4),
          ("hostnameDialup", 5))
    )


_DasAniAniType_Type.__name__ = "Integer32"
_DasAniAniType_Object = MibTableColumn
dasAniAniType = _DasAniAniType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 3),
    _DasAniAniType_Type()
)
dasAniAniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniAniType.setStatus("mandatory")


class _DasAniMaxTxQDepth_Type(Integer32):
    """Custom type dasAniMaxTxQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasAniMaxTxQDepth_Type.__name__ = "Integer32"
_DasAniMaxTxQDepth_Object = MibTableColumn
dasAniMaxTxQDepth = _DasAniMaxTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 4),
    _DasAniMaxTxQDepth_Type()
)
dasAniMaxTxQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniMaxTxQDepth.setStatus("mandatory")


class _DasAniECNQThresh_Type(Integer32):
    """Custom type dasAniECNQThresh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasAniECNQThresh_Type.__name__ = "Integer32"
_DasAniECNQThresh_Object = MibTableColumn
dasAniECNQThresh = _DasAniECNQThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 5),
    _DasAniECNQThresh_Type()
)
dasAniECNQThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniECNQThresh.setStatus("mandatory")


class _DasAniDEThresh_Type(Integer32):
    """Custom type dasAniDEThresh based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DasAniDEThresh_Type.__name__ = "Integer32"
_DasAniDEThresh_Object = MibTableColumn
dasAniDEThresh = _DasAniDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 6),
    _DasAniDEThresh_Type()
)
dasAniDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniDEThresh.setStatus("mandatory")


class _DasAniCLLMTimer_Type(Integer32):
    """Custom type dasAniCLLMTimer based on Integer32"""
    defaultValue = 0


_DasAniCLLMTimer_Type.__name__ = "Integer32"
_DasAniCLLMTimer_Object = MibTableColumn
dasAniCLLMTimer = _DasAniCLLMTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 7),
    _DasAniCLLMTimer_Type()
)
dasAniCLLMTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniCLLMTimer.setStatus("mandatory")


class _DasAniIDEMap_Type(Integer32):
    """Custom type dasAniIDEMap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DasAniIDEMap_Type.__name__ = "Integer32"
_DasAniIDEMap_Object = MibTableColumn
dasAniIDEMap = _DasAniIDEMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 8),
    _DasAniIDEMap_Type()
)
dasAniIDEMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniIDEMap.setStatus("mandatory")


class _DasAniFrmFlags_Type(Integer32):
    """Custom type dasAniFrmFlags based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DasAniFrmFlags_Type.__name__ = "Integer32"
_DasAniFrmFlags_Object = MibTableColumn
dasAniFrmFlags = _DasAniFrmFlags_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 9),
    _DasAniFrmFlags_Type()
)
dasAniFrmFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniFrmFlags.setStatus("mandatory")


class _DasAniSigProto_Type(Integer32):
    """Custom type dasAniSigProto based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("strataLMI", 2),
          ("annexA", 3),
          ("annexD", 4))
    )


_DasAniSigProto_Type.__name__ = "Integer32"
_DasAniSigProto_Object = MibTableColumn
dasAniSigProto = _DasAniSigProto_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 10),
    _DasAniSigProto_Type()
)
dasAniSigProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniSigProto.setStatus("mandatory")


class _DasAniPortIf_Type(Integer32):
    """Custom type dasAniPortIf based on Integer32"""
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
        *(("nni", 1),
          ("uni", 2),
          ("na", 3))
    )


_DasAniPortIf_Type.__name__ = "Integer32"
_DasAniPortIf_Object = MibTableColumn
dasAniPortIf = _DasAniPortIf_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 11),
    _DasAniPortIf_Type()
)
dasAniPortIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniPortIf.setStatus("mandatory")


class _DasAniAsyncStatus_Type(Integer32):
    """Custom type dasAniAsyncStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DasAniAsyncStatus_Type.__name__ = "Integer32"
_DasAniAsyncStatus_Object = MibTableColumn
dasAniAsyncStatus = _DasAniAsyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 12),
    _DasAniAsyncStatus_Type()
)
dasAniAsyncStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniAsyncStatus.setStatus("mandatory")


class _DasAniPollVerTimer_Type(Integer32):
    """Custom type dasAniPollVerTimer based on Integer32"""
    defaultValue = 15


_DasAniPollVerTimer_Type.__name__ = "Integer32"
_DasAniPollVerTimer_Object = MibTableColumn
dasAniPollVerTimer = _DasAniPollVerTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 13),
    _DasAniPollVerTimer_Type()
)
dasAniPollVerTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniPollVerTimer.setStatus("mandatory")


class _DasAniErrThresh_Type(Integer32):
    """Custom type dasAniErrThresh based on Integer32"""
    defaultValue = 5


_DasAniErrThresh_Type.__name__ = "Integer32"
_DasAniErrThresh_Object = MibTableColumn
dasAniErrThresh = _DasAniErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 14),
    _DasAniErrThresh_Type()
)
dasAniErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniErrThresh.setStatus("mandatory")


class _DasAniMonEveCnt_Type(Integer32):
    """Custom type dasAniMonEveCnt based on Integer32"""
    defaultValue = 5


_DasAniMonEveCnt_Type.__name__ = "Integer32"
_DasAniMonEveCnt_Object = MibTableColumn
dasAniMonEveCnt = _DasAniMonEveCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 15),
    _DasAniMonEveCnt_Type()
)
dasAniMonEveCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniMonEveCnt.setStatus("mandatory")


class _DasAniOamThresh_Type(Integer32):
    """Custom type dasAniOamThresh based on Integer32"""
    defaultValue = 5


_DasAniOamThresh_Type.__name__ = "Integer32"
_DasAniOamThresh_Object = MibTableColumn
dasAniOamThresh = _DasAniOamThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 16),
    _DasAniOamThresh_Type()
)
dasAniOamThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniOamThresh.setStatus("mandatory")


class _DasAniCommPri_Type(Integer32):
    """Custom type dasAniCommPri based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DasAniCommPri_Type.__name__ = "Integer32"
_DasAniCommPri_Object = MibTableColumn
dasAniCommPri = _DasAniCommPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 17),
    _DasAniCommPri_Type()
)
dasAniCommPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniCommPri.setStatus("mandatory")


class _DasAniUpRNR_Type(Integer32):
    """Custom type dasAniUpRNR based on Integer32"""
    defaultValue = 75


_DasAniUpRNR_Type.__name__ = "Integer32"
_DasAniUpRNR_Object = MibTableColumn
dasAniUpRNR = _DasAniUpRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 18),
    _DasAniUpRNR_Type()
)
dasAniUpRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniUpRNR.setStatus("mandatory")


class _DasAniLowRNR_Type(Integer32):
    """Custom type dasAniLowRNR based on Integer32"""
    defaultValue = 75


_DasAniLowRNR_Type.__name__ = "Integer32"
_DasAniLowRNR_Object = MibTableColumn
dasAniLowRNR = _DasAniLowRNR_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 1, 1, 19),
    _DasAniLowRNR_Type()
)
dasAniLowRNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasAniLowRNR.setStatus("mandatory")
_DasConnTable_Object = MibTable
dasConnTable = _DasConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2)
)
if mibBuilder.loadTexts:
    dasConnTable.setStatus("mandatory")
_DasConnEntry_Object = MibTableRow
dasConnEntry = _DasConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1)
)
dasConnEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dasConnAni"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dasConnOrgDlci"),
)
if mibBuilder.loadTexts:
    dasConnEntry.setStatus("mandatory")


class _DasConnAni_Type(DisplayString):
    """Custom type dasConnAni based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DasConnAni_Type.__name__ = "DisplayString"
_DasConnAni_Object = MibTableColumn
dasConnAni = _DasConnAni_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 1),
    _DasConnAni_Type()
)
dasConnAni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnAni.setStatus("mandatory")


class _DasConnOrgDlci_Type(Integer32):
    """Custom type dasConnOrgDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DasConnOrgDlci_Type.__name__ = "Integer32"
_DasConnOrgDlci_Object = MibTableColumn
dasConnOrgDlci = _DasConnOrgDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 2),
    _DasConnOrgDlci_Type()
)
dasConnOrgDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnOrgDlci.setStatus("mandatory")


class _DasConnRowStatus_Type(Integer32):
    """Custom type dasConnRowStatus based on Integer32"""
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
        *(("addConn", 1),
          ("delConn", 2),
          ("modConn", 3),
          ("addAssc", 4),
          ("delAssc", 5),
          ("addConnAndAssc", 6))
    )


_DasConnRowStatus_Type.__name__ = "Integer32"
_DasConnRowStatus_Object = MibTableColumn
dasConnRowStatus = _DasConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 3),
    _DasConnRowStatus_Type()
)
dasConnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnRowStatus.setStatus("mandatory")


class _DasConnAniType_Type(Integer32):
    """Custom type dasConnAniType based on Integer32"""
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
        *(("dialup", 1),
          ("dialbackup", 2),
          ("dasiDialup", 3),
          ("dasiDialbackup", 4))
    )


_DasConnAniType_Type.__name__ = "Integer32"
_DasConnAniType_Object = MibTableColumn
dasConnAniType = _DasConnAniType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 4),
    _DasConnAniType_Type()
)
dasConnAniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnAniType.setStatus("mandatory")


class _DasConnConnType_Type(Integer32):
    """Custom type dasConnConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("fr-fr", 5)
    )


_DasConnConnType_Type.__name__ = "Integer32"
_DasConnConnType_Object = MibTableColumn
dasConnConnType = _DasConnConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 5),
    _DasConnConnType_Type()
)
dasConnConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnConnType.setStatus("mandatory")


class _DasConnTrmEndpt_Type(DisplayString):
    """Custom type dasConnTrmEndpt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_DasConnTrmEndpt_Type.__name__ = "DisplayString"
_DasConnTrmEndpt_Object = MibTableColumn
dasConnTrmEndpt = _DasConnTrmEndpt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 6),
    _DasConnTrmEndpt_Type()
)
dasConnTrmEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEndpt.setStatus("mandatory")


class _DasConnAsscEndpt_Type(DisplayString):
    """Custom type dasConnAsscEndpt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_DasConnAsscEndpt_Type.__name__ = "DisplayString"
_DasConnAsscEndpt_Object = MibTableColumn
dasConnAsscEndpt = _DasConnAsscEndpt_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 7),
    _DasConnAsscEndpt_Type()
)
dasConnAsscEndpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnAsscEndpt.setStatus("mandatory")


class _DasConnForesight_Type(Integer32):
    """Custom type dasConnForesight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DasConnForesight_Type.__name__ = "Integer32"
_DasConnForesight_Object = MibTableColumn
dasConnForesight = _DasConnForesight_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 8),
    _DasConnForesight_Type()
)
dasConnForesight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnForesight.setStatus("mandatory")


class _DasConnCos_Type(Integer32):
    """Custom type dasConnCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DasConnCos_Type.__name__ = "Integer32"
_DasConnCos_Object = MibTableColumn
dasConnCos = _DasConnCos_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 9),
    _DasConnCos_Type()
)
dasConnCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnCos.setStatus("mandatory")


class _DasConnTrkAvoid_Type(Integer32):
    """Custom type dasConnTrkAvoid based on Integer32"""
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
        *(("none", 1),
          ("satellite", 2),
          ("terrestrial", 3))
    )


_DasConnTrkAvoid_Type.__name__ = "Integer32"
_DasConnTrkAvoid_Object = MibTableColumn
dasConnTrkAvoid = _DasConnTrkAvoid_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 10),
    _DasConnTrkAvoid_Type()
)
dasConnTrkAvoid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrkAvoid.setStatus("mandatory")


class _DasConnZcs_Type(Integer32):
    """Custom type dasConnZcs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DasConnZcs_Type.__name__ = "Integer32"
_DasConnZcs_Object = MibTableColumn
dasConnZcs = _DasConnZcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 11),
    _DasConnZcs_Type()
)
dasConnZcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnZcs.setStatus("mandatory")


class _DasConnOrgCir_Type(Integer32):
    """Custom type dasConnOrgCir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnOrgCir_Type.__name__ = "Integer32"
_DasConnOrgCir_Object = MibTableColumn
dasConnOrgCir = _DasConnOrgCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 12),
    _DasConnOrgCir_Type()
)
dasConnOrgCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgCir.setStatus("mandatory")


class _DasConnOrgMir_Type(Integer32):
    """Custom type dasConnOrgMir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnOrgMir_Type.__name__ = "Integer32"
_DasConnOrgMir_Object = MibTableColumn
dasConnOrgMir = _DasConnOrgMir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 13),
    _DasConnOrgMir_Type()
)
dasConnOrgMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgMir.setStatus("mandatory")


class _DasConnOrgPir_Type(Integer32):
    """Custom type dasConnOrgPir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnOrgPir_Type.__name__ = "Integer32"
_DasConnOrgPir_Object = MibTableColumn
dasConnOrgPir = _DasConnOrgPir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 14),
    _DasConnOrgPir_Type()
)
dasConnOrgPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgPir.setStatus("mandatory")


class _DasConnOrgQir_Type(Integer32):
    """Custom type dasConnOrgQir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnOrgQir_Type.__name__ = "Integer32"
_DasConnOrgQir_Object = MibTableColumn
dasConnOrgQir = _DasConnOrgQir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 15),
    _DasConnOrgQir_Type()
)
dasConnOrgQir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgQir.setStatus("mandatory")


class _DasConnOrgBc_Type(Integer32):
    """Custom type dasConnOrgBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnOrgBc_Type.__name__ = "Integer32"
_DasConnOrgBc_Object = MibTableColumn
dasConnOrgBc = _DasConnOrgBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 16),
    _DasConnOrgBc_Type()
)
dasConnOrgBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnOrgBc.setStatus("mandatory")


class _DasConnOrgBe_Type(Integer32):
    """Custom type dasConnOrgBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgBe_Type.__name__ = "Integer32"
_DasConnOrgBe_Object = MibTableColumn
dasConnOrgBe = _DasConnOrgBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 17),
    _DasConnOrgBe_Type()
)
dasConnOrgBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnOrgBe.setStatus("mandatory")


class _DasConnOrgPerUtil_Type(Integer32):
    """Custom type dasConnOrgPerUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DasConnOrgPerUtil_Type.__name__ = "Integer32"
_DasConnOrgPerUtil_Object = MibTableColumn
dasConnOrgPerUtil = _DasConnOrgPerUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 18),
    _DasConnOrgPerUtil_Type()
)
dasConnOrgPerUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgPerUtil.setStatus("mandatory")


class _DasConnOrgIbs_Type(Integer32):
    """Custom type dasConnOrgIbs based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgIbs_Type.__name__ = "Integer32"
_DasConnOrgIbs_Object = MibTableColumn
dasConnOrgIbs = _DasConnOrgIbs_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 19),
    _DasConnOrgIbs_Type()
)
dasConnOrgIbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgIbs.setStatus("mandatory")


class _DasConnOrgCmax_Type(Integer32):
    """Custom type dasConnOrgCmax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DasConnOrgCmax_Type.__name__ = "Integer32"
_DasConnOrgCmax_Object = MibTableColumn
dasConnOrgCmax = _DasConnOrgCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 20),
    _DasConnOrgCmax_Type()
)
dasConnOrgCmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgCmax.setStatus("mandatory")


class _DasConnOrgVcQDepth_Type(Integer32):
    """Custom type dasConnOrgVcQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnOrgVcQDepth_Type.__name__ = "Integer32"
_DasConnOrgVcQDepth_Object = MibTableColumn
dasConnOrgVcQDepth = _DasConnOrgVcQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 21),
    _DasConnOrgVcQDepth_Type()
)
dasConnOrgVcQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgVcQDepth.setStatus("mandatory")


class _DasConnOrgEgrVcQDepth_Type(Integer32):
    """Custom type dasConnOrgEgrVcQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnOrgEgrVcQDepth_Type.__name__ = "Integer32"
_DasConnOrgEgrVcQDepth_Object = MibTableColumn
dasConnOrgEgrVcQDepth = _DasConnOrgEgrVcQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 22),
    _DasConnOrgEgrVcQDepth_Type()
)
dasConnOrgEgrVcQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgEgrVcQDepth.setStatus("mandatory")


class _DasConnOrgEcnThresh_Type(Integer32):
    """Custom type dasConnOrgEcnThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgEcnThresh_Type.__name__ = "Integer32"
_DasConnOrgEcnThresh_Object = MibTableColumn
dasConnOrgEcnThresh = _DasConnOrgEcnThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 23),
    _DasConnOrgEcnThresh_Type()
)
dasConnOrgEcnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgEcnThresh.setStatus("mandatory")


class _DasConnOrgEgrEcnThresh_Type(Integer32):
    """Custom type dasConnOrgEgrEcnThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgEgrEcnThresh_Type.__name__ = "Integer32"
_DasConnOrgEgrEcnThresh_Object = MibTableColumn
dasConnOrgEgrEcnThresh = _DasConnOrgEgrEcnThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 24),
    _DasConnOrgEgrEcnThresh_Type()
)
dasConnOrgEgrEcnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgEgrEcnThresh.setStatus("mandatory")


class _DasConnOrgIngDeThresh_Type(Integer32):
    """Custom type dasConnOrgIngDeThresh based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgIngDeThresh_Type.__name__ = "Integer32"
_DasConnOrgIngDeThresh_Object = MibTableColumn
dasConnOrgIngDeThresh = _DasConnOrgIngDeThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 25),
    _DasConnOrgIngDeThresh_Type()
)
dasConnOrgIngDeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgIngDeThresh.setStatus("mandatory")


class _DasConnOrgEgrDeThresh_Type(Integer32):
    """Custom type dasConnOrgEgrDeThresh based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnOrgEgrDeThresh_Type.__name__ = "Integer32"
_DasConnOrgEgrDeThresh_Object = MibTableColumn
dasConnOrgEgrDeThresh = _DasConnOrgEgrDeThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 26),
    _DasConnOrgEgrDeThresh_Type()
)
dasConnOrgEgrDeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgEgrDeThresh.setStatus("mandatory")


class _DasConnOrgEgrQSelect_Type(Integer32):
    """Custom type dasConnOrgEgrQSelect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_DasConnOrgEgrQSelect_Type.__name__ = "Integer32"
_DasConnOrgEgrQSelect_Object = MibTableColumn
dasConnOrgEgrQSelect = _DasConnOrgEgrQSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 27),
    _DasConnOrgEgrQSelect_Type()
)
dasConnOrgEgrQSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgEgrQSelect.setStatus("mandatory")


class _DasConnOrgIgrDeTag_Type(Integer32):
    """Custom type dasConnOrgIgrDeTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DasConnOrgIgrDeTag_Type.__name__ = "Integer32"
_DasConnOrgIgrDeTag_Object = MibTableColumn
dasConnOrgIgrDeTag = _DasConnOrgIgrDeTag_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 28),
    _DasConnOrgIgrDeTag_Type()
)
dasConnOrgIgrDeTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgIgrDeTag.setStatus("mandatory")


class _DasConnTrmCir_Type(Integer32):
    """Custom type dasConnTrmCir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnTrmCir_Type.__name__ = "Integer32"
_DasConnTrmCir_Object = MibTableColumn
dasConnTrmCir = _DasConnTrmCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 29),
    _DasConnTrmCir_Type()
)
dasConnTrmCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmCir.setStatus("mandatory")


class _DasConnTrmMir_Type(Integer32):
    """Custom type dasConnTrmMir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnTrmMir_Type.__name__ = "Integer32"
_DasConnTrmMir_Object = MibTableColumn
dasConnTrmMir = _DasConnTrmMir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 30),
    _DasConnTrmMir_Type()
)
dasConnTrmMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmMir.setStatus("mandatory")


class _DasConnTrmPir_Type(Integer32):
    """Custom type dasConnTrmPir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnTrmPir_Type.__name__ = "Integer32"
_DasConnTrmPir_Object = MibTableColumn
dasConnTrmPir = _DasConnTrmPir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 31),
    _DasConnTrmPir_Type()
)
dasConnTrmPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmPir.setStatus("mandatory")


class _DasConnTrmQir_Type(Integer32):
    """Custom type dasConnTrmQir based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2048000),
    )


_DasConnTrmQir_Type.__name__ = "Integer32"
_DasConnTrmQir_Object = MibTableColumn
dasConnTrmQir = _DasConnTrmQir_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 32),
    _DasConnTrmQir_Type()
)
dasConnTrmQir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmQir.setStatus("mandatory")


class _DasConnTrmBc_Type(Integer32):
    """Custom type dasConnTrmBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnTrmBc_Type.__name__ = "Integer32"
_DasConnTrmBc_Object = MibTableColumn
dasConnTrmBc = _DasConnTrmBc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 33),
    _DasConnTrmBc_Type()
)
dasConnTrmBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnTrmBc.setStatus("mandatory")


class _DasConnTrmBe_Type(Integer32):
    """Custom type dasConnTrmBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmBe_Type.__name__ = "Integer32"
_DasConnTrmBe_Object = MibTableColumn
dasConnTrmBe = _DasConnTrmBe_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 34),
    _DasConnTrmBe_Type()
)
dasConnTrmBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasConnTrmBe.setStatus("mandatory")


class _DasConnTrmPerUtil_Type(Integer32):
    """Custom type dasConnTrmPerUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DasConnTrmPerUtil_Type.__name__ = "Integer32"
_DasConnTrmPerUtil_Object = MibTableColumn
dasConnTrmPerUtil = _DasConnTrmPerUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 35),
    _DasConnTrmPerUtil_Type()
)
dasConnTrmPerUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmPerUtil.setStatus("mandatory")


class _DasConnTrmIbs_Type(Integer32):
    """Custom type dasConnTrmIbs based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmIbs_Type.__name__ = "Integer32"
_DasConnTrmIbs_Object = MibTableColumn
dasConnTrmIbs = _DasConnTrmIbs_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 36),
    _DasConnTrmIbs_Type()
)
dasConnTrmIbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmIbs.setStatus("mandatory")


class _DasConnTrmCmax_Type(Integer32):
    """Custom type dasConnTrmCmax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DasConnTrmCmax_Type.__name__ = "Integer32"
_DasConnTrmCmax_Object = MibTableColumn
dasConnTrmCmax = _DasConnTrmCmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 37),
    _DasConnTrmCmax_Type()
)
dasConnTrmCmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmCmax.setStatus("mandatory")


class _DasConnTrmVcQDepth_Type(Integer32):
    """Custom type dasConnTrmVcQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnTrmVcQDepth_Type.__name__ = "Integer32"
_DasConnTrmVcQDepth_Object = MibTableColumn
dasConnTrmVcQDepth = _DasConnTrmVcQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 38),
    _DasConnTrmVcQDepth_Type()
)
dasConnTrmVcQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmVcQDepth.setStatus("mandatory")


class _DasConnTrmEgrVcQDepth_Type(Integer32):
    """Custom type dasConnTrmEgrVcQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DasConnTrmEgrVcQDepth_Type.__name__ = "Integer32"
_DasConnTrmEgrVcQDepth_Object = MibTableColumn
dasConnTrmEgrVcQDepth = _DasConnTrmEgrVcQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 39),
    _DasConnTrmEgrVcQDepth_Type()
)
dasConnTrmEgrVcQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEgrVcQDepth.setStatus("mandatory")


class _DasConnTrmEcnThresh_Type(Integer32):
    """Custom type dasConnTrmEcnThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmEcnThresh_Type.__name__ = "Integer32"
_DasConnTrmEcnThresh_Object = MibTableColumn
dasConnTrmEcnThresh = _DasConnTrmEcnThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 40),
    _DasConnTrmEcnThresh_Type()
)
dasConnTrmEcnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEcnThresh.setStatus("mandatory")


class _DasConnTrmEgrEcnThresh_Type(Integer32):
    """Custom type dasConnTrmEgrEcnThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmEgrEcnThresh_Type.__name__ = "Integer32"
_DasConnTrmEgrEcnThresh_Object = MibTableColumn
dasConnTrmEgrEcnThresh = _DasConnTrmEgrEcnThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 41),
    _DasConnTrmEgrEcnThresh_Type()
)
dasConnTrmEgrEcnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEgrEcnThresh.setStatus("mandatory")


class _DasConnTrmIngDeThresh_Type(Integer32):
    """Custom type dasConnTrmIngDeThresh based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmIngDeThresh_Type.__name__ = "Integer32"
_DasConnTrmIngDeThresh_Object = MibTableColumn
dasConnTrmIngDeThresh = _DasConnTrmIngDeThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 42),
    _DasConnTrmIngDeThresh_Type()
)
dasConnTrmIngDeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmIngDeThresh.setStatus("mandatory")


class _DasConnTrmEgrDeThresh_Type(Integer32):
    """Custom type dasConnTrmEgrDeThresh based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DasConnTrmEgrDeThresh_Type.__name__ = "Integer32"
_DasConnTrmEgrDeThresh_Object = MibTableColumn
dasConnTrmEgrDeThresh = _DasConnTrmEgrDeThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 43),
    _DasConnTrmEgrDeThresh_Type()
)
dasConnTrmEgrDeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEgrDeThresh.setStatus("mandatory")


class _DasConnTrmEgrQSelect_Type(Integer32):
    """Custom type dasConnTrmEgrQSelect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_DasConnTrmEgrQSelect_Type.__name__ = "Integer32"
_DasConnTrmEgrQSelect_Object = MibTableColumn
dasConnTrmEgrQSelect = _DasConnTrmEgrQSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 44),
    _DasConnTrmEgrQSelect_Type()
)
dasConnTrmEgrQSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmEgrQSelect.setStatus("mandatory")


class _DasConnTrmIgrDeTag_Type(Integer32):
    """Custom type dasConnTrmIgrDeTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DasConnTrmIgrDeTag_Type.__name__ = "Integer32"
_DasConnTrmIgrDeTag_Object = MibTableColumn
dasConnTrmIgrDeTag = _DasConnTrmIgrDeTag_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 45),
    _DasConnTrmIgrDeTag_Type()
)
dasConnTrmIgrDeTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmIgrDeTag.setStatus("mandatory")


class _DasConnOrgPriority_Type(Integer32):
    """Custom type dasConnOrgPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_DasConnOrgPriority_Type.__name__ = "Integer32"
_DasConnOrgPriority_Object = MibTableColumn
dasConnOrgPriority = _DasConnOrgPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 46),
    _DasConnOrgPriority_Type()
)
dasConnOrgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnOrgPriority.setStatus("mandatory")


class _DasConnTrmPriority_Type(Integer32):
    """Custom type dasConnTrmPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 2))
    )


_DasConnTrmPriority_Type.__name__ = "Integer32"
_DasConnTrmPriority_Object = MibTableColumn
dasConnTrmPriority = _DasConnTrmPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 2, 1, 47),
    _DasConnTrmPriority_Type()
)
dasConnTrmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasConnTrmPriority.setStatus("mandatory")
_DasErrorTable_Object = MibTable
dasErrorTable = _DasErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 4)
)
if mibBuilder.loadTexts:
    dasErrorTable.setStatus("mandatory")
_DasErrorEntry_Object = MibTableRow
dasErrorEntry = _DasErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 4, 1)
)
dasErrorEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "dasErrorReqId"),
)
if mibBuilder.loadTexts:
    dasErrorEntry.setStatus("mandatory")
_DasErrorReqId_Type = Integer32
_DasErrorReqId_Object = MibTableColumn
dasErrorReqId = _DasErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 4, 1, 1),
    _DasErrorReqId_Type()
)
dasErrorReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorReqId.setStatus("mandatory")


class _DasErrorDesc_Type(DisplayString):
    """Custom type dasErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DasErrorDesc_Type.__name__ = "DisplayString"
_DasErrorDesc_Object = MibTableColumn
dasErrorDesc = _DasErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 4, 1, 2),
    _DasErrorDesc_Type()
)
dasErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorDesc.setStatus("mandatory")
_DasErrorEcode_Type = ErrCode
_DasErrorEcode_Object = MibTableColumn
dasErrorEcode = _DasErrorEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 4, 1, 3),
    _DasErrorEcode_Type()
)
dasErrorEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorEcode.setStatus("mandatory")
_DasErrorLastIndex_Type = Integer32
_DasErrorLastIndex_Object = MibScalar
dasErrorLastIndex = _DasErrorLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 5),
    _DasErrorLastIndex_Type()
)
dasErrorLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorLastIndex.setStatus("mandatory")


class _DasErrorFlushAll_Type(Integer32):
    """Custom type dasErrorFlushAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("flush", 2))
    )


_DasErrorFlushAll_Type.__name__ = "Integer32"
_DasErrorFlushAll_Object = MibScalar
dasErrorFlushAll = _DasErrorFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 6),
    _DasErrorFlushAll_Type()
)
dasErrorFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasErrorFlushAll.setStatus("mandatory")


class _DasErrorLastDesc_Type(DisplayString):
    """Custom type dasErrorLastDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DasErrorLastDesc_Type.__name__ = "DisplayString"
_DasErrorLastDesc_Object = MibScalar
dasErrorLastDesc = _DasErrorLastDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 7),
    _DasErrorLastDesc_Type()
)
dasErrorLastDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorLastDesc.setStatus("mandatory")
_DasErrorLastEcode_Type = ErrCode
_DasErrorLastEcode_Object = MibScalar
dasErrorLastEcode = _DasErrorLastEcode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 101, 3, 8),
    _DasErrorLastEcode_Type()
)
dasErrorLastEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dasErrorLastEcode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1",
    **{"ErrCode": ErrCode,
       "stratacom": stratacom,
       "svplus": svplus,
       "serviceGroup": serviceGroup,
       "connGroup": connGroup,
       "svConnMibUpTime": svConnMibUpTime,
       "svConnTable": svConnTable,
       "svConnEntry": svConnEntry,
       "svConnIndex": svConnIndex,
       "svConnLocalEndPt": svConnLocalEndPt,
       "svConnRemoteEndPt": svConnRemoteEndPt,
       "svConnAdminStatus": svConnAdminStatus,
       "svConnOpStatus": svConnOpStatus,
       "svConnRowStatus": svConnRowStatus,
       "svConnTrkAvoidType": svConnTrkAvoidType,
       "svConnTrkAvoidZCS": svConnTrkAvoidZCS,
       "svConnForesight": svConnForesight,
       "svConnClassOfService": svConnClassOfService,
       "svConnCurrRouteDesc": svConnCurrRouteDesc,
       "svConnPrefRouteDesc": svConnPrefRouteDesc,
       "svConnRouteMaster": svConnRouteMaster,
       "svConnLocOSpacePkts": svConnLocOSpacePkts,
       "svConnLocOSpaceBdaCmax": svConnLocOSpaceBdaCmax,
       "svConnLocOSpaceBdbCmax": svConnLocOSpaceBdbCmax,
       "svConnRemOSpacePkts": svConnRemOSpacePkts,
       "svConnRemOSpaceBdaCmax": svConnRemOSpaceBdaCmax,
       "svConnRemOSpaceBdbCmax": svConnRemOSpaceBdbCmax,
       "svConnTestType": svConnTestType,
       "svConnTestResult": svConnTestResult,
       "svConnAbitStatus": svConnAbitStatus,
       "svConnType": svConnType,
       "svConnLocalStr": svConnLocalStr,
       "svConnRemoteStr": svConnRemoteStr,
       "svConnSubType": svConnSubType,
       "svConnMiddlEndPt": svConnMiddlEndPt,
       "svConnMiddleStr": svConnMiddleStr,
       "svConnNumSegments": svConnNumSegments,
       "svConnSegment1": svConnSegment1,
       "svConnSegment2": svConnSegment2,
       "svConnSegment3": svConnSegment3,
       "svConnOvrSubOvrRide": svConnOvrSubOvrRide,
       "svConnLocOSpaceCells": svConnLocOSpaceCells,
       "svConnRemOSpaceCells": svConnRemOSpaceCells,
       "svConnCellRouting": svConnCellRouting,
       "svCmpaErrorLastIndex": svCmpaErrorLastIndex,
       "svCmpaErrorFlushAll": svCmpaErrorFlushAll,
       "svCmpaErrorTable": svCmpaErrorTable,
       "svCmpaErrorEntry": svCmpaErrorEntry,
       "svCmpaErrorReqId": svCmpaErrorReqId,
       "svCmpaErrorDesc": svCmpaErrorDesc,
       "svCmpaErrorEcode": svCmpaErrorEcode,
       "svCmpaErrorLastDesc": svCmpaErrorLastDesc,
       "svCmpaErrorLastEcode": svCmpaErrorLastEcode,
       "atmEndPointTable": atmEndPointTable,
       "atmEndPointEntry": atmEndPointEntry,
       "atmEndPointNodeName": atmEndPointNodeName,
       "atmEndPointIfShelf": atmEndPointIfShelf,
       "atmEndPointSlot": atmEndPointSlot,
       "atmEndPointPort": atmEndPointPort,
       "atmEndPointVpi": atmEndPointVpi,
       "atmEndPointVci": atmEndPointVci,
       "atmEndPointConnIndx": atmEndPointConnIndx,
       "atmEndPointOpStatus": atmEndPointOpStatus,
       "atmEndPointRowStatus": atmEndPointRowStatus,
       "atmEndPointType": atmEndPointType,
       "atmEndPointPCRZeroPlus1": atmEndPointPCRZeroPlus1,
       "atmEndPointCDVTZeroPlus1": atmEndPointCDVTZeroPlus1,
       "atmEndPointMCR": atmEndPointMCR,
       "atmEndPointPercUtil": atmEndPointPercUtil,
       "atmEndPointSCRZeroPlus1": atmEndPointSCRZeroPlus1,
       "atmEndPointMBS": atmEndPointMBS,
       "atmEndPointFGCRA": atmEndPointFGCRA,
       "atmEndPointBCM": atmEndPointBCM,
       "atmEndPointICR": atmEndPointICR,
       "atmEndPointRateUp": atmEndPointRateUp,
       "atmEndPointRateDown": atmEndPointRateDown,
       "atmEndPointICRTO": atmEndPointICRTO,
       "atmEndPointMinAdjustPeriod": atmEndPointMinAdjustPeriod,
       "atmEndPointNRM": atmEndPointNRM,
       "atmEndPointTBE": atmEndPointTBE,
       "atmEndPointFRTT": atmEndPointFRTT,
       "atmEndPointVSVD": atmEndPointVSVD,
       "atmEndPointPolicing": atmEndPointPolicing,
       "atmEndPointHiCLP": atmEndPointHiCLP,
       "atmEndPointLoCLP": atmEndPointLoCLP,
       "atmEndPointVcQSize": atmEndPointVcQSize,
       "atmEndPointEfciQSize": atmEndPointEfciQSize,
       "atmEndPointIBS": atmEndPointIBS,
       "frEndPointTable": frEndPointTable,
       "frEndPointEntry": frEndPointEntry,
       "frEndPointNodeName": frEndPointNodeName,
       "frEndPointIfShelf": frEndPointIfShelf,
       "frEndPointSlot": frEndPointSlot,
       "frEndPointPort": frEndPointPort,
       "frEndPointDlci": frEndPointDlci,
       "frEndPointConnIndex": frEndPointConnIndex,
       "frEndPointOpStatus": frEndPointOpStatus,
       "frEndPointRowStatus": frEndPointRowStatus,
       "frEndPointMIR": frEndPointMIR,
       "frEndPointCIR": frEndPointCIR,
       "frEndPointBc": frEndPointBc,
       "frEndPointBe": frEndPointBe,
       "frEndPointVcQSize": frEndPointVcQSize,
       "frEndPointPIR": frEndPointPIR,
       "frEndPointCMAX": frEndPointCMAX,
       "frEndPointEcnQSize": frEndPointEcnQSize,
       "frEndPointQIR": frEndPointQIR,
       "frEndPointPercUtil": frEndPointPercUtil,
       "frEndPointPriority": frEndPointPriority,
       "frEndPointInitialBurstSize": frEndPointInitialBurstSize,
       "frEndPointDeTagging": frEndPointDeTagging,
       "frEndPointIngressDeThreshold": frEndPointIngressDeThreshold,
       "frEndPointEgressQDepth": frEndPointEgressQDepth,
       "frEndPointEgressDeThreshold": frEndPointEgressDeThreshold,
       "frEndPointEgressEcnThreshold": frEndPointEgressEcnThreshold,
       "frEndPointEgressQSelect": frEndPointEgressQSelect,
       "frEndPointLpbkState": frEndPointLpbkState,
       "frEndPointType": frEndPointType,
       "frEndPointchanType": frEndPointchanType,
       "frEndPointchanFECNconfig": frEndPointchanFECNconfig,
       "frEndPointchanDEtoCLPmap": frEndPointchanDEtoCLPmap,
       "frEndPointchanCLPtoDEmap": frEndPointchanCLPtoDEmap,
       "frEndPointLine": frEndPointLine,
       "svConnAlarmTable": svConnAlarmTable,
       "svConnAlarmEntry": svConnAlarmEntry,
       "svConnAlarmNode": svConnAlarmNode,
       "svConnAlarmShelf": svConnAlarmShelf,
       "svConnAlarmSlot": svConnAlarmSlot,
       "svConnAlarmLine": svConnAlarmLine,
       "svConnAlarmPort": svConnAlarmPort,
       "svConnAlarmVpiOrDlci": svConnAlarmVpiOrDlci,
       "svConnAlarmVci": svConnAlarmVci,
       "svConnAlarmRemoteEnd": svConnAlarmRemoteEnd,
       "svConnAlarmConnType": svConnAlarmConnType,
       "svConnAlarmLocalEndNNI": svConnAlarmLocalEndNNI,
       "svConnAlarmRemoteEndNNI": svConnAlarmRemoteEndNNI,
       "voiceEndPointTable": voiceEndPointTable,
       "voiceEndPointEntry": voiceEndPointEntry,
       "voiceEndPointNodeName": voiceEndPointNodeName,
       "voiceEndPointIfShelf": voiceEndPointIfShelf,
       "voiceEndPointSlot": voiceEndPointSlot,
       "voiceEndPointPort": voiceEndPointPort,
       "voiceEndPointDlci": voiceEndPointDlci,
       "voiceEndPointConnIndex": voiceEndPointConnIndex,
       "voiceEndPointLine": voiceEndPointLine,
       "dataEndPointTable": dataEndPointTable,
       "dataEndPointEntry": dataEndPointEntry,
       "dataEndPointNodeName": dataEndPointNodeName,
       "dataEndPointIfShelf": dataEndPointIfShelf,
       "dataEndPointSlot": dataEndPointSlot,
       "dataEndPointPort": dataEndPointPort,
       "dataEndPointDlci": dataEndPointDlci,
       "dataEndPointConnIndex": dataEndPointConnIndex,
       "dataEndPointLine": dataEndPointLine,
       "svCeEndPointTable": svCeEndPointTable,
       "svCeEndPointEntry": svCeEndPointEntry,
       "svCeEndPointNodeName": svCeEndPointNodeName,
       "svCeEndPointIfShelf": svCeEndPointIfShelf,
       "svCeEndPointSlot": svCeEndPointSlot,
       "svCeEndPointPort": svCeEndPointPort,
       "svCeEndPointConnIndex": svCeEndPointConnIndex,
       "svCeEndPointOpStatus": svCeEndPointOpStatus,
       "svCeEndPointRowStatus": svCeEndPointRowStatus,
       "svCeEndPointType": svCeEndPointType,
       "svCeEndPointBufMaxSize": svCeEndPointBufMaxSize,
       "svCeEndPointCDVRxT": svCeEndPointCDVRxT,
       "svCeEndPointCellLossPeriod": svCeEndPointCellLossPeriod,
       "svCeEndPointLine": svCeEndPointLine,
       "svCeEndPointCBRClockMode": svCeEndPointCBRClockMode,
       "svCeEndPointCAS": svCeEndPointCAS,
       "svCeEndPointPartialFill": svCeEndPointPartialFill,
       "svCeEndPointIdleDet": svCeEndPointIdleDet,
       "svCeEndPointOnhookCode": svCeEndPointOnhookCode,
       "svCeEndPointIdleSupp": svCeEndPointIdleSupp,
       "svCeEndPointIdleCodeIntgnPeriod": svCeEndPointIdleCodeIntgnPeriod,
       "portGroup": portGroup,
       "svPortTable": svPortTable,
       "svPortEntry": svPortEntry,
       "svPortNode": svPortNode,
       "svPortShelf": svPortShelf,
       "svPortSlot": svPortSlot,
       "svPortPort": svPortPort,
       "svPortCardType": svPortCardType,
       "svPortIfType": svPortIfType,
       "svPortState": svPortState,
       "svPortSpeed": svPortSpeed,
       "svPortLine": svPortLine,
       "svPortLineIndex": svPortLineIndex,
       "svPortPhysicalPort": svPortPhysicalPort,
       "svNextLogicalPortTable": svNextLogicalPortTable,
       "svNextLogicalPortEntry": svNextLogicalPortEntry,
       "svNode": svNode,
       "svShelf": svShelf,
       "svSlot": svSlot,
       "svPort": svPort,
       "svPhysicalToLogicalMapTable": svPhysicalToLogicalMapTable,
       "svPhysicalToLogicalMapEntry": svPhysicalToLogicalMapEntry,
       "svMapNode": svMapNode,
       "svMapShelf": svMapShelf,
       "svMapSlot": svMapSlot,
       "svMapPhysicalInfo": svMapPhysicalInfo,
       "svMapLogicalPort": svMapLogicalPort,
       "svFrPortTable": svFrPortTable,
       "svFrPortEntry": svFrPortEntry,
       "svFrPortNode": svFrPortNode,
       "svFrPortShelf": svFrPortShelf,
       "svFrPortSlot": svFrPortSlot,
       "svFrPortPort": svFrPortPort,
       "svFrPortRowStatus": svFrPortRowStatus,
       "svFrPortType": svFrPortType,
       "svFrPortCardType": svFrPortCardType,
       "svFrPortIfType": svFrPortIfType,
       "svFrPortOperState": svFrPortOperState,
       "svFrPortAdminState": svFrPortAdminState,
       "svFrPortLine": svFrPortLine,
       "svFrPortStartingCh": svFrPortStartingCh,
       "svFrPortChCnt": svFrPortChCnt,
       "svFrPortSpeed": svFrPortSpeed,
       "svFrPortDs0ChSpeed": svFrPortDs0ChSpeed,
       "svFrPortSigProt": svFrPortSigProt,
       "svFrPortNNIStatus": svFrPortNNIStatus,
       "svFrPortAsyncUpd": svFrPortAsyncUpd,
       "svFrPortPollVerTimer": svFrPortPollVerTimer,
       "svFrPortErrThresh": svFrPortErrThresh,
       "svFrPortMonEveCnt": svFrPortMonEveCnt,
       "svFrPortFrmFlags": svFrPortFrmFlags,
       "svFrPortLinkTimer": svFrPortLinkTimer,
       "svFrPortPollCycle": svFrPortPollCycle,
       "svFrPortCLLMEnable": svFrPortCLLMEnable,
       "svFrPortCLLMTimer": svFrPortCLLMTimer,
       "svFrPortVcCount": svFrPortVcCount,
       "svFrPortVcPtr": svFrPortVcPtr,
       "svFrAxPortSvcRatio": svFrAxPortSvcRatio,
       "svFrIxPortMaxTxQDepth": svFrIxPortMaxTxQDepth,
       "svFrIxPortECNQThresh": svFrIxPortECNQThresh,
       "svFrIxPortDEThresh": svFrIxPortDEThresh,
       "svFrIxPortIDEMap": svFrIxPortIDEMap,
       "svFrIxPortCommPri": svFrIxPortCommPri,
       "svFrIxPortUpRNR": svFrIxPortUpRNR,
       "svFrIxPortLowRNR": svFrIxPortLowRNR,
       "svFrIxPortOamThresh": svFrIxPortOamThresh,
       "svFrIxPortEFCItoBECN": svFrIxPortEFCItoBECN,
       "svFrIxPortClockType": svFrIxPortClockType,
       "svFrIxPortSrRTS": svFrIxPortSrRTS,
       "svFrIxPortSrDTR": svFrIxPortSrDTR,
       "svFrIxPortSrDCD": svFrIxPortSrDCD,
       "svFrIxPortSrCTS": svFrIxPortSrCTS,
       "svFrIxPortSrDSR": svFrIxPortSrDSR,
       "svFrIxPortLoopBack": svFrIxPortLoopBack,
       "svFrIxPortExtConFail": svFrIxPortExtConFail,
       "svFrPortLineIndex": svFrPortLineIndex,
       "svFrPortEnhancedLmi": svFrPortEnhancedLmi,
       "svFrPortSubRateSpeed": svFrPortSubRateSpeed,
       "svFrPortPhysicalInterface": svFrPortPhysicalInterface,
       "svFrPortDataEncoding": svFrPortDataEncoding,
       "svFrPortRole": svFrPortRole,
       "svFrPortMaxFrame": svFrPortMaxFrame,
       "svFrPortRetryCnt": svFrPortRetryCnt,
       "svFrPortAckWaitTime": svFrPortAckWaitTime,
       "svFrPortPollInterval": svFrPortPollInterval,
       "svFrPortPollTimeout": svFrPortPollTimeout,
       "svFrPortProtocolGroup": svFrPortProtocolGroup,
       "svAtmPortTable": svAtmPortTable,
       "svAtmPortEntry": svAtmPortEntry,
       "svAtmPortNode": svAtmPortNode,
       "svAtmPortShelf": svAtmPortShelf,
       "svAtmPortSlot": svAtmPortSlot,
       "svAtmPortPort": svAtmPortPort,
       "svAtmPortRowStatus": svAtmPortRowStatus,
       "svAtmPortOperState": svAtmPortOperState,
       "svAtmPortAdminState": svAtmPortAdminState,
       "svAtmPortCardType": svAtmPortCardType,
       "svAtmPortIfType": svAtmPortIfType,
       "svAtmPortSpeed": svAtmPortSpeed,
       "svAtmPortVcCount": svAtmPortVcCount,
       "svAtmPortVcPtr": svAtmPortVcPtr,
       "svAtmPortType": svAtmPortType,
       "svAtmPortSignallingProtocol": svAtmPortSignallingProtocol,
       "svAtmPortIlmiVpi": svAtmPortIlmiVpi,
       "svAtmPortIlmiVci": svAtmPortIlmiVci,
       "svAtmPortIlmiTrapEnable": svAtmPortIlmiTrapEnable,
       "svAtmPortIlmiMinimumTrapInterval": svAtmPortIlmiMinimumTrapInterval,
       "svAtmPortIlmiAlivePollEnable": svAtmPortIlmiAlivePollEnable,
       "svAtmPortIlmiAlivePollInterval": svAtmPortIlmiAlivePollInterval,
       "svAtmPortIlmiEventThreshold": svAtmPortIlmiEventThreshold,
       "svAtmPortIlmiErrorThreshold": svAtmPortIlmiErrorThreshold,
       "svAtmPortIlmiEnquiryInterval": svAtmPortIlmiEnquiryInterval,
       "svAtmPortLmiVpi": svAtmPortLmiVpi,
       "svAtmPortLmiVci": svAtmPortLmiVci,
       "svAtmPortLmiPollEnable": svAtmPortLmiPollEnable,
       "svAtmPortLmiStatEnqTimer": svAtmPortLmiStatEnqTimer,
       "svAtmPortLmiUpdStatTimer": svAtmPortLmiUpdStatTimer,
       "svAtmPortLmiStatEnqRetry": svAtmPortLmiStatEnqRetry,
       "svAtmPortLmiUpdStatRetry": svAtmPortLmiUpdStatRetry,
       "svAtmPortLmiPollTimer": svAtmPortLmiPollTimer,
       "svAtmBxPortMetro": svAtmBxPortMetro,
       "svAtmPortNumLines": svAtmPortNumLines,
       "svAtmPortAssociatedLines": svAtmPortAssociatedLines,
       "svAtmImaPortMode": svAtmImaPortMode,
       "svAtmImaPortNumRedundantLines": svAtmImaPortNumRedundantLines,
       "svAtmImaPortMaxTolerableDiffDelay": svAtmImaPortMaxTolerableDiffDelay,
       "svAtmPortCACOverride": svAtmPortCACOverride,
       "svAtmPortlcpCellsPeriodicity": svAtmPortlcpCellsPeriodicity,
       "svAtmPortTxAvailCellRate": svAtmPortTxAvailCellRate,
       "svAtmPortSymmetry": svAtmPortSymmetry,
       "svAtmPortMinNumRxLinks": svAtmPortMinNumRxLinks,
       "svAtmPortNeTxClkMode": svAtmPortNeTxClkMode,
       "svAtmPortNumRxCfgLnks": svAtmPortNumRxCfgLnks,
       "svAtmPortTestLinkIfIndex": svAtmPortTestLinkIfIndex,
       "svAtmPortTestPattern": svAtmPortTestPattern,
       "svAtmPortTestProcStatus": svAtmPortTestProcStatus,
       "svAtmPortIntegrationUpTime": svAtmPortIntegrationUpTime,
       "svAtmPortIntegrationDownTime": svAtmPortIntegrationDownTime,
       "svAtmPortMinNumTxLinks": svAtmPortMinNumTxLinks,
       "svAtmPortnumLinksPresentInImaGroup": svAtmPortnumLinksPresentInImaGroup,
       "svAtmPortimaArbitrationWinner": svAtmPortimaArbitrationWinner,
       "svAtmPortremoteImaId": svAtmPortremoteImaId,
       "svAtmPortlocImaId": svAtmPortlocImaId,
       "svAtmPortimaObsDiffDelay": svAtmPortimaObsDiffDelay,
       "svAtmPortOversubscribed": svAtmPortOversubscribed,
       "svAtmPortRxAvailCellRate": svAtmPortRxAvailCellRate,
       "svAtmPortFeState": svAtmPortFeState,
       "svAtmPortFailureStatus": svAtmPortFailureStatus,
       "svAtmPortFeTxClkMode": svAtmPortFeTxClkMode,
       "svAtmPortTxTimingRefLink": svAtmPortTxTimingRefLink,
       "svAtmPortRxTimingRefLink": svAtmPortRxTimingRefLink,
       "svAtmPortRxFrameLength": svAtmPortRxFrameLength,
       "svAtmPortLeastDelayLink": svAtmPortLeastDelayLink,
       "svAtmPortNumRxActLnks": svAtmPortNumRxActLnks,
       "svAtmPortNeState": svAtmPortNeState,
       "psaErrorLastIndex": psaErrorLastIndex,
       "psaErrorFlushAll": psaErrorFlushAll,
       "psaErrorTable": psaErrorTable,
       "psaErrorEntry": psaErrorEntry,
       "psaErrorReqId": psaErrorReqId,
       "psaErrorDesc": psaErrorDesc,
       "psaErrorEcode": psaErrorEcode,
       "psaErrorLastDesc": psaErrorLastDesc,
       "psaErrorLastEcode": psaErrorLastEcode,
       "svPortAlarmTable": svPortAlarmTable,
       "svPortAlarmEntry": svPortAlarmEntry,
       "svPortAlarmNode": svPortAlarmNode,
       "svPortAlarmShelf": svPortAlarmShelf,
       "svPortAlarmSlot": svPortAlarmSlot,
       "svPortAlarmLine": svPortAlarmLine,
       "svPortAlarmPort": svPortAlarmPort,
       "svPortAlarmPortType": svPortAlarmPortType,
       "svFrasmProtocolGroupTable": svFrasmProtocolGroupTable,
       "svFrasmProtocolGroupEntry": svFrasmProtocolGroupEntry,
       "svFrasmProtocolGroupNode": svFrasmProtocolGroupNode,
       "svFrasmProtocolGroupShelf": svFrasmProtocolGroupShelf,
       "svFrasmProtocolGroupSlot": svFrasmProtocolGroupSlot,
       "svFrasmProtocolGroupType": svFrasmProtocolGroupType,
       "svFrasmProtocolGroupNumber": svFrasmProtocolGroupNumber,
       "svFrasmProtocolGroupRowStatus": svFrasmProtocolGroupRowStatus,
       "svFrasmProtocolGroupConfigType": svFrasmProtocolGroupConfigType,
       "svFrasmProtocolGroupLocalAck": svFrasmProtocolGroupLocalAck,
       "svFrasmProtocolGroupOperStatus": svFrasmProtocolGroupOperStatus,
       "svSdlcLinkStationTable": svSdlcLinkStationTable,
       "svSdlcLinkStationEntry": svSdlcLinkStationEntry,
       "svSdlcLinkStationNode": svSdlcLinkStationNode,
       "svSdlcLinkStationShelf": svSdlcLinkStationShelf,
       "svSdlcLinkStationSlot": svSdlcLinkStationSlot,
       "svSdlcLinkStationLine": svSdlcLinkStationLine,
       "svSdlcLinkStationPort": svSdlcLinkStationPort,
       "svSdlcLinkStationAddress": svSdlcLinkStationAddress,
       "svSdlcLinkStationRowStatus": svSdlcLinkStationRowStatus,
       "svSdlcLinkStationXID": svSdlcLinkStationXID,
       "svSdlcLinkStationMaxFrame": svSdlcLinkStationMaxFrame,
       "svSdlcLinkStationOperStatus": svSdlcLinkStationOperStatus,
       "svChannelRouteTable": svChannelRouteTable,
       "svChannelRouteEntry": svChannelRouteEntry,
       "svChannelRouteNode": svChannelRouteNode,
       "svChannelRouteShelf": svChannelRouteShelf,
       "svChannelRouteSlot": svChannelRouteSlot,
       "svChannelRouteLine": svChannelRouteLine,
       "svChannelRoutePort": svChannelRoutePort,
       "svChannelRouteStationAddress": svChannelRouteStationAddress,
       "svChannelRouteRowStatus": svChannelRouteRowStatus,
       "svChannelRouteDlci": svChannelRouteDlci,
       "svChannelRouteOperStatus": svChannelRouteOperStatus,
       "svChannelRouteLSAP": svChannelRouteLSAP,
       "svChannelRouteRSAP": svChannelRouteRSAP,
       "svChannelRouteTHType": svChannelRouteTHType,
       "svChannelRouteChannelType": svChannelRouteChannelType,
       "svLlcChannelParamTable": svLlcChannelParamTable,
       "svLlcChannelParamEntry": svLlcChannelParamEntry,
       "svLlcChannelParamNode": svLlcChannelParamNode,
       "svLlcChannelParamShelf": svLlcChannelParamShelf,
       "svLlcChannelParamSlot": svLlcChannelParamSlot,
       "svLlcChannelParamLine": svLlcChannelParamLine,
       "svLlcChannelParamPort": svLlcChannelParamPort,
       "svLlcChannelParamDlci": svLlcChannelParamDlci,
       "svLlcChannelParamRowStatus": svLlcChannelParamRowStatus,
       "svLlcChannelParamRetryCnt": svLlcChannelParamRetryCnt,
       "svLlcChannelParamAckWaitTime": svLlcChannelParamAckWaitTime,
       "svCesmPortTable": svCesmPortTable,
       "svCesmPortEntry": svCesmPortEntry,
       "svCesmPortNode": svCesmPortNode,
       "svCesmPortShelf": svCesmPortShelf,
       "svCesmPortSlot": svCesmPortSlot,
       "svCesmPortLine": svCesmPortLine,
       "svCesmPortPort": svCesmPortPort,
       "svCesmPortRowStatus": svCesmPortRowStatus,
       "svCesmPortOperState": svCesmPortOperState,
       "svCesmPortAdminState": svCesmPortAdminState,
       "svCesmPortCardType": svCesmPortCardType,
       "svCesmPortIfType": svCesmPortIfType,
       "svCesmPortSpeed": svCesmPortSpeed,
       "svCesmPortVcCount": svCesmPortVcCount,
       "svCesmPortVcPtr": svCesmPortVcPtr,
       "svCesmPortType": svCesmPortType,
       "svCesmPortChCnt": svCesmPortChCnt,
       "insDas": insDas,
       "dasAniTable": dasAniTable,
       "dasAniEntry": dasAniEntry,
       "dasAniAni": dasAniAni,
       "dasAniRowStatus": dasAniRowStatus,
       "dasAniAniType": dasAniAniType,
       "dasAniMaxTxQDepth": dasAniMaxTxQDepth,
       "dasAniECNQThresh": dasAniECNQThresh,
       "dasAniDEThresh": dasAniDEThresh,
       "dasAniCLLMTimer": dasAniCLLMTimer,
       "dasAniIDEMap": dasAniIDEMap,
       "dasAniFrmFlags": dasAniFrmFlags,
       "dasAniSigProto": dasAniSigProto,
       "dasAniPortIf": dasAniPortIf,
       "dasAniAsyncStatus": dasAniAsyncStatus,
       "dasAniPollVerTimer": dasAniPollVerTimer,
       "dasAniErrThresh": dasAniErrThresh,
       "dasAniMonEveCnt": dasAniMonEveCnt,
       "dasAniOamThresh": dasAniOamThresh,
       "dasAniCommPri": dasAniCommPri,
       "dasAniUpRNR": dasAniUpRNR,
       "dasAniLowRNR": dasAniLowRNR,
       "dasConnTable": dasConnTable,
       "dasConnEntry": dasConnEntry,
       "dasConnAni": dasConnAni,
       "dasConnOrgDlci": dasConnOrgDlci,
       "dasConnRowStatus": dasConnRowStatus,
       "dasConnAniType": dasConnAniType,
       "dasConnConnType": dasConnConnType,
       "dasConnTrmEndpt": dasConnTrmEndpt,
       "dasConnAsscEndpt": dasConnAsscEndpt,
       "dasConnForesight": dasConnForesight,
       "dasConnCos": dasConnCos,
       "dasConnTrkAvoid": dasConnTrkAvoid,
       "dasConnZcs": dasConnZcs,
       "dasConnOrgCir": dasConnOrgCir,
       "dasConnOrgMir": dasConnOrgMir,
       "dasConnOrgPir": dasConnOrgPir,
       "dasConnOrgQir": dasConnOrgQir,
       "dasConnOrgBc": dasConnOrgBc,
       "dasConnOrgBe": dasConnOrgBe,
       "dasConnOrgPerUtil": dasConnOrgPerUtil,
       "dasConnOrgIbs": dasConnOrgIbs,
       "dasConnOrgCmax": dasConnOrgCmax,
       "dasConnOrgVcQDepth": dasConnOrgVcQDepth,
       "dasConnOrgEgrVcQDepth": dasConnOrgEgrVcQDepth,
       "dasConnOrgEcnThresh": dasConnOrgEcnThresh,
       "dasConnOrgEgrEcnThresh": dasConnOrgEgrEcnThresh,
       "dasConnOrgIngDeThresh": dasConnOrgIngDeThresh,
       "dasConnOrgEgrDeThresh": dasConnOrgEgrDeThresh,
       "dasConnOrgEgrQSelect": dasConnOrgEgrQSelect,
       "dasConnOrgIgrDeTag": dasConnOrgIgrDeTag,
       "dasConnTrmCir": dasConnTrmCir,
       "dasConnTrmMir": dasConnTrmMir,
       "dasConnTrmPir": dasConnTrmPir,
       "dasConnTrmQir": dasConnTrmQir,
       "dasConnTrmBc": dasConnTrmBc,
       "dasConnTrmBe": dasConnTrmBe,
       "dasConnTrmPerUtil": dasConnTrmPerUtil,
       "dasConnTrmIbs": dasConnTrmIbs,
       "dasConnTrmCmax": dasConnTrmCmax,
       "dasConnTrmVcQDepth": dasConnTrmVcQDepth,
       "dasConnTrmEgrVcQDepth": dasConnTrmEgrVcQDepth,
       "dasConnTrmEcnThresh": dasConnTrmEcnThresh,
       "dasConnTrmEgrEcnThresh": dasConnTrmEgrEcnThresh,
       "dasConnTrmIngDeThresh": dasConnTrmIngDeThresh,
       "dasConnTrmEgrDeThresh": dasConnTrmEgrDeThresh,
       "dasConnTrmEgrQSelect": dasConnTrmEgrQSelect,
       "dasConnTrmIgrDeTag": dasConnTrmIgrDeTag,
       "dasConnOrgPriority": dasConnOrgPriority,
       "dasConnTrmPriority": dasConnTrmPriority,
       "dasErrorTable": dasErrorTable,
       "dasErrorEntry": dasErrorEntry,
       "dasErrorReqId": dasErrorReqId,
       "dasErrorDesc": dasErrorDesc,
       "dasErrorEcode": dasErrorEcode,
       "dasErrorLastIndex": dasErrorLastIndex,
       "dasErrorFlushAll": dasErrorFlushAll,
       "dasErrorLastDesc": dasErrorLastDesc,
       "dasErrorLastEcode": dasErrorLastEcode}
)
