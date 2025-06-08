# SNMP MIB module (SNMPv2-TM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMPv2-TM.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:29:08 2025
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
 iso,
 snmpDomains,
 snmpModules,
 snmpProxys) = mibBuilder.importSymbols(
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
    "iso",
    "snmpDomains",
    "snmpModules",
    "snmpProxys")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpv2tm = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 19)
)
if mibBuilder.loadTexts:
    snmpv2tm.setRevisions(
        ("2002-10-16 00:00",
         "1996-01-01 00:00",
         "1993-04-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpUDPAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class SnmpOSIAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "*1x:/1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(4, 85),
    )



class SnmpNBPAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 99),
    )



class SnmpIPXAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x.1x:1x:1x:1x:1x:1x.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixedLength = 12



# MIB Managed Objects in the order of their OIDs

_SnmpUDPDomain_ObjectIdentity = ObjectIdentity
snmpUDPDomain = _SnmpUDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    snmpUDPDomain.setStatus("current")
_SnmpCLNSDomain_ObjectIdentity = ObjectIdentity
snmpCLNSDomain = _SnmpCLNSDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    snmpCLNSDomain.setStatus("current")
_SnmpCONSDomain_ObjectIdentity = ObjectIdentity
snmpCONSDomain = _SnmpCONSDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    snmpCONSDomain.setStatus("current")
_SnmpDDPDomain_ObjectIdentity = ObjectIdentity
snmpDDPDomain = _SnmpDDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    snmpDDPDomain.setStatus("current")
_SnmpIPXDomain_ObjectIdentity = ObjectIdentity
snmpIPXDomain = _SnmpIPXDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    snmpIPXDomain.setStatus("current")
_Rfc1157Proxy_ObjectIdentity = ObjectIdentity
rfc1157Proxy = _Rfc1157Proxy_ObjectIdentity(
    (1, 3, 6, 1, 6, 2, 1)
)
_Rfc1157Domain_ObjectIdentity = ObjectIdentity
rfc1157Domain = _Rfc1157Domain_ObjectIdentity(
    (1, 3, 6, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rfc1157Domain.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPv2-TM",
    **{"SnmpUDPAddress": SnmpUDPAddress,
       "SnmpOSIAddress": SnmpOSIAddress,
       "SnmpNBPAddress": SnmpNBPAddress,
       "SnmpIPXAddress": SnmpIPXAddress,
       "snmpUDPDomain": snmpUDPDomain,
       "snmpCLNSDomain": snmpCLNSDomain,
       "snmpCONSDomain": snmpCONSDomain,
       "snmpDDPDomain": snmpDDPDomain,
       "snmpIPXDomain": snmpIPXDomain,
       "rfc1157Proxy": rfc1157Proxy,
       "rfc1157Domain": rfc1157Domain,
       "snmpv2tm": snmpv2tm}
)
