# SNMP MIB module (RUIJIE-AC-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AC-DOT11-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:22 2025
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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieAcDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65)
)
if mibBuilder.loadTexts:
    ruijieAcDot11MIB.setRevisions(
        ("2009-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAcDot11MIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcDot11MIBObjects = _RuijieAcDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1)
)
_RuijieAcDot11LinkTestStaTable_Object = MibTable
ruijieAcDot11LinkTestStaTable = _RuijieAcDot11LinkTestStaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieAcDot11LinkTestStaTable.setStatus("current")
_RuijieAcDot11LinkTestStaEntry_Object = MibTableRow
ruijieAcDot11LinkTestStaEntry = _RuijieAcDot11LinkTestStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 1, 1)
)
ruijieAcDot11LinkTestStaEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieAcDot11LinkMac"),
)
if mibBuilder.loadTexts:
    ruijieAcDot11LinkTestStaEntry.setStatus("current")
_RuijieAcDot11LinkMac_Type = MacAddress
_RuijieAcDot11LinkMac_Object = MibTableColumn
ruijieAcDot11LinkMac = _RuijieAcDot11LinkMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 1, 1, 1),
    _RuijieAcDot11LinkMac_Type()
)
ruijieAcDot11LinkMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAcDot11LinkMac.setStatus("current")


class _RuijieAcDot11Link_Type(DisplayString):
    """Custom type ruijieAcDot11Link based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAcDot11Link_Type.__name__ = "DisplayString"
_RuijieAcDot11Link_Object = MibTableColumn
ruijieAcDot11Link = _RuijieAcDot11Link_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 1, 1, 2),
    _RuijieAcDot11Link_Type()
)
ruijieAcDot11Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcDot11Link.setStatus("current")
_RuijieAcDot11ShowClientTable_Object = MibTable
ruijieAcDot11ShowClientTable = _RuijieAcDot11ShowClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieAcDot11ShowClientTable.setStatus("current")
_RuijieAcDot11ShowClientEntry_Object = MibTableRow
ruijieAcDot11ShowClientEntry = _RuijieAcDot11ShowClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 2, 1)
)
ruijieAcDot11ShowClientEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieAcDot11ClientMac"),
)
if mibBuilder.loadTexts:
    ruijieAcDot11ShowClientEntry.setStatus("current")
_RuijieAcDot11ClientMac_Type = MacAddress
_RuijieAcDot11ClientMac_Object = MibTableColumn
ruijieAcDot11ClientMac = _RuijieAcDot11ClientMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 2, 1, 1),
    _RuijieAcDot11ClientMac_Type()
)
ruijieAcDot11ClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAcDot11ClientMac.setStatus("current")


class _RuijieAcDot11Client_Type(DisplayString):
    """Custom type ruijieAcDot11Client based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAcDot11Client_Type.__name__ = "DisplayString"
_RuijieAcDot11Client_Object = MibTableColumn
ruijieAcDot11Client = _RuijieAcDot11Client_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 2, 1, 2),
    _RuijieAcDot11Client_Type()
)
ruijieAcDot11Client.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcDot11Client.setStatus("current")
_RuijieAcDot11AuthTimeout_Type = Integer32
_RuijieAcDot11AuthTimeout_Object = MibScalar
ruijieAcDot11AuthTimeout = _RuijieAcDot11AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 3),
    _RuijieAcDot11AuthTimeout_Type()
)
ruijieAcDot11AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcDot11AuthTimeout.setStatus("current")
_RuijieAcDot11CountryTable_Object = MibTable
ruijieAcDot11CountryTable = _RuijieAcDot11CountryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieAcDot11CountryTable.setStatus("current")
_RuijieAcDot11CountryEntry_Object = MibTableRow
ruijieAcDot11CountryEntry = _RuijieAcDot11CountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 4, 1)
)
ruijieAcDot11CountryEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieAcDot11CountryNum"),
)
if mibBuilder.loadTexts:
    ruijieAcDot11CountryEntry.setStatus("current")
_RuijieAcDot11CountryNum_Type = Integer32
_RuijieAcDot11CountryNum_Object = MibTableColumn
ruijieAcDot11CountryNum = _RuijieAcDot11CountryNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 4, 1, 1),
    _RuijieAcDot11CountryNum_Type()
)
ruijieAcDot11CountryNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAcDot11CountryNum.setStatus("current")


