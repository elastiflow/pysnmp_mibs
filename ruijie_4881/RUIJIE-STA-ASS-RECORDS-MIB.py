# SNMP MIB module (RUIJIE-STA-ASS-RECORDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-STA-ASS-RECORDS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:11 2025
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

(ruijieIfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-INTERFACE-MIB",
    "ruijieIfIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieStaAssRecordsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101)
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieStaAssRecordsMIBTrap_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsMIBTrap = _RuijieStaAssRecordsMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 0)
)
_RuijieStaAssRecordsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsMIBObjects = _RuijieStaAssRecordsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1)
)
_RuijieStaAssRecordsGrobal_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsGrobal = _RuijieStaAssRecordsGrobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1)
)
_RuijieStaAssRecordsGrobalTable_Object = MibTable
ruijieStaAssRecordsGrobalTable = _RuijieStaAssRecordsGrobalTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsGrobalTable.setStatus("current")
_RuijieStaAssRecordsGrobalEntry_Object = MibTableRow
ruijieStaAssRecordsGrobalEntry = _RuijieStaAssRecordsGrobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1)
)
ruijieStaAssRecordsGrobalEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalAddress"),
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsGrobalEntry.setStatus("current")
_RuijieStaMacGrobalAddress_Type = MacAddress
_RuijieStaMacGrobalAddress_Object = MibTableColumn
ruijieStaMacGrobalAddress = _RuijieStaMacGrobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 1),
    _RuijieStaMacGrobalAddress_Type()
)
ruijieStaMacGrobalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalAddress.setStatus("current")


class _RuijieStaMacGrobalAPName_Type(DisplayString):
    """Custom type ruijieStaMacGrobalAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaMacGrobalAPName_Type.__name__ = "DisplayString"
_RuijieStaMacGrobalAPName_Object = MibTableColumn
ruijieStaMacGrobalAPName = _RuijieStaMacGrobalAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 2),
    _RuijieStaMacGrobalAPName_Type()
)
ruijieStaMacGrobalAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalAPName.setStatus("current")


class _RuijieStaMacGrobalISUP_Type(Integer32):
    """Custom type ruijieStaMacGrobalISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_RuijieStaMacGrobalISUP_Type.__name__ = "Integer32"
_RuijieStaMacGrobalISUP_Object = MibTableColumn
ruijieStaMacGrobalISUP = _RuijieStaMacGrobalISUP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 3),
    _RuijieStaMacGrobalISUP_Type()
)
ruijieStaMacGrobalISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalISUP.setStatus("current")
_RuijieStaMacGrobalStartime_Type = DateAndTime
_RuijieStaMacGrobalStartime_Object = MibTableColumn
ruijieStaMacGrobalStartime = _RuijieStaMacGrobalStartime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 4),
    _RuijieStaMacGrobalStartime_Type()
)
ruijieStaMacGrobalStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalStartime.setStatus("current")
_RuijieStaMacGrobalupdowntimes_Type = Unsigned32
_RuijieStaMacGrobalupdowntimes_Object = MibTableColumn
ruijieStaMacGrobalupdowntimes = _RuijieStaMacGrobalupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 5),
    _RuijieStaMacGrobalupdowntimes_Type()
)
ruijieStaMacGrobalupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalupdowntimes.setStatus("current")
_RuijieStaMacGrobalroamtimes_Type = Unsigned32
_RuijieStaMacGrobalroamtimes_Object = MibTableColumn
ruijieStaMacGrobalroamtimes = _RuijieStaMacGrobalroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 6),
    _RuijieStaMacGrobalroamtimes_Type()
)
ruijieStaMacGrobalroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalroamtimes.setStatus("current")
_RuijieStaMacGrobaltotaltimes_Type = Unsigned32
_RuijieStaMacGrobaltotaltimes_Object = MibTableColumn
ruijieStaMacGrobaltotaltimes = _RuijieStaMacGrobaltotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 7),
    _RuijieStaMacGrobaltotaltimes_Type()
)
ruijieStaMacGrobaltotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobaltotaltimes.setStatus("current")
_RuijieStaMacGrobalrealdowntimes_Type = Unsigned32
_RuijieStaMacGrobalrealdowntimes_Object = MibTableColumn
ruijieStaMacGrobalrealdowntimes = _RuijieStaMacGrobalrealdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 8),
    _RuijieStaMacGrobalrealdowntimes_Type()
)
ruijieStaMacGrobalrealdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalrealdowntimes.setStatus("current")


