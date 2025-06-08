# SNMP MIB module (HH3C-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-MULTICAST-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:40:11 2025
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

hh3cMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50)
)
if mibBuilder.loadTexts:
    hh3cMulticast.setRevisions(
        ("2005-04-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMulticastObject_ObjectIdentity = ObjectIdentity
hh3cMulticastObject = _Hh3cMulticastObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50, 1)
)


class _Hh3cMulticastEnable_Type(EnabledStatus):
    """Custom type hh3cMulticastEnable based on EnabledStatus"""
    defaultValue = 2


_Hh3cMulticastEnable_Type.__name__ = "EnabledStatus"
_Hh3cMulticastEnable_Object = MibScalar
hh3cMulticastEnable = _Hh3cMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50, 1, 1),
    _Hh3cMulticastEnable_Type()
)
hh3cMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMulticastEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MULTICAST-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cMulticast": hh3cMulticast,
       "hh3cMulticastObject": hh3cMulticastObject,
       "hh3cMulticastEnable": hh3cMulticastEnable}
)
