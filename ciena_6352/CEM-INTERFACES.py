# SNMP MIB module (CEM-INTERFACES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-INTERFACES.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(cnInterfaces,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "cnInterfaces")

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

cnInterfacesModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CnIfGroupIndexRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CnIfGroupLinkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cnLinkNotInUse", 0),
          ("cnPrimaryLink", 1),
          ("cnSecondaryLink", 2),
          ("cnNormalLink", 3),
          ("cnALink", 4),
          ("cnBLink", 5),
          ("cnCLink", 6),
          ("cnDLink", 7),
          ("cnPLink", 8),
          ("cnSubtendingLink", 9))
    )



# MIB Managed Objects in the order of their OIDs

_CnGR303_ObjectIdentity = ObjectIdentity
cnGR303 = _CnGR303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1)
)
_CnTR08_ObjectIdentity = ObjectIdentity
cnTR08 = _CnTR08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 2)
)
_CnPOTS_ObjectIdentity = ObjectIdentity
cnPOTS = _CnPOTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 3)
)
_CnDS3_ObjectIdentity = ObjectIdentity
cnDS3 = _CnDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 4)
)
_CnOC3_ObjectIdentity = ObjectIdentity
cnOC3 = _CnOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 5)
)
_CnSLC5COT_ObjectIdentity = ObjectIdentity
cnSLC5COT = _CnSLC5COT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 6)
)
_CnMetallicInterface_ObjectIdentity = ObjectIdentity
cnMetallicInterface = _CnMetallicInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 7)
)
_CnDAX_ObjectIdentity = ObjectIdentity
cnDAX = _CnDAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 8)
)
_CnV5_ObjectIdentity = ObjectIdentity
cnV5 = _CnV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-INTERFACES",
    **{"CnIfGroupIndexRange": CnIfGroupIndexRange,
       "CnIfGroupLinkType": CnIfGroupLinkType,
       "cnInterfacesModule": cnInterfacesModule,
       "cnGR303": cnGR303,
       "cnTR08": cnTR08,
       "cnPOTS": cnPOTS,
       "cnDS3": cnDS3,
       "cnOC3": cnOC3,
       "cnSLC5COT": cnSLC5COT,
       "cnMetallicInterface": cnMetallicInterface,
       "cnDAX": cnDAX,
       "cnV5": cnV5}
)