class _RuijieStaMacGrobalSSID_Type(DisplayString):
    """Custom type ruijieStaMacGrobalSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaMacGrobalSSID_Type.__name__ = "DisplayString"
_RuijieStaMacGrobalSSID_Object = MibTableColumn
ruijieStaMacGrobalSSID = _RuijieStaMacGrobalSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 1, 1, 1, 9),
    _RuijieStaMacGrobalSSID_Type()
)
ruijieStaMacGrobalSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacGrobalSSID.setStatus("current")
_RuijieStaAssRecordsByMAC_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsByMAC = _RuijieStaAssRecordsByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2)
)
_RuijieStaAssRecordsByMACTable_Object = MibTable
ruijieStaAssRecordsByMACTable = _RuijieStaAssRecordsByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsByMACTable.setStatus("current")
_RuijieStaAssRecordsByMACEntry_Object = MibTableRow
ruijieStaAssRecordsByMACEntry = _RuijieStaAssRecordsByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1)
)
ruijieStaAssRecordsByMACEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacAddress"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacindex"),
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsByMACEntry.setStatus("current")
_RuijieStaMacAddress_Type = MacAddress
_RuijieStaMacAddress_Object = MibTableColumn
ruijieStaMacAddress = _RuijieStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 1),
    _RuijieStaMacAddress_Type()
)
ruijieStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaMacAddress.setStatus("current")
_RuijieStaMacindex_Type = Unsigned32
_RuijieStaMacindex_Object = MibTableColumn
ruijieStaMacindex = _RuijieStaMacindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 2),
    _RuijieStaMacindex_Type()
)
ruijieStaMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaMacindex.setStatus("current")
_RuijieStaAsstime_Type = DateAndTime
_RuijieStaAsstime_Object = MibTableColumn
ruijieStaAsstime = _RuijieStaAsstime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 3),
    _RuijieStaAsstime_Type()
)
ruijieStaAsstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAsstime.setStatus("current")


class _RuijieStaAssAction_Type(Integer32):
    """Custom type ruijieStaAssAction based on Integer32"""
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
        *(("join", 1),
          ("leave", 2),
          ("roam", 3),
          ("delete", 4))
    )


_RuijieStaAssAction_Type.__name__ = "Integer32"
_RuijieStaAssAction_Object = MibTableColumn
ruijieStaAssAction = _RuijieStaAssAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 4),
    _RuijieStaAssAction_Type()
)
ruijieStaAssAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssAction.setStatus("current")
_RuijieStaAssSubAction_Type = Integer32
_RuijieStaAssSubAction_Object = MibTableColumn
ruijieStaAssSubAction = _RuijieStaAssSubAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 5),
    _RuijieStaAssSubAction_Type()
)
ruijieStaAssSubAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssSubAction.setStatus("current")


class _RuijieStaAssResult_Type(Integer32):
    """Custom type ruijieStaAssResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1))
    )


_RuijieStaAssResult_Type.__name__ = "Integer32"
_RuijieStaAssResult_Object = MibTableColumn
ruijieStaAssResult = _RuijieStaAssResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 6),
    _RuijieStaAssResult_Type()
)
ruijieStaAssResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssResult.setStatus("current")
_RuijieStaAssReason_Type = Integer32
_RuijieStaAssReason_Object = MibTableColumn
ruijieStaAssReason = _RuijieStaAssReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 7),
    _RuijieStaAssReason_Type()
)
ruijieStaAssReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssReason.setStatus("current")


class _RuijieStaAssApNamePre_Type(DisplayString):
    """Custom type ruijieStaAssApNamePre based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaAssApNamePre_Type.__name__ = "DisplayString"
_RuijieStaAssApNamePre_Object = MibTableColumn
ruijieStaAssApNamePre = _RuijieStaAssApNamePre_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 8),
    _RuijieStaAssApNamePre_Type()
)
ruijieStaAssApNamePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssApNamePre.setStatus("current")


class _RuijieStaAssApNameNow_Type(DisplayString):
    """Custom type ruijieStaAssApNameNow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaAssApNameNow_Type.__name__ = "DisplayString"
