# SNMP MIB module (HPCIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nordic_akkasource_36378/HPCIP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:47:37 2025
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

hpcipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36378)
)
if mibBuilder.loadTexts:
    hpcipMib.setRevisions(
        ("2015-10-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsipMibs_ObjectIdentity = ObjectIdentity
bsipMibs = _BsipMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 1)
)
_BsipStatistics_ObjectIdentity = ObjectIdentity
bsipStatistics = _BsipStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1)
)
_BsipStatistics_Version_Type = OctetString
_BsipStatistics_Version_Object = MibScalar
bsipStatistics_Version = _BsipStatistics_Version_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 1),
    _BsipStatistics_Version_Type()
)
bsipStatistics_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsipStatistics_Version.setStatus("current")
_BsipStatistics_MgwIndex_Type = Integer32
_BsipStatistics_MgwIndex_Object = MibScalar
bsipStatistics_MgwIndex = _BsipStatistics_MgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 2),
    _BsipStatistics_MgwIndex_Type()
)
bsipStatistics_MgwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsipStatistics_MgwIndex.setStatus("current")
_BsipStatistics_01_Object = MibTable
bsipStatistics_01 = _BsipStatistics_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bsipStatistics_01.setStatus("current")
_BsEntry01_Object = MibTableRow
bsEntry01 = _BsEntry01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1)
)
bsEntry01.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-01"),
)
if mibBuilder.loadTexts:
    bsEntry01.setStatus("current")


class _BsIndex_01_Type(Integer32):
    """Custom type bsIndex_01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_01_Type.__name__ = "Integer32"
_BsIndex_01_Object = MibTableColumn
bsIndex_01 = _BsIndex_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 1),
    _BsIndex_01_Type()
)
bsIndex_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_01.setStatus("current")
_BsFrom_01_Type = OctetString
_BsFrom_01_Object = MibTableColumn
bsFrom_01 = _BsFrom_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 2),
    _BsFrom_01_Type()
)
bsFrom_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_01.setStatus("current")
_BsTo_01_Type = OctetString
_BsTo_01_Object = MibTableColumn
bsTo_01 = _BsTo_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 3),
    _BsTo_01_Type()
)
bsTo_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_01.setStatus("current")
_BsRPN_01_Type = OctetString
_BsRPN_01_Object = MibTableColumn
bsRPN_01 = _BsRPN_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 4),
    _BsRPN_01_Type()
)
bsRPN_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_01.setStatus("current")
_BsMAC_01_Type = OctetString
_BsMAC_01_Object = MibTableColumn
bsMAC_01 = _BsMAC_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 5),
    _BsMAC_01_Type()
)
bsMAC_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_01.setStatus("current")
_BsName_01_Type = OctetString
_BsName_01_Object = MibTableColumn
bsName_01 = _BsName_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 6),
    _BsName_01_Type()
)
bsName_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_01.setStatus("current")
_BsOVL70_01_Type = OctetString
_BsOVL70_01_Object = MibTableColumn
bsOVL70_01 = _BsOVL70_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 7),
    _BsOVL70_01_Type()
)
bsOVL70_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_01.setStatus("current")
_BsOVL100_01_Type = OctetString
_BsOVL100_01_Object = MibTableColumn
bsOVL100_01 = _BsOVL100_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 8),
    _BsOVL100_01_Type()
)
bsOVL100_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_01.setStatus("current")
_BsRoaming_01_Type = OctetString
_BsRoaming_01_Object = MibTableColumn
bsRoaming_01 = _BsRoaming_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 3, 1, 9),
    _BsRoaming_01_Type()
)
bsRoaming_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_01.setStatus("current")
_BsipStatistics_02_Object = MibTable
bsipStatistics_02 = _BsipStatistics_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4)
)
if mibBuilder.loadTexts:
    bsipStatistics_02.setStatus("current")
_BsEntry02_Object = MibTableRow
bsEntry02 = _BsEntry02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1)
)
bsEntry02.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-02"),
)
if mibBuilder.loadTexts:
    bsEntry02.setStatus("current")


class _BsIndex_02_Type(Integer32):
    """Custom type bsIndex_02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_02_Type.__name__ = "Integer32"
_BsIndex_02_Object = MibTableColumn
bsIndex_02 = _BsIndex_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 1),
    _BsIndex_02_Type()
)
bsIndex_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_02.setStatus("current")
_BsFrom_02_Type = OctetString
_BsFrom_02_Object = MibTableColumn
bsFrom_02 = _BsFrom_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 2),
    _BsFrom_02_Type()
)
bsFrom_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_02.setStatus("current")
_BsTo_02_Type = OctetString
_BsTo_02_Object = MibTableColumn
bsTo_02 = _BsTo_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 3),
    _BsTo_02_Type()
)
bsTo_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_02.setStatus("current")
_BsRPN_02_Type = OctetString
_BsRPN_02_Object = MibTableColumn
bsRPN_02 = _BsRPN_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 4),
    _BsRPN_02_Type()
)
bsRPN_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_02.setStatus("current")
_BsMAC_02_Type = OctetString
_BsMAC_02_Object = MibTableColumn
bsMAC_02 = _BsMAC_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 5),
    _BsMAC_02_Type()
)
bsMAC_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_02.setStatus("current")
_BsName_02_Type = OctetString
_BsName_02_Object = MibTableColumn
bsName_02 = _BsName_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 6),
    _BsName_02_Type()
)
bsName_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_02.setStatus("current")
_BsOVL70_02_Type = OctetString
_BsOVL70_02_Object = MibTableColumn
bsOVL70_02 = _BsOVL70_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 7),
    _BsOVL70_02_Type()
)
bsOVL70_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_02.setStatus("current")
_BsOVL100_02_Type = OctetString
_BsOVL100_02_Object = MibTableColumn
bsOVL100_02 = _BsOVL100_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 8),
    _BsOVL100_02_Type()
)
bsOVL100_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_02.setStatus("current")
_BsRoaming_02_Type = OctetString
_BsRoaming_02_Object = MibTableColumn
bsRoaming_02 = _BsRoaming_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 4, 1, 9),
    _BsRoaming_02_Type()
)
bsRoaming_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_02.setStatus("current")
_BsipStatistics_03_Object = MibTable
bsipStatistics_03 = _BsipStatistics_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5)
)
if mibBuilder.loadTexts:
    bsipStatistics_03.setStatus("current")
_BsEntry03_Object = MibTableRow
bsEntry03 = _BsEntry03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1)
)
bsEntry03.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-03"),
)
if mibBuilder.loadTexts:
    bsEntry03.setStatus("current")


class _BsIndex_03_Type(Integer32):
    """Custom type bsIndex_03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_03_Type.__name__ = "Integer32"
_BsIndex_03_Object = MibTableColumn
bsIndex_03 = _BsIndex_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 1),
    _BsIndex_03_Type()
)
bsIndex_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_03.setStatus("current")
_BsFrom_03_Type = OctetString
_BsFrom_03_Object = MibTableColumn
bsFrom_03 = _BsFrom_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 2),
    _BsFrom_03_Type()
)
bsFrom_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_03.setStatus("current")
_BsTo_03_Type = OctetString
_BsTo_03_Object = MibTableColumn
bsTo_03 = _BsTo_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 3),
    _BsTo_03_Type()
)
bsTo_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_03.setStatus("current")
_BsRPN_03_Type = OctetString
_BsRPN_03_Object = MibTableColumn
bsRPN_03 = _BsRPN_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 4),
    _BsRPN_03_Type()
)
bsRPN_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_03.setStatus("current")
_BsMAC_03_Type = OctetString
_BsMAC_03_Object = MibTableColumn
bsMAC_03 = _BsMAC_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 5),
    _BsMAC_03_Type()
)
bsMAC_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_03.setStatus("current")
_BsName_03_Type = OctetString
_BsName_03_Object = MibTableColumn
bsName_03 = _BsName_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 6),
    _BsName_03_Type()
)
bsName_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_03.setStatus("current")
_BsOVL70_03_Type = OctetString
_BsOVL70_03_Object = MibTableColumn
bsOVL70_03 = _BsOVL70_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 7),
    _BsOVL70_03_Type()
)
bsOVL70_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_03.setStatus("current")
_BsOVL100_03_Type = OctetString
_BsOVL100_03_Object = MibTableColumn
bsOVL100_03 = _BsOVL100_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 8),
    _BsOVL100_03_Type()
)
bsOVL100_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_03.setStatus("current")
_BsRoaming_03_Type = OctetString
_BsRoaming_03_Object = MibTableColumn
bsRoaming_03 = _BsRoaming_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 5, 1, 9),
    _BsRoaming_03_Type()
)
bsRoaming_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_03.setStatus("current")
_BsipStatistics_04_Object = MibTable
bsipStatistics_04 = _BsipStatistics_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6)
)
if mibBuilder.loadTexts:
    bsipStatistics_04.setStatus("current")
_BsEntry04_Object = MibTableRow
bsEntry04 = _BsEntry04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1)
)
bsEntry04.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-04"),
)
if mibBuilder.loadTexts:
    bsEntry04.setStatus("current")


class _BsIndex_04_Type(Integer32):
    """Custom type bsIndex_04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_04_Type.__name__ = "Integer32"
_BsIndex_04_Object = MibTableColumn
bsIndex_04 = _BsIndex_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 1),
    _BsIndex_04_Type()
)
bsIndex_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_04.setStatus("current")
_BsFrom_04_Type = OctetString
_BsFrom_04_Object = MibTableColumn
bsFrom_04 = _BsFrom_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 2),
    _BsFrom_04_Type()
)
bsFrom_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_04.setStatus("current")
_BsTo_04_Type = OctetString
_BsTo_04_Object = MibTableColumn
bsTo_04 = _BsTo_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 3),
    _BsTo_04_Type()
)
bsTo_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_04.setStatus("current")
_BsRPN_04_Type = OctetString
_BsRPN_04_Object = MibTableColumn
bsRPN_04 = _BsRPN_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 4),
    _BsRPN_04_Type()
)
bsRPN_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_04.setStatus("current")
_BsMAC_04_Type = OctetString
_BsMAC_04_Object = MibTableColumn
bsMAC_04 = _BsMAC_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 5),
    _BsMAC_04_Type()
)
bsMAC_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_04.setStatus("current")
_BsName_04_Type = OctetString
_BsName_04_Object = MibTableColumn
bsName_04 = _BsName_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 6),
    _BsName_04_Type()
)
bsName_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_04.setStatus("current")
_BsOVL70_04_Type = OctetString
_BsOVL70_04_Object = MibTableColumn
bsOVL70_04 = _BsOVL70_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 7),
    _BsOVL70_04_Type()
)
bsOVL70_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_04.setStatus("current")
_BsOVL100_04_Type = OctetString
_BsOVL100_04_Object = MibTableColumn
bsOVL100_04 = _BsOVL100_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 8),
    _BsOVL100_04_Type()
)
bsOVL100_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_04.setStatus("current")
_BsRoaming_04_Type = OctetString
_BsRoaming_04_Object = MibTableColumn
bsRoaming_04 = _BsRoaming_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 6, 1, 9),
    _BsRoaming_04_Type()
)
bsRoaming_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_04.setStatus("current")
_BsipStatistics_05_Object = MibTable
bsipStatistics_05 = _BsipStatistics_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7)
)
if mibBuilder.loadTexts:
    bsipStatistics_05.setStatus("current")
_BsEntry05_Object = MibTableRow
bsEntry05 = _BsEntry05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1)
)
bsEntry05.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-05"),
)
if mibBuilder.loadTexts:
    bsEntry05.setStatus("current")