class _RuijieAcDot11Country_Type(DisplayString):
    """Custom type ruijieAcDot11Country based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_RuijieAcDot11Country_Type.__name__ = "DisplayString"
_RuijieAcDot11Country_Object = MibTableColumn
ruijieAcDot11Country = _RuijieAcDot11Country_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 4, 1, 2),
    _RuijieAcDot11Country_Type()
)
ruijieAcDot11Country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcDot11Country.setStatus("current")
_RuijieAcDot11CountryEnable_Type = TruthValue
_RuijieAcDot11CountryEnable_Object = MibTableColumn
ruijieAcDot11CountryEnable = _RuijieAcDot11CountryEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 4, 1, 3),
    _RuijieAcDot11CountryEnable_Type()
)
ruijieAcDot11CountryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcDot11CountryEnable.setStatus("current")


class _RuijieNetDot11AEnable_Type(TruthValue):
    """Custom type ruijieNetDot11AEnable based on TruthValue"""
    defaultValue = 1


_RuijieNetDot11AEnable_Type.__name__ = "TruthValue"
_RuijieNetDot11AEnable_Object = MibScalar
ruijieNetDot11AEnable = _RuijieNetDot11AEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 5),
    _RuijieNetDot11AEnable_Type()
)
ruijieNetDot11AEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AEnable.setStatus("current")
_RuijieNetDot11AMCS0_Type = TruthValue
_RuijieNetDot11AMCS0_Object = MibScalar
ruijieNetDot11AMCS0 = _RuijieNetDot11AMCS0_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 6),
    _RuijieNetDot11AMCS0_Type()
)
ruijieNetDot11AMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS0.setStatus("current")
_RuijieNetDot11AMCS1_Type = TruthValue
_RuijieNetDot11AMCS1_Object = MibScalar
ruijieNetDot11AMCS1 = _RuijieNetDot11AMCS1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 7),
    _RuijieNetDot11AMCS1_Type()
)
ruijieNetDot11AMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS1.setStatus("current")
_RuijieNetDot11AMCS2_Type = TruthValue
_RuijieNetDot11AMCS2_Object = MibScalar
ruijieNetDot11AMCS2 = _RuijieNetDot11AMCS2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 8),
    _RuijieNetDot11AMCS2_Type()
)
ruijieNetDot11AMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS2.setStatus("current")
_RuijieNetDot11AMCS3_Type = TruthValue
_RuijieNetDot11AMCS3_Object = MibScalar
ruijieNetDot11AMCS3 = _RuijieNetDot11AMCS3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 9),
    _RuijieNetDot11AMCS3_Type()
)
ruijieNetDot11AMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS3.setStatus("current")
_RuijieNetDot11AMCS4_Type = TruthValue
_RuijieNetDot11AMCS4_Object = MibScalar
ruijieNetDot11AMCS4 = _RuijieNetDot11AMCS4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 10),
    _RuijieNetDot11AMCS4_Type()
)
ruijieNetDot11AMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS4.setStatus("current")
_RuijieNetDot11AMCS5_Type = TruthValue
_RuijieNetDot11AMCS5_Object = MibScalar
ruijieNetDot11AMCS5 = _RuijieNetDot11AMCS5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 11),
    _RuijieNetDot11AMCS5_Type()
)
ruijieNetDot11AMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS5.setStatus("current")
_RuijieNetDot11AMCS6_Type = TruthValue
_RuijieNetDot11AMCS6_Object = MibScalar
ruijieNetDot11AMCS6 = _RuijieNetDot11AMCS6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 12),
    _RuijieNetDot11AMCS6_Type()
)
ruijieNetDot11AMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS6.setStatus("current")
_RuijieNetDot11AMCS7_Type = TruthValue
_RuijieNetDot11AMCS7_Object = MibScalar
ruijieNetDot11AMCS7 = _RuijieNetDot11AMCS7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 13),
    _RuijieNetDot11AMCS7_Type()
)
ruijieNetDot11AMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS7.setStatus("current")
_RuijieNetDot11AMCS8_Type = TruthValue
_RuijieNetDot11AMCS8_Object = MibScalar
ruijieNetDot11AMCS8 = _RuijieNetDot11AMCS8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 14),
    _RuijieNetDot11AMCS8_Type()
)
ruijieNetDot11AMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS8.setStatus("current")
_RuijieNetDot11AMCS9_Type = TruthValue
_RuijieNetDot11AMCS9_Object = MibScalar
ruijieNetDot11AMCS9 = _RuijieNetDot11AMCS9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 15),
    _RuijieNetDot11AMCS9_Type()
)
ruijieNetDot11AMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS9.setStatus("current")
_RuijieNetDot11AMCS10_Type = TruthValue
_RuijieNetDot11AMCS10_Object = MibScalar
ruijieNetDot11AMCS10 = _RuijieNetDot11AMCS10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 16),
    _RuijieNetDot11AMCS10_Type()
)
ruijieNetDot11AMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS10.setStatus("current")
_RuijieNetDot11AMCS11_Type = TruthValue
_RuijieNetDot11AMCS11_Object = MibScalar
ruijieNetDot11AMCS11 = _RuijieNetDot11AMCS11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 17),
    _RuijieNetDot11AMCS11_Type()
)
ruijieNetDot11AMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS11.setStatus("current")
_RuijieNetDot11AMCS12_Type = TruthValue
_RuijieNetDot11AMCS12_Object = MibScalar
ruijieNetDot11AMCS12 = _RuijieNetDot11AMCS12_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 18),
    _RuijieNetDot11AMCS12_Type()
)
ruijieNetDot11AMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS12.setStatus("current")
_RuijieNetDot11AMCS13_Type = TruthValue
_RuijieNetDot11AMCS13_Object = MibScalar
ruijieNetDot11AMCS13 = _RuijieNetDot11AMCS13_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 19),
    _RuijieNetDot11AMCS13_Type()
)
ruijieNetDot11AMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS13.setStatus("current")
_RuijieNetDot11AMCS14_Type = TruthValue
_RuijieNetDot11AMCS14_Object = MibScalar
ruijieNetDot11AMCS14 = _RuijieNetDot11AMCS14_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 20),
    _RuijieNetDot11AMCS14_Type()
)
ruijieNetDot11AMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS14.setStatus("current")
_RuijieNetDot11AMCS15_Type = TruthValue
_RuijieNetDot11AMCS15_Object = MibScalar
ruijieNetDot11AMCS15 = _RuijieNetDot11AMCS15_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 21),
    _RuijieNetDot11AMCS15_Type()
)
ruijieNetDot11AMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AMCS15.setStatus("current")


class _RuijieNetDot11AAMPDU_Type(Integer32):
    """Custom type ruijieNetDot11AAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieNetDot11AAMPDU_Type.__name__ = "Integer32"