_RuijieStaAssApNameNow_Object = MibTableColumn
ruijieStaAssApNameNow = _RuijieStaAssApNameNow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 9),
    _RuijieStaAssApNameNow_Type()
)
ruijieStaAssApNameNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssApNameNow.setStatus("current")
_RuijieStaAssSignalQua_Type = Integer32
_RuijieStaAssSignalQua_Object = MibTableColumn
ruijieStaAssSignalQua = _RuijieStaAssSignalQua_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 10),
    _RuijieStaAssSignalQua_Type()
)
ruijieStaAssSignalQua.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssSignalQua.setStatus("current")
_RuijieStaAssRoamtype_Type = Integer32
_RuijieStaAssRoamtype_Object = MibTableColumn
ruijieStaAssRoamtype = _RuijieStaAssRoamtype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 11),
    _RuijieStaAssRoamtype_Type()
)
ruijieStaAssRoamtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssRoamtype.setStatus("current")
_RuijieStaAssjitter_Type = Integer32
_RuijieStaAssjitter_Object = MibTableColumn
ruijieStaAssjitter = _RuijieStaAssjitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 12),
    _RuijieStaAssjitter_Type()
)
ruijieStaAssjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssjitter.setStatus("current")
_RuijieStaAssjointimes_Type = Unsigned32
_RuijieStaAssjointimes_Object = MibTableColumn
ruijieStaAssjointimes = _RuijieStaAssjointimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 13),
    _RuijieStaAssjointimes_Type()
)
ruijieStaAssjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssjointimes.setStatus("current")
_RuijieStaAsslatelytime_Type = DateAndTime
_RuijieStaAsslatelytime_Object = MibTableColumn
ruijieStaAsslatelytime = _RuijieStaAsslatelytime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 14),
    _RuijieStaAsslatelytime_Type()
)
ruijieStaAsslatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAsslatelytime.setStatus("current")
_RuijieStaAssSSID_Type = DisplayString
_RuijieStaAssSSID_Object = MibTableColumn
ruijieStaAssSSID = _RuijieStaAssSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 2, 1, 1, 15),
    _RuijieStaAssSSID_Type()
)
ruijieStaAssSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssSSID.setStatus("current")
_RuijieStaAssRecordsByTime_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsByTime = _RuijieStaAssRecordsByTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3)
)
_RuijieStaAssRecordsSearchByTimeTable_Object = MibTable
ruijieStaAssRecordsSearchByTimeTable = _RuijieStaAssRecordsSearchByTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByTimeTable.setStatus("current")
_RuijieStaAssRecordsSearchByTimeEntry_Object = MibTableRow
ruijieStaAssRecordsSearchByTimeEntry = _RuijieStaAssRecordsSearchByTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1)
)
ruijieStaAssRecordsSearchByTimeEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaUptimeLow"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaUptimeHigh"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaDowntimeLow"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaDowntimeHigh"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeindex"),
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByTimeEntry.setStatus("current")
_RuijieStaUptimeLow_Type = DateAndTime
_RuijieStaUptimeLow_Object = MibTableColumn
ruijieStaUptimeLow = _RuijieStaUptimeLow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 1),
    _RuijieStaUptimeLow_Type()
)
ruijieStaUptimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaUptimeLow.setStatus("current")
_RuijieStaUptimeHigh_Type = DateAndTime
_RuijieStaUptimeHigh_Object = MibTableColumn
ruijieStaUptimeHigh = _RuijieStaUptimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 2),
    _RuijieStaUptimeHigh_Type()
)
ruijieStaUptimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaUptimeHigh.setStatus("current")
_RuijieStaDowntimeLow_Type = DateAndTime
_RuijieStaDowntimeLow_Object = MibTableColumn
ruijieStaDowntimeLow = _RuijieStaDowntimeLow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 3),
    _RuijieStaDowntimeLow_Type()
)
ruijieStaDowntimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaDowntimeLow.setStatus("current")
_RuijieStaDowntimeHigh_Type = DateAndTime
_RuijieStaDowntimeHigh_Object = MibTableColumn
ruijieStaDowntimeHigh = _RuijieStaDowntimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 4),
    _RuijieStaDowntimeHigh_Type()
)
ruijieStaDowntimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaDowntimeHigh.setStatus("current")
_RuijieStaTimeindex_Type = Unsigned32
_RuijieStaTimeindex_Object = MibTableColumn
ruijieStaTimeindex = _RuijieStaTimeindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 5),
    _RuijieStaTimeindex_Type()
)
ruijieStaTimeindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaTimeindex.setStatus("current")
_RuijieStaTimeMac_Type = MacAddress
_RuijieStaTimeMac_Object = MibTableColumn
ruijieStaTimeMac = _RuijieStaTimeMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 6),
    _RuijieStaTimeMac_Type()
)
ruijieStaTimeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeMac.setStatus("current")


class _RuijieStaTimeAPName_Type(DisplayString):
    """Custom type ruijieStaTimeAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaTimeAPName_Type.__name__ = "DisplayString"
_RuijieStaTimeAPName_Object = MibTableColumn
ruijieStaTimeAPName = _RuijieStaTimeAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 7),
    _RuijieStaTimeAPName_Type()
)
ruijieStaTimeAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeAPName.setStatus("current")


class _RuijieStaTimeISUP_Type(Integer32):
    """Custom type ruijieStaTimeISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_RuijieStaTimeISUP_Type.__name__ = "Integer32"
