# SNMP MIB module (CISCO-TM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-TM.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:06 2025
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

(ciscoDomains,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoDomains")

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

ciscoTransportMappings = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1)
)
if mibBuilder.loadTexts:
    ciscoTransportMappings.setRevisions(
        ("2001-08-23 16:00",
         "2000-06-21 16:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpUDPVPNAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/2d/32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 38),
    )



class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d/4d/4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixedLength = 12



class SnmpCNSIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "19a.255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 274),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpUDPVPNDomain_ObjectIdentity = ObjectIdentity
snmpUDPVPNDomain = _SnmpUDPVPNDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 1)
)
if mibBuilder.loadTexts:
    snmpUDPVPNDomain.setStatus("current")
_SnmpAAL5Domain_ObjectIdentity = ObjectIdentity
snmpAAL5Domain = _SnmpAAL5Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 2)
)
if mibBuilder.loadTexts:
    snmpAAL5Domain.setStatus("current")
_SnmpCNSDomain_ObjectIdentity = ObjectIdentity
snmpCNSDomain = _SnmpCNSDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 1, 3)
)
if mibBuilder.loadTexts:
    snmpCNSDomain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TM",
    **{"SnmpUDPVPNAddress": SnmpUDPVPNAddress,
       "SnmpAAL5VCIdentifier": SnmpAAL5VCIdentifier,
       "SnmpCNSIdentifier": SnmpCNSIdentifier,
       "ciscoTransportMappings": ciscoTransportMappings,
       "snmpUDPVPNDomain": snmpUDPVPNDomain,
       "snmpAAL5Domain": snmpAAL5Domain,
       "snmpCNSDomain": snmpCNSDomain}
)