_RuijieNetDot11AAMPDU_Object = MibScalar
ruijieNetDot11AAMPDU = _RuijieNetDot11AAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 22),
    _RuijieNetDot11AAMPDU_Type()
)
ruijieNetDot11AAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AAMPDU.setStatus("current")


class _RuijieNetDot11BEnable_Type(TruthValue):
    """Custom type ruijieNetDot11BEnable based on TruthValue"""
    defaultValue = 1


_RuijieNetDot11BEnable_Type.__name__ = "TruthValue"
_RuijieNetDot11BEnable_Object = MibScalar
ruijieNetDot11BEnable = _RuijieNetDot11BEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 23),
    _RuijieNetDot11BEnable_Type()
)
ruijieNetDot11BEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BEnable.setStatus("current")


class _RuijieNetDot11BMCS0_Type(Integer32):
    """Custom type ruijieNetDot11BMCS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS0_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS0_Object = MibScalar
ruijieNetDot11BMCS0 = _RuijieNetDot11BMCS0_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 24),
    _RuijieNetDot11BMCS0_Type()
)
ruijieNetDot11BMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS0.setStatus("current")


class _RuijieNetDot11BMCS1_Type(Integer32):
    """Custom type ruijieNetDot11BMCS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS1_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS1_Object = MibScalar
ruijieNetDot11BMCS1 = _RuijieNetDot11BMCS1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 25),
    _RuijieNetDot11BMCS1_Type()
)
ruijieNetDot11BMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS1.setStatus("current")


class _RuijieNetDot11BMCS2_Type(Integer32):
    """Custom type ruijieNetDot11BMCS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS2_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS2_Object = MibScalar
ruijieNetDot11BMCS2 = _RuijieNetDot11BMCS2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 26),
    _RuijieNetDot11BMCS2_Type()
)
ruijieNetDot11BMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS2.setStatus("current")


class _RuijieNetDot11BMCS3_Type(Integer32):
    """Custom type ruijieNetDot11BMCS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS3_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS3_Object = MibScalar
ruijieNetDot11BMCS3 = _RuijieNetDot11BMCS3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 27),
    _RuijieNetDot11BMCS3_Type()
)
ruijieNetDot11BMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS3.setStatus("current")


class _RuijieNetDot11BMCS4_Type(Integer32):
    """Custom type ruijieNetDot11BMCS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS4_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS4_Object = MibScalar
ruijieNetDot11BMCS4 = _RuijieNetDot11BMCS4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 28),
    _RuijieNetDot11BMCS4_Type()
)
ruijieNetDot11BMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS4.setStatus("current")


class _RuijieNetDot11BMCS5_Type(Integer32):
    """Custom type ruijieNetDot11BMCS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS5_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS5_Object = MibScalar