_RuijieStaTimeISUP_Object = MibTableColumn
ruijieStaTimeISUP = _RuijieStaTimeISUP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 8),
    _RuijieStaTimeISUP_Type()
)
ruijieStaTimeISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeISUP.setStatus("current")
_RuijieStaTimeStartime_Type = DateAndTime
_RuijieStaTimeStartime_Object = MibTableColumn
ruijieStaTimeStartime = _RuijieStaTimeStartime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 9),
    _RuijieStaTimeStartime_Type()
)
ruijieStaTimeStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeStartime.setStatus("current")
_RuijieStaTimeupdowntimes_Type = Unsigned32
_RuijieStaTimeupdowntimes_Object = MibTableColumn
ruijieStaTimeupdowntimes = _RuijieStaTimeupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 10),
    _RuijieStaTimeupdowntimes_Type()
)
ruijieStaTimeupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeupdowntimes.setStatus("current")
_RuijieStaTimeroamtimes_Type = Unsigned32
_RuijieStaTimeroamtimes_Object = MibTableColumn
ruijieStaTimeroamtimes = _RuijieStaTimeroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 11),
    _RuijieStaTimeroamtimes_Type()
)
ruijieStaTimeroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimeroamtimes.setStatus("current")
_RuijieStaTimertotaltimes_Type = Unsigned32
_RuijieStaTimertotaltimes_Object = MibTableColumn
ruijieStaTimertotaltimes = _RuijieStaTimertotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 12),
    _RuijieStaTimertotaltimes_Type()
)
ruijieStaTimertotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimertotaltimes.setStatus("current")
_RuijieStaTimerjitter_Type = Integer32
_RuijieStaTimerjitter_Object = MibTableColumn
ruijieStaTimerjitter = _RuijieStaTimerjitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 13),
    _RuijieStaTimerjitter_Type()
)
ruijieStaTimerjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimerjitter.setStatus("current")
_RuijieStaTimerjointimes_Type = Unsigned32
_RuijieStaTimerjointimes_Object = MibTableColumn
ruijieStaTimerjointimes = _RuijieStaTimerjointimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 14),
    _RuijieStaTimerjointimes_Type()
)
ruijieStaTimerjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimerjointimes.setStatus("current")
_RuijieStaTimerlatelytime_Type = DateAndTime
_RuijieStaTimerlatelytime_Object = MibTableColumn
ruijieStaTimerlatelytime = _RuijieStaTimerlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 15),
    _RuijieStaTimerlatelytime_Type()
)
ruijieStaTimerlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimerlatelytime.setStatus("current")
_RuijieStaTimerSSID_Type = DisplayString
_RuijieStaTimerSSID_Object = MibTableColumn
ruijieStaTimerSSID = _RuijieStaTimerSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 3, 1, 1, 16),
    _RuijieStaTimerSSID_Type()
)
ruijieStaTimerSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTimerSSID.setStatus("current")
_RuijieStaAssRecordsByAP_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsByAP = _RuijieStaAssRecordsByAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4)
)
_RuijieStaAssRecordsSearchByAPTable_Object = MibTable
ruijieStaAssRecordsSearchByAPTable = _RuijieStaAssRecordsSearchByAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByAPTable.setStatus("current")
_RuijieStaAssRecordsSearchByAPEntry_Object = MibTableRow
ruijieStaAssRecordsSearchByAPEntry = _RuijieStaAssRecordsSearchByAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1)
)
ruijieStaAssRecordsSearchByAPEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPAPName"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPindex"),
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByAPEntry.setStatus("current")


class _RuijieStaAPAPName_Type(DisplayString):
    """Custom type ruijieStaAPAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieStaAPAPName_Type.__name__ = "DisplayString"
_RuijieStaAPAPName_Object = MibTableColumn
ruijieStaAPAPName = _RuijieStaAPAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 1),
    _RuijieStaAPAPName_Type()
)
ruijieStaAPAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaAPAPName.setStatus("current")
_RuijieStaAPindex_Type = Unsigned32
_RuijieStaAPindex_Object = MibTableColumn
ruijieStaAPindex = _RuijieStaAPindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 2),
    _RuijieStaAPindex_Type()
)
ruijieStaAPindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaAPindex.setStatus("current")
_RuijieStaAPMac_Type = MacAddress
_RuijieStaAPMac_Object = MibTableColumn
ruijieStaAPMac = _RuijieStaAPMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 3),
    _RuijieStaAPMac_Type()
)
ruijieStaAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPMac.setStatus("current")


class _RuijieStaAPISUP_Type(Integer32):
    """Custom type ruijieStaAPISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_RuijieStaAPISUP_Type.__name__ = "Integer32"
