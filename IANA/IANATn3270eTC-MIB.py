# SNMP MIB module (IANATn3270eTC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANATn3270eTC-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:48:31 2025
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaTn3270eTcMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 61)
)
if mibBuilder.loadTexts:
    ianaTn3270eTcMib.setRevisions(
        ("2014-05-22 00:00",
         "2000-05-10 00:00",
         "1999-09-01 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IANATn3270eAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )



class IANATn3270eAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class IANATn3270eClientType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("ipv4", 3),
          ("ipv6", 4),
          ("domainName", 5),
          ("truncDomainName", 6),
          ("string", 7),
          ("certificate", 8),
          ("userId", 9),
          ("x509dn", 10))
    )



class IANATn3270Functions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("transmitBinary", 0),
          ("timemark", 1),
          ("endOfRecord", 2),
          ("terminalType", 3),
          ("tn3270Regime", 4),
          ("scsCtlCodes", 5),
          ("dataStreamCtl", 6),
          ("responses", 7),
          ("bindImage", 8),
          ("sysreq", 9))
    )


class IANATn3270ResourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("terminal", 2),
          ("printer", 3),
          ("terminalOrPrinter", 4))
    )



class IANATn3270DeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ibm3278d2", 1),
          ("ibm3278d2E", 2),
          ("ibm3278d3", 3),
          ("ibm3278d3E", 4),
          ("ibm3278d4", 5),
          ("ibm3278d4E", 6),
          ("ibm3278d5", 7),
          ("ibm3278d5E", 8),
          ("ibmDynamic", 9),
          ("ibm3287d1", 10),
          ("unknown", 100))
    )



class IANATn3270eLogData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 2048),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANATn3270eTC-MIB",
    **{"IANATn3270eAddrType": IANATn3270eAddrType,
       "IANATn3270eAddress": IANATn3270eAddress,
       "IANATn3270eClientType": IANATn3270eClientType,
       "IANATn3270Functions": IANATn3270Functions,
       "IANATn3270ResourceType": IANATn3270ResourceType,
       "IANATn3270DeviceType": IANATn3270DeviceType,
       "IANATn3270eLogData": IANATn3270eLogData,
       "ianaTn3270eTcMib": ianaTn3270eTcMib}
)