ruijieNetDot11BMCS5 = _RuijieNetDot11BMCS5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 29),
    _RuijieNetDot11BMCS5_Type()
)
ruijieNetDot11BMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS5.setStatus("current")


class _RuijieNetDot11BMCS6_Type(Integer32):
    """Custom type ruijieNetDot11BMCS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS6_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS6_Object = MibScalar
ruijieNetDot11BMCS6 = _RuijieNetDot11BMCS6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 30),
    _RuijieNetDot11BMCS6_Type()
)
ruijieNetDot11BMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS6.setStatus("current")


class _RuijieNetDot11BMCS7_Type(Integer32):
    """Custom type ruijieNetDot11BMCS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS7_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS7_Object = MibScalar
ruijieNetDot11BMCS7 = _RuijieNetDot11BMCS7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 31),
    _RuijieNetDot11BMCS7_Type()
)
ruijieNetDot11BMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS7.setStatus("current")


class _RuijieNetDot11BMCS8_Type(Integer32):
    """Custom type ruijieNetDot11BMCS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS8_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS8_Object = MibScalar
ruijieNetDot11BMCS8 = _RuijieNetDot11BMCS8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 32),
    _RuijieNetDot11BMCS8_Type()
)
ruijieNetDot11BMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS8.setStatus("current")


class _RuijieNetDot11BMCS9_Type(Integer32):
    """Custom type ruijieNetDot11BMCS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS9_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS9_Object = MibScalar
ruijieNetDot11BMCS9 = _RuijieNetDot11BMCS9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 33),
    _RuijieNetDot11BMCS9_Type()
)
ruijieNetDot11BMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS9.setStatus("current")


class _RuijieNetDot11BMCS10_Type(Integer32):
    """Custom type ruijieNetDot11BMCS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS10_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS10_Object = MibScalar
ruijieNetDot11BMCS10 = _RuijieNetDot11BMCS10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 34),
    _RuijieNetDot11BMCS10_Type()
)
ruijieNetDot11BMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS10.setStatus("current")


class _RuijieNetDot11BMCS11_Type(Integer32):
    """Custom type ruijieNetDot11BMCS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS11_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS11_Object = MibScalar
ruijieNetDot11BMCS11 = _RuijieNetDot11BMCS11_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 35),
    _RuijieNetDot11BMCS11_Type()
)
ruijieNetDot11BMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS11.setStatus("current")


class _RuijieNetDot11BMCS12_Type(Integer32):
    """Custom type ruijieNetDot11BMCS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS12_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS12_Object = MibScalar
ruijieNetDot11BMCS12 = _RuijieNetDot11BMCS12_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 36),
    _RuijieNetDot11BMCS12_Type()
)
ruijieNetDot11BMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS12.setStatus("current")


class _RuijieNetDot11BMCS13_Type(Integer32):
    """Custom type ruijieNetDot11BMCS13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS13_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS13_Object = MibScalar
ruijieNetDot11BMCS13 = _RuijieNetDot11BMCS13_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 37),
    _RuijieNetDot11BMCS13_Type()
)
ruijieNetDot11BMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS13.setStatus("current")


class _RuijieNetDot11BMCS14_Type(Integer32):
    """Custom type ruijieNetDot11BMCS14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS14_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS14_Object = MibScalar
ruijieNetDot11BMCS14 = _RuijieNetDot11BMCS14_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 38),
    _RuijieNetDot11BMCS14_Type()
)
ruijieNetDot11BMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS14.setStatus("current")


class _RuijieNetDot11BMCS15_Type(Integer32):
    """Custom type ruijieNetDot11BMCS15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RuijieNetDot11BMCS15_Type.__name__ = "Integer32"
_RuijieNetDot11BMCS15_Object = MibScalar
ruijieNetDot11BMCS15 = _RuijieNetDot11BMCS15_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 39),
    _RuijieNetDot11BMCS15_Type()
)
ruijieNetDot11BMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BMCS15.setStatus("current")