_RuijieStaAPISUP_Object = MibTableColumn
ruijieStaAPISUP = _RuijieStaAPISUP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 4),
    _RuijieStaAPISUP_Type()
)
ruijieStaAPISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPISUP.setStatus("current")
_RuijieStaAPStartime_Type = DateAndTime
_RuijieStaAPStartime_Object = MibTableColumn
ruijieStaAPStartime = _RuijieStaAPStartime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 5),
    _RuijieStaAPStartime_Type()
)
ruijieStaAPStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPStartime.setStatus("current")
_RuijieStaAPupdowntimes_Type = Unsigned32
_RuijieStaAPupdowntimes_Object = MibTableColumn
ruijieStaAPupdowntimes = _RuijieStaAPupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 6),
    _RuijieStaAPupdowntimes_Type()
)
ruijieStaAPupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPupdowntimes.setStatus("current")
_RuijieStaAProamtimes_Type = Unsigned32
_RuijieStaAProamtimes_Object = MibTableColumn
ruijieStaAProamtimes = _RuijieStaAProamtimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 7),
    _RuijieStaAProamtimes_Type()
)
ruijieStaAProamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAProamtimes.setStatus("current")
_RuijieStaAPtotaltimes_Type = Unsigned32
_RuijieStaAPtotaltimes_Object = MibTableColumn
ruijieStaAPtotaltimes = _RuijieStaAPtotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 8),
    _RuijieStaAPtotaltimes_Type()
)
ruijieStaAPtotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPtotaltimes.setStatus("current")
_RuijieStaAPjitter_Type = Integer32
_RuijieStaAPjitter_Object = MibTableColumn
ruijieStaAPjitter = _RuijieStaAPjitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 9),
    _RuijieStaAPjitter_Type()
)
ruijieStaAPjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPjitter.setStatus("current")
_RuijieStaAPjointimes_Type = Unsigned32
_RuijieStaAPjointimes_Object = MibTableColumn
ruijieStaAPjointimes = _RuijieStaAPjointimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 10),
    _RuijieStaAPjointimes_Type()
)
ruijieStaAPjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPjointimes.setStatus("current")
_RuijieStaAPlatelytime_Type = DateAndTime
_RuijieStaAPlatelytime_Object = MibTableColumn
ruijieStaAPlatelytime = _RuijieStaAPlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 11),
    _RuijieStaAPlatelytime_Type()
)
ruijieStaAPlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPlatelytime.setStatus("current")
_RuijieStaAPSSID_Type = DisplayString
_RuijieStaAPSSID_Object = MibTableColumn
ruijieStaAPSSID = _RuijieStaAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 4, 1, 1, 12),
    _RuijieStaAPSSID_Type()
)
ruijieStaAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAPSSID.setStatus("current")
_RuijieStaAssSignalByMAC_ObjectIdentity = ObjectIdentity
ruijieStaAssSignalByMAC = _RuijieStaAssSignalByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5)
)
_RuijieStaAssSignalByMACTable_Object = MibTable
ruijieStaAssSignalByMACTable = _RuijieStaAssSignalByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssSignalByMACTable.setStatus("current")
_RuijieStaAssSignalByMACEntry_Object = MibTableRow
ruijieStaAssSignalByMACEntry = _RuijieStaAssSignalByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1, 1)
)
ruijieStaAssSignalByMACEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaSignalMacAddress"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaSignalMacindex"),
)
if mibBuilder.loadTexts:
    ruijieStaAssSignalByMACEntry.setStatus("current")
_RuijieStaSignalMacAddress_Type = MacAddress
_RuijieStaSignalMacAddress_Object = MibTableColumn
ruijieStaSignalMacAddress = _RuijieStaSignalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1, 1, 1),
    _RuijieStaSignalMacAddress_Type()
)
ruijieStaSignalMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaSignalMacAddress.setStatus("current")
_RuijieStaSignalMacindex_Type = Unsigned32
_RuijieStaSignalMacindex_Object = MibTableColumn
ruijieStaSignalMacindex = _RuijieStaSignalMacindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1, 1, 2),
    _RuijieStaSignalMacindex_Type()
)
ruijieStaSignalMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaSignalMacindex.setStatus("current")
_RuijieStaSignaltime_Type = DateAndTime
_RuijieStaSignaltime_Object = MibTableColumn
ruijieStaSignaltime = _RuijieStaSignaltime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1, 1, 3),
    _RuijieStaSignaltime_Type()
)
ruijieStaSignaltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaSignaltime.setStatus("current")
_RuijieStaSignalValue_Type = Integer32
_RuijieStaSignalValue_Object = MibTableColumn
ruijieStaSignalValue = _RuijieStaSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 5, 1, 1, 4),
    _RuijieStaSignalValue_Type()
)
ruijieStaSignalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaSignalValue.setStatus("current")
_RuijieStaAssRetryByMAC_ObjectIdentity = ObjectIdentity
ruijieStaAssRetryByMAC = _RuijieStaAssRetryByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6)
)
_RuijieStaAssRetryByMACTable_Object = MibTable
ruijieStaAssRetryByMACTable = _RuijieStaAssRetryByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ruijieStaAssRetryByMACTable.setStatus("current")
_RuijieStaAssRetryByMACEntry_Object = MibTableRow
ruijieStaAssRetryByMACEntry = _RuijieStaAssRetryByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1, 1)
)
ruijieStaAssRetryByMACEntry.setIndexNames(
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaRetryMacAddress"),
    (0, "RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaRetryMacindex"),
)
if mibBuilder.loadTexts:
    ruijieStaAssRetryByMACEntry.setStatus("current")
