# SNMP MIB module (PKTC-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-SEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:44 2025
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

(clabProjPacketCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjPacketCable")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pktcSecMib.setRevisions(
        ("2003-07-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MemberBody_ObjectIdentity = ObjectIdentity
memberBody = _MemberBody_ObjectIdentity(
    (1, 2)
)
_Us_ObjectIdentity = ObjectIdentity
us = _Us_ObjectIdentity(
    (1, 2, 840)
)
_AnsiX942_ObjectIdentity = ObjectIdentity
ansiX942 = _AnsiX942_ObjectIdentity(
    (1, 2, 840, 10046)
)
_NumberType_ObjectIdentity = ObjectIdentity
numberType = _NumberType_ObjectIdentity(
    (1, 2, 840, 10046, 2)
)
_DhPublicNumber_ObjectIdentity = ObjectIdentity
dhPublicNumber = _DhPublicNumber_ObjectIdentity(
    (1, 2, 840, 10046, 2, 1)
)
_PktcSecErrorCodes_ObjectIdentity = ObjectIdentity
pktcSecErrorCodes = _PktcSecErrorCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1)
)
_PktcSecErrorIpsec_ObjectIdentity = ObjectIdentity
pktcSecErrorIpsec = _PktcSecErrorIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 1)
)
_PktcSecErrorSnmpv3_ObjectIdentity = ObjectIdentity
pktcSecErrorSnmpv3 = _PktcSecErrorSnmpv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 2)
)
_PktcSecErrorFqdn_ObjectIdentity = ObjectIdentity
pktcSecErrorFqdn = _PktcSecErrorFqdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-SEC-MIB",
    **{"memberBody": memberBody,
       "us": us,
       "ansiX942": ansiX942,
       "numberType": numberType,
       "dhPublicNumber": dhPublicNumber,
       "pktcSecMib": pktcSecMib,
       "pktcSecErrorCodes": pktcSecErrorCodes,
       "pktcSecErrorIpsec": pktcSecErrorIpsec,
       "pktcSecErrorSnmpv3": pktcSecErrorSnmpv3,
       "pktcSecErrorFqdn": pktcSecErrorFqdn}
)
