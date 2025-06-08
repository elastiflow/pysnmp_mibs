# SNMP MIB module (HH3C-NMS-EXTEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-NMS-EXTEND-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:41:14 2025
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

(hh3cMpMemberlinkDescr,
 hh3cMpMemberlinkIfIndex) = mibBuilder.importSymbols(
    "HH3C-MP-MIB",
    "hh3cMpMemberlinkDescr",
    "hh3cMpMemberlinkIfIndex")

(hh3cNM,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cNM")

(hh3cwapiASIPAddress,
 hh3cwapiASIPAddressType,
 hh3cwapiCertificateInstalled,
 hh3cwapiModeEnabled) = mibBuilder.importSymbols(
    "HH3C-WAPI-MIB",
    "hh3cwapiASIPAddress",
    "hh3cwapiASIPAddressType",
    "hh3cwapiCertificateInstalled",
    "hh3cwapiModeEnabled")

(ifAdminStatus,
 ifAlias,
 ifDescr,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifAlias",
    "ifDescr",
    "ifIndex",
    "ifOperStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cNMIMCExtend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cNMIMCExtend.setRevisions(
        ("2015-11-14 14:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NMS-EXTEND-MIB",
    **{"hh3cNMIMCExtend": hh3cNMIMCExtend}
)