class _BsIndex_05_Type(Integer32):
    """Custom type bsIndex_05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_05_Type.__name__ = "Integer32"
_BsIndex_05_Object = MibTableColumn
bsIndex_05 = _BsIndex_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 1),
    _BsIndex_05_Type()
)
bsIndex_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_05.setStatus("current")
_BsFrom_05_Type = OctetString
_BsFrom_05_Object = MibTableColumn
bsFrom_05 = _BsFrom_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 2),
    _BsFrom_05_Type()
)
bsFrom_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_05.setStatus("current")
_BsTo_05_Type = OctetString
_BsTo_05_Object = MibTableColumn
bsTo_05 = _BsTo_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 3),
    _BsTo_05_Type()
)
bsTo_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_05.setStatus("current")
_BsRPN_05_Type = OctetString
_BsRPN_05_Object = MibTableColumn
bsRPN_05 = _BsRPN_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 4),
    _BsRPN_05_Type()
)
bsRPN_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_05.setStatus("current")
_BsMAC_05_Type = OctetString
_BsMAC_05_Object = MibTableColumn
bsMAC_05 = _BsMAC_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 5),
    _BsMAC_05_Type()
)
bsMAC_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_05.setStatus("current")
_BsName_05_Type = OctetString
_BsName_05_Object = MibTableColumn
bsName_05 = _BsName_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 6),
    _BsName_05_Type()
)
bsName_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_05.setStatus("current")
_BsOVL70_05_Type = OctetString
_BsOVL70_05_Object = MibTableColumn
bsOVL70_05 = _BsOVL70_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 7),
    _BsOVL70_05_Type()
)
bsOVL70_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_05.setStatus("current")
_BsOVL100_05_Type = OctetString
_BsOVL100_05_Object = MibTableColumn
bsOVL100_05 = _BsOVL100_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 8),
    _BsOVL100_05_Type()
)
bsOVL100_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_05.setStatus("current")
_BsRoaming_05_Type = OctetString
_BsRoaming_05_Object = MibTableColumn
bsRoaming_05 = _BsRoaming_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 7, 1, 9),
    _BsRoaming_05_Type()
)
bsRoaming_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_05.setStatus("current")
_BsipStatistics_06_Object = MibTable
bsipStatistics_06 = _BsipStatistics_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8)
)
if mibBuilder.loadTexts:
    bsipStatistics_06.setStatus("current")
_BsEntry06_Object = MibTableRow
bsEntry06 = _BsEntry06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1)
)
bsEntry06.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-06"),
)
if mibBuilder.loadTexts:
    bsEntry06.setStatus("current")


class _BsIndex_06_Type(Integer32):
    """Custom type bsIndex_06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_06_Type.__name__ = "Integer32"
_BsIndex_06_Object = MibTableColumn
bsIndex_06 = _BsIndex_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 1),
    _BsIndex_06_Type()
)
bsIndex_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_06.setStatus("current")
_BsFrom_06_Type = OctetString
_BsFrom_06_Object = MibTableColumn
bsFrom_06 = _BsFrom_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 2),
    _BsFrom_06_Type()
)
bsFrom_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_06.setStatus("current")
_BsTo_06_Type = OctetString
_BsTo_06_Object = MibTableColumn
bsTo_06 = _BsTo_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 3),
    _BsTo_06_Type()
)
bsTo_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_06.setStatus("current")
_BsRPN_06_Type = OctetString
_BsRPN_06_Object = MibTableColumn
bsRPN_06 = _BsRPN_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 4),
    _BsRPN_06_Type()
)
bsRPN_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_06.setStatus("current")
_BsMAC_06_Type = OctetString
_BsMAC_06_Object = MibTableColumn
bsMAC_06 = _BsMAC_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 5),
    _BsMAC_06_Type()
)
bsMAC_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_06.setStatus("current")
_BsName_06_Type = OctetString
_BsName_06_Object = MibTableColumn
bsName_06 = _BsName_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 6),
    _BsName_06_Type()
)
bsName_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_06.setStatus("current")
_BsOVL70_06_Type = OctetString
_BsOVL70_06_Object = MibTableColumn
bsOVL70_06 = _BsOVL70_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 7),
    _BsOVL70_06_Type()
)
bsOVL70_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_06.setStatus("current")
_BsOVL100_06_Type = OctetString
_BsOVL100_06_Object = MibTableColumn
bsOVL100_06 = _BsOVL100_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 8),
    _BsOVL100_06_Type()
)
bsOVL100_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_06.setStatus("current")
_BsRoaming_06_Type = OctetString
_BsRoaming_06_Object = MibTableColumn
bsRoaming_06 = _BsRoaming_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 8, 1, 9),
    _BsRoaming_06_Type()
)
bsRoaming_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_06.setStatus("current")
_BsipStatistics_07_Object = MibTable
bsipStatistics_07 = _BsipStatistics_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9)
)
if mibBuilder.loadTexts:
    bsipStatistics_07.setStatus("current")
_BsEntry07_Object = MibTableRow
bsEntry07 = _BsEntry07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1)
)
bsEntry07.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-07"),
)
if mibBuilder.loadTexts:
    bsEntry07.setStatus("current")


class _BsIndex_07_Type(Integer32):
    """Custom type bsIndex_07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_07_Type.__name__ = "Integer32"
_BsIndex_07_Object = MibTableColumn
bsIndex_07 = _BsIndex_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 1),
    _BsIndex_07_Type()
)
bsIndex_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_07.setStatus("current")
_BsFrom_07_Type = OctetString
_BsFrom_07_Object = MibTableColumn
bsFrom_07 = _BsFrom_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 2),
    _BsFrom_07_Type()
)
bsFrom_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_07.setStatus("current")
_BsTo_07_Type = OctetString
_BsTo_07_Object = MibTableColumn
bsTo_07 = _BsTo_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 3),
    _BsTo_07_Type()
)
bsTo_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_07.setStatus("current")
_BsRPN_07_Type = OctetString
_BsRPN_07_Object = MibTableColumn
bsRPN_07 = _BsRPN_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 4),
    _BsRPN_07_Type()
)
bsRPN_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_07.setStatus("current")
_BsMAC_07_Type = OctetString
_BsMAC_07_Object = MibTableColumn
bsMAC_07 = _BsMAC_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 5),
    _BsMAC_07_Type()
)
bsMAC_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_07.setStatus("current")
_BsName_07_Type = OctetString
_BsName_07_Object = MibTableColumn
bsName_07 = _BsName_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 6),
    _BsName_07_Type()
)
bsName_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_07.setStatus("current")
_BsOVL70_07_Type = OctetString
_BsOVL70_07_Object = MibTableColumn
bsOVL70_07 = _BsOVL70_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 7),
    _BsOVL70_07_Type()
)
bsOVL70_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_07.setStatus("current")
_BsOVL100_07_Type = OctetString
_BsOVL100_07_Object = MibTableColumn
bsOVL100_07 = _BsOVL100_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 8),
    _BsOVL100_07_Type()
)
bsOVL100_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_07.setStatus("current")
_BsRoaming_07_Type = OctetString
_BsRoaming_07_Object = MibTableColumn
bsRoaming_07 = _BsRoaming_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 9, 1, 9),
    _BsRoaming_07_Type()
)
bsRoaming_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_07.setStatus("current")
_BsipStatistics_08_Object = MibTable
bsipStatistics_08 = _BsipStatistics_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10)
)
if mibBuilder.loadTexts:
    bsipStatistics_08.setStatus("current")
_BsEntry08_Object = MibTableRow
bsEntry08 = _BsEntry08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1)
)
bsEntry08.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-08"),
)
if mibBuilder.loadTexts:
    bsEntry08.setStatus("current")


class _BsIndex_08_Type(Integer32):
    """Custom type bsIndex_08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_08_Type.__name__ = "Integer32"
_BsIndex_08_Object = MibTableColumn
bsIndex_08 = _BsIndex_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 1),
    _BsIndex_08_Type()
)
bsIndex_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_08.setStatus("current")
_BsFrom_08_Type = OctetString
_BsFrom_08_Object = MibTableColumn
bsFrom_08 = _BsFrom_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 2),
    _BsFrom_08_Type()
)
bsFrom_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_08.setStatus("current")
_BsTo_08_Type = OctetString
_BsTo_08_Object = MibTableColumn
bsTo_08 = _BsTo_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 3),
    _BsTo_08_Type()
)
bsTo_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_08.setStatus("current")
_BsRPN_08_Type = OctetString
_BsRPN_08_Object = MibTableColumn
bsRPN_08 = _BsRPN_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 4),
    _BsRPN_08_Type()
)
bsRPN_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_08.setStatus("current")
_BsMAC_08_Type = OctetString
_BsMAC_08_Object = MibTableColumn
bsMAC_08 = _BsMAC_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 5),
    _BsMAC_08_Type()
)
bsMAC_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_08.setStatus("current")
_BsName_08_Type = OctetString
_BsName_08_Object = MibTableColumn
bsName_08 = _BsName_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 6),
    _BsName_08_Type()
)
bsName_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_08.setStatus("current")
_BsOVL70_08_Type = OctetString
_BsOVL70_08_Object = MibTableColumn
bsOVL70_08 = _BsOVL70_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 7),
    _BsOVL70_08_Type()
)
bsOVL70_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_08.setStatus("current")
_BsOVL100_08_Type = OctetString
_BsOVL100_08_Object = MibTableColumn
bsOVL100_08 = _BsOVL100_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 8),
    _BsOVL100_08_Type()
)
bsOVL100_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_08.setStatus("current")
_BsRoaming_08_Type = OctetString
_BsRoaming_08_Object = MibTableColumn
bsRoaming_08 = _BsRoaming_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 10, 1, 9),
    _BsRoaming_08_Type()
)
bsRoaming_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_08.setStatus("current")
_BsipStatistics_09_Object = MibTable
bsipStatistics_09 = _BsipStatistics_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11)
)
if mibBuilder.loadTexts:
    bsipStatistics_09.setStatus("current")
_BsEntry09_Object = MibTableRow
bsEntry09 = _BsEntry09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1)
)
bsEntry09.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-09"),
)
if mibBuilder.loadTexts:
    bsEntry09.setStatus("current")


class _BsIndex_09_Type(Integer32):
    """Custom type bsIndex_09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_09_Type.__name__ = "Integer32"
_BsIndex_09_Object = MibTableColumn
bsIndex_09 = _BsIndex_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 1),
    _BsIndex_09_Type()
)
bsIndex_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_09.setStatus("current")
_BsFrom_09_Type = OctetString
_BsFrom_09_Object = MibTableColumn
bsFrom_09 = _BsFrom_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 2),
    _BsFrom_09_Type()
)
bsFrom_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_09.setStatus("current")
_BsTo_09_Type = OctetString
_BsTo_09_Object = MibTableColumn
bsTo_09 = _BsTo_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 3),
    _BsTo_09_Type()
)
bsTo_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_09.setStatus("current")
_BsRPN_09_Type = OctetString
_BsRPN_09_Object = MibTableColumn
bsRPN_09 = _BsRPN_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 4),
    _BsRPN_09_Type()
)
bsRPN_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_09.setStatus("current")
_BsMAC_09_Type = OctetString
_BsMAC_09_Object = MibTableColumn
bsMAC_09 = _BsMAC_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 5),
    _BsMAC_09_Type()
)
bsMAC_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_09.setStatus("current")
_BsName_09_Type = OctetString
_BsName_09_Object = MibTableColumn
bsName_09 = _BsName_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 6),
    _BsName_09_Type()
)
bsName_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_09.setStatus("current")
_BsOVL70_09_Type = OctetString
_BsOVL70_09_Object = MibTableColumn
bsOVL70_09 = _BsOVL70_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 7),
    _BsOVL70_09_Type()
)
bsOVL70_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_09.setStatus("current")
_BsOVL100_09_Type = OctetString
_BsOVL100_09_Object = MibTableColumn
bsOVL100_09 = _BsOVL100_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 8),
    _BsOVL100_09_Type()
)
bsOVL100_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_09.setStatus("current")
_BsRoaming_09_Type = OctetString
_BsRoaming_09_Object = MibTableColumn
bsRoaming_09 = _BsRoaming_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 11, 1, 9),
    _BsRoaming_09_Type()
)
bsRoaming_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_09.setStatus("current")
_BsipStatistics_10_Object = MibTable
bsipStatistics_10 = _BsipStatistics_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12)
)
if mibBuilder.loadTexts:
    bsipStatistics_10.setStatus("current")
_BsEntry10_Object = MibTableRow
bsEntry10 = _BsEntry10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1)
)
bsEntry10.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-10"),
)
if mibBuilder.loadTexts:
    bsEntry10.setStatus("current")


class _BsIndex_10_Type(Integer32):
    """Custom type bsIndex_10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_10_Type.__name__ = "Integer32"
