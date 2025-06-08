# SNMP MIB module (HH3C-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-SESSION-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:43:37 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSession = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149)
)
if mibBuilder.loadTexts:
    hh3cSession.setRevisions(
        ("2014-07-15 15:30",
         "2013-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSessionTables_ObjectIdentity = ObjectIdentity
hh3cSessionTables = _Hh3cSessionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1)
)
_Hh3cSessionStatTable_Object = MibTable
hh3cSessionStatTable = _Hh3cSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSessionStatTable.setStatus("current")
_Hh3cSessionStatEntry_Object = MibTableRow
hh3cSessionStatEntry = _Hh3cSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1)
)
hh3cSessionStatEntry.setIndexNames(
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatChassis"),
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatSlot"),
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatCPUID"),
)
if mibBuilder.loadTexts:
    hh3cSessionStatEntry.setStatus("current")


class _Hh3cSessionStatChassis_Type(Unsigned32):
    """Custom type hh3cSessionStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cSessionStatChassis_Type.__name__ = "Unsigned32"
_Hh3cSessionStatChassis_Object = MibTableColumn
hh3cSessionStatChassis = _Hh3cSessionStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 1),
    _Hh3cSessionStatChassis_Type()
)
hh3cSessionStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatChassis.setStatus("current")


class _Hh3cSessionStatSlot_Type(Unsigned32):
    """Custom type hh3cSessionStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cSessionStatSlot_Type.__name__ = "Unsigned32"
_Hh3cSessionStatSlot_Object = MibTableColumn
hh3cSessionStatSlot = _Hh3cSessionStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 2),
    _Hh3cSessionStatSlot_Type()
)
hh3cSessionStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatSlot.setStatus("current")


class _Hh3cSessionStatCPUID_Type(Unsigned32):
    """Custom type hh3cSessionStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cSessionStatCPUID_Type.__name__ = "Unsigned32"
_Hh3cSessionStatCPUID_Object = MibTableColumn
hh3cSessionStatCPUID = _Hh3cSessionStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 3),
    _Hh3cSessionStatCPUID_Type()
)
hh3cSessionStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatCPUID.setStatus("current")
_Hh3cSessionStatCount_Type = Unsigned32
_Hh3cSessionStatCount_Object = MibTableColumn
hh3cSessionStatCount = _Hh3cSessionStatCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 4),
    _Hh3cSessionStatCount_Type()
)
hh3cSessionStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatCount.setStatus("current")
_Hh3cSessionStatCreateRate_Type = Unsigned32
_Hh3cSessionStatCreateRate_Object = MibTableColumn
hh3cSessionStatCreateRate = _Hh3cSessionStatCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 5),
    _Hh3cSessionStatCreateRate_Type()
)
hh3cSessionStatCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatCreateRate.setStatus("current")
_Hh3cSessionStatTCPCount_Type = Unsigned32
_Hh3cSessionStatTCPCount_Object = MibTableColumn
hh3cSessionStatTCPCount = _Hh3cSessionStatTCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 6),
    _Hh3cSessionStatTCPCount_Type()
)
hh3cSessionStatTCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTCPCount.setStatus("current")
_Hh3cSessionStatUDPCount_Type = Unsigned32
_Hh3cSessionStatUDPCount_Object = MibTableColumn
hh3cSessionStatUDPCount = _Hh3cSessionStatUDPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 7),
    _Hh3cSessionStatUDPCount_Type()
)
hh3cSessionStatUDPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatUDPCount.setStatus("current")
_Hh3cSessionStatOtherCount_Type = Unsigned32
_Hh3cSessionStatOtherCount_Object = MibTableColumn
hh3cSessionStatOtherCount = _Hh3cSessionStatOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 8),
    _Hh3cSessionStatOtherCount_Type()
)
hh3cSessionStatOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatOtherCount.setStatus("current")
_Hh3cSessionStatTCPCreateRate_Type = Unsigned32
_Hh3cSessionStatTCPCreateRate_Object = MibTableColumn
hh3cSessionStatTCPCreateRate = _Hh3cSessionStatTCPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 9),
    _Hh3cSessionStatTCPCreateRate_Type()
)
hh3cSessionStatTCPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTCPCreateRate.setStatus("current")
_Hh3cSessionStatUDPCreateRate_Type = Unsigned32
_Hh3cSessionStatUDPCreateRate_Object = MibTableColumn
hh3cSessionStatUDPCreateRate = _Hh3cSessionStatUDPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 10),
    _Hh3cSessionStatUDPCreateRate_Type()
)
hh3cSessionStatUDPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatUDPCreateRate.setStatus("current")
_Hh3cSessionStatOtherCreateRate_Type = Unsigned32
_Hh3cSessionStatOtherCreateRate_Object = MibTableColumn
hh3cSessionStatOtherCreateRate = _Hh3cSessionStatOtherCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 11),
    _Hh3cSessionStatOtherCreateRate_Type()
)
hh3cSessionStatOtherCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatOtherCreateRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SESSION-MIB",
    **{"hh3cSession": hh3cSession,
       "hh3cSessionTables": hh3cSessionTables,
       "hh3cSessionStatTable": hh3cSessionStatTable,
       "hh3cSessionStatEntry": hh3cSessionStatEntry,
       "hh3cSessionStatChassis": hh3cSessionStatChassis,
       "hh3cSessionStatSlot": hh3cSessionStatSlot,
       "hh3cSessionStatCPUID": hh3cSessionStatCPUID,
       "hh3cSessionStatCount": hh3cSessionStatCount,
       "hh3cSessionStatCreateRate": hh3cSessionStatCreateRate,
       "hh3cSessionStatTCPCount": hh3cSessionStatTCPCount,
       "hh3cSessionStatUDPCount": hh3cSessionStatUDPCount,
       "hh3cSessionStatOtherCount": hh3cSessionStatOtherCount,
       "hh3cSessionStatTCPCreateRate": hh3cSessionStatTCPCreateRate,
       "hh3cSessionStatUDPCreateRate": hh3cSessionStatUDPCreateRate,
       "hh3cSessionStatOtherCreateRate": hh3cSessionStatOtherCreateRate}
)
