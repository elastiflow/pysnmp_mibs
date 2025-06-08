# SNMP MIB module (CEM-CN1000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000.mib
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

(cnCN1000,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "cnCN1000")

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

cnCN1000Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000ShelfRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class Cn1000SlotRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class Cn1000PortRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class Cn1000ConfigurationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configSucceeded", 1),
          ("configPending", 2),
          ("configFailed", 3),
          ("deleteInProgress", 4),
          ("deleteFailed", 5),
          ("configInProgress", 6))
    )



class Cn1000LineAppearanceRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000Hardware_ObjectIdentity = ObjectIdentity
cn1000Hardware = _Cn1000Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 1)
)
_Cn1000NetSync_ObjectIdentity = ObjectIdentity
cn1000NetSync = _Cn1000NetSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 2)
)
_Cn1000VoiceInfrastructure_ObjectIdentity = ObjectIdentity
cn1000VoiceInfrastructure = _Cn1000VoiceInfrastructure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3)
)
_Cn1000VoiceLineServices_ObjectIdentity = ObjectIdentity
cn1000VoiceLineServices = _Cn1000VoiceLineServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4)
)
_Cn1000IfTranslatioins_ObjectIdentity = ObjectIdentity
cn1000IfTranslatioins = _Cn1000IfTranslatioins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5)
)
_CnCN1000Temperature_ObjectIdentity = ObjectIdentity
cnCN1000Temperature = _CnCN1000Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6)
)
_CnOnuSpecials_ObjectIdentity = ObjectIdentity
cnOnuSpecials = _CnOnuSpecials_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000",
    **{"Cn1000ShelfRange": Cn1000ShelfRange,
       "Cn1000SlotRange": Cn1000SlotRange,
       "Cn1000PortRange": Cn1000PortRange,
       "Cn1000ConfigurationStatus": Cn1000ConfigurationStatus,
       "Cn1000LineAppearanceRange": Cn1000LineAppearanceRange,
       "cnCN1000Module": cnCN1000Module,
       "cn1000Hardware": cn1000Hardware,
       "cn1000NetSync": cn1000NetSync,
       "cn1000VoiceInfrastructure": cn1000VoiceInfrastructure,
       "cn1000VoiceLineServices": cn1000VoiceLineServices,
       "cn1000IfTranslatioins": cn1000IfTranslatioins,
       "cnCN1000Temperature": cnCN1000Temperature,
       "cnOnuSpecials": cnOnuSpecials}
)