_BsIndex_10_Object = MibTableColumn
bsIndex_10 = _BsIndex_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 1),
    _BsIndex_10_Type()
)
bsIndex_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_10.setStatus("current")
_BsFrom_10_Type = OctetString
_BsFrom_10_Object = MibTableColumn
bsFrom_10 = _BsFrom_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 2),
    _BsFrom_10_Type()
)
bsFrom_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_10.setStatus("current")
_BsTo_10_Type = OctetString
_BsTo_10_Object = MibTableColumn
bsTo_10 = _BsTo_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 3),
    _BsTo_10_Type()
)
bsTo_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_10.setStatus("current")
_BsRPN_10_Type = OctetString
_BsRPN_10_Object = MibTableColumn
bsRPN_10 = _BsRPN_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 4),
    _BsRPN_10_Type()
)
bsRPN_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_10.setStatus("current")
_BsMAC_10_Type = OctetString
_BsMAC_10_Object = MibTableColumn
bsMAC_10 = _BsMAC_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 5),
    _BsMAC_10_Type()
)
bsMAC_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_10.setStatus("current")
_BsName_10_Type = OctetString
_BsName_10_Object = MibTableColumn
bsName_10 = _BsName_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 6),
    _BsName_10_Type()
)
bsName_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_10.setStatus("current")
_BsOVL70_10_Type = OctetString
_BsOVL70_10_Object = MibTableColumn
bsOVL70_10 = _BsOVL70_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 7),
    _BsOVL70_10_Type()
)
bsOVL70_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_10.setStatus("current")
_BsOVL100_10_Type = OctetString
_BsOVL100_10_Object = MibTableColumn
bsOVL100_10 = _BsOVL100_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 8),
    _BsOVL100_10_Type()
)
bsOVL100_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_10.setStatus("current")
_BsRoaming_10_Type = OctetString
_BsRoaming_10_Object = MibTableColumn
bsRoaming_10 = _BsRoaming_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 12, 1, 9),
    _BsRoaming_10_Type()
)
bsRoaming_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_10.setStatus("current")
_BsipStatistics_11_Object = MibTable
bsipStatistics_11 = _BsipStatistics_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13)
)
if mibBuilder.loadTexts:
    bsipStatistics_11.setStatus("current")
_BsEntry11_Object = MibTableRow
bsEntry11 = _BsEntry11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1)
)
bsEntry11.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-11"),
)
if mibBuilder.loadTexts:
    bsEntry11.setStatus("current")


class _BsIndex_11_Type(Integer32):
    """Custom type bsIndex_11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_11_Type.__name__ = "Integer32"
_BsIndex_11_Object = MibTableColumn
bsIndex_11 = _BsIndex_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 1),
    _BsIndex_11_Type()
)
bsIndex_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_11.setStatus("current")
_BsFrom_11_Type = OctetString
_BsFrom_11_Object = MibTableColumn
bsFrom_11 = _BsFrom_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 2),
    _BsFrom_11_Type()
)
bsFrom_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_11.setStatus("current")
_BsTo_11_Type = OctetString
_BsTo_11_Object = MibTableColumn
bsTo_11 = _BsTo_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 3),
    _BsTo_11_Type()
)
bsTo_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_11.setStatus("current")
_BsRPN_11_Type = OctetString
_BsRPN_11_Object = MibTableColumn
bsRPN_11 = _BsRPN_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 4),
    _BsRPN_11_Type()
)
bsRPN_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_11.setStatus("current")
_BsMAC_11_Type = OctetString
_BsMAC_11_Object = MibTableColumn
bsMAC_11 = _BsMAC_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 5),
    _BsMAC_11_Type()
)
bsMAC_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_11.setStatus("current")
_BsName_11_Type = OctetString
_BsName_11_Object = MibTableColumn
bsName_11 = _BsName_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 6),
    _BsName_11_Type()
)
bsName_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_11.setStatus("current")
_BsOVL70_11_Type = OctetString
_BsOVL70_11_Object = MibTableColumn
bsOVL70_11 = _BsOVL70_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 7),
    _BsOVL70_11_Type()
)
bsOVL70_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_11.setStatus("current")
_BsOVL100_11_Type = OctetString
_BsOVL100_11_Object = MibTableColumn
bsOVL100_11 = _BsOVL100_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 8),
    _BsOVL100_11_Type()
)
bsOVL100_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_11.setStatus("current")
_BsRoaming_11_Type = OctetString
_BsRoaming_11_Object = MibTableColumn
bsRoaming_11 = _BsRoaming_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 13, 1, 9),
    _BsRoaming_11_Type()
)
bsRoaming_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_11.setStatus("current")
_BsipStatistics_12_Object = MibTable
bsipStatistics_12 = _BsipStatistics_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14)
)
if mibBuilder.loadTexts:
    bsipStatistics_12.setStatus("current")
_BsEntry12_Object = MibTableRow
bsEntry12 = _BsEntry12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1)
)
bsEntry12.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-12"),
)
if mibBuilder.loadTexts:
    bsEntry12.setStatus("current")


class _BsIndex_12_Type(Integer32):
    """Custom type bsIndex_12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_12_Type.__name__ = "Integer32"
_BsIndex_12_Object = MibTableColumn
bsIndex_12 = _BsIndex_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 1),
    _BsIndex_12_Type()
)
bsIndex_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_12.setStatus("current")
_BsFrom_12_Type = OctetString
_BsFrom_12_Object = MibTableColumn
bsFrom_12 = _BsFrom_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 2),
    _BsFrom_12_Type()
)
bsFrom_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_12.setStatus("current")
_BsTo_12_Type = OctetString
_BsTo_12_Object = MibTableColumn
bsTo_12 = _BsTo_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 3),
    _BsTo_12_Type()
)
bsTo_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_12.setStatus("current")
_BsRPN_12_Type = OctetString
_BsRPN_12_Object = MibTableColumn
bsRPN_12 = _BsRPN_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 4),
    _BsRPN_12_Type()
)
bsRPN_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_12.setStatus("current")
_BsMAC_12_Type = OctetString
_BsMAC_12_Object = MibTableColumn
bsMAC_12 = _BsMAC_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 5),
    _BsMAC_12_Type()
)
bsMAC_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_12.setStatus("current")
_BsName_12_Type = OctetString
_BsName_12_Object = MibTableColumn
bsName_12 = _BsName_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 6),
    _BsName_12_Type()
)
bsName_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_12.setStatus("current")
_BsOVL70_12_Type = OctetString
_BsOVL70_12_Object = MibTableColumn
bsOVL70_12 = _BsOVL70_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 7),
    _BsOVL70_12_Type()
)
bsOVL70_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_12.setStatus("current")
_BsOVL100_12_Type = OctetString
_BsOVL100_12_Object = MibTableColumn
bsOVL100_12 = _BsOVL100_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 8),
    _BsOVL100_12_Type()
)
bsOVL100_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_12.setStatus("current")
_BsRoaming_12_Type = OctetString
_BsRoaming_12_Object = MibTableColumn
bsRoaming_12 = _BsRoaming_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 14, 1, 9),
    _BsRoaming_12_Type()
)
bsRoaming_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_12.setStatus("current")
_BsipStatistics_13_Object = MibTable
bsipStatistics_13 = _BsipStatistics_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15)
)
if mibBuilder.loadTexts:
    bsipStatistics_13.setStatus("current")
_BsEntry13_Object = MibTableRow
bsEntry13 = _BsEntry13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1)
)
bsEntry13.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-13"),
)
if mibBuilder.loadTexts:
    bsEntry13.setStatus("current")


class _BsIndex_13_Type(Integer32):
    """Custom type bsIndex_13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_13_Type.__name__ = "Integer32"
_BsIndex_13_Object = MibTableColumn
bsIndex_13 = _BsIndex_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 1),
    _BsIndex_13_Type()
)
bsIndex_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_13.setStatus("current")
_BsFrom_13_Type = OctetString
_BsFrom_13_Object = MibTableColumn
bsFrom_13 = _BsFrom_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 2),
    _BsFrom_13_Type()
)
bsFrom_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_13.setStatus("current")
_BsTo_13_Type = OctetString
_BsTo_13_Object = MibTableColumn
bsTo_13 = _BsTo_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 3),
    _BsTo_13_Type()
)
bsTo_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_13.setStatus("current")
_BsRPN_13_Type = OctetString
_BsRPN_13_Object = MibTableColumn
bsRPN_13 = _BsRPN_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 4),
    _BsRPN_13_Type()
)
bsRPN_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_13.setStatus("current")
_BsMAC_13_Type = OctetString
_BsMAC_13_Object = MibTableColumn
bsMAC_13 = _BsMAC_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 5),
    _BsMAC_13_Type()
)
bsMAC_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_13.setStatus("current")
_BsName_13_Type = OctetString
_BsName_13_Object = MibTableColumn
bsName_13 = _BsName_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 6),
    _BsName_13_Type()
)
bsName_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_13.setStatus("current")
_BsOVL70_13_Type = OctetString
_BsOVL70_13_Object = MibTableColumn
bsOVL70_13 = _BsOVL70_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 7),
    _BsOVL70_13_Type()
)
bsOVL70_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_13.setStatus("current")
_BsOVL100_13_Type = OctetString
_BsOVL100_13_Object = MibTableColumn
bsOVL100_13 = _BsOVL100_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 8),
    _BsOVL100_13_Type()
)
bsOVL100_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_13.setStatus("current")
_BsRoaming_13_Type = OctetString
_BsRoaming_13_Object = MibTableColumn
bsRoaming_13 = _BsRoaming_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 15, 1, 9),
    _BsRoaming_13_Type()
)
bsRoaming_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_13.setStatus("current")
_BsipStatistics_14_Object = MibTable
bsipStatistics_14 = _BsipStatistics_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16)
)
if mibBuilder.loadTexts:
    bsipStatistics_14.setStatus("current")
_BsEntry14_Object = MibTableRow
bsEntry14 = _BsEntry14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1)
)
bsEntry14.setIndexNames(
    (0, "HPCIP-MIB", "bsIndex-14"),
)
if mibBuilder.loadTexts:
    bsEntry14.setStatus("current")


class _BsIndex_14_Type(Integer32):
    """Custom type bsIndex_14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BsIndex_14_Type.__name__ = "Integer32"
