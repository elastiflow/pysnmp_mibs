# SNMP MIB module (VIPTELA-GLOBAL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/viptela_41916/VIPTELA-GLOBAL.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 11:37:37 2025
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

viptela_global = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 7)
)
if mibBuilder.loadTexts:
    viptela_global.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Viptela_ObjectIdentity = ObjectIdentity
viptela = _Viptela_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-GLOBAL",
    **{"viptela": viptela,
       "viptela-global": viptela_global}
)
