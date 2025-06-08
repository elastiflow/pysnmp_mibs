# SNMP MIB module (JUNIPER-WX-GLOBAL-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-WX-GLOBAL-REG.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:31:35 2025
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

(jnxWxModules,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-REG",
    "jnxWxModules")

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

jnxWxGlobalTcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxGlobalTcModule.setRevisions(
        ("2006-06-08 18:00",
         "2005-05-09 10:10",
         "2004-03-15 14:00",
         "2003-06-26 20:00",
         "2002-11-07 19:00",
         "2001-07-29 22:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TcAppName(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TcQosIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "24a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )



class TcChassisType(TextualConvention, Integer32):
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("jnxWxOther", 1),
          ("jnxWx50", 2),
          ("jnxWx20", 3),
          ("jnxWx80", 4),
          ("jnxWx100", 5),
          ("jnxWxc500", 6),
          ("jnxWx15", 7),
          ("jnxWxc250", 8),
          ("jnxWx100V3", 9),
          ("jnxWx60", 10),
          ("jnxWxc590", 11),
          ("jnxIsm200Wxc", 12),
          ("jnxWxc1800", 13),
          ("jnxWxc2600", 14),
          ("jnxWxc3400", 15))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-GLOBAL-TC",
    **{"TcAppName": TcAppName,
       "TcQosIdentifier": TcQosIdentifier,
       "TcChassisType": TcChassisType,
       "jnxWxGlobalTcModule": jnxWxGlobalTcModule}
)