_BsIndex_14_Object = MibTableColumn
bsIndex_14 = _BsIndex_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 1),
    _BsIndex_14_Type()
)
bsIndex_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIndex_14.setStatus("current")
_BsFrom_14_Type = OctetString
_BsFrom_14_Object = MibTableColumn
bsFrom_14 = _BsFrom_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 2),
    _BsFrom_14_Type()
)
bsFrom_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsFrom_14.setStatus("current")
_BsTo_14_Type = OctetString
_BsTo_14_Object = MibTableColumn
bsTo_14 = _BsTo_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 3),
    _BsTo_14_Type()
)
bsTo_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsTo_14.setStatus("current")
_BsRPN_14_Type = OctetString
_BsRPN_14_Object = MibTableColumn
bsRPN_14 = _BsRPN_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 4),
    _BsRPN_14_Type()
)
bsRPN_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRPN_14.setStatus("current")
_BsMAC_14_Type = OctetString
_BsMAC_14_Object = MibTableColumn
bsMAC_14 = _BsMAC_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 5),
    _BsMAC_14_Type()
)
bsMAC_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsMAC_14.setStatus("current")
_BsName_14_Type = OctetString
_BsName_14_Object = MibTableColumn
bsName_14 = _BsName_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 6),
    _BsName_14_Type()
)
bsName_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsName_14.setStatus("current")
_BsOVL70_14_Type = OctetString
_BsOVL70_14_Object = MibTableColumn
bsOVL70_14 = _BsOVL70_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 7),
    _BsOVL70_14_Type()
)
bsOVL70_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL70_14.setStatus("current")
_BsOVL100_14_Type = OctetString
_BsOVL100_14_Object = MibTableColumn
bsOVL100_14 = _BsOVL100_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 8),
    _BsOVL100_14_Type()
)
bsOVL100_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsOVL100_14.setStatus("current")
_BsRoaming_14_Type = OctetString
_BsRoaming_14_Object = MibTableColumn
bsRoaming_14 = _BsRoaming_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 1, 1, 16, 1, 9),
    _BsRoaming_14_Type()
)
bsRoaming_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRoaming_14.setStatus("current")
_BsipTraps_ObjectIdentity = ObjectIdentity
bsipTraps = _BsipTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 2)
)
_TrBsip_ObjectIdentity = ObjectIdentity
trBsip = _TrBsip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 2, 4)
)
_TrBsipMAC_Type = OctetString
_TrBsipMAC_Object = MibScalar
trBsipMAC = _TrBsipMAC_Object(
    (1, 3, 6, 1, 4, 1, 36378, 2, 4, 1),
    _TrBsipMAC_Type()
)
trBsipMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trBsipMAC.setStatus("current")
_TrBsipName_Type = OctetString
_TrBsipName_Object = MibScalar
trBsipName = _TrBsipName_Object(
    (1, 3, 6, 1, 4, 1, 36378, 2, 4, 2),
    _TrBsipName_Type()
)
trBsipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trBsipName.setStatus("current")
_TrBsipEvent_Type = OctetString
_TrBsipEvent_Object = MibScalar
trBsipEvent = _TrBsipEvent_Object(
    (1, 3, 6, 1, 4, 1, 36378, 2, 4, 3),
    _TrBsipEvent_Type()
)
trBsipEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trBsipEvent.setStatus("current")
_TrBsipSeverity_Type = OctetString
_TrBsipSeverity_Object = MibScalar
trBsipSeverity = _TrBsipSeverity_Object(
    (1, 3, 6, 1, 4, 1, 36378, 2, 4, 4),
    _TrBsipSeverity_Type()
)
trBsipSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trBsipSeverity.setStatus("current")
_MgwMibs_ObjectIdentity = ObjectIdentity
mgwMibs = _MgwMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 3)
)
_MgwStatistics_ObjectIdentity = ObjectIdentity
mgwStatistics = _MgwStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1)
)
_MgwStatistics_Version_Type = OctetString
_MgwStatistics_Version_Object = MibScalar
mgwStatistics_Version = _MgwStatistics_Version_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 1),
    _MgwStatistics_Version_Type()
)
mgwStatistics_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwStatistics_Version.setStatus("current")
_MgwStatistics_01_Object = MibTable
mgwStatistics_01 = _MgwStatistics_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mgwStatistics_01.setStatus("current")
_MgwEntry01_Object = MibTableRow
mgwEntry01 = _MgwEntry01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1)
)
mgwEntry01.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-01"),
)
if mibBuilder.loadTexts:
    mgwEntry01.setStatus("current")


class _MgwIndex_01_Type(Integer32):
    """Custom type mgwIndex_01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_01_Type.__name__ = "Integer32"
_MgwIndex_01_Object = MibTableColumn
mgwIndex_01 = _MgwIndex_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 1),
    _MgwIndex_01_Type()
)
mgwIndex_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_01.setStatus("current")
_MgwFrom_01_Type = OctetString
_MgwFrom_01_Object = MibTableColumn
mgwFrom_01 = _MgwFrom_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 2),
    _MgwFrom_01_Type()
)
mgwFrom_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_01.setStatus("current")
_MgwTo_01_Type = OctetString
_MgwTo_01_Object = MibTableColumn
mgwTo_01 = _MgwTo_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 3),
    _MgwTo_01_Type()
)
mgwTo_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_01.setStatus("current")
_MgwMgwIndex_01_Type = OctetString
_MgwMgwIndex_01_Object = MibTableColumn
mgwMgwIndex_01 = _MgwMgwIndex_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 4),
    _MgwMgwIndex_01_Type()
)
mgwMgwIndex_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_01.setStatus("current")
_MgwMAC_01_Type = OctetString
_MgwMAC_01_Object = MibTableColumn
mgwMAC_01 = _MgwMAC_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 5),
    _MgwMAC_01_Type()
)
mgwMAC_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_01.setStatus("current")
_MgwName_01_Type = OctetString
_MgwName_01_Object = MibTableColumn
mgwName_01 = _MgwName_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 6),
    _MgwName_01_Type()
)
mgwName_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_01.setStatus("current")
_MgwOVL70_01_Type = OctetString
_MgwOVL70_01_Object = MibTableColumn
mgwOVL70_01 = _MgwOVL70_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 7),
    _MgwOVL70_01_Type()
)
mgwOVL70_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_01.setStatus("current")
_MgwOVL100_01_Type = OctetString
_MgwOVL100_01_Object = MibTableColumn
mgwOVL100_01 = _MgwOVL100_01_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 2, 1, 8),
    _MgwOVL100_01_Type()
)
mgwOVL100_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_01.setStatus("current")
_MgwStatistics_02_Object = MibTable
mgwStatistics_02 = _MgwStatistics_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3)
)
if mibBuilder.loadTexts:
    mgwStatistics_02.setStatus("current")
_MgwEntry02_Object = MibTableRow
mgwEntry02 = _MgwEntry02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1)
)
mgwEntry02.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-02"),
)
if mibBuilder.loadTexts:
    mgwEntry02.setStatus("current")


class _MgwIndex_02_Type(Integer32):
    """Custom type mgwIndex_02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_02_Type.__name__ = "Integer32"
_MgwIndex_02_Object = MibTableColumn
mgwIndex_02 = _MgwIndex_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 1),
    _MgwIndex_02_Type()
)
mgwIndex_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_02.setStatus("current")
_MgwFrom_02_Type = OctetString
_MgwFrom_02_Object = MibTableColumn
mgwFrom_02 = _MgwFrom_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 2),
    _MgwFrom_02_Type()
)
mgwFrom_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_02.setStatus("current")
_MgwTo_02_Type = OctetString
_MgwTo_02_Object = MibTableColumn
mgwTo_02 = _MgwTo_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 3),
    _MgwTo_02_Type()
)
mgwTo_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_02.setStatus("current")
_MgwMgwIndex_02_Type = OctetString
_MgwMgwIndex_02_Object = MibTableColumn
mgwMgwIndex_02 = _MgwMgwIndex_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 4),
    _MgwMgwIndex_02_Type()
)
mgwMgwIndex_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_02.setStatus("current")
_MgwMAC_02_Type = OctetString
_MgwMAC_02_Object = MibTableColumn
mgwMAC_02 = _MgwMAC_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 5),
    _MgwMAC_02_Type()
)
mgwMAC_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_02.setStatus("current")
_MgwName_02_Type = OctetString
_MgwName_02_Object = MibTableColumn
mgwName_02 = _MgwName_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 6),
    _MgwName_02_Type()
)
mgwName_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_02.setStatus("current")
_MgwOVL70_02_Type = OctetString
_MgwOVL70_02_Object = MibTableColumn
mgwOVL70_02 = _MgwOVL70_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 7),
    _MgwOVL70_02_Type()
)
mgwOVL70_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_02.setStatus("current")
_MgwOVL100_02_Type = OctetString
_MgwOVL100_02_Object = MibTableColumn
mgwOVL100_02 = _MgwOVL100_02_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 3, 1, 8),
    _MgwOVL100_02_Type()
)
mgwOVL100_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_02.setStatus("current")
_MgwStatistics_03_Object = MibTable
mgwStatistics_03 = _MgwStatistics_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4)
)
if mibBuilder.loadTexts:
    mgwStatistics_03.setStatus("current")
_MgwEntry03_Object = MibTableRow
mgwEntry03 = _MgwEntry03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1)
)
mgwEntry03.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-03"),
)
if mibBuilder.loadTexts:
    mgwEntry03.setStatus("current")


class _MgwIndex_03_Type(Integer32):
    """Custom type mgwIndex_03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_03_Type.__name__ = "Integer32"
_MgwIndex_03_Object = MibTableColumn
mgwIndex_03 = _MgwIndex_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 1),
    _MgwIndex_03_Type()
)
mgwIndex_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_03.setStatus("current")
_MgwFrom_03_Type = OctetString
_MgwFrom_03_Object = MibTableColumn
mgwFrom_03 = _MgwFrom_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 2),
    _MgwFrom_03_Type()
)
mgwFrom_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_03.setStatus("current")
_MgwTo_03_Type = OctetString
_MgwTo_03_Object = MibTableColumn
mgwTo_03 = _MgwTo_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 3),
    _MgwTo_03_Type()
)
mgwTo_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_03.setStatus("current")
_MgwMgwIndex_03_Type = OctetString
_MgwMgwIndex_03_Object = MibTableColumn
mgwMgwIndex_03 = _MgwMgwIndex_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 4),
    _MgwMgwIndex_03_Type()
)
mgwMgwIndex_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_03.setStatus("current")
_MgwMAC_03_Type = OctetString
_MgwMAC_03_Object = MibTableColumn
mgwMAC_03 = _MgwMAC_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 5),
    _MgwMAC_03_Type()
)
mgwMAC_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_03.setStatus("current")
_MgwName_03_Type = OctetString
_MgwName_03_Object = MibTableColumn
mgwName_03 = _MgwName_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 6),
    _MgwName_03_Type()
)
mgwName_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_03.setStatus("current")
_MgwOVL70_03_Type = OctetString
_MgwOVL70_03_Object = MibTableColumn
mgwOVL70_03 = _MgwOVL70_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 7),
    _MgwOVL70_03_Type()
)
mgwOVL70_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_03.setStatus("current")
_MgwOVL100_03_Type = OctetString
_MgwOVL100_03_Object = MibTableColumn
mgwOVL100_03 = _MgwOVL100_03_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 4, 1, 8),
    _MgwOVL100_03_Type()
)
mgwOVL100_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_03.setStatus("current")
_MgwStatistics_04_Object = MibTable
mgwStatistics_04 = _MgwStatistics_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5)
)
if mibBuilder.loadTexts:
    mgwStatistics_04.setStatus("current")
_MgwEntry04_Object = MibTableRow
mgwEntry04 = _MgwEntry04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1)
)
mgwEntry04.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-04"),
)
if mibBuilder.loadTexts:
    mgwEntry04.setStatus("current")


class _MgwIndex_04_Type(Integer32):
    """Custom type mgwIndex_04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_04_Type.__name__ = "Integer32"