class _RuijieNetDot11BAMPDU_Type(Integer32):
    """Custom type ruijieNetDot11BAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieNetDot11BAMPDU_Type.__name__ = "Integer32"
_RuijieNetDot11BAMPDU_Object = MibScalar
ruijieNetDot11BAMPDU = _RuijieNetDot11BAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 40),
    _RuijieNetDot11BAMPDU_Type()
)
ruijieNetDot11BAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BAMPDU.setStatus("current")


class _RuijieNetDot11AGEnable_Type(TruthValue):
    """Custom type ruijieNetDot11AGEnable based on TruthValue"""
    defaultValue = 1


_RuijieNetDot11AGEnable_Type.__name__ = "TruthValue"
_RuijieNetDot11AGEnable_Object = MibScalar
ruijieNetDot11AGEnable = _RuijieNetDot11AGEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 41),
    _RuijieNetDot11AGEnable_Type()
)
ruijieNetDot11AGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11AGEnable.setStatus("current")


class _RuijieNetDot11BGEnable_Type(TruthValue):
    """Custom type ruijieNetDot11BGEnable based on TruthValue"""
    defaultValue = 1


_RuijieNetDot11BGEnable_Type.__name__ = "TruthValue"
_RuijieNetDot11BGEnable_Object = MibScalar
ruijieNetDot11BGEnable = _RuijieNetDot11BGEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 1, 42),
    _RuijieNetDot11BGEnable_Type()
)
ruijieNetDot11BGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieNetDot11BGEnable.setStatus("current")
_RuijieApDot11MIBObjects_ObjectIdentity = ObjectIdentity
ruijieApDot11MIBObjects = _RuijieApDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2)
)
_RuijieApDot11PoeTable_Object = MibTable
ruijieApDot11PoeTable = _RuijieApDot11PoeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieApDot11PoeTable.setStatus("current")
_RuijieApDot11PoeEntry_Object = MibTableRow
ruijieApDot11PoeEntry = _RuijieApDot11PoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 1, 1)
)
ruijieApDot11PoeEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieApDot11PoeAPID"),
)
if mibBuilder.loadTexts:
    ruijieApDot11PoeEntry.setStatus("current")
_RuijieApDot11PoeAPID_Type = TruthValue
_RuijieApDot11PoeAPID_Object = MibTableColumn
ruijieApDot11PoeAPID = _RuijieApDot11PoeAPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 1, 1, 1),
    _RuijieApDot11PoeAPID_Type()
)
ruijieApDot11PoeAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApDot11PoeAPID.setStatus("current")
_RuijieApDot11PoeEnable_Type = TruthValue
_RuijieApDot11PoeEnable_Object = MibTableColumn
ruijieApDot11PoeEnable = _RuijieApDot11PoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 1, 1, 2),
    _RuijieApDot11PoeEnable_Type()
)
ruijieApDot11PoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11PoeEnable.setStatus("current")
_RuijieApDot11ChannelTable_Object = MibTable
ruijieApDot11ChannelTable = _RuijieApDot11ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieApDot11ChannelTable.setStatus("current")
_RuijieApDot11ChannelEntry_Object = MibTableRow
ruijieApDot11ChannelEntry = _RuijieApDot11ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 2, 1)
)
ruijieApDot11ChannelEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieApDot11ChannelAPID"),
)
if mibBuilder.loadTexts:
    ruijieApDot11ChannelEntry.setStatus("current")
_RuijieApDot11ChannelAPID_Type = Integer32
_RuijieApDot11ChannelAPID_Object = MibTableColumn
ruijieApDot11ChannelAPID = _RuijieApDot11ChannelAPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 2, 1, 1),
    _RuijieApDot11ChannelAPID_Type()
)
ruijieApDot11ChannelAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApDot11ChannelAPID.setStatus("current")


class _RuijieApDot11ChannelWidthA_Type(Integer32):
    """Custom type ruijieApDot11ChannelWidthA based on Integer32"""
    defaultValue = 20


_RuijieApDot11ChannelWidthA_Type.__name__ = "Integer32"
_RuijieApDot11ChannelWidthA_Object = MibTableColumn
ruijieApDot11ChannelWidthA = _RuijieApDot11ChannelWidthA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 2, 1, 2),
    _RuijieApDot11ChannelWidthA_Type()
)
ruijieApDot11ChannelWidthA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11ChannelWidthA.setStatus("current")


class _RuijieApDot11ChannelWidthB_Type(Integer32):
    """Custom type ruijieApDot11ChannelWidthB based on Integer32"""
    defaultValue = 20


_RuijieApDot11ChannelWidthB_Type.__name__ = "Integer32"
_RuijieApDot11ChannelWidthB_Object = MibTableColumn
ruijieApDot11ChannelWidthB = _RuijieApDot11ChannelWidthB_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 2, 1, 3),
    _RuijieApDot11ChannelWidthB_Type()
)
ruijieApDot11ChannelWidthB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11ChannelWidthB.setStatus("current")
_RuijieApDot11AntenneTable_Object = MibTable
ruijieApDot11AntenneTable = _RuijieApDot11AntenneTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieApDot11AntenneTable.setStatus("current")
_RuijieApDot11AntenneEntry_Object = MibTableRow
ruijieApDot11AntenneEntry = _RuijieApDot11AntenneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1)
)
ruijieApDot11AntenneEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieApDot11AntenneAPID"),
)
if mibBuilder.loadTexts:
    ruijieApDot11AntenneEntry.setStatus("current")
_RuijieApDot11AntenneAPID_Type = Integer32
_RuijieApDot11AntenneAPID_Object = MibTableColumn
ruijieApDot11AntenneAPID = _RuijieApDot11AntenneAPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1, 1),
    _RuijieApDot11AntenneAPID_Type()
)
ruijieApDot11AntenneAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApDot11AntenneAPID.setStatus("current")


class _RuijieApDot11AntenneRxA_Type(Integer32):
    """Custom type ruijieApDot11AntenneRxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieApDot11AntenneRxA_Type.__name__ = "Integer32"
