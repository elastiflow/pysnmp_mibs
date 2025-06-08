# SNMP MIB module (UCD-DEMO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/UCD-DEMO-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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

(ucdavis,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdavis")


# MODULE-IDENTITY

ucdDemoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 14)
)
if mibBuilder.loadTexts:
    ucdDemoMIB.setRevisions(
        ("1999-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UcdDemoMIBObjects_ObjectIdentity = ObjectIdentity
ucdDemoMIBObjects = _UcdDemoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1)
)
_UcdDemoPublic_ObjectIdentity = ObjectIdentity
ucdDemoPublic = _UcdDemoPublic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1, 1)
)


class _UcdDemoResetKeys_Type(Integer32):
    """Custom type ucdDemoResetKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UcdDemoResetKeys_Type.__name__ = "Integer32"
_UcdDemoResetKeys_Object = MibScalar
ucdDemoResetKeys = _UcdDemoResetKeys_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 1),
    _UcdDemoResetKeys_Type()
)
ucdDemoResetKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucdDemoResetKeys.setStatus("current")


class _UcdDemoPublicString_Type(OctetString):
    """Custom type ucdDemoPublicString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_UcdDemoPublicString_Type.__name__ = "OctetString"
_UcdDemoPublicString_Object = MibScalar
ucdDemoPublicString = _UcdDemoPublicString_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 2),
    _UcdDemoPublicString_Type()
)
ucdDemoPublicString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucdDemoPublicString.setStatus("current")
_UcdDemoUserList_Type = OctetString
_UcdDemoUserList_Object = MibScalar
ucdDemoUserList = _UcdDemoUserList_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 3),
    _UcdDemoUserList_Type()
)
ucdDemoUserList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucdDemoUserList.setStatus("current")
_UcdDemoPassphrase_Type = OctetString
_UcdDemoPassphrase_Object = MibScalar
ucdDemoPassphrase = _UcdDemoPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 4),
    _UcdDemoPassphrase_Type()
)
ucdDemoPassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucdDemoPassphrase.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-DEMO-MIB",
    **{"ucdDemoMIB": ucdDemoMIB,
       "ucdDemoMIBObjects": ucdDemoMIBObjects,
       "ucdDemoPublic": ucdDemoPublic,
       "ucdDemoResetKeys": ucdDemoResetKeys,
       "ucdDemoPublicString": ucdDemoPublicString,
       "ucdDemoUserList": ucdDemoUserList,
       "ucdDemoPassphrase": ucdDemoPassphrase}
)