_MgwIndex_04_Object = MibTableColumn
mgwIndex_04 = _MgwIndex_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 1),
    _MgwIndex_04_Type()
)
mgwIndex_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_04.setStatus("current")
_MgwFrom_04_Type = OctetString
_MgwFrom_04_Object = MibTableColumn
mgwFrom_04 = _MgwFrom_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 2),
    _MgwFrom_04_Type()
)
mgwFrom_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_04.setStatus("current")
_MgwTo_04_Type = OctetString
_MgwTo_04_Object = MibTableColumn
mgwTo_04 = _MgwTo_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 3),
    _MgwTo_04_Type()
)
mgwTo_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_04.setStatus("current")
_MgwMgwIndex_04_Type = OctetString
_MgwMgwIndex_04_Object = MibTableColumn
mgwMgwIndex_04 = _MgwMgwIndex_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 4),
    _MgwMgwIndex_04_Type()
)
mgwMgwIndex_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_04.setStatus("current")
_MgwMAC_04_Type = OctetString
_MgwMAC_04_Object = MibTableColumn
mgwMAC_04 = _MgwMAC_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 5),
    _MgwMAC_04_Type()
)
mgwMAC_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_04.setStatus("current")
_MgwName_04_Type = OctetString
_MgwName_04_Object = MibTableColumn
mgwName_04 = _MgwName_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 6),
    _MgwName_04_Type()
)
mgwName_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_04.setStatus("current")
_MgwOVL70_04_Type = OctetString
_MgwOVL70_04_Object = MibTableColumn
mgwOVL70_04 = _MgwOVL70_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 7),
    _MgwOVL70_04_Type()
)
mgwOVL70_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_04.setStatus("current")
_MgwOVL100_04_Type = OctetString
_MgwOVL100_04_Object = MibTableColumn
mgwOVL100_04 = _MgwOVL100_04_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 5, 1, 8),
    _MgwOVL100_04_Type()
)
mgwOVL100_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_04.setStatus("current")
_MgwStatistics_05_Object = MibTable
mgwStatistics_05 = _MgwStatistics_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6)
)
if mibBuilder.loadTexts:
    mgwStatistics_05.setStatus("current")
_MgwEntry05_Object = MibTableRow
mgwEntry05 = _MgwEntry05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1)
)
mgwEntry05.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-05"),
)
if mibBuilder.loadTexts:
    mgwEntry05.setStatus("current")


class _MgwIndex_05_Type(Integer32):
    """Custom type mgwIndex_05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_05_Type.__name__ = "Integer32"
_MgwIndex_05_Object = MibTableColumn
mgwIndex_05 = _MgwIndex_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 1),
    _MgwIndex_05_Type()
)
mgwIndex_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_05.setStatus("current")
_MgwFrom_05_Type = OctetString
_MgwFrom_05_Object = MibTableColumn
mgwFrom_05 = _MgwFrom_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 2),
    _MgwFrom_05_Type()
)
mgwFrom_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_05.setStatus("current")
_MgwTo_05_Type = OctetString
_MgwTo_05_Object = MibTableColumn
mgwTo_05 = _MgwTo_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 3),
    _MgwTo_05_Type()
)
mgwTo_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_05.setStatus("current")
_MgwMgwIndex_05_Type = OctetString
_MgwMgwIndex_05_Object = MibTableColumn
mgwMgwIndex_05 = _MgwMgwIndex_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 4),
    _MgwMgwIndex_05_Type()
)
mgwMgwIndex_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_05.setStatus("current")
_MgwMAC_05_Type = OctetString
_MgwMAC_05_Object = MibTableColumn
mgwMAC_05 = _MgwMAC_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 5),
    _MgwMAC_05_Type()
)
mgwMAC_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_05.setStatus("current")
_MgwName_05_Type = OctetString
_MgwName_05_Object = MibTableColumn
mgwName_05 = _MgwName_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 6),
    _MgwName_05_Type()
)
mgwName_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_05.setStatus("current")
_MgwOVL70_05_Type = OctetString
_MgwOVL70_05_Object = MibTableColumn
mgwOVL70_05 = _MgwOVL70_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 7),
    _MgwOVL70_05_Type()
)
mgwOVL70_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_05.setStatus("current")
_MgwOVL100_05_Type = OctetString
_MgwOVL100_05_Object = MibTableColumn
mgwOVL100_05 = _MgwOVL100_05_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 6, 1, 8),
    _MgwOVL100_05_Type()
)
mgwOVL100_05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_05.setStatus("current")
_MgwStatistics_06_Object = MibTable
mgwStatistics_06 = _MgwStatistics_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7)
)
if mibBuilder.loadTexts:
    mgwStatistics_06.setStatus("current")
_MgwEntry06_Object = MibTableRow
mgwEntry06 = _MgwEntry06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1)
)
mgwEntry06.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-06"),
)
if mibBuilder.loadTexts:
    mgwEntry06.setStatus("current")


class _MgwIndex_06_Type(Integer32):
    """Custom type mgwIndex_06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_06_Type.__name__ = "Integer32"
_MgwIndex_06_Object = MibTableColumn
mgwIndex_06 = _MgwIndex_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 1),
    _MgwIndex_06_Type()
)
mgwIndex_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_06.setStatus("current")
_MgwFrom_06_Type = OctetString
_MgwFrom_06_Object = MibTableColumn
mgwFrom_06 = _MgwFrom_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 2),
    _MgwFrom_06_Type()
)
mgwFrom_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_06.setStatus("current")
_MgwTo_06_Type = OctetString
_MgwTo_06_Object = MibTableColumn
mgwTo_06 = _MgwTo_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 3),
    _MgwTo_06_Type()
)
mgwTo_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_06.setStatus("current")
_MgwMgwIndex_06_Type = OctetString
_MgwMgwIndex_06_Object = MibTableColumn
mgwMgwIndex_06 = _MgwMgwIndex_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 4),
    _MgwMgwIndex_06_Type()
)
mgwMgwIndex_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_06.setStatus("current")
_MgwMAC_06_Type = OctetString
_MgwMAC_06_Object = MibTableColumn
mgwMAC_06 = _MgwMAC_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 5),
    _MgwMAC_06_Type()
)
mgwMAC_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_06.setStatus("current")
_MgwName_06_Type = OctetString
_MgwName_06_Object = MibTableColumn
mgwName_06 = _MgwName_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 6),
    _MgwName_06_Type()
)
mgwName_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_06.setStatus("current")
_MgwOVL70_06_Type = OctetString
_MgwOVL70_06_Object = MibTableColumn
mgwOVL70_06 = _MgwOVL70_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 7),
    _MgwOVL70_06_Type()
)
mgwOVL70_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_06.setStatus("current")
_MgwOVL100_06_Type = OctetString
_MgwOVL100_06_Object = MibTableColumn
mgwOVL100_06 = _MgwOVL100_06_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 7, 1, 8),
    _MgwOVL100_06_Type()
)
mgwOVL100_06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_06.setStatus("current")
_MgwStatistics_07_Object = MibTable
mgwStatistics_07 = _MgwStatistics_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8)
)
if mibBuilder.loadTexts:
    mgwStatistics_07.setStatus("current")
_MgwEntry07_Object = MibTableRow
mgwEntry07 = _MgwEntry07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1)
)
mgwEntry07.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-07"),
)
if mibBuilder.loadTexts:
    mgwEntry07.setStatus("current")


class _MgwIndex_07_Type(Integer32):
    """Custom type mgwIndex_07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_07_Type.__name__ = "Integer32"
_MgwIndex_07_Object = MibTableColumn
mgwIndex_07 = _MgwIndex_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 1),
    _MgwIndex_07_Type()
)
mgwIndex_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_07.setStatus("current")
_MgwFrom_07_Type = OctetString
_MgwFrom_07_Object = MibTableColumn
mgwFrom_07 = _MgwFrom_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 2),
    _MgwFrom_07_Type()
)
mgwFrom_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_07.setStatus("current")
_MgwTo_07_Type = OctetString
_MgwTo_07_Object = MibTableColumn
mgwTo_07 = _MgwTo_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 3),
    _MgwTo_07_Type()
)
mgwTo_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_07.setStatus("current")
_MgwMgwIndex_07_Type = OctetString
_MgwMgwIndex_07_Object = MibTableColumn
mgwMgwIndex_07 = _MgwMgwIndex_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 4),
    _MgwMgwIndex_07_Type()
)
mgwMgwIndex_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_07.setStatus("current")
_MgwMAC_07_Type = OctetString
_MgwMAC_07_Object = MibTableColumn
mgwMAC_07 = _MgwMAC_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 5),
    _MgwMAC_07_Type()
)
mgwMAC_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_07.setStatus("current")
_MgwName_07_Type = OctetString
_MgwName_07_Object = MibTableColumn
mgwName_07 = _MgwName_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 6),
    _MgwName_07_Type()
)
mgwName_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_07.setStatus("current")
_MgwOVL70_07_Type = OctetString
_MgwOVL70_07_Object = MibTableColumn
mgwOVL70_07 = _MgwOVL70_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 7),
    _MgwOVL70_07_Type()
)
mgwOVL70_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_07.setStatus("current")
_MgwOVL100_07_Type = OctetString
_MgwOVL100_07_Object = MibTableColumn
mgwOVL100_07 = _MgwOVL100_07_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 8, 1, 8),
    _MgwOVL100_07_Type()
)
mgwOVL100_07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_07.setStatus("current")
_MgwStatistics_08_Object = MibTable
mgwStatistics_08 = _MgwStatistics_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9)
)
if mibBuilder.loadTexts:
    mgwStatistics_08.setStatus("current")
_MgwEntry08_Object = MibTableRow
mgwEntry08 = _MgwEntry08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1)
)
mgwEntry08.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-08"),
)
if mibBuilder.loadTexts:
    mgwEntry08.setStatus("current")


class _MgwIndex_08_Type(Integer32):
    """Custom type mgwIndex_08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_08_Type.__name__ = "Integer32"
_MgwIndex_08_Object = MibTableColumn
mgwIndex_08 = _MgwIndex_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 1),
    _MgwIndex_08_Type()
)
mgwIndex_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_08.setStatus("current")
_MgwFrom_08_Type = OctetString
_MgwFrom_08_Object = MibTableColumn
mgwFrom_08 = _MgwFrom_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 2),
    _MgwFrom_08_Type()
)
mgwFrom_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_08.setStatus("current")
_MgwTo_08_Type = OctetString
_MgwTo_08_Object = MibTableColumn
mgwTo_08 = _MgwTo_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 3),
    _MgwTo_08_Type()
)
mgwTo_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_08.setStatus("current")
_MgwMgwIndex_08_Type = OctetString
_MgwMgwIndex_08_Object = MibTableColumn
mgwMgwIndex_08 = _MgwMgwIndex_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 4),
    _MgwMgwIndex_08_Type()
)
mgwMgwIndex_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_08.setStatus("current")
_MgwMAC_08_Type = OctetString
_MgwMAC_08_Object = MibTableColumn
mgwMAC_08 = _MgwMAC_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 5),
    _MgwMAC_08_Type()
)
mgwMAC_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_08.setStatus("current")
_MgwName_08_Type = OctetString
_MgwName_08_Object = MibTableColumn
mgwName_08 = _MgwName_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 6),
    _MgwName_08_Type()
)
mgwName_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_08.setStatus("current")
_MgwOVL70_08_Type = OctetString
_MgwOVL70_08_Object = MibTableColumn
mgwOVL70_08 = _MgwOVL70_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 7),
    _MgwOVL70_08_Type()
)
mgwOVL70_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_08.setStatus("current")
_MgwOVL100_08_Type = OctetString
_MgwOVL100_08_Object = MibTableColumn
mgwOVL100_08 = _MgwOVL100_08_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 9, 1, 8),
    _MgwOVL100_08_Type()
)
mgwOVL100_08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_08.setStatus("current")
_MgwStatistics_09_Object = MibTable
mgwStatistics_09 = _MgwStatistics_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10)
)
if mibBuilder.loadTexts:
    mgwStatistics_09.setStatus("current")