_RuijieApDot11AntenneRxA_Object = MibTableColumn
ruijieApDot11AntenneRxA = _RuijieApDot11AntenneRxA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1, 2),
    _RuijieApDot11AntenneRxA_Type()
)
ruijieApDot11AntenneRxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11AntenneRxA.setStatus("current")


class _RuijieApDot11AntenneTxA_Type(Integer32):
    """Custom type ruijieApDot11AntenneTxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieApDot11AntenneTxA_Type.__name__ = "Integer32"
_RuijieApDot11AntenneTxA_Object = MibTableColumn
ruijieApDot11AntenneTxA = _RuijieApDot11AntenneTxA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1, 3),
    _RuijieApDot11AntenneTxA_Type()
)
ruijieApDot11AntenneTxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11AntenneTxA.setStatus("current")


class _RuijieApDot11AntenneRxB_Type(Integer32):
    """Custom type ruijieApDot11AntenneRxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieApDot11AntenneRxB_Type.__name__ = "Integer32"
_RuijieApDot11AntenneRxB_Object = MibTableColumn
ruijieApDot11AntenneRxB = _RuijieApDot11AntenneRxB_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1, 4),
    _RuijieApDot11AntenneRxB_Type()
)
ruijieApDot11AntenneRxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11AntenneRxB.setStatus("current")


class _RuijieApDot11AntenneTxB_Type(Integer32):
    """Custom type ruijieApDot11AntenneTxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RuijieApDot11AntenneTxB_Type.__name__ = "Integer32"
_RuijieApDot11AntenneTxB_Object = MibTableColumn
ruijieApDot11AntenneTxB = _RuijieApDot11AntenneTxB_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 2, 3, 1, 5),
    _RuijieApDot11AntenneTxB_Type()
)
ruijieApDot11AntenneTxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDot11AntenneTxB.setStatus("current")
_RuijieWlanDot11MIBObjects_ObjectIdentity = ObjectIdentity
ruijieWlanDot11MIBObjects = _RuijieWlanDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3)
)
_RuijieWlanDot11LoadTable_Object = MibTable
ruijieWlanDot11LoadTable = _RuijieWlanDot11LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieWlanDot11LoadTable.setStatus("current")
_RuijieWlanDot11LoadTEntry_Object = MibTableRow
ruijieWlanDot11LoadTEntry = _RuijieWlanDot11LoadTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1, 1)
)
ruijieWlanDot11LoadTEntry.setIndexNames(
    (0, "RUIJIE-AC-DOT11-MIB", "ruijieWlanDot11WlanId"),
)
if mibBuilder.loadTexts:
    ruijieWlanDot11LoadTEntry.setStatus("current")
_RuijieWlanDot11WlanId_Type = Integer32
_RuijieWlanDot11WlanId_Object = MibTableColumn
ruijieWlanDot11WlanId = _RuijieWlanDot11WlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1, 1, 1),
    _RuijieWlanDot11WlanId_Type()
)
ruijieWlanDot11WlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieWlanDot11WlanId.setStatus("current")


class _RuijieWlanDot11Enable_Type(TruthValue):
    """Custom type ruijieWlanDot11Enable based on TruthValue"""
    defaultValue = 2


_RuijieWlanDot11Enable_Type.__name__ = "TruthValue"
_RuijieWlanDot11Enable_Object = MibTableColumn
ruijieWlanDot11Enable = _RuijieWlanDot11Enable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1, 1, 2),
    _RuijieWlanDot11Enable_Type()
)
ruijieWlanDot11Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanDot11Enable.setStatus("current")


class _RuijieWlanDot11Window_Type(Integer32):
    """Custom type ruijieWlanDot11Window based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_RuijieWlanDot11Window_Type.__name__ = "Integer32"
_RuijieWlanDot11Window_Object = MibTableColumn
ruijieWlanDot11Window = _RuijieWlanDot11Window_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1, 1, 3),
    _RuijieWlanDot11Window_Type()
)
ruijieWlanDot11Window.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanDot11Window.setStatus("current")