_RuijieStaRetryMacAddress_Type = MacAddress
_RuijieStaRetryMacAddress_Object = MibTableColumn
ruijieStaRetryMacAddress = _RuijieStaRetryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1, 1, 1),
    _RuijieStaRetryMacAddress_Type()
)
ruijieStaRetryMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaRetryMacAddress.setStatus("current")
_RuijieStaRetryMacindex_Type = Unsigned32
_RuijieStaRetryMacindex_Object = MibTableColumn
ruijieStaRetryMacindex = _RuijieStaRetryMacindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1, 1, 2),
    _RuijieStaRetryMacindex_Type()
)
ruijieStaRetryMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieStaRetryMacindex.setStatus("current")
_RuijieStaRetrytime_Type = DateAndTime
_RuijieStaRetrytime_Object = MibTableColumn
ruijieStaRetrytime = _RuijieStaRetrytime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1, 1, 3),
    _RuijieStaRetrytime_Type()
)
ruijieStaRetrytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaRetrytime.setStatus("current")
_RuijieStaRetryValue_Type = Integer32
_RuijieStaRetryValue_Object = MibTableColumn
ruijieStaRetryValue = _RuijieStaRetryValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 6, 1, 1, 4),
    _RuijieStaRetryValue_Type()
)
ruijieStaRetryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaRetryValue.setStatus("current")
_RuijieStaAssStatistic_ObjectIdentity = ObjectIdentity
ruijieStaAssStatistic = _RuijieStaAssStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7)
)
_RuijieAssStatisticsTotalsta_Type = Unsigned32
_RuijieAssStatisticsTotalsta_Object = MibScalar
ruijieAssStatisticsTotalsta = _RuijieAssStatisticsTotalsta_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 1),
    _RuijieAssStatisticsTotalsta_Type()
)
ruijieAssStatisticsTotalsta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsTotalsta.setStatus("current")
_RuijieAssStatisticsTotalinfo_Type = Unsigned32
_RuijieAssStatisticsTotalinfo_Object = MibScalar
ruijieAssStatisticsTotalinfo = _RuijieAssStatisticsTotalinfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 2),
    _RuijieAssStatisticsTotalinfo_Type()
)
ruijieAssStatisticsTotalinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsTotalinfo.setStatus("current")
_RuijieAssStatisticsdown_Type = Unsigned32
_RuijieAssStatisticsdown_Object = MibScalar
ruijieAssStatisticsdown = _RuijieAssStatisticsdown_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 3),
    _RuijieAssStatisticsdown_Type()
)
ruijieAssStatisticsdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsdown.setStatus("current")
_RuijieAssStatisticsObligate1_Type = Unsigned32
_RuijieAssStatisticsObligate1_Object = MibScalar
ruijieAssStatisticsObligate1 = _RuijieAssStatisticsObligate1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 4),
    _RuijieAssStatisticsObligate1_Type()
)
ruijieAssStatisticsObligate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsObligate1.setStatus("current")
_RuijieAssStatisticsObligate2_Type = Unsigned32
_RuijieAssStatisticsObligate2_Object = MibScalar
ruijieAssStatisticsObligate2 = _RuijieAssStatisticsObligate2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 5),
    _RuijieAssStatisticsObligate2_Type()
)
ruijieAssStatisticsObligate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsObligate2.setStatus("current")
_RuijieAssStatisticsObligate3_Type = Unsigned32
_RuijieAssStatisticsObligate3_Object = MibScalar
ruijieAssStatisticsObligate3 = _RuijieAssStatisticsObligate3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 1, 7, 6),
    _RuijieAssStatisticsObligate3_Type()
)
ruijieAssStatisticsObligate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAssStatisticsObligate3.setStatus("current")
_RuijieStaAssRecordsMIBConformance_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsMIBConformance = _RuijieStaAssRecordsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2)
)
_RuijieStaAssRecordsMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsMIBCompliances = _RuijieStaAssRecordsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 1)
)
_RuijieStaAssRecordsMIBGroups_ObjectIdentity = ObjectIdentity
ruijieStaAssRecordsMIBGroups = _RuijieStaAssRecordsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2)
)

# Managed Objects groups

ruijieStaAssRecordsGrobalMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 1)
)
ruijieStaAssRecordsGrobalMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalAPName"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalISUP"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalStartime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalupdowntimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalroamtimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobaltotaltimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalrealdowntimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaMacGrobalSSID"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsGrobalMIBroup.setStatus("current")

ruijieStaAssRecordsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 2)
)
ruijieStaAssRecordsMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAsstime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssAction"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssSubAction"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssResult"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssReason"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssApNamePre"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssApNameNow"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssSignalQua"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRoamtype"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssjitter"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssjointimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAsslatelytime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssSSID"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsMIBroup.setStatus("current")

ruijieStaAssRecordsSearchByTimeMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 3)
)
ruijieStaAssRecordsSearchByTimeMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeMac"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeAPName"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeISUP"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeStartime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeupdowntimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimeroamtimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimertotaltimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimerjitter"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimerjointimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimerlatelytime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaTimerSSID"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByTimeMIBroup.setStatus("current")

ruijieStaAssRecordsSearchByAPMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 4)
)
ruijieStaAssRecordsSearchByAPMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPMac"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPISUP"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPStartime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPupdowntimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAProamtimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPtotaltimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPjitter"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPjointimes"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPlatelytime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAPSSID"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsSearchByAPMIBroup.setStatus("current")

ruijieStaAssSignalSearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 5)
)
ruijieStaAssSignalSearchByMACMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaSignaltime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaSignalValue"))
)
if mibBuilder.loadTexts:
    ruijieStaAssSignalSearchByMACMIBroup.setStatus("current")

ruijieStaAssRetrySearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 6)
)
ruijieStaAssRetrySearchByMACMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaRetrytime"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaRetryValue"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRetrySearchByMACMIBroup.setStatus("current")

ruijieStaAssStatisticsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 2, 7)
)
ruijieStaAssStatisticsMIBroup.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsTotalsta"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsTotalinfo"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsdown"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsObligate1"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsObligate2"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieAssStatisticsObligate3"))
)
if mibBuilder.loadTexts:
    ruijieStaAssStatisticsMIBroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieStaAssRecordsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 101, 2, 1, 1)
)
ruijieStaAssRecordsMIBCompliance.setObjects(
      *(("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRecordsGrobalMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRecordsMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRecordsSearchByTimeMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRecordsSearchByAPMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssSignalSearchByMACMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssRetrySearchByMACMIBroup"),
        ("RUIJIE-STA-ASS-RECORDS-MIB", "ruijieStaAssStatisticsMIBroup"))
)
if mibBuilder.loadTexts:
    ruijieStaAssRecordsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-STA-ASS-RECORDS-MIB",
    **{"ruijieStaAssRecordsMIB": ruijieStaAssRecordsMIB,
       "ruijieStaAssRecordsMIBTrap": ruijieStaAssRecordsMIBTrap,
       "ruijieStaAssRecordsMIBObjects": ruijieStaAssRecordsMIBObjects,
       "ruijieStaAssRecordsGrobal": ruijieStaAssRecordsGrobal,
       "ruijieStaAssRecordsGrobalTable": ruijieStaAssRecordsGrobalTable,
       "ruijieStaAssRecordsGrobalEntry": ruijieStaAssRecordsGrobalEntry,
       "ruijieStaMacGrobalAddress": ruijieStaMacGrobalAddress,
       "ruijieStaMacGrobalAPName": ruijieStaMacGrobalAPName,
       "ruijieStaMacGrobalISUP": ruijieStaMacGrobalISUP,
       "ruijieStaMacGrobalStartime": ruijieStaMacGrobalStartime,
       "ruijieStaMacGrobalupdowntimes": ruijieStaMacGrobalupdowntimes,
       "ruijieStaMacGrobalroamtimes": ruijieStaMacGrobalroamtimes,
       "ruijieStaMacGrobaltotaltimes": ruijieStaMacGrobaltotaltimes,
       "ruijieStaMacGrobalrealdowntimes": ruijieStaMacGrobalrealdowntimes,
       "ruijieStaMacGrobalSSID": ruijieStaMacGrobalSSID,
       "ruijieStaAssRecordsByMAC": ruijieStaAssRecordsByMAC,
       "ruijieStaAssRecordsByMACTable": ruijieStaAssRecordsByMACTable,
       "ruijieStaAssRecordsByMACEntry": ruijieStaAssRecordsByMACEntry,
       "ruijieStaMacAddress": ruijieStaMacAddress,
       "ruijieStaMacindex": ruijieStaMacindex,
       "ruijieStaAsstime": ruijieStaAsstime,
       "ruijieStaAssAction": ruijieStaAssAction,
       "ruijieStaAssSubAction": ruijieStaAssSubAction,
       "ruijieStaAssResult": ruijieStaAssResult,
       "ruijieStaAssReason": ruijieStaAssReason,
       "ruijieStaAssApNamePre": ruijieStaAssApNamePre,
       "ruijieStaAssApNameNow": ruijieStaAssApNameNow,
       "ruijieStaAssSignalQua": ruijieStaAssSignalQua,
       "ruijieStaAssRoamtype": ruijieStaAssRoamtype,
       "ruijieStaAssjitter": ruijieStaAssjitter,
       "ruijieStaAssjointimes": ruijieStaAssjointimes,
       "ruijieStaAsslatelytime": ruijieStaAsslatelytime,
       "ruijieStaAssSSID": ruijieStaAssSSID,
       "ruijieStaAssRecordsByTime": ruijieStaAssRecordsByTime,
       "ruijieStaAssRecordsSearchByTimeTable": ruijieStaAssRecordsSearchByTimeTable,
       "ruijieStaAssRecordsSearchByTimeEntry": ruijieStaAssRecordsSearchByTimeEntry,
       "ruijieStaUptimeLow": ruijieStaUptimeLow,
       "ruijieStaUptimeHigh": ruijieStaUptimeHigh,
       "ruijieStaDowntimeLow": ruijieStaDowntimeLow,
       "ruijieStaDowntimeHigh": ruijieStaDowntimeHigh,
       "ruijieStaTimeindex": ruijieStaTimeindex,
       "ruijieStaTimeMac": ruijieStaTimeMac,
       "ruijieStaTimeAPName": ruijieStaTimeAPName,
       "ruijieStaTimeISUP": ruijieStaTimeISUP,
       "ruijieStaTimeStartime": ruijieStaTimeStartime,
       "ruijieStaTimeupdowntimes": ruijieStaTimeupdowntimes,
       "ruijieStaTimeroamtimes": ruijieStaTimeroamtimes,
       "ruijieStaTimertotaltimes": ruijieStaTimertotaltimes,
       "ruijieStaTimerjitter": ruijieStaTimerjitter,
       "ruijieStaTimerjointimes": ruijieStaTimerjointimes,
       "ruijieStaTimerlatelytime": ruijieStaTimerlatelytime,
       "ruijieStaTimerSSID": ruijieStaTimerSSID,
       "ruijieStaAssRecordsByAP": ruijieStaAssRecordsByAP,
       "ruijieStaAssRecordsSearchByAPTable": ruijieStaAssRecordsSearchByAPTable,
       "ruijieStaAssRecordsSearchByAPEntry": ruijieStaAssRecordsSearchByAPEntry,
       "ruijieStaAPAPName": ruijieStaAPAPName,
       "ruijieStaAPindex": ruijieStaAPindex,
       "ruijieStaAPMac": ruijieStaAPMac,
       "ruijieStaAPISUP": ruijieStaAPISUP,
       "ruijieStaAPStartime": ruijieStaAPStartime,
       "ruijieStaAPupdowntimes": ruijieStaAPupdowntimes,
       "ruijieStaAProamtimes": ruijieStaAProamtimes,
       "ruijieStaAPtotaltimes": ruijieStaAPtotaltimes,
       "ruijieStaAPjitter": ruijieStaAPjitter,
       "ruijieStaAPjointimes": ruijieStaAPjointimes,
       "ruijieStaAPlatelytime": ruijieStaAPlatelytime,
       "ruijieStaAPSSID": ruijieStaAPSSID,
       "ruijieStaAssSignalByMAC": ruijieStaAssSignalByMAC,
       "ruijieStaAssSignalByMACTable": ruijieStaAssSignalByMACTable,
       "ruijieStaAssSignalByMACEntry": ruijieStaAssSignalByMACEntry,
       "ruijieStaSignalMacAddress": ruijieStaSignalMacAddress,
       "ruijieStaSignalMacindex": ruijieStaSignalMacindex,
       "ruijieStaSignaltime": ruijieStaSignaltime,
       "ruijieStaSignalValue": ruijieStaSignalValue,
       "ruijieStaAssRetryByMAC": ruijieStaAssRetryByMAC,
       "ruijieStaAssRetryByMACTable": ruijieStaAssRetryByMACTable,
       "ruijieStaAssRetryByMACEntry": ruijieStaAssRetryByMACEntry,
       "ruijieStaRetryMacAddress": ruijieStaRetryMacAddress,
       "ruijieStaRetryMacindex": ruijieStaRetryMacindex,
       "ruijieStaRetrytime": ruijieStaRetrytime,
       "ruijieStaRetryValue": ruijieStaRetryValue,
       "ruijieStaAssStatistic": ruijieStaAssStatistic,
       "ruijieAssStatisticsTotalsta": ruijieAssStatisticsTotalsta,
       "ruijieAssStatisticsTotalinfo": ruijieAssStatisticsTotalinfo,
       "ruijieAssStatisticsdown": ruijieAssStatisticsdown,
       "ruijieAssStatisticsObligate1": ruijieAssStatisticsObligate1,
       "ruijieAssStatisticsObligate2": ruijieAssStatisticsObligate2,
       "ruijieAssStatisticsObligate3": ruijieAssStatisticsObligate3,
       "ruijieStaAssRecordsMIBConformance": ruijieStaAssRecordsMIBConformance,
       "ruijieStaAssRecordsMIBCompliances": ruijieStaAssRecordsMIBCompliances,
       "ruijieStaAssRecordsMIBCompliance": ruijieStaAssRecordsMIBCompliance,
       "ruijieStaAssRecordsMIBGroups": ruijieStaAssRecordsMIBGroups,
       "ruijieStaAssRecordsGrobalMIBroup": ruijieStaAssRecordsGrobalMIBroup,
       "ruijieStaAssRecordsMIBroup": ruijieStaAssRecordsMIBroup,
       "ruijieStaAssRecordsSearchByTimeMIBroup": ruijieStaAssRecordsSearchByTimeMIBroup,
       "ruijieStaAssRecordsSearchByAPMIBroup": ruijieStaAssRecordsSearchByAPMIBroup,
       "ruijieStaAssSignalSearchByMACMIBroup": ruijieStaAssSignalSearchByMACMIBroup,
       "ruijieStaAssRetrySearchByMACMIBroup": ruijieStaAssRetrySearchByMACMIBroup,
       "ruijieStaAssStatisticsMIBroup": ruijieStaAssStatisticsMIBroup}
)