_MgwEntry09_Object = MibTableRow
mgwEntry09 = _MgwEntry09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1)
)
mgwEntry09.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-09"),
)
if mibBuilder.loadTexts:
    mgwEntry09.setStatus("current")


class _MgwIndex_09_Type(Integer32):
    """Custom type mgwIndex_09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_09_Type.__name__ = "Integer32"
_MgwIndex_09_Object = MibTableColumn
mgwIndex_09 = _MgwIndex_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 1),
    _MgwIndex_09_Type()
)
mgwIndex_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_09.setStatus("current")
_MgwFrom_09_Type = OctetString
_MgwFrom_09_Object = MibTableColumn
mgwFrom_09 = _MgwFrom_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 2),
    _MgwFrom_09_Type()
)
mgwFrom_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_09.setStatus("current")
_MgwTo_09_Type = OctetString
_MgwTo_09_Object = MibTableColumn
mgwTo_09 = _MgwTo_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 3),
    _MgwTo_09_Type()
)
mgwTo_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_09.setStatus("current")
_MgwMgwIndex_09_Type = OctetString
_MgwMgwIndex_09_Object = MibTableColumn
mgwMgwIndex_09 = _MgwMgwIndex_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 4),
    _MgwMgwIndex_09_Type()
)
mgwMgwIndex_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_09.setStatus("current")
_MgwMAC_09_Type = OctetString
_MgwMAC_09_Object = MibTableColumn
mgwMAC_09 = _MgwMAC_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 5),
    _MgwMAC_09_Type()
)
mgwMAC_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_09.setStatus("current")
_MgwName_09_Type = OctetString
_MgwName_09_Object = MibTableColumn
mgwName_09 = _MgwName_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 6),
    _MgwName_09_Type()
)
mgwName_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_09.setStatus("current")
_MgwOVL70_09_Type = OctetString
_MgwOVL70_09_Object = MibTableColumn
mgwOVL70_09 = _MgwOVL70_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 7),
    _MgwOVL70_09_Type()
)
mgwOVL70_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_09.setStatus("current")
_MgwOVL100_09_Type = OctetString
_MgwOVL100_09_Object = MibTableColumn
mgwOVL100_09 = _MgwOVL100_09_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 10, 1, 8),
    _MgwOVL100_09_Type()
)
mgwOVL100_09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_09.setStatus("current")
_MgwStatistics_10_Object = MibTable
mgwStatistics_10 = _MgwStatistics_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11)
)
if mibBuilder.loadTexts:
    mgwStatistics_10.setStatus("current")
_MgwEntry10_Object = MibTableRow
mgwEntry10 = _MgwEntry10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1)
)
mgwEntry10.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-10"),
)
if mibBuilder.loadTexts:
    mgwEntry10.setStatus("current")


class _MgwIndex_10_Type(Integer32):
    """Custom type mgwIndex_10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_10_Type.__name__ = "Integer32"
_MgwIndex_10_Object = MibTableColumn
mgwIndex_10 = _MgwIndex_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 1),
    _MgwIndex_10_Type()
)
mgwIndex_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_10.setStatus("current")
_MgwFrom_10_Type = OctetString
_MgwFrom_10_Object = MibTableColumn
mgwFrom_10 = _MgwFrom_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 2),
    _MgwFrom_10_Type()
)
mgwFrom_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_10.setStatus("current")
_MgwTo_10_Type = OctetString
_MgwTo_10_Object = MibTableColumn
mgwTo_10 = _MgwTo_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 3),
    _MgwTo_10_Type()
)
mgwTo_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_10.setStatus("current")
_MgwMgwIndex_10_Type = OctetString
_MgwMgwIndex_10_Object = MibTableColumn
mgwMgwIndex_10 = _MgwMgwIndex_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 4),
    _MgwMgwIndex_10_Type()
)
mgwMgwIndex_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_10.setStatus("current")
_MgwMAC_10_Type = OctetString
_MgwMAC_10_Object = MibTableColumn
mgwMAC_10 = _MgwMAC_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 5),
    _MgwMAC_10_Type()
)
mgwMAC_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_10.setStatus("current")
_MgwName_10_Type = OctetString
_MgwName_10_Object = MibTableColumn
mgwName_10 = _MgwName_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 6),
    _MgwName_10_Type()
)
mgwName_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_10.setStatus("current")
_MgwOVL70_10_Type = OctetString
_MgwOVL70_10_Object = MibTableColumn
mgwOVL70_10 = _MgwOVL70_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 7),
    _MgwOVL70_10_Type()
)
mgwOVL70_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_10.setStatus("current")
_MgwOVL100_10_Type = OctetString
_MgwOVL100_10_Object = MibTableColumn
mgwOVL100_10 = _MgwOVL100_10_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 11, 1, 8),
    _MgwOVL100_10_Type()
)
mgwOVL100_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_10.setStatus("current")
_MgwStatistics_11_Object = MibTable
mgwStatistics_11 = _MgwStatistics_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12)
)
if mibBuilder.loadTexts:
    mgwStatistics_11.setStatus("current")
_MgwEntry11_Object = MibTableRow
mgwEntry11 = _MgwEntry11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1)
)
mgwEntry11.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-11"),
)
if mibBuilder.loadTexts:
    mgwEntry11.setStatus("current")


class _MgwIndex_11_Type(Integer32):
    """Custom type mgwIndex_11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_11_Type.__name__ = "Integer32"
_MgwIndex_11_Object = MibTableColumn
mgwIndex_11 = _MgwIndex_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 1),
    _MgwIndex_11_Type()
)
mgwIndex_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_11.setStatus("current")
_MgwFrom_11_Type = OctetString
_MgwFrom_11_Object = MibTableColumn
mgwFrom_11 = _MgwFrom_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 2),
    _MgwFrom_11_Type()
)
mgwFrom_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_11.setStatus("current")
_MgwTo_11_Type = OctetString
_MgwTo_11_Object = MibTableColumn
mgwTo_11 = _MgwTo_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 3),
    _MgwTo_11_Type()
)
mgwTo_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_11.setStatus("current")
_MgwMgwIndex_11_Type = OctetString
_MgwMgwIndex_11_Object = MibTableColumn
mgwMgwIndex_11 = _MgwMgwIndex_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 4),
    _MgwMgwIndex_11_Type()
)
mgwMgwIndex_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_11.setStatus("current")
_MgwMAC_11_Type = OctetString
_MgwMAC_11_Object = MibTableColumn
mgwMAC_11 = _MgwMAC_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 5),
    _MgwMAC_11_Type()
)
mgwMAC_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_11.setStatus("current")
_MgwName_11_Type = OctetString
_MgwName_11_Object = MibTableColumn
mgwName_11 = _MgwName_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 6),
    _MgwName_11_Type()
)
mgwName_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_11.setStatus("current")
_MgwOVL70_11_Type = OctetString
_MgwOVL70_11_Object = MibTableColumn
mgwOVL70_11 = _MgwOVL70_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 7),
    _MgwOVL70_11_Type()
)
mgwOVL70_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_11.setStatus("current")
_MgwOVL100_11_Type = OctetString
_MgwOVL100_11_Object = MibTableColumn
mgwOVL100_11 = _MgwOVL100_11_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 12, 1, 8),
    _MgwOVL100_11_Type()
)
mgwOVL100_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_11.setStatus("current")
_MgwStatistics_12_Object = MibTable
mgwStatistics_12 = _MgwStatistics_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13)
)
if mibBuilder.loadTexts:
    mgwStatistics_12.setStatus("current")
_MgwEntry12_Object = MibTableRow
mgwEntry12 = _MgwEntry12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1)
)
mgwEntry12.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-12"),
)
if mibBuilder.loadTexts:
    mgwEntry12.setStatus("current")


class _MgwIndex_12_Type(Integer32):
    """Custom type mgwIndex_12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_12_Type.__name__ = "Integer32"
_MgwIndex_12_Object = MibTableColumn
mgwIndex_12 = _MgwIndex_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 1),
    _MgwIndex_12_Type()
)
mgwIndex_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_12.setStatus("current")
_MgwFrom_12_Type = OctetString
_MgwFrom_12_Object = MibTableColumn
mgwFrom_12 = _MgwFrom_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 2),
    _MgwFrom_12_Type()
)
mgwFrom_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_12.setStatus("current")
_MgwTo_12_Type = OctetString
_MgwTo_12_Object = MibTableColumn
mgwTo_12 = _MgwTo_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 3),
    _MgwTo_12_Type()
)
mgwTo_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_12.setStatus("current")
_MgwMgwIndex_12_Type = OctetString
_MgwMgwIndex_12_Object = MibTableColumn
mgwMgwIndex_12 = _MgwMgwIndex_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 4),
    _MgwMgwIndex_12_Type()
)
mgwMgwIndex_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_12.setStatus("current")
_MgwMAC_12_Type = OctetString
_MgwMAC_12_Object = MibTableColumn
mgwMAC_12 = _MgwMAC_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 5),
    _MgwMAC_12_Type()
)
mgwMAC_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_12.setStatus("current")
_MgwName_12_Type = OctetString
_MgwName_12_Object = MibTableColumn
mgwName_12 = _MgwName_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 6),
    _MgwName_12_Type()
)
mgwName_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_12.setStatus("current")
_MgwOVL70_12_Type = OctetString
_MgwOVL70_12_Object = MibTableColumn
mgwOVL70_12 = _MgwOVL70_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 7),
    _MgwOVL70_12_Type()
)
mgwOVL70_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_12.setStatus("current")
_MgwOVL100_12_Type = OctetString
_MgwOVL100_12_Object = MibTableColumn
mgwOVL100_12 = _MgwOVL100_12_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 13, 1, 8),
    _MgwOVL100_12_Type()
)
mgwOVL100_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_12.setStatus("current")
_MgwStatistics_13_Object = MibTable
mgwStatistics_13 = _MgwStatistics_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14)
)
if mibBuilder.loadTexts:
    mgwStatistics_13.setStatus("current")
_MgwEntry13_Object = MibTableRow
mgwEntry13 = _MgwEntry13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1)
)
mgwEntry13.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-13"),
)
if mibBuilder.loadTexts:
    mgwEntry13.setStatus("current")