class _RuijieWlanDot11Flow_Type(Integer32):
    """Custom type ruijieWlanDot11Flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 130),
    )


_RuijieWlanDot11Flow_Type.__name__ = "Integer32"
_RuijieWlanDot11Flow_Object = MibTableColumn
ruijieWlanDot11Flow = _RuijieWlanDot11Flow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 3, 1, 1, 4),
    _RuijieWlanDot11Flow_Type()
)
ruijieWlanDot11Flow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanDot11Flow.setStatus("current")
_RuijieAcDot11MIBConformance_ObjectIdentity = ObjectIdentity
ruijieAcDot11MIBConformance = _RuijieAcDot11MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 5)
)
_RuijieAcDot11MIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAcDot11MIBCompliances = _RuijieAcDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 5, 1)
)
_RuijieAcDot11MIBGroups_ObjectIdentity = ObjectIdentity
ruijieAcDot11MIBGroups = _RuijieAcDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 5, 2)
)

# Managed Objects groups

ruijieAcDot11MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 5, 2, 1)
)
ruijieAcDot11MIBGroup.setObjects(
      *(("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11Link"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11Client"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11AuthTimeout"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11Country"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11CountryEnable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11PoeEnable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11ChannelWidthA"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11ChannelWidthB"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11AntenneRxA"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11AntenneTxA"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11AntenneRxB"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieApDot11AntenneTxB"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieWlanDot11Enable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieWlanDot11Window"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieWlanDot11Flow"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AEnable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS0"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS1"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS2"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS3"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS4"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS5"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS6"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS7"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS8"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS9"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS10"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS11"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS12"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS13"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS14"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AMCS15"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AAMPDU"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BEnable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS0"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS1"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS2"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS3"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS4"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS5"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS6"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS7"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS8"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS9"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS10"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS11"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS12"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS13"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS14"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BMCS15"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BAMPDU"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11AGEnable"),
        ("RUIJIE-AC-DOT11-MIB", "ruijieNetDot11BGEnable"))
)
if mibBuilder.loadTexts:
    ruijieAcDot11MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAcDot11MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 65, 5, 1, 1)
)
ruijieAcDot11MIBCompliance.setObjects(
    ("RUIJIE-AC-DOT11-MIB", "ruijieAcDot11MIBGroup")
)
if mibBuilder.loadTexts:
    ruijieAcDot11MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AC-DOT11-MIB",
    **{"ruijieAcDot11MIB": ruijieAcDot11MIB,
       "ruijieAcDot11MIBObjects": ruijieAcDot11MIBObjects,
       "ruijieAcDot11LinkTestStaTable": ruijieAcDot11LinkTestStaTable,
       "ruijieAcDot11LinkTestStaEntry": ruijieAcDot11LinkTestStaEntry,
       "ruijieAcDot11LinkMac": ruijieAcDot11LinkMac,
       "ruijieAcDot11Link": ruijieAcDot11Link,
       "ruijieAcDot11ShowClientTable": ruijieAcDot11ShowClientTable,
       "ruijieAcDot11ShowClientEntry": ruijieAcDot11ShowClientEntry,
       "ruijieAcDot11ClientMac": ruijieAcDot11ClientMac,
       "ruijieAcDot11Client": ruijieAcDot11Client,
       "ruijieAcDot11AuthTimeout": ruijieAcDot11AuthTimeout,
       "ruijieAcDot11CountryTable": ruijieAcDot11CountryTable,
       "ruijieAcDot11CountryEntry": ruijieAcDot11CountryEntry,
       "ruijieAcDot11CountryNum": ruijieAcDot11CountryNum,
       "ruijieAcDot11Country": ruijieAcDot11Country,
       "ruijieAcDot11CountryEnable": ruijieAcDot11CountryEnable,
       "ruijieNetDot11AEnable": ruijieNetDot11AEnable,
       "ruijieNetDot11AMCS0": ruijieNetDot11AMCS0,
       "ruijieNetDot11AMCS1": ruijieNetDot11AMCS1,
       "ruijieNetDot11AMCS2": ruijieNetDot11AMCS2,
       "ruijieNetDot11AMCS3": ruijieNetDot11AMCS3,
       "ruijieNetDot11AMCS4": ruijieNetDot11AMCS4,
       "ruijieNetDot11AMCS5": ruijieNetDot11AMCS5,
       "ruijieNetDot11AMCS6": ruijieNetDot11AMCS6,
       "ruijieNetDot11AMCS7": ruijieNetDot11AMCS7,
       "ruijieNetDot11AMCS8": ruijieNetDot11AMCS8,
       "ruijieNetDot11AMCS9": ruijieNetDot11AMCS9,
       "ruijieNetDot11AMCS10": ruijieNetDot11AMCS10,
       "ruijieNetDot11AMCS11": ruijieNetDot11AMCS11,
       "ruijieNetDot11AMCS12": ruijieNetDot11AMCS12,
       "ruijieNetDot11AMCS13": ruijieNetDot11AMCS13,
       "ruijieNetDot11AMCS14": ruijieNetDot11AMCS14,
       "ruijieNetDot11AMCS15": ruijieNetDot11AMCS15,
       "ruijieNetDot11AAMPDU": ruijieNetDot11AAMPDU,
       "ruijieNetDot11BEnable": ruijieNetDot11BEnable,
       "ruijieNetDot11BMCS0": ruijieNetDot11BMCS0,
       "ruijieNetDot11BMCS1": ruijieNetDot11BMCS1,
       "ruijieNetDot11BMCS2": ruijieNetDot11BMCS2,
       "ruijieNetDot11BMCS3": ruijieNetDot11BMCS3,
       "ruijieNetDot11BMCS4": ruijieNetDot11BMCS4,
       "ruijieNetDot11BMCS5": ruijieNetDot11BMCS5,
       "ruijieNetDot11BMCS6": ruijieNetDot11BMCS6,
       "ruijieNetDot11BMCS7": ruijieNetDot11BMCS7,
       "ruijieNetDot11BMCS8": ruijieNetDot11BMCS8,
       "ruijieNetDot11BMCS9": ruijieNetDot11BMCS9,
       "ruijieNetDot11BMCS10": ruijieNetDot11BMCS10,
       "ruijieNetDot11BMCS11": ruijieNetDot11BMCS11,
       "ruijieNetDot11BMCS12": ruijieNetDot11BMCS12,
       "ruijieNetDot11BMCS13": ruijieNetDot11BMCS13,
       "ruijieNetDot11BMCS14": ruijieNetDot11BMCS14,
       "ruijieNetDot11BMCS15": ruijieNetDot11BMCS15,
       "ruijieNetDot11BAMPDU": ruijieNetDot11BAMPDU,
       "ruijieNetDot11AGEnable": ruijieNetDot11AGEnable,
       "ruijieNetDot11BGEnable": ruijieNetDot11BGEnable,
       "ruijieApDot11MIBObjects": ruijieApDot11MIBObjects,
       "ruijieApDot11PoeTable": ruijieApDot11PoeTable,
       "ruijieApDot11PoeEntry": ruijieApDot11PoeEntry,
       "ruijieApDot11PoeAPID": ruijieApDot11PoeAPID,
       "ruijieApDot11PoeEnable": ruijieApDot11PoeEnable,
       "ruijieApDot11ChannelTable": ruijieApDot11ChannelTable,
       "ruijieApDot11ChannelEntry": ruijieApDot11ChannelEntry,
       "ruijieApDot11ChannelAPID": ruijieApDot11ChannelAPID,
       "ruijieApDot11ChannelWidthA": ruijieApDot11ChannelWidthA,
       "ruijieApDot11ChannelWidthB": ruijieApDot11ChannelWidthB,
       "ruijieApDot11AntenneTable": ruijieApDot11AntenneTable,
       "ruijieApDot11AntenneEntry": ruijieApDot11AntenneEntry,
       "ruijieApDot11AntenneAPID": ruijieApDot11AntenneAPID,
       "ruijieApDot11AntenneRxA": ruijieApDot11AntenneRxA,
       "ruijieApDot11AntenneTxA": ruijieApDot11AntenneTxA,
       "ruijieApDot11AntenneRxB": ruijieApDot11AntenneRxB,
       "ruijieApDot11AntenneTxB": ruijieApDot11AntenneTxB,
       "ruijieWlanDot11MIBObjects": ruijieWlanDot11MIBObjects,
       "ruijieWlanDot11LoadTable": ruijieWlanDot11LoadTable,
       "ruijieWlanDot11LoadTEntry": ruijieWlanDot11LoadTEntry,
       "ruijieWlanDot11WlanId": ruijieWlanDot11WlanId,
       "ruijieWlanDot11Enable": ruijieWlanDot11Enable,
       "ruijieWlanDot11Window": ruijieWlanDot11Window,
       "ruijieWlanDot11Flow": ruijieWlanDot11Flow,
       "ruijieAcDot11MIBConformance": ruijieAcDot11MIBConformance,
       "ruijieAcDot11MIBCompliances": ruijieAcDot11MIBCompliances,
       "ruijieAcDot11MIBCompliance": ruijieAcDot11MIBCompliance,
       "ruijieAcDot11MIBGroups": ruijieAcDot11MIBGroups,
       "ruijieAcDot11MIBGroup": ruijieAcDot11MIBGroup}
)