class _MgwIndex_13_Type(Integer32):
    """Custom type mgwIndex_13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_13_Type.__name__ = "Integer32"
_MgwIndex_13_Object = MibTableColumn
mgwIndex_13 = _MgwIndex_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 1),
    _MgwIndex_13_Type()
)
mgwIndex_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_13.setStatus("current")
_MgwFrom_13_Type = OctetString
_MgwFrom_13_Object = MibTableColumn
mgwFrom_13 = _MgwFrom_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 2),
    _MgwFrom_13_Type()
)
mgwFrom_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_13.setStatus("current")
_MgwTo_13_Type = OctetString
_MgwTo_13_Object = MibTableColumn
mgwTo_13 = _MgwTo_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 3),
    _MgwTo_13_Type()
)
mgwTo_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_13.setStatus("current")
_MgwMgwIndex_13_Type = OctetString
_MgwMgwIndex_13_Object = MibTableColumn
mgwMgwIndex_13 = _MgwMgwIndex_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 4),
    _MgwMgwIndex_13_Type()
)
mgwMgwIndex_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_13.setStatus("current")
_MgwMAC_13_Type = OctetString
_MgwMAC_13_Object = MibTableColumn
mgwMAC_13 = _MgwMAC_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 5),
    _MgwMAC_13_Type()
)
mgwMAC_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_13.setStatus("current")
_MgwName_13_Type = OctetString
_MgwName_13_Object = MibTableColumn
mgwName_13 = _MgwName_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 6),
    _MgwName_13_Type()
)
mgwName_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_13.setStatus("current")
_MgwOVL70_13_Type = OctetString
_MgwOVL70_13_Object = MibTableColumn
mgwOVL70_13 = _MgwOVL70_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 7),
    _MgwOVL70_13_Type()
)
mgwOVL70_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_13.setStatus("current")
_MgwOVL100_13_Type = OctetString
_MgwOVL100_13_Object = MibTableColumn
mgwOVL100_13 = _MgwOVL100_13_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 14, 1, 8),
    _MgwOVL100_13_Type()
)
mgwOVL100_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_13.setStatus("current")
_MgwStatistics_14_Object = MibTable
mgwStatistics_14 = _MgwStatistics_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15)
)
if mibBuilder.loadTexts:
    mgwStatistics_14.setStatus("current")
_MgwEntry14_Object = MibTableRow
mgwEntry14 = _MgwEntry14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1)
)
mgwEntry14.setIndexNames(
    (0, "HPCIP-MIB", "mgwIndex-14"),
)
if mibBuilder.loadTexts:
    mgwEntry14.setStatus("current")


class _MgwIndex_14_Type(Integer32):
    """Custom type mgwIndex_14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MgwIndex_14_Type.__name__ = "Integer32"
_MgwIndex_14_Object = MibTableColumn
mgwIndex_14 = _MgwIndex_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 1),
    _MgwIndex_14_Type()
)
mgwIndex_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwIndex_14.setStatus("current")
_MgwFrom_14_Type = OctetString
_MgwFrom_14_Object = MibTableColumn
mgwFrom_14 = _MgwFrom_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 2),
    _MgwFrom_14_Type()
)
mgwFrom_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwFrom_14.setStatus("current")
_MgwTo_14_Type = OctetString
_MgwTo_14_Object = MibTableColumn
mgwTo_14 = _MgwTo_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 3),
    _MgwTo_14_Type()
)
mgwTo_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwTo_14.setStatus("current")
_MgwMgwIndex_14_Type = OctetString
_MgwMgwIndex_14_Object = MibTableColumn
mgwMgwIndex_14 = _MgwMgwIndex_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 4),
    _MgwMgwIndex_14_Type()
)
mgwMgwIndex_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMgwIndex_14.setStatus("current")
_MgwMAC_14_Type = OctetString
_MgwMAC_14_Object = MibTableColumn
mgwMAC_14 = _MgwMAC_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 5),
    _MgwMAC_14_Type()
)
mgwMAC_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwMAC_14.setStatus("current")
_MgwName_14_Type = OctetString
_MgwName_14_Object = MibTableColumn
mgwName_14 = _MgwName_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 6),
    _MgwName_14_Type()
)
mgwName_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwName_14.setStatus("current")
_MgwOVL70_14_Type = OctetString
_MgwOVL70_14_Object = MibTableColumn
mgwOVL70_14 = _MgwOVL70_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 7),
    _MgwOVL70_14_Type()
)
mgwOVL70_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL70_14.setStatus("current")
_MgwOVL100_14_Type = OctetString
_MgwOVL100_14_Object = MibTableColumn
mgwOVL100_14 = _MgwOVL100_14_Object(
    (1, 3, 6, 1, 4, 1, 36378, 3, 1, 15, 1, 8),
    _MgwOVL100_14_Type()
)
mgwOVL100_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgwOVL100_14.setStatus("current")
_MgwTraps_ObjectIdentity = ObjectIdentity
mgwTraps = _MgwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 4)
)
_TrMgw_ObjectIdentity = ObjectIdentity
trMgw = _TrMgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36378, 4, 4)
)
_TrMgwIndex_Type = OctetString
_TrMgwIndex_Object = MibScalar
trMgwIndex = _TrMgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 36378, 4, 4, 1),
    _TrMgwIndex_Type()
)
trMgwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trMgwIndex.setStatus("current")
_TrMgwMAC_Type = OctetString
_TrMgwMAC_Object = MibScalar
trMgwMAC = _TrMgwMAC_Object(
    (1, 3, 6, 1, 4, 1, 36378, 4, 4, 2),
    _TrMgwMAC_Type()
)
trMgwMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trMgwMAC.setStatus("current")
_TrMgwName_Type = OctetString
_TrMgwName_Object = MibScalar
trMgwName = _TrMgwName_Object(
    (1, 3, 6, 1, 4, 1, 36378, 4, 4, 3),
    _TrMgwName_Type()
)
trMgwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trMgwName.setStatus("current")
_TrMgwEvent_Type = OctetString
_TrMgwEvent_Object = MibScalar
trMgwEvent = _TrMgwEvent_Object(
    (1, 3, 6, 1, 4, 1, 36378, 4, 4, 4),
    _TrMgwEvent_Type()
)
trMgwEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trMgwEvent.setStatus("current")

# Managed Objects groups


# Notification objects

trBsipOnlineState = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 2, 1)
)
trBsipOnlineState.setObjects(
      *(("HPCIP-MIB", "trBsipMAC"),
        ("HPCIP-MIB", "trBsipName"),
        ("HPCIP-MIB", "trBsipEvent"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trBsipOnlineState.setStatus(
        "current"
    )

trBsipSyncState = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 2, 2)
)
trBsipSyncState.setObjects(
      *(("HPCIP-MIB", "trBsipMAC"),
        ("HPCIP-MIB", "trBsipName"),
        ("HPCIP-MIB", "trBsipEvent"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trBsipSyncState.setStatus(
        "current"
    )

trBsip10Ovl100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 2, 3)
)
trBsip10Ovl100.setObjects(
      *(("HPCIP-MIB", "trBsipMAC"),
        ("HPCIP-MIB", "trBsipName"),
        ("HPCIP-MIB", "trBsipEvent"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trBsip10Ovl100.setStatus(
        "current"
    )

trMgwControlOnlineState = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 4, 1)
)
trMgwControlOnlineState.setObjects(
      *(("HPCIP-MIB", "trMgwIndex"),
        ("HPCIP-MIB", "trMgwMAC"),
        ("HPCIP-MIB", "trMgwName"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trMgwControlOnlineState.setStatus(
        "current"
    )

trMgwSignalOnlineState = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 4, 2)
)
trMgwSignalOnlineState.setObjects(
      *(("HPCIP-MIB", "trMgwIndex"),
        ("HPCIP-MIB", "trMgwMAC"),
        ("HPCIP-MIB", "trMgwName"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trMgwSignalOnlineState.setStatus(
        "current"
    )

trMgwOvl100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 36378, 4, 3)
)
trMgwOvl100.setObjects(
      *(("HPCIP-MIB", "trMgwIndex"),
        ("HPCIP-MIB", "trMgwMAC"),
        ("HPCIP-MIB", "trMgwName"),
        ("HPCIP-MIB", "trBsipSeverity"))
)
if mibBuilder.loadTexts:
    trMgwOvl100.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPCIP-MIB",
    **{"hpcipMib": hpcipMib,
       "bsipMibs": bsipMibs,
       "bsipStatistics": bsipStatistics,
       "bsipStatistics-Version": bsipStatistics_Version,
       "bsipStatistics-MgwIndex": bsipStatistics_MgwIndex,
       "bsipStatistics-01": bsipStatistics_01,
       "bsEntry01": bsEntry01,
       "bsIndex-01": bsIndex_01,
       "bsFrom-01": bsFrom_01,
       "bsTo-01": bsTo_01,
       "bsRPN-01": bsRPN_01,
       "bsMAC-01": bsMAC_01,
       "bsName-01": bsName_01,
       "bsOVL70-01": bsOVL70_01,
       "bsOVL100-01": bsOVL100_01,
       "bsRoaming-01": bsRoaming_01,
       "bsipStatistics-02": bsipStatistics_02,
       "bsEntry02": bsEntry02,
       "bsIndex-02": bsIndex_02,
       "bsFrom-02": bsFrom_02,
       "bsTo-02": bsTo_02,
       "bsRPN-02": bsRPN_02,
       "bsMAC-02": bsMAC_02,
       "bsName-02": bsName_02,
       "bsOVL70-02": bsOVL70_02,
       "bsOVL100-02": bsOVL100_02,
       "bsRoaming-02": bsRoaming_02,
       "bsipStatistics-03": bsipStatistics_03,
       "bsEntry03": bsEntry03,
       "bsIndex-03": bsIndex_03,
       "bsFrom-03": bsFrom_03,
       "bsTo-03": bsTo_03,
       "bsRPN-03": bsRPN_03,
       "bsMAC-03": bsMAC_03,
       "bsName-03": bsName_03,
       "bsOVL70-03": bsOVL70_03,
       "bsOVL100-03": bsOVL100_03,
       "bsRoaming-03": bsRoaming_03,
       "bsipStatistics-04": bsipStatistics_04,
       "bsEntry04": bsEntry04,
       "bsIndex-04": bsIndex_04,
       "bsFrom-04": bsFrom_04,
       "bsTo-04": bsTo_04,
       "bsRPN-04": bsRPN_04,
       "bsMAC-04": bsMAC_04,
       "bsName-04": bsName_04,
       "bsOVL70-04": bsOVL70_04,
       "bsOVL100-04": bsOVL100_04,
       "bsRoaming-04": bsRoaming_04,
       "bsipStatistics-05": bsipStatistics_05,
       "bsEntry05": bsEntry05,
       "bsIndex-05": bsIndex_05,
       "bsFrom-05": bsFrom_05,
       "bsTo-05": bsTo_05,
       "bsRPN-05": bsRPN_05,
       "bsMAC-05": bsMAC_05,
       "bsName-05": bsName_05,
       "bsOVL70-05": bsOVL70_05,
       "bsOVL100-05": bsOVL100_05,
       "bsRoaming-05": bsRoaming_05,
       "bsipStatistics-06": bsipStatistics_06,
       "bsEntry06": bsEntry06,
       "bsIndex-06": bsIndex_06,
       "bsFrom-06": bsFrom_06,
       "bsTo-06": bsTo_06,
       "bsRPN-06": bsRPN_06,
       "bsMAC-06": bsMAC_06,
       "bsName-06": bsName_06,
       "bsOVL70-06": bsOVL70_06,
       "bsOVL100-06": bsOVL100_06,
       "bsRoaming-06": bsRoaming_06,
       "bsipStatistics-07": bsipStatistics_07,
       "bsEntry07": bsEntry07,
       "bsIndex-07": bsIndex_07,
       "bsFrom-07": bsFrom_07,
       "bsTo-07": bsTo_07,
       "bsRPN-07": bsRPN_07,
       "bsMAC-07": bsMAC_07,
       "bsName-07": bsName_07,
       "bsOVL70-07": bsOVL70_07,
       "bsOVL100-07": bsOVL100_07,
       "bsRoaming-07": bsRoaming_07,
       "bsipStatistics-08": bsipStatistics_08,
       "bsEntry08": bsEntry08,
       "bsIndex-08": bsIndex_08,
       "bsFrom-08": bsFrom_08,
       "bsTo-08": bsTo_08,
       "bsRPN-08": bsRPN_08,
       "bsMAC-08": bsMAC_08,
       "bsName-08": bsName_08,
       "bsOVL70-08": bsOVL70_08,
       "bsOVL100-08": bsOVL100_08,
       "bsRoaming-08": bsRoaming_08,
       "bsipStatistics-09": bsipStatistics_09,
       "bsEntry09": bsEntry09,
       "bsIndex-09": bsIndex_09,
       "bsFrom-09": bsFrom_09,
       "bsTo-09": bsTo_09,
       "bsRPN-09": bsRPN_09,
       "bsMAC-09": bsMAC_09,
       "bsName-09": bsName_09,
       "bsOVL70-09": bsOVL70_09,
       "bsOVL100-09": bsOVL100_09,
       "bsRoaming-09": bsRoaming_09,
       "bsipStatistics-10": bsipStatistics_10,
       "bsEntry10": bsEntry10,
       "bsIndex-10": bsIndex_10,
       "bsFrom-10": bsFrom_10,
       "bsTo-10": bsTo_10,
       "bsRPN-10": bsRPN_10,
       "bsMAC-10": bsMAC_10,
       "bsName-10": bsName_10,
       "bsOVL70-10": bsOVL70_10,
       "bsOVL100-10": bsOVL100_10,
       "bsRoaming-10": bsRoaming_10,
       "bsipStatistics-11": bsipStatistics_11,
       "bsEntry11": bsEntry11,
       "bsIndex-11": bsIndex_11,
       "bsFrom-11": bsFrom_11,
       "bsTo-11": bsTo_11,
       "bsRPN-11": bsRPN_11,
       "bsMAC-11": bsMAC_11,
       "bsName-11": bsName_11,
       "bsOVL70-11": bsOVL70_11,
       "bsOVL100-11": bsOVL100_11,
       "bsRoaming-11": bsRoaming_11,
       "bsipStatistics-12": bsipStatistics_12,
       "bsEntry12": bsEntry12,
       "bsIndex-12": bsIndex_12,
       "bsFrom-12": bsFrom_12,
       "bsTo-12": bsTo_12,
       "bsRPN-12": bsRPN_12,
       "bsMAC-12": bsMAC_12,
       "bsName-12": bsName_12,
       "bsOVL70-12": bsOVL70_12,
       "bsOVL100-12": bsOVL100_12,
       "bsRoaming-12": bsRoaming_12,
       "bsipStatistics-13": bsipStatistics_13,
       "bsEntry13": bsEntry13,
       "bsIndex-13": bsIndex_13,
       "bsFrom-13": bsFrom_13,
       "bsTo-13": bsTo_13,
       "bsRPN-13": bsRPN_13,
       "bsMAC-13": bsMAC_13,
       "bsName-13": bsName_13,
       "bsOVL70-13": bsOVL70_13,
       "bsOVL100-13": bsOVL100_13,
       "bsRoaming-13": bsRoaming_13,
       "bsipStatistics-14": bsipStatistics_14,
       "bsEntry14": bsEntry14,
       "bsIndex-14": bsIndex_14,
       "bsFrom-14": bsFrom_14,
       "bsTo-14": bsTo_14,
       "bsRPN-14": bsRPN_14,
       "bsMAC-14": bsMAC_14,
       "bsName-14": bsName_14,
       "bsOVL70-14": bsOVL70_14,
       "bsOVL100-14": bsOVL100_14,
       "bsRoaming-14": bsRoaming_14,
       "bsipTraps": bsipTraps,
       "trBsipOnlineState": trBsipOnlineState,
       "trBsipSyncState": trBsipSyncState,
       "trBsip10Ovl100": trBsip10Ovl100,
       "trBsip": trBsip,
       "trBsipMAC": trBsipMAC,
       "trBsipName": trBsipName,
       "trBsipEvent": trBsipEvent,
       "trBsipSeverity": trBsipSeverity,
       "mgwMibs": mgwMibs,
       "mgwStatistics": mgwStatistics,
       "mgwStatistics-Version": mgwStatistics_Version,
       "mgwStatistics-01": mgwStatistics_01,
       "mgwEntry01": mgwEntry01,
       "mgwIndex-01": mgwIndex_01,
       "mgwFrom-01": mgwFrom_01,
       "mgwTo-01": mgwTo_01,
       "mgwMgwIndex-01": mgwMgwIndex_01,
       "mgwMAC-01": mgwMAC_01,
       "mgwName-01": mgwName_01,
       "mgwOVL70-01": mgwOVL70_01,
       "mgwOVL100-01": mgwOVL100_01,
       "mgwStatistics-02": mgwStatistics_02,
       "mgwEntry02": mgwEntry02,
       "mgwIndex-02": mgwIndex_02,
       "mgwFrom-02": mgwFrom_02,
       "mgwTo-02": mgwTo_02,
       "mgwMgwIndex-02": mgwMgwIndex_02,
       "mgwMAC-02": mgwMAC_02,
       "mgwName-02": mgwName_02,
       "mgwOVL70-02": mgwOVL70_02,
       "mgwOVL100-02": mgwOVL100_02,
       "mgwStatistics-03": mgwStatistics_03,
       "mgwEntry03": mgwEntry03,
       "mgwIndex-03": mgwIndex_03,
       "mgwFrom-03": mgwFrom_03,
       "mgwTo-03": mgwTo_03,
       "mgwMgwIndex-03": mgwMgwIndex_03,
       "mgwMAC-03": mgwMAC_03,
       "mgwName-03": mgwName_03,
       "mgwOVL70-03": mgwOVL70_03,
       "mgwOVL100-03": mgwOVL100_03,
       "mgwStatistics-04": mgwStatistics_04,
       "mgwEntry04": mgwEntry04,
       "mgwIndex-04": mgwIndex_04,
       "mgwFrom-04": mgwFrom_04,
       "mgwTo-04": mgwTo_04,
       "mgwMgwIndex-04": mgwMgwIndex_04,
       "mgwMAC-04": mgwMAC_04,
       "mgwName-04": mgwName_04,
       "mgwOVL70-04": mgwOVL70_04,
       "mgwOVL100-04": mgwOVL100_04,
       "mgwStatistics-05": mgwStatistics_05,
       "mgwEntry05": mgwEntry05,
       "mgwIndex-05": mgwIndex_05,
       "mgwFrom-05": mgwFrom_05,
       "mgwTo-05": mgwTo_05,
       "mgwMgwIndex-05": mgwMgwIndex_05,
       "mgwMAC-05": mgwMAC_05,
       "mgwName-05": mgwName_05,
       "mgwOVL70-05": mgwOVL70_05,
       "mgwOVL100-05": mgwOVL100_05,
       "mgwStatistics-06": mgwStatistics_06,
       "mgwEntry06": mgwEntry06,
       "mgwIndex-06": mgwIndex_06,
       "mgwFrom-06": mgwFrom_06,
       "mgwTo-06": mgwTo_06,
       "mgwMgwIndex-06": mgwMgwIndex_06,
       "mgwMAC-06": mgwMAC_06,
       "mgwName-06": mgwName_06,
       "mgwOVL70-06": mgwOVL70_06,
       "mgwOVL100-06": mgwOVL100_06,
       "mgwStatistics-07": mgwStatistics_07,
       "mgwEntry07": mgwEntry07,
       "mgwIndex-07": mgwIndex_07,
       "mgwFrom-07": mgwFrom_07,
       "mgwTo-07": mgwTo_07,
       "mgwMgwIndex-07": mgwMgwIndex_07,
       "mgwMAC-07": mgwMAC_07,
       "mgwName-07": mgwName_07,
       "mgwOVL70-07": mgwOVL70_07,
       "mgwOVL100-07": mgwOVL100_07,
       "mgwStatistics-08": mgwStatistics_08,
       "mgwEntry08": mgwEntry08,
       "mgwIndex-08": mgwIndex_08,
       "mgwFrom-08": mgwFrom_08,
       "mgwTo-08": mgwTo_08,
       "mgwMgwIndex-08": mgwMgwIndex_08,
       "mgwMAC-08": mgwMAC_08,
       "mgwName-08": mgwName_08,
       "mgwOVL70-08": mgwOVL70_08,
       "mgwOVL100-08": mgwOVL100_08,
       "mgwStatistics-09": mgwStatistics_09,
       "mgwEntry09": mgwEntry09,
       "mgwIndex-09": mgwIndex_09,
       "mgwFrom-09": mgwFrom_09,
       "mgwTo-09": mgwTo_09,
       "mgwMgwIndex-09": mgwMgwIndex_09,
       "mgwMAC-09": mgwMAC_09,
       "mgwName-09": mgwName_09,
       "mgwOVL70-09": mgwOVL70_09,
       "mgwOVL100-09": mgwOVL100_09,
       "mgwStatistics-10": mgwStatistics_10,
       "mgwEntry10": mgwEntry10,
       "mgwIndex-10": mgwIndex_10,
       "mgwFrom-10": mgwFrom_10,
       "mgwTo-10": mgwTo_10,
       "mgwMgwIndex-10": mgwMgwIndex_10,
       "mgwMAC-10": mgwMAC_10,
       "mgwName-10": mgwName_10,
       "mgwOVL70-10": mgwOVL70_10,
       "mgwOVL100-10": mgwOVL100_10,
       "mgwStatistics-11": mgwStatistics_11,
       "mgwEntry11": mgwEntry11,
       "mgwIndex-11": mgwIndex_11,
       "mgwFrom-11": mgwFrom_11,
       "mgwTo-11": mgwTo_11,
       "mgwMgwIndex-11": mgwMgwIndex_11,
       "mgwMAC-11": mgwMAC_11,
       "mgwName-11": mgwName_11,
       "mgwOVL70-11": mgwOVL70_11,
       "mgwOVL100-11": mgwOVL100_11,
       "mgwStatistics-12": mgwStatistics_12,
       "mgwEntry12": mgwEntry12,
       "mgwIndex-12": mgwIndex_12,
       "mgwFrom-12": mgwFrom_12,
       "mgwTo-12": mgwTo_12,
       "mgwMgwIndex-12": mgwMgwIndex_12,
       "mgwMAC-12": mgwMAC_12,
       "mgwName-12": mgwName_12,
       "mgwOVL70-12": mgwOVL70_12,
       "mgwOVL100-12": mgwOVL100_12,
       "mgwStatistics-13": mgwStatistics_13,
       "mgwEntry13": mgwEntry13,
       "mgwIndex-13": mgwIndex_13,
       "mgwFrom-13": mgwFrom_13,
       "mgwTo-13": mgwTo_13,
       "mgwMgwIndex-13": mgwMgwIndex_13,
       "mgwMAC-13": mgwMAC_13,
       "mgwName-13": mgwName_13,
       "mgwOVL70-13": mgwOVL70_13,
       "mgwOVL100-13": mgwOVL100_13,
       "mgwStatistics-14": mgwStatistics_14,
       "mgwEntry14": mgwEntry14,
       "mgwIndex-14": mgwIndex_14,
       "mgwFrom-14": mgwFrom_14,
       "mgwTo-14": mgwTo_14,
       "mgwMgwIndex-14": mgwMgwIndex_14,
       "mgwMAC-14": mgwMAC_14,
       "mgwName-14": mgwName_14,
       "mgwOVL70-14": mgwOVL70_14,
       "mgwOVL100-14": mgwOVL100_14,
       "mgwTraps": mgwTraps,
       "trMgwControlOnlineState": trMgwControlOnlineState,
       "trMgwSignalOnlineState": trMgwSignalOnlineState,
       "trMgwOvl100": trMgwOvl100,
       "trMgw": trMgw,
       "trMgwIndex": trMgwIndex,
       "trMgwMAC": trMgwMAC,
       "trMgwName": trMgwName,
       "trMgwEvent": trMgwEvent}
)
